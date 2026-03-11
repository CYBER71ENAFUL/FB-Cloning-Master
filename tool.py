import os
import time

def banner():
    os.system('clear')
    print("\033[1;36m==============================")
    print("\033[1;32m      FB CLONING MASTER       ")
    print("\033[1;36m==============================")

def main():
    banner()
    print("[01] File Cloning")
    print("[02] UID Cloning")
    print("[00] Exit")
    
    choice = input("\n[?] মেথড সিলেক্ট করুন: ")
    
    if choice == '1':
        file = input("[?] ফাইলের পাথ দিন (যেমন: /sdcard/ids.txt): ")
        if os.path.exists(file):
            print(f"\n[+] {file} ফাইলটি লোড হচ্ছে...")
            # এখানে আপনার আসল ক্লোনিং স্ক্রিপ্টের কমান্ড দিন
            # যেমন: os.system('python clone.py ' + file)
        else:
            print("\n[!] এরর: ফাইলটি পাওয়া যায়নি!")
            
    elif choice == '2':
        uid = input("[?] UID দিন: ")
        print(f"\n[+] {uid} এর উপর ক্লোনিং শুরু হচ্ছে...")
        # এখানে আপনার ক্লোনিং লজিক বসবে
        
    elif choice == '0':
        exit()
    else:
        print("[!] ভুল ইনপুট!")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
