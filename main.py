import os
import sys
import requests
from datetime import datetime
from pyfiglet import Figlet
import colorama
from colorama import Fore
os.system("clear")
colorama.init()


def get_ip_address():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data['ip']
        return ip
    except Exception as e:
        return f'Error fetching IP: {e}'


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        country = data.get('country', 'Unknown')
        return country
    except Exception as e:
        return f'Error fetching country info: {e}'


def print_banner():
    figlet = Figlet(font="standard")
    banner = figlet.renderText("OnionHost")
    print(Fore.GREEN + banner)
    print(Fore.BLUE + "[-] OnionHost Allowed To Host Your Website On Darkweb")
    print(Fore.GREEN + "[+] Made By BlackHat-Abhi")
    print(Fore.CYAN + "[=] OnionHost Tools Version : 1.0\n\n")  


    ip_address = get_ip_address()
    country = get_ip_info(ip_address)
    current_datetime = get_current_datetime()


    print(Fore.YELLOW + "Your IP: " + Fore.GREEN + f"{ip_address}")
    print(Fore.YELLOW + "Your Country: " + Fore.GREEN + f"{country}")
    print(Fore.YELLOW + "Date & Time: " + Fore.GREEN + f"{current_datetime}")


def run_termux_host():
    os.system('python3 TermuxOnionHost.py')


def run_linux_host():
    os.system('python3 LinuxOnionHost.py')


def display_social_media():
    while True:
        print_banner()
        print(Fore.MAGENTA + "\nSocial Media Contacts:")
        print(Fore.YELLOW + "1. Telegram")
        print(Fore.YELLOW + "2. WhatsApp")
        print(Fore.YELLOW + "3. Instagram")
        print(Fore.YELLOW + "4. GitHub")
        print(Fore.RED + "5. Back to Main Menu")

        choice = input(Fore.WHITE + "Enter your choice: ").strip()

        if choice == '1':
            os.system('xdg-open https://telegram.me/BlackEagle_Sec')  
        elif choice == '2':
            os.system('xdg-open https://whatsapp.com/channel/0029Va9G5SOHFxOt0W2QRn10')
        elif choice == '3':
            os.system('xdg-open https://instagram.com/blackhat_abhi')  
        elif choice == '4':
            os.system('xdg-open https://github.com/BlackHat-Abhi') 
        elif choice == '5':
            return
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")


def main():
    while True:
        print_banner()
        print(Fore.CYAN + "\nChoose an option:")
        print(Fore.GREEN + "1. Termux")
        print(Fore.GREEN + "2. Linux")
        print(Fore.GREEN + "3. Contect Us")
        print(Fore.RED + "4. Exit")
        
        choice = input(Fore.WHITE + "Enter your choice: ").strip()
        
        if choice == '1':
            run_termux_host()
        elif choice == '2':
            run_linux_host()
        elif choice == '3':
            display_social_media()
        elif choice == '4':
            print(Fore.RED + "Exiting...")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
