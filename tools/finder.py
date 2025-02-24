import os
import requests
import re
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

class ShellFinder:
    SUSPICIOUS_PATTERNS = [
        r"base64_decode",
        r"eval\(",
        r"exec\(",
        r"system\(",
        r"shell_exec\(",
        r"passthru\(",
        r"assert\(",
        r"preg_replace.*\/e",
        r"create_function",
        r"file_put_contents",
        r"fwrite",
        r"curl_exec",
        r"wget ",
        r"GET / HTTP",
        r"https?:\/\/[^\/]+\/(shell|mini|d7net|backdoor|webshell)\.php",
        r"\.(php|phtml|php3|php5)\?(cmd|exec|system|shell_exec|passthru)=",
        r"\/(mass|deface|config|symlink)\="
    ]

    PROXY_SOURCES = {
        'SOCKS5': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
        'SOCKS4': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
        'HTTP': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
    }

    def __init__(self):
        self.url_file = os.getenv("URL_FILE")
        self.pwd_file = os.getenv("PWD_FILE")
        self.path_file = os.getenv("PATH_FILE")
        self.proxy_type = os.getenv("PROXY_TYPE", "HTTP").upper()
        self.proxy_list = []
        self.current_proxy = None
        self.domains = []
        self.endpoints = []
        self.paths = []

        if os.getenv("USE_PROXY", "false").lower() == "true":
            self._load_proxies()

    def _load_proxies(self):
        """Muat daftar proxy dari sumber eksternal"""
        try:
            url = self.PROXY_SOURCES.get(self.proxy_type)
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                self.proxy_list = [p.strip() for p in response.text.split('\n') if p.strip()]
                print(f"[*] Loaded {len(self.proxy_list)} {self.proxy_type} proxies")
                self._rotate_proxy()
        except Exception as e:
            print(f"[!] Gagal memuat proxy: {str(e)[:50]}")

    def _rotate_proxy(self):
        """Ganti ke proxy berikutnya"""
        if self.proxy_list:
            self.current_proxy = self.proxy_list.pop(0)
            print(f"[*] Menggunakan proxy: {self.current_proxy}")
        else:
            print("[!] Daftar proxy habis")
            self.current_proxy = None

    def load_resources(self):
        """Muat semua sumber daya yang diperlukan"""
        # Muat daftar domain
        self.domains = self._load_file(self.url_file)
        self.domains = [self._add_protocol(d) for d in self.domains if d.strip()]
        
        # Muat endpoint dan path
        self.endpoints = self._load_file(self.pwd_file)
        self.paths = self._load_file(self.path_file)
        
        if not self.domains:
            raise ValueError("Daftar domain kosong")
        if not self.endpoints:
            raise ValueError("Daftar endpoint kosong")
        if not self.paths:
            raise ValueError("Daftar path kosong")

    def start_scan(self):
        """Mulai proses pemindaian"""
        print("[*] Memulai pemindaian mendalam...")
        for domain in self.domains:
            for path in self.paths:
                for endpoint in self.endpoints:
                    url = self._build_url(domain, path, endpoint)
                    print(f"[*] Memindai: {url}")
                    content = self._fetch_with_retry(url)
                    if content and self._scan_content(content):
                        self._save_result(url)
        print("[*] Pemindaian selesai")

    def _add_protocol(self, url):
        """Tambahkan protokol jika belum ada"""
        if not url.startswith(('http://', 'https://')):
            return f"http://{url}"
        return url

    def _build_url(self, domain, path, endpoint):
        """Bangun URL lengkap"""
        parsed = urlparse(domain)
        base = f"{parsed.scheme}://{parsed.netloc}"
        return f"{base}/{path.strip('/')}/{endpoint.lstrip('/')}"

    def _fetch_with_retry(self, url):
        """Coba akses URL dengan mekanisme retry"""
        for _ in range(int(os.getenv("RETRY_COUNT", 3))):
            try:
                proxies = self._get_proxies()
                response = requests.get(
                    url,
                    proxies=proxies,
                    timeout=int(os.getenv("REQUEST_TIMEOUT", 30)),
                    verify=False,
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                if response.status_code == 200:
                    return response.text
            except Exception as e:
                print(f"[!] Gagal akses {url}: {str(e)[:50]}")
                if self.current_proxy:
                    self._rotate_proxy()
        return None

    def _get_proxies(self):
        """Dapatkan konfigurasi proxy"""
        if not self.current_proxy:
            return None
        return {
            'http': f"{self.proxy_type.lower()}://{self.current_proxy}",
            'https': f"{self.proxy_type.lower()}://{self.current_proxy}"
        }

    def _scan_content(self, content):
        """Periksa konten untuk pola mencurigakan"""
        return any(re.search(pattern, content, re.IGNORECASE) 
                for pattern in self.SUSPICIOUS_PATTERNS)

    def _save_result(self, url):
        """Simpan hasil ke file"""
        os.makedirs('result', exist_ok=True)
        with open('result/shell.txt', 'a') as f:
            f.write(f"{url}\n")
        print(f"[+] Berhasil menyimpan: {url}")

    def _load_file(self, filename):
        """Muat isi file teks"""
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[!] Gagal memuat file {filename}: {e}")
            return []

if __name__ == "__main__":
    finder = ShellFinder()
    finder.load_resources()
    finder.start_scan()