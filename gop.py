import requests, json, os, sys
from sys import platform
from datetime import datetime        
from time import sleep,strftime
try:from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:os.system('pip install pystyle'); from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
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
print('[•] Key Free 5 ngày: free 5day')
print("┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print("│ STT │             MENU TOOL              │ STATUS  │ VERSION │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  1  │ SERVER FREE                        │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  2  │ SERVER MẤT PHÍ                     │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  5  │ THOÁT TOOL                         │   =.=   │   NEXT  │")
print("└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input('CHỌN: ')
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get('https://raw.githubusercontent.com/nobi101/gop_free/main/gop_free.py').text
        elif chon == '2':
                run = requests.get('https://raw.githubusercontent.com/nobi101/gop_phi/main/gop_phi.py').text
        else:
                run = print('Lựa Chọn Không Xác Định')
except:
        if not is_connected():
                print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
        else:
                print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
        exit()
exec(run)
