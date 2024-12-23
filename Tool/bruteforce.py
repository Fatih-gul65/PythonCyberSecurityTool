import win32com.client
import time

flag = False

excel_dosya = r'C:\Users\AHMET\Source\Repos\PythonCyberSecurityTool\Kitap1.xlsx'
sifre_dosya = r'C:\Users\AHMET\Source\Repos\PythonCyberSecurityTool\wordlist.txt'

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