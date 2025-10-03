<cite/>

```markdown
# Python Cybersecurity Toolkit

A comprehensive, GUI-based cybersecurity toolkit built with Python and PyQt5. This project consolidates essential tools for network analysis, penetration testing, and educational purposes into a single, user-friendly interface.

## 🛡️ About The Project

This toolkit provides a unified interface for common cybersecurity tasks, making complex network operations accessible for security professionals, students, and enthusiasts. Each tool is designed as a modular component within a single application, leveraging powerful libraries like Scapy, Requests, and PyQt5.

## 🔧 Features & Tools

The toolkit includes seven distinct cybersecurity modules:

### Network Analysis Tools
- **Port Scanner**: Multi-threaded scanner to discover open ports on target IPs
- **Packet Sniffer**: Real-time network traffic analyzer with protocol filtering (TCP, ICMP, etc.)
- **Wi-Fi Scanner**: Detects nearby wireless networks with SSID, signal strength, and security protocols

### Network Attack Tools
- **ARP Spoofer**: Executes ARP poisoning attacks for Man-in-the-Middle (MITM) scenarios
- **MAC Changer**: Modifies network interface MAC addresses for privacy or bypass filters
- **Whois & DoS Tool**: Domain registration lookup and HTTP flood stress testing

### Security Testing Tools
- **ZIP Password Cracker**: Dictionary-based attack on password-protected ZIP archives

## 📋 Prerequisites

- **Python 3.8+**
- **Linux-based Operating System** (recommended for full functionality)
- **pip** (Python Package Installer)
- **Root privileges** (required for network-level operations)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fatih-gul65/PythonCyberSecurityTool.git
   cd PythonCyberSecurityTool
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install PyQt5 scapy requests python-whois pywifi
   ```

## 🎯 Usage

**Important:** Run with sudo privileges for network operations:

```bash
sudo python3 Tool/Tool.py
```

The main interface will display buttons for each tool. Select your desired tool, fill in the required parameters, and start the operation.

### Tool-Specific Requirements

- **ARP Spoofer, Packet Sniffer**: Require raw socket access
- **MAC Changer**: Needs interface modification privileges  
- **Wi-Fi Scanner**: Linux-specific (uses system commands)
- **Port Scanner, ZIP Cracker, Whois/DoS**: Standard user privileges

## 📁 Project Structure

```
PythonCyberSecurityTool/
├── Tool/
│   └── Tool.py          # Main application with all security tools
├── wordlist.txt         # Password dictionary for ZIP cracking
├── sifreliDosya.zip    # Test encrypted archive
├── README.md           # This file
└── LICENSE             # MIT License
```

## ⚠️ Legal & Ethical Disclaimer

**This toolkit is intended for educational, research, and authorized security testing purposes only.**

- Usage against targets without prior mutual consent is **illegal**
- Developers assume no liability for misuse or damage
- Users must comply with all applicable laws and regulations
- Only use on networks and systems you own or have explicit permission to test

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🔗 Repository

[https://github.com/Fatih-gul65/PythonCyberSecurityTool](https://github.com/Fatih-gul65/PythonCyberSecurityTool)

---

**Note**: This tool is designed for educational purposes and authorized penetration testing. Always ensure you have proper authorization before using these tools on any network or system.
```
