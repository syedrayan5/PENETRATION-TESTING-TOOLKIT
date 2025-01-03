# PENETRATION TESTING TOOLKIT


*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : SYED RAYAN
*INTERN ID* : CT08HWO
*DOMAIN* : CYBERSECURITY AND ETHICAL HACKING
*BATCH DURATION* : December 30th, 2024 to January 30th, 2025
*MENTOR NAME* : NEELA SANTHOSH

# DESCRIPTION OF THE PROJECT


This is a simple Python-based modular toolkit for penetration testing that includes a port scanner and a brute-forcer.

## Modules
- Port Scanner
   Scans a range of ports on a target IP address to identify open ports.

# Usage

To run the port scanner and brute forcer modules in the Python-based penetration testing toolkit, follow these steps:

- Prerequisites
Python Installation: Ensure you have Python 3.x installed on your system. You can download it from python.org.

Install Required Libraries: The brute-forcer module requires the paramiko library for SSH connections. You can install it using pip. Open your terminal or command prompt and run:

pip install paramiko


- Running the Toolkit
Download the Toolkit: Create a directory for the toolkit and save the provided Python files (port_scanner.py, brute_forcer.py, main.py, and README.md) in that directory.

Navigate to the Toolkit Directory: Open your terminal or command prompt and navigate to the directory where you saved the toolkit files. For example:


Copy code
cd path/to/penetration_testing_toolkit
Run the Main Application: Execute the main application by running the following command:

python main.py


- Using the Port Scanner
Select the Port Scanner Module: When prompted, enter 1 to select the port scanner module.

Input Target IP: Enter the target IP address you want to scan. For example:


Enter target IP: 192.168.1.1
Input Port Range: Specify the range of ports you want to scan. For example:


Enter start port: 1
Enter end port: 1024
View Results: The program will output a list of open ports within the specified range.

- Using the Brute Forcer
Select the Brute Forcer Module: When prompted, enter 2 to select the brute forcer module.

Input Target IP: Enter the target IP address you want to brute-force. For example:

Enter target IP: 192.168.1.1
Input Username: Enter the username for the SSH login attempt. For example:

Enter username: admin
Input Password List: Provide the path to a text file containing a list of passwords (one password per line). For example:


Enter path to password list: /path/to/passwords.txt
View Results: The program will attempt to connect using each password in the list. If a valid password is found, it will be displayed. If no valid password is found, it will indicate that as well.