#!/usr/bin/env python3

import subprocess
import re

print("##############################################################")
print("1) Bu scripti y�netici yetkileriyle �al��t�rd���n�zdan emin olun")
print("2) A� adapt�r�n�n aktif ve ba�l� oldu�undan emin olun")
print("##############################################################\n")

# Kullan�lacak MAC adresleri. Gerekirse g�ncelleyin.
mac_to_change_to = ["00:11:22:33:44:55", "00:22:33:44:55:66", "00:AA:BB:CC:DD:EE", "00:FF:EE:DD:CC:BB"]

# MAC adreslerini do�rulamak i�in regex
macAddRegex = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")

# Komutlar� �al��t�rmak ve ��kt� almak i�in fonksiyon
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Hata: {result.stderr.strip()}")
    return result.stdout.strip()

# `ip` komutunu kullanarak a� aray�zlerini al�n
interfaces_output = run_command(["ip", "link"])
interfaces = re.findall(r"\d+: (\w+): <", interfaces_output)

print("Mevcut a� aray�zleri:")
for index, interface in enumerate(interfaces):
    print(f"{index} - {interface}")

# Kullan�c� bir a� aray�z� se�er
interface_index = int(input("MAC adresini de�i�tirmek istedi�iniz aray�z� se�in: "))
selected_interface = interfaces[interface_index]
print(f"Se�ilen aray�z: {selected_interface}\n")

# MAC adresi se�enekleri i�in men� g�ster
while True:
    print("Hangi MAC adresini kullanmak istiyorsunuz?")
    for index, mac in enumerate(mac_to_change_to):
        print(f"{index} - {mac}")

    update_option = int(input("Kullanmak istedi�iniz MAC adresini se�in: "))
    if 0 <= update_option < len(mac_to_change_to):
        new_mac_address = mac_to_change_to[update_option]
        print(f"MAC adresiniz �u �ekilde de�i�tirilecek: {new_mac_address}\n")
        break
    else:
        print("Ge�ersiz se�enek. L�tfen tekrar deneyin!\n")

# Aray�z� kapat
print(f"Aray�z kapat�l�yor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "down"])

# MAC adresini de�i�tir
print(f"{selected_interface} i�in MAC adresi �u �ekilde de�i�tiriliyor: {new_mac_address}")
run_command(["ip", "link", "set", "dev", selected_interface, "address", new_mac_address])

# Aray�z� tekrar a�
print(f"Aray�z a��l�yor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "up"])

# De�i�ikli�i do�rulay�n
current_mac = run_command(["cat", f"/sys/class/net/{selected_interface}/address"])
if current_mac.strip() == new_mac_address.lower():
    print(f"MAC adresi ba�ar�yla de�i�tirildi: {current_mac}")
else:
    print(f"MAC adresi de�i�tirilemedi. Mevcut MAC: {current_mac}")
