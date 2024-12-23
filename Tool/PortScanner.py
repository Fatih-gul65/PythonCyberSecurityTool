# -*- coding: utf-8 -*-
import threading
import socket

# Port tarama fonksiyonu
def portarama(ip, port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.5)
        if soket.connect_ex((ip, port)) == 0:
            print(f'{ip} ---> {port} Açýk')
        else:
            print(f'{ip} ---> {port} Kapalý')
    except:
        pass

# Çoklu IP ve port taramasý için thread kullanýmý
def threadile(hedef1, hedef2, portlar):
    bas_ip = int(hedef1.split('.')[3])
    bit_ip = int(hedef2.split('.')[3])
    threadliste = []

    for sonblok in range(bas_ip, bit_ip+1):
        hedef_ip = hedef1.split('.')[0] + '.' + hedef1.split('.')[1] + '.' + hedef1.split('.')[2] + '.' + str(sonblok)
        portlar_listesi = portlar.split(',')
        for port in portlar_listesi:
            thread = threading.Thread(target=portarama, args=(hedef_ip, int(port)))
            threadliste.append(thread)
            thread.start()

# Tek bir IP için port aralýðý taramasý
def port_aralik_tarama(hedef, baslangic_portu, bitis_portu):
    print('Tarama Baþlýyor.....')
    print('*'*50)
    for port in range(baslangic_portu, bitis_portu+1):
        portarama(hedef, port)

# Kullanýcýdan seçim al
print("1 - IP Aralýðýnda Belirli Portlarý Tara")
print("2 - Tek Bir IP Ýçin Port Aralýðýný Tara")
secim = input("Yapmak istediðiniz iþlemi seçin (1 veya 2): ")

if secim == '1':
    ip_araligi = input('Hedef IP aralýðýný giriniz (örnek: 192.168.1.1-192.168.1.5): ')
    _portlar = input('Virgül ile ayýrarak portlarý giriniz: ')
    _ip1, _ip2 = ip_araligi.split('-')  # "-" ile ayýrarak iki IP'yi alýyoruz
    threadile(_ip1.strip(), _ip2.strip(), _portlar)  # Strip ile boþluklarý temizliyoruz
    input('Taramayý tamamlamak için bekleyin...')
elif secim == '2':
    _ip = input('Hedefin IP adresini giriniz: ')
    _baslangic_portu = int(input('Baþlangýç portunu giriniz: '))
    _bitis_portu = int(input('Bitiþ portunu giriniz: '))
    port_aralik_tarama(_ip, _baslangic_portu, _bitis_portu)
else:
    print("Hatalý seçim yaptýnýz!")
