from port_scanner import PortScanner
from brute_forcer import BruteForcer

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Select a module (1/2): ")

    if choice == '1':
        target = input("Enter target IP: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scanner = PortScanner(target)
        open_ports = scanner.scan(start_port, end_port)
        print(f"Open ports: {open_ports}")

    elif choice == '2':
        target = input("Enter target IP: ")
        username = input("Enter username: ")
        password_file = input("Enter path to password list: ")
        with open(password_file, 'r') as f:
            passwords = f.read().splitlines()
        brute_forcer = BruteForcer(target, username, passwords)
        brute_forcer.brute_force()

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()