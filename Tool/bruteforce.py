import win32com.client
import time
import rarfile

print ("excel dosyasına bruteforce yapmak için 1, rar dosyasına yapmak için 2 ye basınız. \n")
secim = input("Seçiminizi giriniz: ")


if secim == 1:

    flag = False

    excel_dosya = r'C:\Users\Administrator\Source\Repos\Fatih-gul65\PythonCyberSecurityTool\Kitap1.xlsx'
    sifre_dosya = r'C:\Users\Administrator\Source\Repos\Fatih-gul65\PythonCyberSecurityTool\wordlist.txt'

    excel_app = win32com.client.Dispatch("Excel.Application")

    password_list = []

    with open(sifre_dosya, "r", encoding = "utf-8") as pwd:
        passwords = pwd.readlines()
        for password in passwords:
            password_list.append(password.replace("\n", ""))
        

    for password in password_list:
        try:
            wb = excel_app.Workbooks.Open(excel_dosya, False, True, None, password)
            wb.Unprotect(password)
            print("Şifreniz: " + password)
            excel_app.DisplayAlerts = False
            excel_app.Quit()
            time.sleep(1)
            flag = True
            quit()
        except:
            if flag == True:
                break
            else: 
                print("Şifre Hatalı: " + password)
            continue
        

elif secim == 2:


    rar_dosya = r'C:\Users\Administrator\Source\Repos\Fatih-gul65\PythonCyberSecurityTool\Kitap1.rar'
    sifre_dosya = r'C:\Users\Administrator\Source\Repos\Fatih-gul65\PythonCyberSecurityTool\wordlist.txt'

    # RAR dosyasını işlemek için rarfile modülünü etkinleştirin
    rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\Rar.exe"  # UNRAR aracının doğru yolunu belirtin

    password_list = []
    flag = False

    with open(sifre_dosya, "r", encoding="utf-8") as pwd: 
        passwords = pwd.readlines()
        for password in passwords:
            password_list.append(password.strip())

    for password in password_list:
        try:
            with rarfile.RarFile(rar_dosya) as rf:
                rf.extractall(pwd=password)  # Şifre ile dosyaları çıkart
                print("Şifreniz: " + password)
                flag = True
                break
        except rarfile.BadRarFile:
            print("Geçersiz RAR dosyası!")
            break
        except rarfile.RarWrongPassword:
            print("Şifre Hatalı: " + password)
            continue
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            continue

    if not flag:
        print("Doğru şifre bulunamadı.")
