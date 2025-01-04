import zipfile

def crack_zip(zip_file, passwords):
    """ZIP dosyasının şifresini kırmaya çalışır."""
    with zipfile.ZipFile(zip_file) as zf:
        for password in passwords:
            try:
                # Şifreyi dener
                zf.extractall(pwd=password.encode())
                print(f"Şifre bulundu: {password}")
                return password
            except RuntimeError:
                # Yanlış şifre durumunda devam eder
                continue
    print("Şifre bulunamadı.")
    return None

# Wordlist'ten şifreleri okuma
def load_passwords(wordlist_file):
    """Wordlist dosyasından şifreleri okur."""
    with open(wordlist_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

# Kullanım
zip_file = "sifreliDosya.zip"  # Şifreli ZIP dosyanız
wordlist_file = "wordlist.txt"  # Şifre listesi dosyanız

passwords = load_passwords(wordlist_file)
found_password = crack_zip(zip_file, passwords)

if found_password:
    print(f"ZIP dosyasının şifresi: {found_password}")
else:
    print("Şifre bulunamadı.")