import os
import time

def banner():
    os.system('clear')
    print("\033[1;36m" + " ="*25)
    print("\033[1;32m" + "   FB CLONING MASTER - CYBER 71")
    print("\033[1;36m" + " ="*25)

def clone_menu():
    banner()
    print("[01] File Cloning (File Method)")
    print("[02] UID Cloning (UID Method)")
    print("[00] Back")
    print("\033[1;36m" + " ="*25)
    
    choice = input("\n[?] আপনার মেথড সিলেক্ট করুন: ")
    
    if choice == '1' or choice == '01':
        file_path = input("\n[?] ফাইল পাথ দিন (যেমন: /sdcard/file.txt): ")
        if os.path.exists(file_path):
            print(f"\n[!] {file_path} থেকে ক্লোনিং শুরু হচ্ছে...")
            # এখানে আপনার আসল ক্লোনিং লজিক বসবে
            time.sleep(3)
            print("[+] কাজ শেষ!")
        else:
            print("\n[!] এরর: ফাইলটি পাওয়া যায়নি!")
            time.sleep(2)
            clone_menu()
            
    elif choice == '2' or choice == '02':
        uid = input("\n[?] ফেসবুক UID দিন: ")
        print(f"\n[!] UID: {uid} এর উপর কাজ শুরু হচ্ছে...")
        time.sleep(3)
        print("[+] কাজ শেষ!")
    
    else:
        print("ফিরে যাওয়া হচ্ছে...")
        time.sleep(1)

# মূল মেনু
if __name__ == "__main__":
    clone_menu()
