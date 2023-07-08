from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
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
from datetime import datetime
import datetime
from pystyle import Colors, Colorate
os.system('title TOOL GỘP FRTVE-TOOL')

def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
        
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
        print('[•] Zalo group: https://zalo.me/g/cdcazh320')
        print('[•] Email: fivetool.official@gmail.com')
        print('[•] Youtube: https://www.youtube.com/@TOOLFRIVE')
        
              

os.system("cls" if os.name == "nt" else "clear")
logo()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def find_listlink(url):
    response = requests.get(url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    listlink = []

    for link in links:
        link_url = link.get('href')
        if link_url and f'{url}/2023/' in link_url:
            link_response = requests.get(link_url)
            link_response.raise_for_status()

            link_soup = BeautifulSoup(link_response.text, 'html.parser')
            key_container = link_soup.find('div', id='get-key-container')
            key_button = link_soup.find('button', id='get-key-btn', string='Lấy key')

            if key_container and key_button:
                listlink.append(link_url)

    return listlink

ngay=int(strftime('%d'))
key1 = str(ngay * 24122006 + 2412260144)
key2 = 'FRIVE_ANH_50D'
key = '00000' + key1
if not os.path.exists('key.txt'):
    print(" ")
    print("Tạo Key Hơi Lâu Anh Em Thông Cảm")
    url = 'https://webkeyfree.blogspot.com'
    key_links = find_listlink(url)
    random_url = random.choice(key_links)
    encoded_key = base64.b64encode(key.encode()).decode()
    formatted_url = f'{random_url}?key={encoded_key}'
    token_link1s = '68fbb912babb9890428ecd33804f4cd8528d7bfe'
    link1s = requests.get(f'https://link1s.com/api?api={token_link1s}&url={formatted_url}').json()
    if link1s['status']=="error":
        print(link1s['message']+'')
        quit()
    else:
        link_key=link1s['shortenedUrl']
    print(f"""Link Vượt Key: {link_key} """)
    password = input('Nhập Key: ')
    with open('key.txt', 'w') as f:
        f.write(password)

with open('key.txt', 'r') as f:
    password = f.read()

if password == key or key2:
    print('Key hợp lệ.')
else:
    print('Key không hợp lệ. Xin thử lại.')
    os.remove('key.txt')
    quit()
clear()

print('             ███████╗██████╗ ██╗██╗   ██╗███████╗')
print('             ██╔════╝██╔══██╗██║██║   ██║██╔════╝')
print('             █████╗  ██████╔╝██║██║   ██║█████╗  ')
print('             ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ')
print('             ██║     ██║  ██║██║ ╚████╔╝ ███████╗')
print('             ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝')
print('           Copyright © FRIVE-Tool 2023 | Version 1.1')
print('[•] Zalo group: https://zalo.me/g/cdcazh320')
print('[•] Email: fivetool.official@gmail.com')
print('[•] Youtube: https://www.youtube.com/@TOOLFRIVE')
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
