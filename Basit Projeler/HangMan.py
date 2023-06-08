"""
Aşağıdaki kod bir adam asmaca oyunudur.
"""

name = input("Oyuncu Adı=")
print("Merhaba " + name)
secret_word = "hindistan"
guess_string = ""
lives = 10
while(lives > 0):
    character_left = 0
    for character in secret_word:
        if character in guess_string:  
            print(character)
        else:
            print("-")
            character_left = character_left + 1
    if(character_left == 0):
        print("Kazandınız")
        break
    guess = input("Harf Tahmini=")
    guess_string = guess_string + guess
    if guess not in secret_word:
        lives = lives - 1
        print("Yanlış")
        print(f"Kalan can sayısı: {lives}")
    if(lives == 0):
        print("Kaybettin!!")
