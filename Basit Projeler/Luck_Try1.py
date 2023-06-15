"""
Bu proje kişilerin isimlerini girdikten sonra bilgisayarın rastgele kişilere değer vererek kimin kazanacağını bulmaktadır.
"""

import random
import time



def atis(namex, namey):
    x = 0
    y = 0
    i = 1
    while True:
        print(f"{i}. Raund Başladı ")
        atis1 = random.randint(1,7)
        time.sleep(2)
        print(f"{namex} {atis1} değerini attı.")
        atis2 = random.randint(1,7)
        time.sleep(2)
        print(f"{namey} {atis2} değerini attı.")
        time.sleep(2)
        if(atis1 > atis2):
            x = x + 1 
            print(f"{namex} {i}. Raundu Kazandı ")
            time.sleep(3)
        elif(atis1 < atis2):
            y = y + 1
            print(f"{namey} {i}. Raundu Kazandı ")
            time.sleep(3)
        elif(atis1 == atis2):
            print("Çekiliş Berabere")
        if(x == 3):
            print(f"{namex} Kazandı ")
            time.sleep(3)
            break
        elif(y == 3):
            print(f"{namey} Kazandı ")
            time.sleep(3)
            break
                    
        i = i + 1

    
    
print("#"*30)
print("BİLGİLENDİRME \nİlk önce isminizi girin daha sonra 0 ile 10 arasında bir sayı girin \nEn yakın sayıyı giren ilk zar atacak kişi olur.")
print("#"*30)
def zar():

    name1 = input("Birinci yarışmacı isimini gir:").title()
    name2 = input("İkinci yarışmacı isimini gir:").title()
    
    while True:
        number =random.randint(0,11)
        number1 = int(input("Sayı girin:"))
        number2 = int(input("Sayı girin:"))
        if(abs(number1-number) > abs(number2-number)):
            print(f"İlk başlayan {name2} ")
            atis(name2, name1)
            break
        elif(abs(number1-number) < abs(number2-number)):
            print(f"İlk başlayan {name1} ")
            atis(name1, name2)
            break
        elif(abs(number1-number) == abs(number2-number)):
            print("Berabere tekrar çekiliş yapın")
            continue
        else:
            print("Hatalı giriş yaptınız!! \nTekrar Deneyiniz")
            continue
            
            
        
while True:
    choice = input("Çarkı çevirmek için w ye bas \nÇıkış yapmak için q ya bas \nCevap:")
    if(choice == "w"):
        print("Oyuna Hoşgeldiniz")
        zar()
    elif(choice == "q"):
        print("Çıkış yapıldı")
        time.sleep(2)
        break
    else:
        print("Hatalı tuşlama yaptınız!! \nTekrar Deneyiniz.")
        time.sleep(2)
        continue