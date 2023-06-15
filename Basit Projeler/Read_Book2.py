"""
Bu kod bir .txt uzantılı bir metnin içeriğini sesli bir şekilde okur.
"""


from gtts import gTTS
import pygame
import time

def oynat():
    pygame.init()
    file = "oku.mp3" 
    pygame.mixer.music.load(file)
    pygame.mixer_music.play()

with open("oku.txt", "r", encoding="utf-8") as file:
    yazi = file.read()
cikti = gTTS(text=yazi, lang="tr", slow=False )
cikti.save("oku.mp3")

oynat()
time.sleep(30)