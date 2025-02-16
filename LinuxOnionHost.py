import os
import subprocess
import time
from http.server import SimpleHTTPRequestHandler
import socketserver
import sys
import requests
from datetime import datetime

# Color codes for banner and text
lime = "\033[92m"
white = "\033[97m"
cyan = "\033[96m"
pur = "\033[95m"
reset = "\033[0m"
yellow = "\033[93m"
red = "\033[91m"
blue = "\033[94m"
green = "\033[92m"  # Green for IP and Country values

# **Password to access the tool**
PASSWORD = "abhi"

# Function to fetch IP address
def get_ip_address():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data['ip']
        return ip
    except Exception as e:
        return f'Error fetching IP: {e}'

# Function to fetch current date and time
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Function to fetch IP info (like full country name)
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        country = data.get('country', 'Unknown')
        return country
    except Exception as e:
        return f'Error fetching country info: {e}'

# Banner function (first banner)
def title():
    sys.stdout.write(f"{lime}                 ..\n")
    sys.stdout.write(f"                ,:\n")
    sys.stdout.write(f"        .      ::\n")
    sys.stdout.write(f"        .:    :2.\n")
    sys.stdout.write(f"         .:,  1L\n")
    sys.stdout.write(f"          .v: Z, ..::, \n")
    sys.stdout.write(f"           :k:N.Lv:\n")
    sys.stdout.write(f"            22ukL\n")
    sys.stdout.write(f"            JSYk.\n")
    sys.stdout.write(f"{white}           ,B@B@i\n")
    sys.stdout.write(f"           BO@@B@.\n")
    sys.stdout.write(f"         :B@L@Bv:@7\n")
    sys.stdout.write(f"       .PB@iBB@  .@Mi\n")
    sys.stdout.write(f"     .P@B@iE@@r  . 7B@i\n")
    sys.stdout.write(f"    5@@B@:NB@1{pur} r  ri:{white}7@M\n")
    sys.stdout.write(f"  .@B@BG.OB@B{pur}  ,.. .i,{white} MB,\n")
    sys.stdout.write(f"  @B@BO.B@@B {pur} i7777,{white}    MB.\n")
    sys.stdout.write(f" PB@B@.OB@BE  {pur}LririL,.L.{white} @P\n")
    sys.stdout.write(f" B@B@5iB@B@i  {pur}:77r7L, L7{white} O@\n")
    sys.stdout.write(f" @B1B27@B@B, {pur}. .:ii.  r7{white} BB\n")
    sys.stdout.write(f" O@.@M:B@B@: {pur}v7:    ::.{white}  BM\n")
    sys.stdout.write(f" :Br7@L5B@BO {pur}irL: :v7L.{white} P@,\n")
    sys.stdout.write(f"  7@,Y@UqB@B7 {pur}ir ,L;r:{white} u@7\n")
    sys.stdout.write(f"   r@LiBMBB@Bu   {pur}rr:.{white}:B@i\n")
    sys.stdout.write(f"     FNL1NB@@@@:   ;OBX\n")
    sys.stdout.write(f"       rLu2ZB@B@@XqG7\n")
    sys.stdout.write(f"          . rJuv::\n\n")
    sys.stdout.write(reset)

# Second banner and user information (IP, country, date, etc.)
def help_banner():
    sys.stdout.write(f"{pur}╔═════════════════════════════════════════╗\n")
    sys.stdout.write(f"{white}║{cyan} [+] {white}Tool Name  : OnionHost              {white}║\n")
    sys.stdout.write(f"{pur}║{cyan} [+] {white}Author     : BlackHat-Abhi          {pur}║\n")
    sys.stdout.write(f"{white}║{cyan} [+] {white}Team       : Black Eagle Security 🦅{white}║\n")
    sys.stdout.write(f"{pur}╚═════════════════════════════════════════╝\n\n")
    sys.stdout.write(reset)

    ip_address = get_ip_address()
    country = get_ip_info(ip_address)
    current_datetime = get_current_datetime()

    # Print IP, Country, and Date & Time on one line
    sys.stdout.write(f"{cyan}Your IP : {yellow}{green}{ip_address}{reset} | {blue}Your Country: {yellow}{green}{country}{reset} | {blue}Date & Time: {yellow}{green}{current_datetime}{reset}\n\n")

# Custom HTTP request handler
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def handle(self):
        try:
            super().handle()
        finally:
            pass

# Start the HTTP server
def start_http_server(directory, port=8080):
    os.chdir(directory)
    handler = CustomHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"{cyan}SERVING WEBSITE ON PORT {port}{reset}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("Server stopped")

# Start Tor hidden service
def start_tor_hidden_service(torrc_path):
    print(f"{lime}Starting Tor service...{reset}")
    tor_process = subprocess.Popen(["tor", "-f", torrc_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    onion_address_file = "/var/lib/tor/hidden_service/hostname"
    
    # Check if Tor is running and address file exists
    while not os.path.exists(onion_address_file):
        print("Waiting for .onion address...")
        time.sleep(2)
    
    with open(onion_address_file, 'r') as f:
        onion_address = f.read().strip()
    
    return onion_address, tor_process

# Main function
def host_darkweb_site():
    entered_password = input(f"{cyan}ENTER PASSWORD : {reset}").strip()
    os.system("clear")
    if entered_password != PASSWORD:
        print(f"{pur}INCORRECT PASSWORD! ACCESS DENIED.{reset}")
        return
    
    title()  # First banner
    help_banner()  # Second banner with IP, Country, Date & Time on one line
    
    website_directory = input(f"{yellow}ENTER THE PATH TO YOUR WEBSITE FOLDER: {reset}").strip()
    torrc_path = "/etc/tor/torrc"

    onion_address, tor_process = start_tor_hidden_service(torrc_path)
    
    print(f"{blue}YOUR DARKWEB WEBSITE LINK :{reset} {red}{onion_address}{reset}")
    start_http_server(website_directory)

    tor_process.terminate()

if __name__ == "__main__":
    host_darkweb_site()