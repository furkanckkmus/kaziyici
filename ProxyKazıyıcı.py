import builtins
import requests
from bs4 import BeautifulSoup
import re
import time
import threading
import base64
import random
import sys
file = open("proxylist.txt","a+")

def progress(count, total, status=''):
    bar_len = 75
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

progres_sayı = 0





def spysme():
    global progres_sayı
    progres_sayı = progres_sayı + 1
    try:
        url = "https://spys.me/proxy.txt"
        time.sleep(1)
        git = requests.get(url=url,timeout=3)
        soup = BeautifulSoup(git.content,"lxml")
        soup=str(soup)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        proxyliste = re.findall(pattern,soup)
        for i in range(len(proxyliste)):
            ip = proxyliste[i][0]
            port = proxyliste[i][1]
            proxy= ip+":"+port+"\n"
            file.write(proxy)
        #print(f"{url}\nSitede\t{len(proxyliste)}\tAdet Proxy Bulundu")
        progres_sayı = progres_sayı + 1
    except:
        print("Hata Var     Spysme")
        pass
#----------------------------------------------------------------------------------------------------------------
def freeproxylist():
    global progres_sayı
    progres_sayı = progres_sayı + 1
    try:
        url = "https://free-proxy-list.net/#"
        git = requests.get(url=url,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul = bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu") 
    except:
        print("Hata Var     freeproxylist")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxyscrapehttp():
    global progres_sayı
    progres_sayı = progres_sayı + 1    
    try:
        url="https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=7000&country=all&ssl=all&anonymity=all"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))

        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxyscrapehttp")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxyscrapesocks4():
    global progres_sayı
    progres_sayı = progres_sayı + 1
    try:
        url="https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=7000&country=all"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxyscrapesocks4")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxyscrapesocks5():
    try:
        url="https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=7000&country=all"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxyscrapesocks5")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxydb():
    try:
        url = "http://proxydb.net/"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxydb")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxylistdownloadhttp():
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=http"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxylistdownloadhttp")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxylistdownloadhttps():
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=https"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxylistdownloadhttps")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxylistdownloadsocks4():
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=socks4"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxylistdownloadsocks4")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxylistdownloadsocks5():
    try:
        url = "https://www.proxy-list.download/api/v1/get?type=socks5"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     proxylistdownloadsocks5")
        pass
