"""
Bu proje milli piyango çekiliş uygulamasıdır. Logo tasarımı için arka plan resminin uzantısı eklenmesi gerekmektedir.
"""
import random
from tkinter import *

window = Tk()
window.title("Sayisal Loto")
window.geometry("900x400+500+200")
window.configure(bg="#eb0029")
window.resizable(False, False)

# LOGO
resim = PhotoImage(file="foroğraf uzantısı")
l0 = Label(image=resim, width=290, height=100)
l0.pack()

#SAYILAR
l1 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l1.place(x=150, y=120)

l2 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l2.place(x=250, y=120)

l3 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l3.place(x=350, y=120)

l4 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l4.place(x=450, y=120)

l5 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l5.place(x=550, y=120)

l6 = Label(window, text="00", font="verdana 40 underline bold", bg="#eb0029", fg="white")
l6.place(x=650, y=120)

#BUTON
def cekilis():
    sayi1 = random.randint(1,90) 
    sayi2 = random.randint(1,90) 
    while(sayi1==sayi2):
        sayi2 = random.randint(1,90)
    sayi3 = random.randint(1,90) 
    while(sayi1==sayi3 or sayi1 == sayi3):
        sayi3 = random.randint(1,90) 
    sayi4 = random.randint(1,90) 
    while(sayi4==sayi1 or sayi4==sayi2 or sayi4== sayi3):
        sayi4 = random.randint(1,90) 
    sayi5 = random.randint(1,90) 
    while(sayi5==sayi1 or sayi5 == sayi2 or sayi5==sayi3 or sayi5==sayi4):
        sayi5 = random.randint(1,90) 
    sayi6 = random.randint(1,90) 
    while(sayi6==sayi1 or sayi6==sayi2 or sayi6==sayi3 or sayi6==sayi4 or sayi6==sayi5):
        sayi6 = random.randint(1,90) 

    if(sayi1<10):
        l1["text"]="0"+str(sayi1)
    else:
        l1["text"]=str(sayi1)
   
    if(sayi2<10):
        l2["text"]="0"+str(sayi2)
    else:
        l2["text"]=str(sayi2)
    if(sayi3<10):
        l3["text"]="0"+str(sayi3)
    else:
        l3["text"]=str(sayi3)
    if(sayi4<10):
        l4["text"]="0"+str(sayi4)
    else:
        l4["text"]=str(sayi4)
        
    if(sayi5<10):
        l5["text"]="0"+str(sayi5)
    else:
        l5["text"]=str(sayi5)
    if(sayi6<10):
        l6["text"]="0"+str(sayi6)
    else:
        l6["text"]=str(sayi6)

b1 = Button(window, text="çekiliş yap", width=20, height=2, bg="navy", font="verdana 12 bold")
b1.place(x=300, y=250)

