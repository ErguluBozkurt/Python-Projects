"""
Bu kod bir .txt uzantılı bir metnin içeriğini sesli bir şekilde okur.
"""


import PyPDF2
import pyttsx3


path = open('oku.txt', 'rb') # pdf dosyasının belirtilmesi
pdfReader = PyPDF2.PdfFileReader(path)
from_page = pdfReader.getPage(0) # okunacak sayfanın belirtilmesi , tamamı için 0 verilmektedir.
text = from_page.extractText() # pdf dosyasındaki metinlerin text haline dönüştürülmesi
speak = pyttsx3.init()
speak.say(text) # metinin okunması
speak.runAndWait()
speak.stop()