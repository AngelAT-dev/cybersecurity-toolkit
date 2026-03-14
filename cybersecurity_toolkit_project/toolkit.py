from colorama import Fore, Style
from modules.port_scanner import port_scan
from modules.banner_grabber import banner_grab
from modules.vulnerability_scanner import vulnerability_scan
from modules.password_checker import check_password
from modules.ip_info import get_ip_info

def menu():
    print(Fore.GREEN + "=== Cybersecurity Toolkit ===" + Style.RESET_ALL)

    while True:
        print("\nSelect Tool:")
        print("1 - Port Scanner (Multithread)")
        print("2 - Banner Grabber")
        print("3 - Vulnerability Scanner")
        print("4 - Password Strength Checker")
        print("5 - IP Information Tool")
        print("6 - Exit")

        choice = input("Option: ")

        if choice == "1":
            target = input("Target IP: ")
            port_scan(target)

        elif choice == "2":
            target = input("Target IP: ")
            port = int(input("Port: "))
            banner_grab(target, port)

        elif choice == "3":
            target = input("Target IP: ")
            vulnerability_scan(target)

        elif choice == "4":
            password = input("Password: ")
            check_password(password)

        elif choice == "5":
            target = input("Domain or IP: ")
            get_ip_info(target)

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()