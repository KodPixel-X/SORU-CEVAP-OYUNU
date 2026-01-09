import time
import os
from colorama import Fore, init

init(autoreset=True)

puan = 0

print("OYUN BAŞLADI")
time.sleep(0.1)
print (Fore.MAGENTA + "README.TXT'YE GÖRE DAĞITINIZ.")
os.startfile("readme.txt")
time.sleep(0.3)

print("Azerbaycanın başkenti nedir?")
time.sleep(0.3)

cevap = input("Cevap: ")

if cevap.strip().lower() == "bakü":
    puan += 25
    print(Fore.GREEN + "Doğru")
else:
    print(Fore.RED + "YANLIŞ!")

time.sleep(1)

print("Suriyenin başkenti nedir?")
time.sleep(0.3)

cevap2 = input("Cevap: ")

if cevap2.strip().lower() == "şam":
    puan += 25
    print(Fore.GREEN + "Doğru")
else:
    print(Fore.RED + "YANLIŞ!")

time.sleep(1)

print("Bonus soru eğer kaybedersen -10 puan gider :)")
time.sleep(0.4)
print("TÜRKİYENİN BAŞKENTİ NEDİR?")
time.sleep(0.3)

cevap3 = input("Cevap: ")

if cevap3.strip().lower() == "ankara":
    puan += 20
    print(Fore.GREEN + "Doğru ama sadece 20 puan :)")
else:
    puan -= 10
    print(Fore.RED + "YANLIŞ! -10 puan")

time.sleep(1)

print("Son soru")
time.sleep(0.4)
print("AVRUPANIN KALBİ HANGİ ŞEHİRDİR?")
time.sleep(0.3)

cevap4 = input("Cevap: ")

if cevap4.strip().lower() == "viyana":
    puan -= 1
    print(Fore.RED + "YANLIŞ! -1 puan :o")
else:
    puan += 30
    print(Fore.GREEN + "DOĞRU!")

time.sleep(0.3)
print("BİTTİ ama 0,5 saniye sonra puanını göreceksin :)")
time.sleep(0.5)

if puan <= 50:
    os.startfile("kötü.vbs")
else:
    os.startfile("iyi.vbs")

print(Fore.CYAN + f"TOPLAM PUANIN: {puan}")
input("\nOYUN BİTTİ, ÇIKMAK İÇİN ENTER TUŞUNA BAS")
