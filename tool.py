import os
import time

# clear screen
os.system("clear")

# banner
os.system("figlet VS ENAFUL | lolcat")

print("OWNER : VS ENAFUL")
print("USER  : VS ENAFUL")
print("KEY   : JINN-KEY-8081")
print("")

# login system
key = input("ENTER KEY : ")

if key == "8081":
    print("\nACCESS GRANTED")
else:
    print("\nWRONG KEY")
    exit()

time.sleep(2)

# menu system
while True:
    os.system("clear")
    os.system("figlet JINN TOOL | lolcat")

    print("1. Start Tool")
    print("2. Show Info")
    print("3. Exit\n")

    choice = input("Select Option : ")

    if choice == "1":
        print("\nLoading Tool...\n")
        for i in range(10):
            print("Processing :", i)
            time.sleep(0.5)

        input("\nPress Enter to return menu")

    elif choice == "2":
        print("\nTOTAL ACCOUNT : 99999")
        print("METHOD : M1")
        input("\nPress Enter to return menu")

    elif choice == "3":
        print("\nExit Tool")
        break

    else:
        print("Invalid Option")
        time.sleep(1)
