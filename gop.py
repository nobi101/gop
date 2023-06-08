from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
from datetime import datetime
os.system('title TOOL GỘP FRTVE-TOOL')

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def logo():
        os.system("cls" if os.name == "nt" else "clear")
        logo=f"""Copyright © FRIVE-Tool 2023 | Version 1.1\n"""
        print('   ███████╗██████╗ ██╗██╗   ██╗███████╗')
        print('   ██╔════╝██╔══██╗██║██║   ██║██╔════╝')
        print('   █████╗  ██████╔╝██║██║   ██║█████╗  ')
        print('   ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ')
        print('   ██║     ██║  ██║██║ ╚████╔╝ ███████╗')
        print('   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝')
        print(logo)

os.system("cls" if os.name == "nt" else "clear")
logo()
a=now.strftime("%d")
h=int(now.strftime("%d"))
ngay_trc=h-1
b=now.strftime("%m")
day=now.strftime("%d-%m-%Y")
today=now.strftime("%d-%m-%Y")
d=now.strftime("%d-%m")
ngay=int(strftime('%d'))
os.system("cls" if os.name == "nt" else "clear") 
logo()
key1=str(ngay*16579923123456+123456789123456)
key2='FRIVE8-6'
long_url=(f"https://toolfree.elementfx.com/index.html?key={key1}")
api_token='53391e62b871e9c387067f2eada54c276a7c3e85'
web1s=requests.get(f'https://octolinkz.com/api?api={api_token}&url={long_url}').json()
if web1s['status']=="error": 
        print(web1s['message'])
        quit()
else:
        link_key=web1s['shortenedUrl']
file_key=f'key_ngay{ngay_hom_nay}.txt'
file_key_cu=f'key_ngay{ngay_trc}.txt'
check_file_key=os.path.exists(file_key)
if check_file_key == False:
   print(f'[LINK KEY: {link_key}')
   while(True):
      ma = input(f"NHẬP KEY NGÀY {today}: ")
      if ma == key1 or ma == key2:
         print(f'KEY ĐÚNG')
         luu=open(file_key, 'a+')
         luu.write(ma)
         luu.close()
         break
      elif ma != key1 or ma != key2:
         print(f'KEY SAI')
elif check_file_key == True:
    print(f'ĐANG LẤY KEY...',end='\r')
    sleep(1)
    k=open(file_key, 'r')
    ma=k.read()
    k.close()
    if ma == key1 or ma == key2:
        print(f'LẤY KEY THÀNH CÔNG', end = '\r');sleep(1); print('                                                       ', end = '\r')
        sleep(0.5)
    elif ma != key1 or ma != key2:
        if os.path.exists(file_key_cu) == True:
            os.remove(file_key_cu)
        os.remove(file_key)
        print(f'KEY SAI', end = '\r');sleep(1); print('                                                       ', end = '\r')
        print(f'[LINK KEY: {link_key}]')
        while(True):
            ma=input(f"NHẬP KEY NGÀY {today}: ")
            if ma == key1 or ma == key2:
                print(f'KEY ĐÚNG')
                luu=open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key1 or ma != key2:
                print(f'KEY SAI')
os.system("cls" if os.name == "nt" else "clear") 

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
print('             ███████╗██████╗ ██╗██╗   ██╗███████╗')
print('             ██╔════╝██╔══██╗██║██║   ██║██╔════╝')
print('             █████╗  ██████╔╝██║██║   ██║█████╗  ')
print('             ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ')
print('             ██║     ██║  ██║██║ ╚████╔╝ ███████╗')
print('             ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝')
print('           Copyright © FRIVE-Tool 2023 | Version 1.1')
print(f"                Ngày: {ngay_hom_nay} Tháng: {thang_nay} Năm: {nam_}\n")
print("┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print("│ STT │             MENU TOOL              │ STATUS  │ VERSION │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  1  │ TRAODOISUB                         │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  2  │ TUONGTACCHEO                       │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  3  │ TIỆN ÍCH                           │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  4  │ PAGE PROFILE                       │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  5  │ THOÁT TOOL                         │   =.=   │   NEXT  │")
print("└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input("Nhập Lựa Chọn: ")
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get('https://raw.githubusercontent.com/nobi101/d/main/d.py').text
        elif chon == '2':
                run = requests.get('https://raw.githubusercontent.com/nobi101/c/main/c.py').text
        elif chon == '3':
                run = requests.get('https://raw.githubusercontent.com/nobi101/e/main/e.py').text
        elif chon == '4':
                run = requests.get('https://raw.githubusercontent.com/nobi101/b/main/b.py').text
        elif chon == '5':
                run = requests.get('https://raw.githubusercontent.com/nobi101/exit/main/exit.py').text
        else:
                run = print('Lựa Chọn Không Xác Định')
except:
        if not is_connected():
                print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
        else:
                print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
        exit()
exec(run)
