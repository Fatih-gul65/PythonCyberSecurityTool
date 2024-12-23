import subprocess
import re

def scan_wifi():
    # Wi-Fi networks scanning using netsh command
    try:
        command = "netsh wlan show networks mode=bssid"
        # Changing encoding to 'latin-1'
        output = subprocess.check_output(command, shell=True, text=True, encoding='latin-1')
        
        networks = []
        
        # Analyzing the output line by line
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
        print(f"Error: {e}")
        return []

# Scanning networks and displaying results
wifi_networks = scan_wifi()
if wifi_networks:
    print("Detected Wi-Fi Networks:")
    for network in wifi_networks:
        print(f"SSID: {network.get('SSID')}, Encryption: {network.get('Authentication')}, Signal Strength: {network.get('Signal Strength')}%")
else:
    print("No networks found.")
