# PENETRATION TESTING TOOLKIT


**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : SYED RAYAN
**INTERN ID** : CT08HWO
**DOMAIN** : CYBERSECURITY AND ETHICAL HACKING
**BATCH DURATION** : December 30th, 2024 to January 30th, 2025
**MENTOR NAME** : NEELA SANTHOSH

# DESCRIPTION OF THE PROJECT
# Penetration Testing Toolkit (Port Scanner & SSH Brute-Forcer)

## Objective
This Python-based penetration testing toolkit provides two essential modules: a **Port Scanner** and an **SSH Brute-Forcer**. The tool helps security professionals and ethical hackers identify open ports and test SSH login credentials using brute force techniques.

## Key Features
- **Port Scanner:** Quickly scans multiple ports on a target to check if they are open or closed.
- **SSH Brute-Forcer:** Attempts to log in to an SSH service using a provided username and a password wordlist.
- **Multi-threaded Scanning:** Faster port scanning using concurrent threads.
- **Pre-Brute-Force Check:** Ensures SSH is open before attempting brute-force attacks.
- **Error Handling:** Manages connection failures, timeouts, and authentication errors gracefully.

## Libraries Used
- `socket` (built-in) - Used for network communication and port scanning.
- `paramiko` - For SSH brute-force attempts.
- `argparse` - For handling command-line arguments.
- `concurrent.futures` - Enables multi-threaded port scanning.

## Instructions for Usage
### 1️⃣ Installation
Ensure you have Python 3 installed and install required dependencies:
```bash
pip install paramiko
```

### 2️⃣ Running the Port Scanner
Scan specific ports on a target:

python toolkit.py scan <target_ip> --ports <port1,port2,port3>

**Example:**

python toolkit.py scan 192.168.1.1 --ports 22,80,443


### 3️⃣ Running the SSH Brute-Forcer
Attempt SSH login brute-force attack:

python toolkit.py brute-force <target_ip> --username <username> --password_file <password_list>

**Example:**

python toolkit.py brute-force 192.168.1.1 --username root --password_file passwords.txt

## OUTPUT OF THE TASK :
![Penetration Testing toolkit output](https://github.com/user-attachments/assets/c0e9fdef-0c7e-413c-879b-e2924da817b7)

