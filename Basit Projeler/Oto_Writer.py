"""
İmlecin konumuna yazmak istediğniz yazıyı yazar.
"""

import pyautogui
import time

time.sleep(10) # Uygulama çalıştıkdan sonra yazmaya başlama süresi
def mesaj():
    pyautogui.write("Merhaba!!") # yazmak istediğiniz yazı
    pyautogui.press("enter")
    
for i in range(15): # Tekrar sayısı
    mesaj()
    i = i + 1
         