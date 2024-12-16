import threading
import socket

# Port tarama fonksiyonu
def portara(ip, port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.5)
        if soket.connect_ex((ip, port)) == 0:
            print(f'{ip} ---> {port} A��k')
        else:
            print(f'{ip} ---> {port} Kapal�')
    except:
        pass

# �oklu IP ve port taramas� i�in thread kullan�m�
def threadile(hedef1, hedef2, portlar):
    bas_ip = int(hedef1.split('.')[3])
    bit_ip = int(hedef2.split('.')[3])
    threadliste = []

    for sonblok in range(bas_ip, bit_ip+1):
        hedef_ip = hedef1.split('.')[0] + '.' + hedef1.split('.')[1] + '.' + hedef1.split('.')[2] + '.' + str(sonblok)
        portlar_listesi = portlar.split(',')
        for port in portlar_listesi:
            thread = threading.Thread(target=portara, args=(hedef_ip, int(port)))
            threadliste.append(thread)
            thread.start()

# Tek bir IP i�in port aral��� taramas�
def port_aralik_tarama(hedef, baslangic_portu, bitis_portu):
    print('Tarama Ba�l�yor.....')
    print('*'*50)
    for port in range(baslangic_portu, bitis_portu+1):
        portara(hedef, port)

# Kullan�c�dan se�im al
print("1 - IP Aral���nda Belirli Portlar� Tara")
print("2 - Tek Bir IP ��in Port Aral���n� Tara")
secim = input("Yapmak istedi�iniz i�lemi se�in (1 veya 2): ")

if secim == '1':
    _ip1 = input('Hedefin ilk IP adresini giriniz: ')
    _ip2 = input('Hedefin son IP adresini giriniz: ')
    _portlar = input('Virg�l ile ay�rarak portlar� giriniz: ')
    threadile(_ip1, _ip2, _portlar)
    input('Taramay� tamamlamak i�in bekleyin...')
elif secim == '2':
    _ip = input('Hedefin IP adresini giriniz: ')
    _baslangic_portu = int(input('Ba�lang�� portunu giriniz: '))
    _bitis_portu = int(input('Biti� portunu giriniz: '))
    port_aralik_tarama(_ip, _baslangic_portu, _bitis_portu)
else:
    print("Hatal� se�im yapt�n�z!")
