import os
import time
import sys

def banner():

    os.system('clear')
    # সায়ান এবং লাল রঙের কম্বিনেশন
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

def run_command(cmd):
    print(f"\n\033[1;33m[!] কমান্ড রান হচ্ছে: {cmd}")
    time.sleep(2)
    os.system(cmd)

def menu():
    banner()
    print("\033[1;32m [01] FB Cloning (File/UID Method)")
    print(" [02] FB Auto Report (Experimental)")
    print(" [03] Update Termux Packages")
    print(" [00] Exit Tool")
    print("\033[1;36m" + " ="*25)
    
    choice = input("\n\033[1;33m [?] আপনার চয়েস দিন: \033[1;37m")
    
    if choice == '01' or choice == '1':
        print("\n\033[1;32m[!] আপনার গিটহাব ক্লোনিং স্ক্রিপ্ট লোড হচ্ছে...")
        # এখানে আপনি যে গিটহাব টুলটি ব্যবহার করতে চান তার কমান্ড দিতে পারেন
        # উদাহরণ হিসেবে একটি কমন কমান্ড দেওয়া হলো:
        run_command("python -c 'print(\"Cloning process started...\")'") 
        
    elif choice == '02' or choice == '2':
        run_command("pkg install git -y && git clone https://github.com/Example/Report-Tool")
        
    elif choice == '03' or choice == '3':
        run_command("pkg update && pkg upgrade -y")
        
    elif choice == '00' or choice == '0':
        print("\n\033[1;31m[!] আল্লাহ হাফেজ, CYBER 71 ENAFUL!")
        sys.exit()
    else:
        print("\n\033[1;31m[!] ভুল ইনপুট!")
        time.sleep(2)
        menu()

if __name__ == "__main__":
    menu()
print("Hello Enafule")
print("My First Python Tool")
