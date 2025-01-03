# PENETRATION TESTING TOOLKIT


**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : SYED RAYAN
**INTERN ID** : CT08HWO
**DOMAIN** : CYBERSECURITY AND ETHICAL HACKING
**BATCH DURATION** : December 30th, 2024 to January 30th, 2025
**MENTOR NAME** : NEELA SANTHOSH

# DESCRIPTION OF THE PROJECT

# Name - Penetration Testing Toolkit

## Objective
The Penetration Testing Toolkit is a modular Python-based application designed to assist security professionals and enthusiasts in performing basic penetration testing tasks. This toolkit includes a port scanner to identify open ports on a target system and a brute-forcer to test SSH login credentials against a list of passwords.

## Key Features
- **Port Scanner**: Quickly scans a specified range of ports on a target IP address to identify which ports are open and potentially vulnerable.
- **Brute Forcer**: Attempts to gain unauthorized access to SSH services by systematically testing a list of passwords against a specified username.
- **Modular Design**: Each functionality is encapsulated in its own module, making it easy to extend and maintain.
- **User -Friendly Interface**: Simple command-line interface for easy interaction with the toolkit.

## Libraries Used
- **Paramiko**: A Python implementation of the SSH protocol, used for making SSH connections and performing brute-force attacks.
- **Socket**: A built-in Python library used for network connections, specifically for the port scanning functionality.

## Instructions for Usage

### Prerequisites
1. **Python Installation**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required library:
   pip install paramiko

## Running the Toolkit
Download the Toolkit: Clone or download the repository containing the toolkit files (port_scanner.py, brute_forcer.py, main.py, and README.md).

Navigate to the Toolkit Directory: Open your terminal or command prompt and navigate to the directory where you saved the toolkit files. For example:

cd path/to/penetration_testing_toolkit

Run the Main Application: Execute the main application by running:

python main.py
## Using the Port Scanner
- Select the port scanner module by entering 1 when prompted.
- Input the target IP address you want to scan.
- Specify the range of ports to scan (start and end).
- View the list of open ports displayed by the application.
## Using the Brute Forcer
- Select the brute forcer module by entering 2 when prompted.
- Input the target IP address for the SSH login attempt.
- Enter the username for the SSH login.
- Provide the path to a text file containing a list of passwords (one password per line).
- The application will attempt to connect using each password and display the results.

   
