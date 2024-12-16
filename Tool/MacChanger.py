#!/usr/bin/env python3

import subprocess
import re

print("##############################################################")
print("1) Bu scripti yönetici yetkileriyle çalýþtýrdýðýnýzdan emin olun")
print("2) Að adaptörünün aktif ve baðlý olduðundan emin olun")
print("##############################################################\n")

# Kullanýlacak MAC adresleri. Gerekirse güncelleyin.
mac_to_change_to = ["00:11:22:33:44:55", "00:22:33:44:55:66", "00:AA:BB:CC:DD:EE", "00:FF:EE:DD:CC:BB"]

# MAC adreslerini doðrulamak için regex
macAddRegex = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")

# Komutlarý çalýþtýrmak ve çýktý almak için fonksiyon
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Hata: {result.stderr.strip()}")
    return result.stdout.strip()

# `ip` komutunu kullanarak að arayüzlerini alýn
interfaces_output = run_command(["ip", "link"])
interfaces = re.findall(r"\d+: (\w+): <", interfaces_output)

print("Mevcut að arayüzleri:")
for index, interface in enumerate(interfaces):
    print(f"{index} - {interface}")

# Kullanýcý bir að arayüzü seçer
interface_index = int(input("MAC adresini deðiþtirmek istediðiniz arayüzü seçin: "))
selected_interface = interfaces[interface_index]
print(f"Seçilen arayüz: {selected_interface}\n")

# MAC adresi seçenekleri için menü göster
while True:
    print("Hangi MAC adresini kullanmak istiyorsunuz?")
    for index, mac in enumerate(mac_to_change_to):
        print(f"{index} - {mac}")

    update_option = int(input("Kullanmak istediðiniz MAC adresini seçin: "))
    if 0 <= update_option < len(mac_to_change_to):
        new_mac_address = mac_to_change_to[update_option]
        print(f"MAC adresiniz þu þekilde deðiþtirilecek: {new_mac_address}\n")
        break
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin!\n")

# Arayüzü kapat
print(f"Arayüz kapatýlýyor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "down"])

# MAC adresini deðiþtir
print(f"{selected_interface} için MAC adresi þu þekilde deðiþtiriliyor: {new_mac_address}")
run_command(["ip", "link", "set", "dev", selected_interface, "address", new_mac_address])

# Arayüzü tekrar aç
print(f"Arayüz açýlýyor: {selected_interface}")
run_command(["ip", "link", "set", selected_interface, "up"])

# Deðiþikliði doðrulayýn
current_mac = run_command(["cat", f"/sys/class/net/{selected_interface}/address"])
if current_mac.strip() == new_mac_address.lower():
    print(f"MAC adresi baþarýyla deðiþtirildi: {current_mac}")
else:
    print(f"MAC adresi deðiþtirilemedi. Mevcut MAC: {current_mac}")
