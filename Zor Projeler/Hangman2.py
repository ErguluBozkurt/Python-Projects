"""
Bu projede adam asmaca oyununu gerçekleştirdik. Bu proje adam asmaca oyunun ikincisidir. İlk kodu "basit" kodlar içerisinde bulabilirsiniz.
Doğru harf tahminleri ile bilinmeyen kelime takmin edilmektedir. Bir kelime haznesi oluşturulmuş ve rasgele olacak şekilde çekilmektedir.
"""

import random
while True:
    haund = ["""
    +---+
    |   |
        |
        |
        |
        |
    =========""","""
    +---+
    |   |
    O   |
        |
        |
        |
    =========""","""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""","""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""","""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""","""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""","""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""]


    as_human = 0
    my_word = ["sivas", "istanbul", "samsun", "yastık", "kanepe", "koltuk", "yatak", "elma", "armut", "ananas", "leptop", "avize", "battaniye", 
            "maus", "maymun", "donat", "python", "java", "mühendis", "yazılımcı", "türkiye", "ingiltere", "afrika", "asya", "avrupa", "karadeniz",
            "akdeniz", "powerbank", "kod","kahve", "kupa","gözlük", "soba", "traktör", "polar", "depresyon", "insiyatif", "domates", "barbunya"]
    secret_word = random.choice(my_word).upper()


    secret_word_x = list()
    for alphabet in secret_word:
        secret_word_x.append(alphabet)
    lenghtx = len(secret_word_x)
    print(f"Aranan Kelime {lenghtx} Harfden Oluşuyor. ")
    guess_word = list()
    esit = 0
    guess_listem = list()
    dongu_son = 0
    again = 0
    def find():
        ciz = ""
        bil = 0
        for i in secret_word:
            for j in guess_word:
                if(i == j):
                    ciz = ciz + str(i)
                    bil = bil + 1
            else:
                ciz = ciz + '_/ '
        print(ciz)      
        
    find()     

    while True:
        for x in secret_word_x:
            if(dongu_son==1):
                break
            for y in guess_word:
                if(x==y):
                    esit = esit + 1
                    if(lenghtx == esit):
                        print("Tebrikler Kazandınız.")
                        choice = input("Tekrar Oynamak İster misiniz?(y/n)").upper()
                        if(choice == "Y"):
                            again = 1
                            break
                        elif(choice == "N"):
                            dongu_son = 1
                            break
        esit = 0
        if(again == 1):
            break
        
        if(dongu_son==1):
            break
        guess = input("Harf Giriniz:").upper()
        
        for x in guess_listem:
            if(x == guess):
                print("Zaten Daha Önce Söylendiniz \nTekrar Girin!")
                guess = input("Harf Giriniz:").upper()
                
        guess_listem.append(guess)
        
        stop = 0
        adet = 0
        
        for guess_x in secret_word:
            if(guess_x == guess):
                adet = adet + 1
                
        for guess_x in secret_word:
            if(guess_x == guess):
                print("Bildiniz.")
                print(f"Kelimede {adet} Adet {guess} Harfi Var.")
                guess_word.append(guess)
                
                find()
                break
                
        else:
            if(stop==0):
                print("Yanlış Harf !!")
                print(haund[as_human])
                as_human = as_human + 1
                if(as_human==7):
                    print("Kaybettiniz!!!")
                    print(f"Aranan Kelime:{secret_word}")
                    choice = input("Tekrar Oynamak İster misiniz?(y/n)").upper()
                    if(choice == "Y"):
                        break
                    elif(choice == "N"):
                        dongu_son = 1
                        break
                stop = 1
    if(dongu_son==1):
        break            
              
    if(again == 1):
        continue  