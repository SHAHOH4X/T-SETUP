#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time
from rich.panel import Panel
from rich.console import Console

console = Console()

# ----------------- CLEAR ----------------- #
def clear():
    os.system("clear")

# ----------------- FEMALE ENGLISH VOICE ----------------- #
def speak(text):
    os.system(f'espeak -v en+f3 -s 135 "{text}" >/dev/null 2>&1')

# ----------------- ANIMATED ASCII LOGO ----------------- #
def animated_logo():
    clear()
    logo_text = [
        "  _____ _______ _______ ______ ",
        " / ____|__   __|__   __|  ____|",
        "| (___    | |     | |  | |__   ",
        " \\___ \\   | |     | |  |  __|  ",
        " ____) |  | |     | |  | |____ ",
        "|_____/   |_|     |_|  |______|",
        "",
        "        OWNER : SHAHOH4X"
    ]
    for line in logo_text:
        console.print(f"[bold cyan]{line}[/bold cyan]")
        time.sleep(0.15)

    speak("Welcome to Termux setup tool. Owner Shahoh four X.")
    time.sleep(1.5)

# ----------------- INSTALL WITH RGB + VOICE ----------------- #
def install_pkg(name, cmd):
    speak(f"Installing {name}")

    colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    color = colors[int(time.time()) % len(colors)]

    with console.status(
        f"[blink][bold {color}]{name}[/bold {color}][/blink] Installing...",
        spinner="dots"
    ):
        os.system(cmd)

    console.print(f"✔ {name} completed", style="bold green")
    speak(f"{name} installation completed")

# ----------------- STORAGE ----------------- #
def setup_storage():
    storage_path = os.path.expanduser("~/storage")
    if not os.path.exists(storage_path):
        speak("Granting storage permission")
        os.system("termux-setup-storage")
    else:
        speak("Storage permission already granted")

# ----------------- BASIC SETUP ----------------- #
def basic_setup():
    print(Panel("[bold blue]BASIC INSTALL START IN 3 SECONDS[/bold blue]"))
    speak("Basic setup will start in three seconds")
    time.sleep(3)

    packages = [
        ("ESPEAK", "pip install python-espeak"),
        ("PKG UPDATE", "pkg update -y"),
        ("PKG UPGRADE", "pkg upgrade -y"),
        ("PYTHON", "pkg install python -y"),
        ("TMUX", "pkg install tmux -y"),
        ("REQUESTS", "pip install requests"),
        ("BS4", "pip install bs4"),
        ("RICH", "pip install rich"),
        ("PHP", "pkg install php -y")
    ]

    setup_storage()
    for name, cmd in packages:
        install_pkg(name, cmd)

    clear()
    speak("Basic setup completed successfully")

# ----------------- FULL SETUP ----------------- #
def full_setup():
    print(Panel("[bold red]FULL INSTALL START IN 3 SECONDS[/bold red]"))
    speak("Full setup will start in three seconds")
    time.sleep(3)

    packages = [
        ("PKG UPDATE", "pkg update -y"),
        ("PKG UPGRADE", "pkg upgrade -y"),
        ("PYTHON", "pkg install python -y"),
        ("WGET", "pkg install wget -y"),
        ("FISH", "pkg install fish -y"),
        ("RUBY", "pkg install ruby -y"),
        ("PHP", "pkg install php -y"),
        ("NMAP", "pkg install nmap -y"),
        ("BASH", "pkg install bash -y"),
        ("VIM", "pkg install vim -y"),
        ("TOR", "pkg install tor -y"),
        ("OPENSSL", "pkg install openssl -y")
    ]

    setup_storage()
    for name, cmd in packages:
        install_pkg(name, cmd)

    clear()
    speak("Full setup completed successfully")

# ----------------- CONTACTS ----------------- #
def contacts():
    clear()
    console.print(
        Panel(
            "[bold cyan]Facebook Contact[/bold cyan]\n\n"
            "Owner: SHAHOH4X\n"
            "Profile:\n"
            "https://www.facebook.com/md.shaharia.1675275",
            title="CONTACT"
        )
    )
    speak("Opening Facebook contact page")
    time.sleep(1)
    os.system("termux-open-url https://www.facebook.com/md.shaharia.1675275")
    input("\nPress Enter to return to menu...")

# ----------------- MENU ----------------- #
def menu():
    while True:
        clear()
        console.print("""
[1] Basic Setup
[2] Full Setup
[3] Contacts
[0] Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            basic_setup()
        elif choice == "2":
            full_setup()
        elif choice == "3":
            contacts()
        elif choice == "0":
            speak("Thank you for using this tool")
            sys.exit()
        else:
            speak("Invalid option")
            time.sleep(1)

# ----------------- CHECK PYTHON ----------------- #
def check_python():
    if os.system("command -v python3 >/dev/null 2>&1") != 0:
        print("Python3 required!")
        sys.exit(1)

# ----------------- START ----------------- #
if __name__ == "__main__":
    check_python()
    animated_logo()
    menu()
