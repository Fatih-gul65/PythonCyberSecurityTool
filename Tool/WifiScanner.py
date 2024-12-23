import subprocess
import re

def scan_wifi():
    # Wi-Fi a�lar�n� taramak i�in netsh komutunu �al��t�r
    try:
        command = "netsh wlan show networks mode=bssid"
        # encoding'i 'latin-1' olarak de�i�tiriyoruz
        output = subprocess.check_output(command, shell=True, text=True, encoding='latin-1')
        
        networks = []
        
        # ��kt�y� sat�r sat�r analiz et
        for line in output.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                ssid = re.search(r"SSID \d+ : (.+)", line)
                if ssid:
                    networks.append({"SSID": ssid.group(1).strip()})
            elif "Authentication" in line:
                auth = re.search(r"Authentication\s+: (.+)", line)
                if auth and networks:
                    networks[-1]["Authentication"] = auth.group(1).strip()
            elif "Signal" in line:
                signal = re.search(r"Signal\s+: (\d+)%", line)
                if signal and networks:
                    networks[-1]["Signal Strength"] = signal.group(1).strip()
        
        return networks
    except Exception as e:
        print(f"Hata: {e}")
        return []

# A�lar� taray�p sonu�lar� g�ster
wifi_networks = scan_wifi()
if wifi_networks:
    print("Bulunan Wi-Fi A�lar�:")
    for network in wifi_networks:
        print(f"SSID: {network.get('SSID')}, �ifreleme: {network.get('Authentication')}, Sinyal G�c�: {network.get('Signal Strength')}%")
else:
    print("Hi�bir a� bulunamad�.")
