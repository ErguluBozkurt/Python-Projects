"""
Bu proje kelime tahmin oyunudur. Kelime haznesinden rasgele bir kelime seçilerek oyun başlar.
"""

import random
import time

while True:
    print("*"*80)
    print("  Kelime Tahmin Oyunu  ".center(60, "#"))
    print("*"*80)
    
    citys = ["ankara", "samsun", "sivas", "sinop", "malatya", "gaziantep", "bolu", "yozgat", "izmir", "antalya", "kilis"]
    vacubulary = random.choice(citys)
    vacubulary = vacubulary.upper()
    vacubulary_number = len(vacubulary)
    
    print(f"Kelimeniz {vacubulary_number} harflidir. ")
    
    guess = list()
    fail = list()
    heart = 7
    
    while(heart > 0):
        tabela = ""
        for alpabet in vacubulary:
            if(alpabet in guess):
                tabela = tabela + alpabet
            else:
                tabela = tabela + "_"
                
        if(tabela == vacubulary):
            print("İnceleniyor...")
            time.sleep(4)
            print("Kelimeyi doğru bildiniz.")
            break
        print("Kelimeyi tahmin ediniz", tabela)
        print(heart,"Canın var")
        
        new_guess = input("Bir harf giriniz:")
        new_guess = new_guess.upper()
        
        if(new_guess == vacubulary):
            print("İnceleniyor...")
            time.sleep(4)
            print("Doğru Bildin.")
            break
        if(new_guess in guess or new_guess in fail):
            print("İnceleniyor...")
            time.sleep(4)
            print(f"{new_guess} daha önce söylendi. Lütfen başka bir harf söyleyin. ")
        elif(new_guess in vacubulary):
            rpt = vacubulary.count(new_guess)
            print("İnceleniyor...")
            time.sleep(4)
            print(f"Doğru, {new_guess} harfi kelimeniz içerisinde {rpt} kere geçiyor ")
            guess.append(new_guess)
        else:
            print("İnceleniyor...")
            time.sleep(4)
            print("Yanlış!, Kelimede bu harf yok.")
            fail.append(new_guess)
            heart = heart - 1
            
    if(heart == 0):
        print("Hiç Hakkınız Kalmadı")
        print(f"Kelimeniz {vacubulary} ")
        
    out = input("Oyundan Çıkmak istiyorsanız 'q' tuşuna basınız. Devam etmek için her hangi bir tuşa basabilirsiniz.")
    out = out.upper()
    if(out == "Q"):
        print("Çıkış Yapılıyor, Lütfen Bekleyin...")
        time.sleep(3)
        print("Çıkış Yapıldı")
        break
    else:
        print("Oyuna Devam Ediliyor...")
        time.sleep(3)
        continue
        