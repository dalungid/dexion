import requests
import random
import string
import base64
import sys
import re
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

requests.urllib3.disable_warnings()

Wso = [
    '/updates.php', '/libraries/legacy/updates.php', '/web/libraries/legacy/updates.php',
    '/plugins/updates.php', '/includes/updates.php', '/logs/updates.php',
    '/templates/protostar/updates.php', '/libraries/phpmailer/updates.php',
    '/libraries/vendor/updates.php', '/wp.-.admin.php', '/.well-known/pki-validation/wp.-.admin.php',
    '/templates/beez3/wp.-.admin.php', '/libraries/wp.-.admin.php'
]

Wso1 = [
    '/.well-known/wso112233.php','/wso112233.php','/.well-knownold/wso112233.php',
    '/.well-known/acme-challenge/wso112233.php','/.well-known/pkivalidation/wso112233.php',
    '/wp-content/plugins/wso112233.php','/wp-content/uploads/wso112233.php','/wp-content/wso112233.php',
    '/wp-includes/wso112233.php','/wp-admin/wso112233.php','/wp-content/themes/wso112233.php',
    '/.well-known/shell20211028.php','/shell20211028.php','/.well-knownold/shell20211028.php',
    '/.well-known/acme-challenge/shell20211028.php','/.well-known/pkivalidation/shell20211028.php',
    '/wp-content/plugins/shell20211028.php','/wp-content/uploads/shell20211028.php',
    '/wp-content/shell20211028.php','/wp-includes/shell20211028.php','/wp-admin/shell20211028.php',
    '/wp-content/themes/shell20211028.php','/.well-known/bala.php','/bala.php','/.well-knownold/bala.php',
    '/.well-known/acme-challenge/bala.php','/.well-known/pkivalidation/bala.php',
    '/wp-content/plugins/bala.php','/wp-content/uploads/bala.php','/wp-content/bala.php',
    '/wp-includes/bala.php','/wp-admin/bala.php','/wp-content/themes/bala.php','/dropdown.php',
    '/wp-content/dropdown.php','/wp-includes/dropdown.php','/wp-admin/dropdown.php'
]

Wso2 = [
    '/million.php','/404.php','/wp-admin/css/index.php','/ioxi2.php','/wp-content/themes/about.php',
    '/4pric.php','/wp-content/style-css.php','/oxi-rex.php','/wp-content/themes/twenty/twenty.php',
    '/updates.php','/libraries/legacy/updates.php','/libraries/phpmailer/updates.php','/libraries/vendor/updates.php'
]

Tiny = [
    '/.well-known/pki-validation/xmrlpc.php?p=', '/.well-known/acme-challenge/xmrlpc.php?p=',
    '/wp-admin/network/xmrlpc.php?p=', '/xmrlpc.php?p=','/cgi-bin/xmrlpc.php?p=', '/css/xmrlpc.php?p=',
    '/wp-admin/user/xmrlpc.php?p=', '/img/xmrlpc.php?p=', '/wp-admin/css/colors/coffee/xmrlpc.php?p=',
    '/wp-admin/images/xmrlpc.php?p=', '/images/xmrlpc.php?p=', '/wp-admin/js/widgets/xmrlpc.php?p=',
    '/wp-admin/css/colors/xmrlpc.php?p=', '/wp-admin/includes/xmrlpc.php?p=',
    '/wp-admin/css/colors/blue/xmrlpc.php?p=', '/wp-admin/xmrlpc.php?p='
]

Yanz = [
    '/ioxi-rex4.php7','/wp-content/plugins/seoo/alfa-ioxi.php',
    '/wp-content/plugins/classic-editor/wp-login.php'
]

class Eval:
    def __init__(self):
        self.headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                        'referer': 'www.google.com'}

        self.shell_content = """<?php echo "Black Bot" ?>"""

    def url_domain(self, site):
        site = re.sub(r'^https?://', '', site)
        site = re.sub(r'/.*', '', site)
        return site

code_shell = Eval()

def scan_website(url):
    try:
        multiblackbot(url)
        lastgbac(url)
        checker(url)
        chectiny(url)
        checkerWso1(url)
        checkerWso2(url)
        checkerYanz(url)
        alfa(url)
        priv8(url)
        phpfilemanager(url)
        up(url)
        marijuana(url)
    except Exception as e:
        print(' -| ' + url + ' --> {}[Failed]:'.format(fr))

