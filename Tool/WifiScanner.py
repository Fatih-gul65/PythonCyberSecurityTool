import subprocess
import re

def scan_wifi():
    # Wi-Fi aðlarýný taramak için netsh komutunu çalýþtýr
    try:
        command = "netsh wlan show networks mode=bssid"
        # encoding'i 'latin-1' olarak deðiþtiriyoruz
        output = subprocess.check_output(command, shell=True, text=True, encoding='latin-1')
        
        networks = []
        
        # Çýktýyý satýr satýr analiz et
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

# Aðlarý tarayýp sonuçlarý göster
wifi_networks = scan_wifi()
if wifi_networks:
    print("Bulunan Wi-Fi Aðlarý:")
    for network in wifi_networks:
        print(f"SSID: {network.get('SSID')}, Þifreleme: {network.get('Authentication')}, Sinyal Gücü: {network.get('Signal Strength')}%")
else:
    print("Hiçbir að bulunamadý.")
