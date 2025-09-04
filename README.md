Cyber Security Toolkit
PythonLicensePlatformContributions welcome

A comprehensive, GUI-based cybersecurity toolkit built with Python and PyQt5. This project consolidates essential tools for network analysis, penetration testing, and educational purposes into a single, user-friendly interface.

Cyber Security Toolkit Main Interface
(It's recommended to take a screenshot of the main window and save it as main.png in your resimler folder for this image to work.)

📖 About The Project
This toolkit was created to provide a simple yet powerful interface for common cybersecurity tasks. By leveraging powerful libraries like Scapy, Requests, and PyQt5, it makes complex network operations more accessible for security professionals, students, and enthusiasts alike. Each tool is designed as a modular component within a unified application.

🛠️ Key Features & Tools
The toolkit includes the following modules:

Port Scanner: A multi-threaded scanner to quickly discover open ports on a target IP or a range of IPs.
Packet Sniffer: A real-time network traffic analyzer that captures packets and allows filtering by protocol (e.g., TCP, ICMP).
ARP Spoofer: Executes ARP poisoning attacks to intercept traffic on a local network, useful for simulating Man-in-the-Middle (MITM) scenarios.
Wi-Fi Scanner: Detects and lists nearby wireless networks, displaying their SSID, signal strength, and security protocols. (Linux-specific)
MAC Changer: Temporarily modifies the MAC address of a network interface to enhance privacy or bypass MAC-based filters. (Linux-specific)
Whois & DoS Tool: Performs Whois lookups to gather domain registration information and can launch a basic HTTP Flood DoS simulation for stress testing purposes.
Brute-Force ZIP Cracker: Attempts to crack password-protected ZIP archives using a dictionary-based attack.
📸 Screenshots
Port Scanner	Packet Sniffer	ARP Spoofer
Port Scanner	Packet Sniffer	ARP Spoofer
Wi-Fi Scanner	MAC Changer	Whois & DoS Tool
Wi-Fi Scanner	MAC Changer	Whois & DoS
ZIP Cracker		
ZIP Cracker		
(The paths above are configured to use your existing resimler folder.)

⚙️ Setup & Installation
Follow these steps to get the toolkit running on your local machine.

Prerequisites
Python 3.8+
pip (Python Package Installer)
A Linux-based Operating System is recommended, as the Wi-Fi Scanner and MAC Changer depend on Linux system commands (nmcli, ifconfig).
Installation Steps
Clone the repository:

sh
git clone https://github.com/Fatih-gul65/PythonCyberSecurityTool.git
cd PythonCyberSecurityTool
Create and activate a virtual environment (recommended):

sh
python3 -m venv venv
source venv/bin/activate
Install the required packages:
Create a requirements.txt file with the following content:

text
PyQt5
scapy
requests
python-whois
wifi
Then, install them using pip:

sh
pip install -r requirements.txt
🚀 How to Run
Because several tools require elevated privileges to capture packets or modify network interfaces (e.g., Packet Sniffer, ARP Spoofer, MAC Changer), you must run the application with sudo.

sh
sudo python3 main.py
Once the application is running, select the desired tool from the interface, fill in the required fields, and start the operation.

⚠️ Legal & Ethical Disclaimer
This toolkit is intended for educational, research, and authorized security testing purposes only.

Usage of this toolkit for attacking targets without prior mutual consent is illegal.
The developers assume no liability and are not responsible for any misuse or damage caused by this program.
By using this software, you agree to use it responsibly and in compliance with all applicable laws.
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.
