"""
Aşağıdaki kod 1 ile 100 arasında sayının yukarı aşağı komutları kullanarak kullanıcıya buldurmasını sağlayan bir oyundur.

"""

import random

sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz="))
hak = can
sayac = 0
while(hak>0):
    hak = hak - 1
    sayac = sayac + 1
    tahmin = int(input("Tahmin="))
    if(sayi == tahmin):
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puanınız = {100 - (100 / can) * (sayac - 1)}")
        break
    elif(sayi > tahmin):
        print("Yukarı")
    elif(sayi < tahmin):
        print("Aşağı")
    if(hak == 0):
        print(f"Hakkınız bitti. Tutulan sayi = {sayi}")
