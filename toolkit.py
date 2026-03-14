from modules.port_scanner import port_scan
from modules.password_checker import check_password
from modules.vulnerability_scanner import vulnerability_scan
from modules.ip_info import get_ip_info

def menu():
    while True:
        print("\n==== Cybersecurity Toolkit ====")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. Vulnerability Scanner")
        print("4. IP Information Tool")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP: ")
            port_scan(target)

        elif choice == "2":
            password = input("Enter password: ")
            check_password(password)

        elif choice == "3":
            target = input("Enter target IP: ")
            vulnerability_scan(target)

        elif choice == "4":
            target = input("Enter domain or IP: ")
            get_ip_info(target)

        elif choice == "5":
            print("Exiting toolkit...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
