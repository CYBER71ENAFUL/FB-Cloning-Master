import os
import time
import sys

def banner():
    os.system('clear')
    print("\033[1;36m" + " ="*25)
    print("\033[1;31m" + "   ______     ______  ______ _____   ")
    print("  / ___\ \   / / __ )| ____|  _  \  ")
    print(" | |    \ \_/ /|  _  \|  _| | |_| | ")
    print(" | |___  \   / | |_) | |___|  _  /  ")
    print("  \____|  |_|  |____/|_____|_| \_\  ")
    print("\033[1;32m" + "           CYBER 71 ENAFUL")
    print("\033[1;36m" + " ="*25)
    print("\033[1;37m" + " OWNER   : CYBER 71 ENAFUL")
    print(" TOOL    : FB CLONING MASTER")
    print(" VERSION : 2.0 (STABLE)")
    print("\033[1;36m" + " ="*25)
    print(" Hello Enaful | My First Python Tool")

def run_command(cmd):
    print(f"\n\033[1;33m[!] কমান্ড রান হচ্ছে: {cmd}")
    time.sleep(2)
    os.system(cmd)

def menu():
    banner()
    print("\033[1;32m [01] FB Cloning (Method 1)")
    print(" [02] FB Auto Report")
    print(" [03] Update Termux")
    print(" [00] Exit Tool")
    print("\033[1;36m" + " ="*25)
    
    choice = input("\n\033[1;33m [?] আপনার চয়েস দিন: \033[1;37m")
    
    if choice == '01' or choice == '1':
        # এখানে আপনার আসল ফাইলে যদি অন্য কোনো স্ক্রিপ্ট থাকে তবে সেটির নাম দিন
        # ধরুন আপনার ক্লোনিং ফাইলের নাম 'clone.py', তাহলে লিখবেন run_command("python clone.py")
        print("\n\033[1;32m[!] আপনার ক্লোনিং লজিক এখানে শুরু হবে...")
        time.sleep(1)
        
    elif choice == '03' or choice == '3':
        run_command("pkg update && pkg upgrade -y")
        
    elif choice == '00' or choice == '0':
        print("\n\033[1;31m[!] আল্লাহ হাফেজ!")
        sys.exit()
    else:
        menu()

if __name__ == "__main__":
    menu()
