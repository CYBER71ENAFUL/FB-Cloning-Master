import os
import time

os.system("clear")

print("\033[1;36m")
print("================================")
print("      CYBER 71 ENAFUL")
print("================================")
print("OWNER : ENAFUL")
print("VERSION : 1.0")
print("")

password = input("Enter Password : ")

if password != "8081":
    print("Wrong Password")
    exit()

print("Access Granted")
time.sleep(2)

while True:
    os.system("clear")

    print("===== CYBER 71 ENAFUL=====")
    print("1. System Info")
    print("2. Loading Animation")
    print("3. Show Time")
    print("4. Exit")

    choice = input("Select Option : ")

    if choice == "1":
        os.system("clear")
        print("Device : Android")
        print("User : ENAFUL")
        input("Press Enter")

    elif choice == "2":
        os.system("clear")
        print("Loading Tool...")
        for i in range(10):
            print("Processing :", i)
            time.sleep(0.5)
        input("Press Enter")

    elif choice == "3":
        import datetime
        now = datetime.datetime.now()
        print("Current Time :", now)
        input("Press Enter")

    elif choice == "4":
        print("Exit Tool")
        break

    else:
        print("Invalid Option")
        time.sleep(1)
