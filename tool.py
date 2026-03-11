import os
import time

def banner():
    os.system("clear")
    print("\033[1;36m")
    print("====================================")
    print("        CYBER 71 ENAFUL TOOL")
    print("====================================")

while True:
    banner()

    print("[01] Hacker Style")
    print("[02] Matrix Style")
    print("[03] Cyber Style")
    print("[04] Minimal Style")
    print("[00] Exit")

    choice = input("\nSelect Style : ")

    if choice == "01":
        print("Hacker Style Activated")
        time.sleep(2)

    elif choice == "02":
        print("Matrix Style Activated")
        time.sleep(2)

    elif choice == "03":
        print("Cyber Style Activated")
        time.sleep(2)

    elif choice == "04":
        print("Minimal Style Activated")
        time.sleep(2)

    elif choice == "00":
        print("Exit Tool")
        break

    else:
        print("Invalid Option")
        time.sleep(1)