#----------------------------------------------------------------------------------------------------------------
def hidemyipcom():
    try:
        url = "https://www.hide-my-ip.com/tr/proxylist.shtml"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})","p":"(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul=bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     hidemyipcom")
        pass
#----------------------------------------------------------------------------------------------------------------
def sslproxies():
    try:
        url = "https://www.sslproxies.org/"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")   
    except:
        print("Hata Var     sslproxies")
        pass
#----------------------------------------------------------------------------------------------------------------    
def proxyscanhttp():
    try:
        keys = ("socks4","https","socks5","http")
        for i in keys:
            time.sleep(4)
            url = (f"https://www.proxyscan.io/download?type={i}")
            user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            git = requests.get(url=url,headers=user_agent,timeout=10)
            pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
            bul = re.findall(pattern,str(git.content))
            for i in range(len(bul)):
                ipbul=bul[i][0]
                portbul = bul[i][1]
                ipport = (f"{ipbul}:{portbul}\n")
                file.write(ipport)
            #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")        
    except:
        print("Hata Var     proxyscanhttp")
        pass
#----------------------------------------------------------------------------------------------------------------
def hookzof():
    try:
        url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     hookzof")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxylistorg():
    try:
        for arg in range(1,10):
            url = (f"https://proxy-list.org/english/index.php?p={arg}")
            user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            git = requests.get(url=url,headers=user_agent,timeout=3)
            base64pattern = r"Proxy\(\\'(.*?)\\'\)"
            base64bul = re.findall(base64pattern,str(git.content))
            for i in range(len(base64bul)):
                decode = base64.b64decode(base64bul[i]).decode('utf-8')
                file.write(str(decode+"\n"))
            #print(f"{url}\nSitede\t{len(base64bul)}\tAdet Proxy Bulundu")	

    except:
        print("Hata Var     proxylistorg")
        pass
#----------------------------------------------------------------------------------------------------------------
def TheSpeedXsocks5():
    try:
        url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")

    except:
        print("Hata Var     TheSpeedXsocks5")
        pass
#----------------------------------------------------------------------------------------------------------------
def TheSpeedXsocks4():
    try:
        url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     TheSpeedXsocks4")
        pass    
#----------------------------------------------------------------------------------------------------------------
def TheSpeedXhttp():
    try:
        url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     TheSpeedXhttp")
        pass
#----------------------------------------------------------------------------------------------------------------
def hookzofsocks():
    try:
        url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})","port":"(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     hookzofsocks")
        pass
#----------------------------------------------------------------------------------------------------------------
def emailtry(arg):
    try:
        for i in range(arg):
            url = (f"http://www.emailtry.com/index/{i}")
            user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            time.sleep(random.uniform(5, 45))
            git = requests.get(url=url,headers=user_agent,timeout=3)
            pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
            bul = re.findall(pattern,str(git.content))
            for i in range(len(bul)):
                ipbul=bul[i][0]
                portbul=bul[i][1]
                ipport = (f"{ipbul}:{portbul}\n")
                file.write(ipport)
            #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     emailtry")
        pass
#----------------------------------------------------------------------------------------------------------------
def xroxy(arg):
    try:
        url = (f"https://www.xroxy.com/proxylist.php?port=&type=&ssl=&country=&latency=&reliability=&sort=reliability&desc=true&pnum={arg}#table")
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        time.sleep(random.uniform(5, 45))
        git = requests.get(url=url,headers=user_agent,timeout=3)
        patternip = r"details\\'>(.*?)\\n<!"
        patternport = r"number (.*?)\\'>"
        bulip = re.findall(patternip,str(git.content))
        bulport = re.findall(patternport,str(git.content))
        for i in range(len(bulip)):
            ip = bulip[i]
            port = bulport[i]
            ipport = (f"{ip}:{port}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bulip)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     xroxy")
        pass
#----------------------------------------------------------------------------------------------------------------
def kuaidaili(arg):
    try:
        url = (f"https://www.kuaidaili.com/free/inha/{arg}")
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        #time.sleep(random.uniform(5, 10))
        git = requests.get(url=url,headers=user_agent,timeout=3)
        time.sleep(0.5)
        patternip = r'\"IP">(.*?)\<.td>'
        patternport = r'\"PORT">(.*?)\<.td>'
        bulip = re.findall(patternip,str(git.content))
        bulport = re.findall(patternport,str(git.content))
        for i in range(len(bulip)):
            ip = bulip[i]
            port = bulport[i]
            ipport = (f"{ip}:{port}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bulip)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     kuaidaili")
        pass
#----------------------------------------------------------------------------------------------------------------
def hidemyname(deger):
    try:
        url = (f"https://hidemy.name/tr/proxy-list/?start={deger}#list")
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        time.sleep(random.uniform(8, 25))
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d{1,5})'
        bul = re.findall(pattern,str(git.content))

        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu") 
    except:
        print("Hata Var     hidemyname")
        pass
#----------------------------------------------------------------------------------------------------------------
def geonode(sayfa):
    try:     
        url = (f"https://proxylist.geonode.com/api/proxy-list?limit=200&page={sayfa}&sort_by=lastChecked&sort_type=desc")
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        time.sleep(random.uniform(8, 50))
        git = requests.get(url=url,headers=user_agent,timeout=3)
        
        data = git.content
        data = str(data)
        portpattern = r"(port\":\")(\d{1,5})"
        ippattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        ipbul = re.findall(ippattern,data)
        portbul = re.findall(portpattern,data)
        ipport = []
        for i in range(len(ipbul)):
            port = portbul[i][1]
            ipport = (f'{ipbul[i]}:{port}\n')
            file.write(ipport)
        file.write("\n")
        #print(f"{url}\nSitede\t{len(ipbul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     geonode")
        pass
#----------------------------------------------------------------------------------------------------------------
def fineproxyde():
    try:
        url = "https://fineproxy.de/wp-content/themes/fineproxyde/proxy-list.php?0.8526036315162359"
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        git = requests.get(url=url,headers=user_agent,timeout=3)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})","port":"(\d{1,5})'
        bul = re.findall(pattern,str(git.content))
        for i in range(len(bul)):
            ipbul=bul[i][0]
            portbul = bul[i][1]
            ipport = (f"{ipbul}:{portbul}\n")
            file.write(ipport)
        #print(f"{url}\nSitede\t{len(bul)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     fineproxyde")
        pass
#----------------------------------------------------------------------------------------------------------------
def topproxiesru():
    try:
        url = "https://top-proxies.ru/free_proxy/fre_proxy_api.php"
        time.sleep(1)
        git = requests.get(url=url,timeout=3)
        soup = BeautifulSoup(git.content,"lxml")
        soup=str(soup)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        proxyliste = re.findall(pattern,soup)
        for i in range(len(proxyliste)):
            ip = proxyliste[i][0]
            port = proxyliste[i][1]
            proxy= ip+":"+port+"\n"
            file.write(proxy)
        #print(f"{url}\nSitede\t{len(proxyliste)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     topproxiesru")
        pass