def up(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/background-image-cropper/ups.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload' in check.content:
                print(' -| ' + site + ' --> {}[Succefully] [shell]'.format(fg))
                open('Shells.txt', 'a').write(site + '/wp-content/plugins/background-image-cropper/ups.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/background-image-cropper/ups.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if 'enctype="multipart/form-data" name="uploader" id="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload' in check.content:
                    print(' -| ' + site + ' --> {}[Succefully] [shell]'.format(fg))
                    open('Shells.txt', 'a').write(site + '/wp-content/plugins/background-image-cropper/ups.php\n')
            else:
                print(' -| ' + site + ' --> {}[Failed]'.format(fr))
    except :
        pass

def phpfilemanager(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/hellopress/wp_filemanager.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if 'PHP File Manager' in check.content:
                print(' -| ' + site + ' --> {}[Succefully] [phpfile]'.format(fg))
                open('PHPFileManager.txt', 'a').write(site + '/wp-content/plugins/hellopress/wp_filemanager.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/hellopress/wp_filemanager.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if 'PHP File Manager' in check.content:
                    print(' -| ' + site + ' --> {}[Succefully] [phpfile]'.format(fg))
                    open('PHPFileManager.txt', 'a').write(site + '/wp-content/plugins/hellopress/wp_filemanager.php\n')
            else:
                print(' -| ' + site + ' --> {}[Failed]'.format(fr))
    except :
        pass

def priv8(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/network/upfile.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if 'kill_the_net' in check.content:
                print(' -| ' + site + ' --> {}[Succefully] [kill-shell]'.format(fg))
                open('kill-Shells.txt', 'a').write(site + '/wp-admin/network/upfile.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/maint/upfile.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if 'kill_the_net' in check.content:
                    print(' -| ' + site + ' --> {}[Succefully] [kill-shell]'.format(fg))
                    open('kill-Shells.txt', 'a').write(site + '/wp-admin/maint/upfile.php')
            else:
                print(' -| ' + site + ' --> {}[Failed]'.format(fr))
    except :
        print(' -| ' + site + ' --> {}[Failed]'.format(fr))

def alfa(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/.well-known/admin.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if 'ALFA TEaM Shell - v4.1-Tesla' in check.content:
                print(' -| ' + site + ' --> {}[Succefully] [alfa-team]'.format(fg))
                open('ALFATEaMShell.txt', 'a').write(site + '/.well-known/admin.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/.well-known/acme-challenge/wp-signup.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if 'ALFA TEaM Shell - v4.1-Tesla' in check.content:
                    print(' -| ' + site + ' --> {}[Succefully] [alfa-team]'.format(fg))
                    open('ALFATEaMShell.txt', 'a').write(site + '/.well-known/acme-challenge/wp-signup.php\n')
            else:
                print(' -| ' + site + ' --> {}[Failed]'.format(fr))
    except :
        pass

def multiblackbot(site):
    try:
        url = 'http://' + code_shell.url_domain(site)
        check = requests.get(url + '/simple.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '{Ninja-Shell}' in check.content.decode():
            print(' -| ' + url + ' --> {}[Successfully] [ninja]'.format(fg))
            open('Ninja-Shell.txt', 'a').write(url + '/simple.php\n')
        else:

            url = 'https://' + code_shell.url_domain(site)
            check = requests.get(url + '/shell20211028.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
            if 'Uname:' in check.content.decode():
                print(' -| ' + url + ' --> {} [Successfully] [wso]'.format(fg))
                open('wso.txt', 'a').write(url + '/shell20211028.php\n')
            else:
                print(' -| ' + url + ' --> {} [Failed]'.format(fr))
    except:
        print(' -| ' + url + ' --> {} [Failed]'.format(fr))

def lastgbac(url):
    try:
        url_https = 'https://' + code_shell.url_domain(url)
        url_http = 'http://' + code_shell.url_domain(url)

        check = requests.get(url_https + '/wp-content/plugins/yyobang/mar.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [mar]'.format(fg))
            open('MARIJUANA.txt', 'a').write(url_https + '/wp-content/plugins/yyobang/mar.php\n')
        else:
            print(' -| ' + url_https + ' --> {}[Failed]'.format(fr))

        check = requests.get(url_http + '/wp-content/plugins/press/wp-class.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'WSO 4.2.5' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [wso]'.format(fg))
            open('wso.txt', 'a').write(url_http + '/wp-content/plugins/press/wp-class.php\n')

        check = requests.get(url_https + '/xxl.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [xleet]'.format(fg))
            open('xleet.txt', 'a').write(url_https + '/xxl.php\n')

        check = requests.get(url_https + '/wp-includes/Requests/Text/admin.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'Shell Bypass 403 GE-C666C' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_https + '/wp-includes/Requests/Text/admin.php\n')

        check = requests.get(url_http + '/fm1.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [wso]'.format(fg))
            open('wso.txt', 'a').write(url_http + '/fm1.php\n')

        check = requests.get(url_https + '/wp-content/themes/finley/min.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [yanz]'.format(fg))
            open('Yanz Webshell!.txt', 'a').write(url_https + '/wp-content/themes/finley/min.php\n')

        check = requests.get(url_https + '/M1.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Madstore.sk!' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [madstore]'.format(fg))
            open('Madstore.txt', 'a').write(url_https + '/M1.php\n')

        check = requests.get(url_https + '/wp-head.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [yanz]'.format(fg))
            open('Yanz Webshell!.txt', 'a').write(url_https + '/wp-head.php\n')

        check = requests.get(url_https + '/.well-known/index.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [mar]'.format(fg))
            open('MARIJUANA.txt', 'a').write(url_https + '/.well-known/index.php\n')

        check = requests.get(url_https + '/.well-known/acme-challenge/index.php', headers=code_shell.headers, allow_redirects=True, timeout=15)
        if '>Upload: <input type="hidden" value="100000000" name="MAX_FILE_SIZE"><input type="file" name="upfile" id="ltb">' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_https + '/.well-known/acme-challenge/index.php\n')

        check = requests.get(url_https + '/.well-known/fierzashell.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [wso]'.format(fg))
            open('wso.txt', 'a').write(url_https + '/.well-known/fierzashell.php\n')

        check = requests.get(url_https + '/.well-known/pki-validation/x.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [wso]'.format(fg))
            open('wso.txt', 'a').write(url_https + '/.well-known/pki-validation/x.php\n')

        check = requests.get(url_https + '/b0.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Gel4y Mini Shell' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [gel4y]'.format(fg))
            open('Gel4y-Mini-Shell.txt', 'a').write(url_https + '/b0.php\n')

        check = requests.get(url_https + '/style.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'input type="file" name="__"><input name="_" type="submit" value="Upload"' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [style]'.format(fg))
            open('style.txt', 'a').write(url_https + '/style.php\n')

        check = requests.get(url_https + '/chosen.php?p=', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '<title>000</title>' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [choosen]'.format(fg))
            open('chosen.txt', 'a').write(url_https + '/chosen.php?p=\n')

        check = requests.get(url_https + '/nice.php?p=', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'type="button">Upload File<' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [design]'.format(fg))
            open('design.txt', 'a').write(url_https + '/nice.php?p=\n')

        check = requests.get(url_http + '/wp-content/plugins/fix/up.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '<input type="file" name="fileToUpload" id="fileToUpload">' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [up]'.format(fg))
            open('up.txt', 'a').write(url_https + '/wp-content/plugins/fix/up.php\n')

        check = requests.get(url_http + '/wp-content/themes/twentyfive/include.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'b374k 2.8' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [b374k]'.format(fg))
            open('b374k.txt', 'a').write(url_https + '/wp-content/themes/twentyfive/include.php\n')

        check = requests.get(url_https + '/class.api.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '%PDF-0-1<form action="" method="post"><input type="text" name="_rg"><input type="submit" value=">>"' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [class-api]'.format(fg))
            open('class.api.txt', 'a').write(url_https + '/class.api.php\n')
                       
        check = requests.get(url_http + '/cong.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Mr.Combet WebShell' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [shell]'.format(fg))    
            open('shell.txt', 'a').write(url_https + '/cong.php\n')
            
        check = requests.get(url_https + '/st.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [wso]'.format(fg))        
            open('wso.txt', 'a').write(url_https + '/st.php\n')
            
        check = requests.get(url_https + '/css/index.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'L I E R SHELL' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_https + '/css/index.php\n')
         
        check = requests.get(url_https + '/wp-content/plugins/envato-market/inc/class-envato-market-api.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Upload File : <input' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_https + '/wp-content/plugins/envato-market/inc/class-envato-market-api.php\n')

        check = requests.get(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p=', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Tiny File Manager' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [tiny]'.format(fg))
            open('tiny.txt', 'a').write(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p=\n')
            
        check = requests.get(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Tiny File Manager' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [tiny]'.format(fg))
            open('tiny.txt', 'a').write(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p=\n')

        check = requests.get(url_http + '/wp-content/plugins/wordpresss3cll/includes.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'meta name="robots" content="noindex"><form method="post" enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<' in check.text:
            print(' -| ' + url_http + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_http + '/wp-content/plugins/wordpresss3cll/includes.php\n')

        check = requests.get(url_https + '/wp-content/plugins/wordpresss3cll/wp-login.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'C0mmand' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [shell]'.format(fg))
            open('shell.txt', 'a').write(url_https + '/wp-content/plugins/wordpresss3cll/wp-login.php\n')

        check = requests.get(url_http + '/wp-content/plugins/envato-market/inc/class-envato-market-api.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Upload File : <input' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [seo]'.format(fg))
            open('seo.txt', 'a').write(url_https + '/wp-content/plugins/envato-market/inc/class-envato-market-api.php\n')

        check = requests.get(url_https + '/wp-admin/css/colors/blue/atomlib.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.text:
            print(' -| ' + url_https + ' --> {}[Successfully] [mar]'.format(fg))
            open('MARIJUANA.txt', 'a').write(url_https + '/wp-admin/css/colors/blue/atomlib.php\n')

        check = requests.get(url_https + '/wp-admin/network/upfile.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'kill_the_net' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [killnet]')
            open('shell-kill.txt', 'a').write(url_https + '/wp-admin/network/upfile.php\n')

        check = requests.get(url_https + '/wp-content/plugins/wordpresss3cll/wp-login.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'C0mmand ' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [shell]')
            open('shell.txt', 'a').write(url_https + '/wp-content/plugins/wordpresss3cll/wp-login.php\n')
            
        check = requests.get(url_https + '/wp-content/plugins/wordpresss3cll/includes.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'meta name="robots" content="noindex"><form method="post" enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [shell]')
            open('shell.txt', 'a').write(url_https + '/wp-content/plugins/wordpresss3cll/includes.php\n')
            
        check = requests.get(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p=', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Tiny File Manager' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [tiny]')
            open('tiny.txt', 'a').write(url_https + '/wp-includes/js/tinymce/skins/lightgray/img/index.php?p=\n')

        check = requests.get(url_https + '/cong.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Mr.Combet WebShell' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [cong]')
            open('cong.txt', 'a').write(url_https + '/cong.php\n')

        check = requests.get(url_https + '/radio.php', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'BlackDragon' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [radio]')
            open('radio.txt', 'a').write(url_https + '/radio.php\n')
                            
        check = requests.get(url_https + '/wp-content/plugins/w0rdpr3ssnew/about.phpp', headers=code_shell.headers, allow_redirects=True, verify=False, timeout=15)
        if 'Faizzz-Chin ShellXploit' in check.text:
            print(' -| ' + url_https + ' --> [Successfully] [shell]')
            open('shell.txt', 'a').write(url_https + '/wp-content/plugins/w0rdpr3ssnew/about.phpp\n')
                                        
    except Exception as e:
        print(' -| ' + url_http + ' --> {}[Failed]'.format(fr))

def checker(url):
    try:
        site = 'https://' + code_shell.url_domain(url)
        for Path in Wso:
            check = requests.get(site + Path, headers=code_shell.headers, timeout=15)
            if "WSO 4.2.6" in check.decode("latin-1"):
                print(' -| {} --> {}[Successfully] [wso]'.format(url, fg))
                open('wso.txt', 'a').write(site + Path + "\n")
                break
            else:
                print(' -| {} --> {}[Failed]'.format(site, fr))
    except:
        pass

def checkerWso1(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        for Path in Wso1:
            check = requests.get(site + Path, headers=code_shell.headers, timeout=15)
            if "Uname:" in check.decode("latin-1"):
                print(' -| {} --> {}[Successfully] [wso]'.format(url, fg))
                open('wso.txt', 'a').write(site + Path + "\n")
                break
            else:
                print(' -| {} --> {}[Failed]'.format(site, fr))
    except:
        pass

def checkerWso2(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        for Path in Wso2:
            check = requests.get(site + Path, headers=code_shell.headers, timeout=15)
            if "Uname:" in check.content.decode("latin-1"):
                print(' -| {} --> {}[Successfully] [wso]'.format(url, fg))
                open('wso.txt', 'a').write(site + Path + "\n")
                break
            else:
                check = requests.get(site + Path, headers=code_shell.headers, timeout=15)
                if "WSO 4.2.6" in check.content.decode("latin-1"):
                    print(' -| {} --> {}[Successfully] [wso]'.format(url, fg))
                    open('wso.txt', 'a').write(site + Path + "\n")
                    break
    except:
        pass
        
def checkerYanz(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        for Path in Yanz:
            check = requests.get(site + Path, headers=code_shell.headers, timeout=15)
            if "Yanz Webshell!" in check.decode("latin-1"):
                print(' -| {} --> {}[Successfully] [yanz]'.format(url, fg))
                open('Yanz Webshell!.txt', 'a').write(site + Path + "\n")
                break
            else:
                print(' -| {} --> {}[Failed]'.format(site, fr))
    except:
        pass

def chectiny(site):
    try:
        url = "http://" + code_shell.url_domain(site)
        for Path in Tiny:
            check = requests.get(url + Path, headers=code_shell.headers, verify=False, timeout=15)
            if "Tiny File Manager" in check.decode('latin-1'):
                print(' -| {} --> {}[Successfully] [tiny]'.format(url, fg))
                open('tiny.txt', 'a').write(url + Path + "\n")
                break
            else:
                print(' -| {} --> {}[Failed]'.format(site, fr))
    except:
        pass

def marijuana(url):
    try:
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/seoplugins/mar.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/seoplugins/mar.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/seoplugins/mar.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/themes/seotheme/mar.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/themes/seotheme/mar.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/themes/seotheme/mar.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/themes/seotheme/mar.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/images/mar.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/images/mar.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/images/mar.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/images/mar.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/m4r1ju4n4.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/m4r1ju4n4.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/m4r1ju4n4.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/m4r1ju4n4.php\n')
            else:
               pass           
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/marijuana.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/marijuana.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/marijuana.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/marijuana.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/css/colors/coffee/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/coffee/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/css/colors/coffee/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/coffee/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/css/colors/coffee/marijuana.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/coffee/marijuana.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/css/colors/coffee/marijuana.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/coffee/marijuana.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/css/colors/maro.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/maro.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/css/colors/maro.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/colors/maro.php\n')
            else:
                pass
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/css/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/css/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/owfsmac/mar.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/owfsmac/mar.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/owfsmac/mar.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/owfsmac/mar.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/css/maro.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/maro.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/css/maro.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/css/maro.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/includes/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/includes/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/includes/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/includes/mari.php\n')
            else:
                pass  
        site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/maint/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/maint/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/maint/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/maint/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-admin/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-admin/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-admin/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-admin/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/aryabot/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/aryabot/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/aryabot/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/aryabot/mari.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/aryabot/mar.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/aryabot/mar.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/aryabot/mar.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/aryabot/mar.php\n')
            else:
                
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-content/plugins/owfsmac/maro.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/owfsmac/maro.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-content/plugins/owfsmac/maro.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-content/plugins/owfsmac/maro.php\n')
            else:
                pass
                site = 'http://' + code_shell.url_domain(url)
        check = requests.get(site+'/wp-includes/mari.php',headers=code_shell.headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                open('MARIJUANA.txt', 'a').write(site + '/wp-includes/mari.php\n')
        else:
            site = 'https://' + code_shell.url_domain(url)
            check = requests.get(site+'/wp-includes/mari.php',headers=code_shell.headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print(' -| ' + site + ' --> {}[succesfully] [mar]'.format(fg))
                    open('MARIJUANA.txt', 'a').write(site + '/wp-includes/mari.php\n')
            else:
                print (' -| ' + site + ' --> {}[Failed]'.format(fr))                 
    except:
        pass

if __name__ == "__main__":
    try:
        targets = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
        raw = [code_shell.url_domain(target) for target in targets]
    except IndexError:
        path = str(sys.argv[0]).split('/')
        exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

    mp = Pool(150)
    mp.map(scan_website, raw)
    mp.close()
    mp.join()