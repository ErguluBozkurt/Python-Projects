"""
Bu proje basit bir çekiliş projesidir. Çekilişe katılacak kişileri girdikten sonra 'başlat' yazarak çekilişi başlatabilirsiniz.
Çekilişi iptal edip düzenleme yapmak için 'iptal' yazmanız yeterli olacaktır.
"""

import random 
liste = list()
print("Çekilişi Başlatmak için 'başlat', \nİptal Etmek için 'iptal' Yaz.")
while True:
    try:
        giris = input("Çekilişe Katılacak Kişiler:")
        if(giris =="iptal"):
            sor = input("Kişiyi mi İptal Edeceksiniz(kişi), Yoksa çekilişi mi?(çekiliş)")
            if(sor == "kişi"):
                sor1 = input("Kimi İptal Etmek İstiyorsunuz:")
                if(sor1 in liste):
                    yer = liste.index(sor1)
                    liste.pop(yer)
                    print("Kişiyi Çekilişden İptal Ettik")
                    for i in liste:
                        print(i)
                        
                else:
                    print("Böyle Bir Kişi Çekilişte Yok.")
                    for i in liste:
                        print(i)
                        
            elif(sor=="çekiliş"):
                try:
                    while True:
                        liste.pop()
                except:
                    print("Çekiliş İptal Edilmiştir")
        elif(giris=="başlat"):
            sor2 = int(input("Kaç Kişi Kazanacak:"))
            sonuc = random.sample(liste, sor2)
            
            if(len(liste)<sor2):
                print("Kazanacak Olanlar Girilen Kişi Sayısından Fazla Olamaz")
            else:
                print(f"Kazananlar:{sonuc} ")
        else:
            liste.append(giris)
    except:
        print("Hatalı Giriş Yaptınız, Lütfen Tekrar Deneyiniz!!")
        
        