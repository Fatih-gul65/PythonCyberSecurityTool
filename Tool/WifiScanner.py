import subprocess
import re

def scan_wifi():
    # Wi-Fi networks scanning using nmcli command
    try:
        command = "nmcli dev wifi list"
        # Changing encoding to 'utf-8'
        output = subprocess.check_output(command, shell=True, text=True, encoding='utf-8')
        
        networks = []
        
        # Analyzing the output line by line
        for line in output.split('\n'):
            if line.startswith("SSID"):
                continue  # Skip the header line
            elif line.strip():
                parts = re.split(r'\s{2,}', line.strip())  # Split on multiple spaces
                if len(parts) >= 6:
                    ssid = parts[0]
                    signal_strength = parts[3]
                    encryption = parts[5]
                    
                    networks.append({
                        "SSID": ssid,
                        "Signal Strength": signal_strength,
                        "Encryption": encryption
                    })
        
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []

# Scanning networks and displaying results
wifi_networks = scan_wifi()
if wifi_networks:
    print("Detected Wi-Fi Networks:")
    for network in wifi_networks:
        print(f"SSID: {network.get('SSID')}, Encryption: {network.get('Encryption')}, Signal Strength: {network.get('Signal Strength')}%")
else:
    print("No networks found.")
