import requests
import time
import threading
import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

file = open("proxylist.txt","r+")
proxylist=file.read().splitlines()
file.close()

def dosyayaz(ıcerık):
    yazfilehttp = open("Http.txt","a+")
    yazfilehttp.write()

def httpChecker(ip,port,sayı):
    try:
        httpproxy = "http://"+ip+":"+port
        httpsproxy = "http://"+ip+":"+port
        proxies = {
        "http": httpproxy,
        "https": httpsproxy,
        }
        time.sleep(random.uniform(1, 3))
        #url = "https://ifconfig.co/json"
        #url = "http://ifconfig.io/all.json"
        url = "http://info.cern.ch/favicon.ico"
        baslangıctime= time.time()*1000
        git = requests.get(url = url,proxies=proxies, timeout=3)
        bitistime= time.time()*1000
        time.sleep(0.5)
        if git.status_code==200 or git.status_code==403:
            ıcerık = ip+":"+port+"\n"
            dosyayaz(ıcerık)
            #yazfilehttp.write(ip+":"+port+"\n")
            print(Fore.GREEN + f"{sayı}      {int(bitistime-baslangıctime)}ms Status Code : {git.status_code} İp Addr : {ip+':'+port}")
        else:
            print(Fore.RED + f"{sayı}     {int(bitistime-baslangıctime)}ms Status Code : {git.status_code} İp Addr : {ip+':'+port}")
    except:
        pass

print("basladı")


for i in range(len(proxylist)):
    try:
        proxy = proxylist[i].split(":")
        ip = proxy[0]
        port = proxy[1] 
        sayı=i
        t1 = threading.Thread(target = httpChecker, args = (ip,port,sayı,))
        t1.daemon=False
        time.sleep(0.04)
        #print("basladı",i)
        t1.start()
        if i%50== 0:
            time.sleep(1)
        #t1.join()
    except:
        print("hata var")
        pass
