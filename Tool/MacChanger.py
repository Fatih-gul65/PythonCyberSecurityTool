#!/usr/bin/env python3

import subprocess
import re

print("##############################################################")
print("1) Bu scripti yonetici yetkileriyle calistirdiginizdan emin olun")
print("2) Ag adaptörünün aktif ve bagli oldugundan emin olun")
print("##############################################################\n")

# Kullanilacak MAC adresleri. Gerekirse guncelleyiniz.
mac_to_change_to = ["00:11:22:33:44:55", "00:22:33:44:55:66", "00:AA:BB:CC:DD:EE", "00:FF:EE:DD:CC:BB"]

# MAC adreslerini dogrulamak icin regex
macAddRegex = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")

# Komutlari calistirmak ve cikti almak icin fonksiyon
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Hata: {result.stderr.strip()}")
    return result.stdout.strip()

# `ip` komutunu kullanarak ag arayuzlerini alin
interfaces_output = run_command(["ip", "link"])
interfaces = re.findall(r"\d+: (\w+): <", interfaces_output)

print("Mevcut ag arayuzleri:")
for index, interface in enumerate(interfaces):
    print(f"{index} - {interface}")

# Kullanici bir ag arayuzu secer
interface_index = int(input("MAC adresini degistirmek istediginiz arayuzu secin: "))
selected_interface = interfaces[interface_index]
print(f"Secilen arayuz: {selected_interface}\n")

# MAC adresi secenekleri icin menu goster
while True:
    print("Hangi MAC adresini kullanmak istiyorsunuz?")
    for index, mac in enumerate(mac_to_change_to):
        print(f"{index} - {mac}")

    update_option = int(input("Kullanmak istediginiz MAC adresini secin: "))
    if 0 <= update_option < len(mac_to_change_to):
        new_mac_address = mac_to_change_to[update_option]
        print(f"MAC adresiniz su sekilde degistirilecek: {new_mac_address}\n")
        break
    else:
        print("Gecersiz secenek. Lutfen tekrar deneyin!\n")

# Arayuzu kapat
print(f"Arayuz kapatiliyor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "down"])

# MAC adresini degistir
print(f"{selected_interface} icin MAC adresi su sekilde degistiriliyor: {new_mac_address}")
run_command(["ip", "link", "set", "dev", selected_interface, "address", new_mac_address])

# Arayuzu tekrar ac
print(f"Arayuz aciliyor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "up"])

# Degisikligi dogrulayin
current_mac = run_command(["cat", f"/sys/class/net/{selected_interface}/address"])
if current_mac.strip() == new_mac_address.lower():
    print(f"MAC adresi basariyla degistirildi: {current_mac}")
else:
    print(f"MAC adresi degistirilemedi. Mevcut MAC: {current_mac}")
