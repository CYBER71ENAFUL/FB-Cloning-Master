import os
import time

def banner():
    os.system("clear")
    print("\033[1;36m")
    print("====================================")
    print("      CYBER 71 ENAFUL STYLE TOOL")
    print("====================================")

def style_menu():
    print("\nSelect Style\n")
    print("[01] Hacker Style")
    print("[02] Matrix Style")
    print("[03] Cyberpunk Style")
    print("[04] Minimal Style")
    print("[05] Neon Style")
    print("[06] Dark Mode")
    print("[07] Classic Terminal")
    print("[08] Blue Theme")
    print("[09] Red Theme")
    print("[10] Green Theme")
    print("[00] Exit\n")

while True:
    banner()
    style_menu()

    choice = input("Select Style : ")

    if choice == "01":
        print("Hacker Style Activated")
        time.sleep(2)

    elif choice == "02":
        print("Matrix Style Activated")
        time.sleep(2)

    elif choice == "03":
        print("Cyberpunk Style Activated")
        time.sleep(2)

    elif choice == "04":
        print("Minimal Style Activated")
        time.sleep(2)

    elif choice == "05":
        print("Neon Style Activated")
        time.sleep(2)

    elif choice == "00":
        print("Exit Tool")
        break

    else:
        print("Invalid Option")
        time.sleep(1)
