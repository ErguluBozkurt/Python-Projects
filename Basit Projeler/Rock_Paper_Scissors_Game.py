"""
Bu proje gerçek hayatta yaptığımız taş-kağıt-makas oyunu referans alınarak yapılmıştır. Bilgisayar ile karşılıklı oynayacağınız zevkli bir oyundur.

"""

import random

secenek = ["taş", "kağıt", "makas"]
tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]

print("Taş, Kağıt, Makas Oyununa HOŞGELDİNİZ")
print("Oyunu Bitirmek İçin q Tuşuna Basınız.")

while True:
    secim = input("Taş, Kağıt, Makas Hangisini Seçiyorsun:").lower()
    print("Oyunu Bitirmek İçin q Tuşuna Basınız.")
    bil_secim = random.choice(secenek)
    
    if(secim == tas):
        if(bil_secim == tas):
            print("Bilgisayarın Seçimi: Taş")
            print("Sonuç Berabere")
            print("################################")
        elif(bil_secim == kagit):
            print("Bilgisayarın Seçimi: Kağıt")
            print("Kaybettin")
            print("################################")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Kazandın")
            print("################################")

    if(secim == kagit):
        if(bil_secim == tas):
            print("Bilgisayarın Seçimi: Taş")
            print("Kazandın")
            print("################################")
        elif(bil_secim == kagit):
            print("Bilgisayarın Seçimi: Kağıt")
            print("Berabere")
            print("################################")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Kaybettin")
            print("################################")

    if(secim == makas):
        if(bil_secim == tas):
            print("Bilgisayarın Seçimi: Taş")
            print("Kaybettin")
            print("################################")
        elif(bil_secim == kagit):
            print("Bilgisayarın Seçimi: Kağıt")
            print("Kazandın")
            print("################################")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Berabere")
            print("################################")

    if(secim == "q"):
        print("Oyundan Çıktınız.")
        break
    