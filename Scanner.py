import os
import socket
import asyncio
import re
import sys
import requests
import subprocess
import pyfiglet
from termcolor import colored
from scapy.all import *

# ✅ Common ports for normal scan (ordered)
COMMON_PORTS = sorted([21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 5900, 8080])

# ✅ Timeout settings for ultra-fast scans
TIMEOUT = 0.02  

# ✅ Function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ✅ Show ASCII banner
def show_banner():
    clear_screen()
    ascii_logo = pyfiglet.figlet_format("ABU'S TOOLS")
    print(colored(ascii_logo, "green"))
    print(colored("Developed by: Abubakar Bello", "cyan"))
    print(colored("Contact: abubakarbello3914@gmail.com | +2347042725224", "yellow"))
    print(colored("Special Thanks: Suryansh Gupta | syhsrthrug@gmail.com | +919839486431", "magenta"))
    print("=" * 60)

# ✅ OS Detection (Windows/Linux)
def detect_os(ip):
    try:
        pkt = sr1(IP(dst=ip)/ICMP(), timeout=1, verbose=0)
        if pkt:
            return "Linux" if pkt.ttl <= 64 else "Windows"
        return "Unknown"
    except:
        return "Unknown"

# ✅ Asynchronous function for scanning ports
async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.write(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        await writer.drain()
        response = await reader.read(1024)
        writer.close()
        await writer.wait_closed()

        service = socket.getservbyport(port, "tcp") if port <= 1024 else "Unknown"
        match = re.search(r"Server:\s(.+)", response.decode(errors="ignore"))
        version = match.group(1) if match else "Unknown Version"

        return {
            "port": port,
            "service": service,
            "version": version
        }
    except:
        return None

# ✅ WAN Scan (Normal & High Scan)
async def wan_scan():
    target = input(colored("\nEnter the target domain/IP: ", "yellow"))
    ip = socket.gethostbyname(target)
    os_type = detect_os(ip)
    print(colored(f"\n[+] Target OS: {os_type}", "cyan"))

    print(colored("\n[1] Normal Scan (Common Ports)", "yellow"))
    print(colored("[2] High Scan (All Ports 1-65535)", "yellow"))
    print(colored("[3] Back", "red"))

    scan_choice = input(colored("\nChoose scan type: ", "cyan"))

    if scan_choice == "1":
        max_ports = int(input(colored("\nEnter the number of ports to scan (max 20): ", "cyan")))
        ports_to_scan = COMMON_PORTS[:max_ports]
        print(colored(f"\nScanning {target} ({ip}) - Normal Scan...", "green"))
    elif scan_choice == "2":
        max_ports = int(input(colored("\nEnter the number of ports to scan (max 65535): ", "cyan")))
        ports_to_scan = range(1, max_ports + 1)
        print(colored(f"\nScanning {target} ({ip}) - High Scan...", "red"))
    elif scan_choice == "3":
        return
    else:
        print(colored("\n[!] Invalid choice!", "red"))
        return

    results = await asyncio.gather(*[scan_port(ip, port) for port in ports_to_scan])
    results = [res for res in results if res]  # Remove None values

    print(colored("\nScan Completed!\n", "cyan"))
    for res in results:
        print(colored(f"[+] Open Port: {res['port']}", "yellow"))
        print(colored(f"    ├─ Service: {res['service']}", "cyan"))
        print(colored(f"    ├─ Version: {res['version']}", "cyan" if res['version'] != "Unknown Version" else "red"))

    input(colored("\nPress Enter to go back...", "yellow"))  # Back option

# ✅ LAN Scan (Local Network)
async def lan_scan():
    ip_range = input(colored("\nEnter the local network range (e.g., 192.168.1.0/24): ", "yellow"))
    print(colored("\n[+] Scanning LAN for active devices...", "green"))
    os.system(f"nmap -sn {ip_range}")

    input(colored("\nPress Enter to go back...", "yellow"))  # Back option

# ✅ Main menu
def main_menu():
    while True:
        show_banner()
        print(colored("\n[1] WAN Scan (Scan Internet Targets)", "yellow"))
        print(colored("[2] LAN Scan (Scan Local Network)", "yellow"))
        print(colored("[3] Install Metasploit Framework", "yellow"))
        print(colored("[4] Run Metasploit", "yellow"))
        print(colored("[5] Exit", "red"))

        choice = input(colored("\nChoose an option: ", "cyan"))
        
        if choice == "1":
            asyncio.run(wan_scan())
        elif choice == "2":
            asyncio.run(lan_scan())
        elif choice == "3":
            install_metasploit()
        elif choice == "4":
            run_metasploit()
        elif choice == "5":
            print(colored("\nExiting... Goodbye!", "red"))
            sys.exit()
        else:
            print(colored("\nInvalid choice!", "red"))

# ✅ Start the tool
if __name__ == "__main__":
    main_menu()
