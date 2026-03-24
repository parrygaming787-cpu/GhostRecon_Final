#!/usr/bin/env python3
# GhostRecon Final
# Vollgepackt, Rainbow-Banner, Hack Mode, Live Monitor, Disk Usage, File Finder, Netzwerk, Logging

import os
import platform
import time
import random
import subprocess
import socket
from colorama import Fore, Style, init
import psutil
import requests

# Initialize colorama
init(autoreset=True)

LOG_FILE = "logs/ghostrecon.log"
RAINBOW = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# Logging Funktion
def log(action):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.asctime()}: {action}\n")

# Rainbow Banner
def rainbow_banner(text):
    banner_lines = text.split("\n")
    for i, line in enumerate(banner_lines):
        color = RAINBOW[i % len(RAINBOW)]
        print(color + line + Style.RESET_ALL)
    print(Fore.CYAN + "GhostRecon Final - Ultimate Legal Hacker Toolkit\n" + Style.RESET_ALL)

# ASCII Banner
BANNER_TEXT = r"""
  ____ _               _   ____                     
 / ___| |__   ___  ___| |_|  _ \ __ _ _ __ ___  ___ 
| |  _| '_ \ / _ \/ __| __| |_) / _` | '__/ __|/ _ \
| |_| | | | |  __/ (__| |_|  __/ (_| | |  \__ \  __/
 \____|_| |_|\___|\___|\__|_|   \__,_|_|  |___/\___|
"""

# Clear Screen
def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# System Info
def system_info():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] SYSTEM INFO\n" + Style.RESET_ALL)
    print("User:", os.getlogin())
    print("OS:", platform.system(), platform.release())
    print("CPU Cores:", psutil.cpu_count())
    print("RAM Total:", round(psutil.virtual_memory().total / (1024**3),2), "GB")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    log("System Info displayed")
    input("\nPress Enter to return to menu...")

# Live Monitor
def live_monitor():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] LIVE SYSTEM MONITOR (CTRL+C to exit)\n" + Style.RESET_ALL)
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            print(f"CPU: {cpu}% | RAM: {ram}%      ", end="\r")
    except KeyboardInterrupt:
        log("Live Monitor exited")
        input("\nPress Enter to return to menu...")

# Disk Usage
def disk_usage():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] DISK USAGE\n" + Style.RESET_ALL)
    partitions = psutil.disk_partitions()
    for p in partitions:
        usage = psutil.disk_usage(p.mountpoint)
        print(f"{p.device}: {round(usage.used / (1024**3),2)}GB / {round(usage.total / (1024**3),2)}GB used")
    log("Disk Usage displayed")
    input("\nPress Enter to return to menu...")

# Network Info
def network_info():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] NETWORK INFO\n" + Style.RESET_ALL)
    try:
        if platform.system() == "Linux":
            subprocess.run(["ip", "a"])
        elif platform.system() == "Windows":
            subprocess.run(["ipconfig"])
        public_ip = requests.get("https://api.ipify.org").text
        print("\nPublic IP:", public_ip)
    except:
        print("Could not fetch network info")
    log("Network Info displayed")
    input("\nPress Enter to return to menu...")

# Port Scan localhost
def port_scan():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] PORT SCAN (localhost)\n" + Style.RESET_ALL)
    try:
        if platform.system() == "Linux":
            subprocess.run(["ss", "-tuln"])
        elif platform.system() == "Windows":
            subprocess.run(["netstat", "-ano"])
    except Exception as e:
        print("Error:", e)
    log("Port Scan executed")
    input("\nPress Enter to return to menu...")

# Local Network Scan
def local_network_scan():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] LOCAL NETWORK SCAN (192.168.1.1-50)\n" + Style.RESET_ALL)
    for ip in range(1, 51):
        addr = f"192.168.1.{ip}"
        result = subprocess.run(["ping", "-c", "1", "-W", "1", addr], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(Fore.GREEN + f"[+] Device found: {addr}" + Style.RESET_ALL)
            log(f"Device online: {addr}")
    input("\nPress Enter to return to menu...")

# WLAN Scan (Linux only)
def wlan_scan():
    if platform.system() != "Linux":
        print("WLAN Scan is only supported on Linux.")
        input("\nPress Enter to return to menu...")
        return
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] SCANNING WLANs (legal!)\n" + Style.RESET_ALL)
    subprocess.run("sudo iwlist scan | grep ESSID", shell=True)
    log("WLAN Scan executed")
    input("\nPress Enter to return to menu...")

# File Finder
def file_finder():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] FILE FINDER\n" + Style.RESET_ALL)
    filename = input("Enter filename to search: ")
    for root, dirs, files in os.walk("."):
        if filename in files:
            print(Fore.GREEN + f"Found: {os.path.join(root, filename)}" + Style.RESET_ALL)
            log(f"File found: {os.path.join(root, filename)}")
    input("\nPress Enter to return to menu...")

# Password Checker (own files)
def password_checker():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] PASSWORD CHECKER\n" + Style.RESET_ALL)
    path = input("Enter file path: ")
    if os.path.isfile(path):
        with open(path, "r") as f:
            lines = f.readlines()
            print(f"File has {len(lines)} lines")
            log(f"Password check: {path}")
    else:
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        log(f"Password check failed: {path}")
    input("\nPress Enter to return to menu...")

# Hack Mode Animation
def hack_mode():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.RED + "[!] HACK MODE ACTIVATED...\n" + Style.RESET_ALL)
    for i in range(80):
        print(random.choice(["#", "@", "%", "&", "*", "$"]), end="", flush=True)
        time.sleep(0.03)
    print("\nDone 😏")
    log("Hack Mode executed")
    input("\nPress Enter to return to menu...")

# Command Mode
def command_mode():
    clear()
    rainbow_banner(BANNER_TEXT)
    print(Fore.YELLOW + "[+] COMMAND MODE (type 'exit' to return)\n" + Style.RESET_ALL)
    while True:
        cmd = input("ghostrecon> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        try:
            output = subprocess.getoutput(cmd)
            print(output)
            log(f"Command executed: {cmd}")
        except Exception as e:
            print("Error:", e)

# Main Menu
def main_menu():
    while True:
        clear()
        rainbow_banner(BANNER_TEXT)
        print(Fore.GREEN + "1. System Info")
        print("2. Network Info")
        print("3. Port Scan")
        print("4. Local Network Scan")
        print("5. WLAN Scan")
        print("6. Disk Usage")
        print("7. File Finder")
        print("8. Password Checker")
        print("9. Live Monitor")
        print("10. Hack Mode 😏")
        print("11. Command Mode")
        print(Fore.RED + "0. Exit" + Style.RESET_ALL)
        choice = input("\nSelect option: ")
        if choice == "1": system_info()
        elif choice == "2": network_info()
        elif choice == "3": port_scan()
        elif choice == "4": local_network_scan()
        elif choice == "5": wlan_scan()
        elif choice == "6": disk_usage()
        elif choice == "7": file_finder()
        elif choice == "8": password_checker()
        elif choice == "9": live_monitor()
        elif choice == "10": hack_mode()
        elif choice == "11": command_mode()
        elif choice == "0": log("GhostRecon exited"); break
        else: print(Fore.RED + "Invalid option!"); time.sleep(1)

# Start
if __name__ == "__main__":
    main_menu()
