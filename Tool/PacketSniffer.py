from scapy.all import *

class PacketSniffer:
    def __init__(self, source_ip):
        self.source_ip = source_ip

    def yakala_ve_sniff(self, paket):
        if IP in paket:
            print(f"Yakalanan Paket: {paket[IP].src} -> {paket[IP].dst}")
            sahte_paket = IP(src=self.source_ip, dst=paket[IP].dst) / ICMP()
            send(sahte_paket)
            print(f"Sahte Paket Gönderildi: {self.source_ip} -> {paket[IP].dst}")

    def calistir(self, protokol):

        print(f"{protokol} protokolü için paketler dinleniyor...")
        sniff(filter=protokol, prn=self.yakala_ve_sniff)

print("Filtre Seçenekleri: icmp, tcp, udp, port 80, port 443, host 192.168.1.1 vb.")
protokol = input("Filtre türünü giriniz: ")

sniffer = PacketSniffer(source_ip="1.2.3.4")
sniffer.calistir(protokol)
