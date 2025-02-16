import os
import subprocess
import time
from http.server import SimpleHTTPRequestHandler
import socketserver
import sys
import requests
from datetime import datetime

# Color codes for banner and text
lime = "\033[92m"  # Hacker-style green
white = "\033[97m"
cyan = "\033[96m"  # Cyan for specific text
pur = "\033[95m"   # Purple/Magenta for the border
reset = "\033[0m"
plus = "\033[92m"  # Green for [+] symbol
yellow = "\033[93m"  # Yellow color for input prompt
red = "\033[91m"  # Red color for onion address
blue = "\033[94m"  # Blue color for specific text
cyan = "\033[96m"  # Cyan color for serving message
magenta = "\033[35m"  # Magenta color for user input

# Password to access the tool
PASSWORD = "abhi"

# Function to fetch the IP address
def get_ip_address():
    try:
        # Fetch public IP address using the ipinfo.io API
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data['ip']
        return ip
    except Exception as e:
        return f'Error fetching IP: {e}'

# Function to fetch the current date and time
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS

# Function to fetch IP info (like full country name) using ip-api.com
def get_ip_info(ip):
    try:
        # Use ip-api.com API to fetch the details of the IP
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        country = data.get('country', 'Unknown')  # Fetch the full country name
        return country
    except Exception as e:
        return f'Error fetching country info: {e}'

# Banner function
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

# Help function
def help():
    sys.stdout.write(f"{pur}╔═════════════════════════════════════════╗\n")  # Magenta lines
    sys.stdout.write(f"{white}║{plus} [+] {cyan}Tool Name  : OnionHost              {white}║\n")
    sys.stdout.write(f"{pur}║{plus} [+] {cyan}Author     : BlackHat-Abhi          {pur}║\n")
    sys.stdout.write(f"{white}║{plus} [+] {cyan}Team       : Black Eagle Security 🦅{white}║\n")
    sys.stdout.write(f"{pur}╚═════════════════════════════════════════╝\n\n")  # Magenta lines
    sys.stdout.write(reset)

    # Fetch and print the IP address, country, and current date-time after the banner
    ip_address = get_ip_address()
    current_datetime = get_current_datetime()
    country = get_ip_info(ip_address)
    
    sys.stdout.write(f"{cyan}Your IP : {yellow}{ip_address}{reset} {blue} | Your Country: {yellow}{country}{reset} | {blue}Date & Time: {yellow}{current_datetime}{reset}\n\n\n\n")
    

# Function to start the HTTP server
def start_http_server(directory, port=8080):
    os.chdir(directory)  # Change to the website directory

    handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"{cyan}SERVING WEBSITE ON PORT {port}{reset}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("Server stopped")

# Function to setup and start Tor hidden service
def start_tor_hidden_service(torrc_path):
    print(f"{lime}Starting Tor service...{reset}")
    tor_process = subprocess.Popen(["tor", "-f", torrc_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the hostname file to be created by Tor
    onion_address_file = "/data/data/com.termux/files/home/tor-hidden-service/hostname"
    while not os.path.exists(onion_address_file):
        print("Waiting for .onion address...")
        time.sleep(2)  # Wait for Tor to generate the onion address

    # Read and return the .onion address
    with open(onion_address_file, 'r') as f:
        onion_address = f.read().strip()
    
    return onion_address, tor_process

# Main function to start the whole process
def host_darkweb_site():
    # Ask for the password
    entered_password = input(f"{cyan}ENTER PASSWORD : {reset}").strip()
    os.system("clear")
    
    if entered_password != PASSWORD:
        print(f"{pur}INCORRECT PASSWORD! ACCESS DENIED.{reset}")
        return
    
    # Print the banner first
    title()

    # Print help information about the tool
    help()

    # Ask for the website folder path
    website_directory = input(f"{yellow}ENTER THE PATH TO YOUR WEBSITE FOLDER: {reset}").strip()
    sys.stdout.write(magenta)  # Set magenta color for user input
    torrc_path = "/data/data/com.termux/files/home/torrc"
    sys.stdout.write(reset)  # Reset the color after user input

    # Start the Tor hidden service
    onion_address, tor_process = start_tor_hidden_service(torrc_path)
    
    # Corrected print statement to display the .onion address only once
    print(f"{blue}YOUR DAKKWEB WEBSITE LINK :{reset} {red}{onion_address}{reset}")

    # Start the HTTP server to host the website
    start_http_server(website_directory)

    # Stop Tor when done
    tor_process.terminate()

if __name__ == "__main__":
    host_darkweb_site()