#----------------------------------------------------------------------------------------------------------------
def usproxyorg():
    try:
        url = "https://www.us-proxy.org/"
        time.sleep(1)
        git = requests.get(url=url,timeout=3)
        soup = BeautifulSoup(git.content,"lxml")
        soup=str(soup)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        proxyliste = re.findall(pattern,soup)
        for i in range(len(proxyliste)):
            ip = proxyliste[i][0]
            port = proxyliste[i][1]
            proxy= ip+":"+port+"\n"
            file.write(proxy)
        #print(f"{url}\nSitede\t{len(proxyliste)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     usproxyorg")
        pass
#----------------------------------------------------------------------------------------------------------------
def proxydaily():
    try:
        url = "https://proxy-daily.com/"
        time.sleep(1)
        git = requests.get(url=url,timeout=3)
        soup = BeautifulSoup(git.content,"lxml")
        soup=str(soup)
        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
        proxyliste = re.findall(pattern,soup)
        for i in range(len(proxyliste)):
            ip = proxyliste[i][0]
            port = proxyliste[i][1]
            proxy= ip+":"+port+"\n"
            file.write(proxy)
        #print(f"{url}\nSitede\t{len(proxyliste)}\tAdet Proxy Bulundu")
    except:
        print("Hata Var     usproxyorg")
        pass


t1 = threading.Thread(target = spysme)
t2 = threading.Thread(target = freeproxylist)
t3 = threading.Thread(target = proxyscrapehttp)
t4 = threading.Thread(target = proxyscrapesocks4)
t5 = threading.Thread(target = proxyscrapesocks5)
t6 = threading.Thread(target = proxydb)
t7 = threading.Thread(target = proxylistdownloadhttp)
t8 = threading.Thread(target = proxylistdownloadhttps)
t9 = threading.Thread(target = proxylistdownloadsocks4)
t10 = threading.Thread(target = proxylistdownloadsocks5)
t11 = threading.Thread(target = hidemyipcom)
t12 = threading.Thread(target = sslproxies)
t13 = threading.Thread(target = proxyscanhttp)
t14 = threading.Thread(target = hookzof)
t15 = threading.Thread(target = proxylistorg)
t16 = threading.Thread(target = TheSpeedXsocks5)
t17 = threading.Thread(target = TheSpeedXsocks4)
t18 = threading.Thread(target = TheSpeedXhttp)
t19 = threading.Thread(target = hookzofsocks)
t20 = threading.Thread(target = emailtry,args=(60,))
t25 = threading.Thread(target = fineproxyde)
t26 = threading.Thread(target = topproxiesru)
t27 = threading.Thread(target = usproxyorg)
t28 = threading.Thread(target = proxydaily)


for i in range(0,100):
    t21 = threading.Thread(target = xroxy,args=(i,))
    t21.start()
    time.sleep(0.5)
    print("Thread 21 Başladı",i)
for i in range(1,7):
    t22 = threading.Thread(target = kuaidaili,args=(i,))
    time.sleep(2)
    t22.start()
    print("Thread 22 Başladı",i)
for i in range(0,8000,64):
    t23 = threading.Thread(target = hidemyname,args=(i,))
    time.sleep(0.5)
    t23.start()
    print("Thread 23 Başladı",i)
for i in range(20):
    t24 = threading.Thread(target = geonode,args=(i,))
    t24.start()
    time.sleep(0.3)
    print("Thread 2 Başladı",i)

t1.start()
print("Thread 1 Başladı")
t2.start()
print("Thread 2 Başladı")
t3.start()
print("Thread 3 Başladı")
t4.start()
print("Thread 4 Başladı")
t5.start()
print("Thread 5 Başladı")
t6.start()
print("Thread 6 Başladı")
t7.start()
print("Thread 7 Başladı")
t8.start()
print("Thread 8 Başladı")
t9.start()
print("Thread 9 Başladı")
t10.start()
print("Thread 10 Başladı")
t11.start()
print("Thread 11 Başladı")
t12.start()
print("Thread 12 Başladı")
t13.start()
print("Thread 13 Başladı")
t14.start()
print("Thread 14 Başladı")
t15.start()
print("Thread 15 Başladı")
t16.start()
print("Thread 16 Başladı")
t17.start()
print("Thread 17 Başladı")
t18.start()
print("Thread 18 Başladı")
t19.start()
print("Thread 19 Başladı")
t20.start()
print("Thread 20 Başladı")
t25.start()
print("Thread 21 Başladı")
t26.start()
print("Thread 22 Başladı")
t27.start()
print("Thread 23 Başladı")
t28.start()
print("Thread 23 Başladı")




























