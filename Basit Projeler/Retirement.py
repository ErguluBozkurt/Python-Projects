"""
Aşağıdaki kod emeklilik yılı hesaplar.
"""

def emeklilik(yil):
    yas = hesap(yil)
    emeklilik = 65 - yas
    if(emeklilik>0):
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Emekisiniz")

def hesap(yil):
    return(2022 - yil)
emeklilik(int(input("Yıl giriniz=")))
