"""
İstediğiniz herhangi bir müziğin uzantısını adres kısmına ekleyerek çaldırabileceğiniz çok basit bir koddur.
"""


import pygame
import time


def play():
    pygame.init()
    file = "Burak Kut  Ver Allah.mp3" # adres
    pygame.mixer.music.load(file)
    pygame.mixer_music.play()
    
play()
time.sleep(30) # 20 saniye çalmasını istediğimiz durumlarda kullanıyoruz

