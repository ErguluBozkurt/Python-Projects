"""
Şansın denendiği bu projede iki kişi tarafından girilen 0-10 arası sayıların bilgisayarın 
seçtiği en yakın sayıyı giren kişi kazanması üzerine tasarlanmıştır.
"""

import tkinter as tk
import random



window = tk.Tk()
window.geometry("1000x600+450+150")
window.title("Şans Oyunu")
window.resizable(False,False)
window.configure(bg="white")

lb1 = tk.Label(window, text="Birinci yarışmacı ismi", fg="black", bg="white", font="italic 12")
lb1.place(x=150,y=100)
ent1 = tk.Entry(window, fg="black", bg="silver", font="arial 14 bold") 
ent1.place(x=150, y=120)

lb2 = tk.Label(window, text="İkinci yarışmacı ismi", fg="black", bg="white", font="italic 12")
lb2.place(x=150,y=160)
ent2 = tk.Entry(window, fg="black", bg="silver", font="arial 14 bold") 
ent2.place(x=150, y=180)

lb3 = tk.Label(window, text="Sayı Gir", fg="black", bg="white", font="italic 12")
lb3.place(x=450,y=100)
ent3 = tk.Entry(window, fg="black", bg="silver", font="arial 14 bold", width=5) 
ent3.place(x=450, y=120)

lb4 = tk.Label(window, text="Sayı Gir", fg="black", bg="white", font="italic 12")
lb4.place(x=450,y=160)
ent4 = tk.Entry(window, fg="black", bg="silver", font="arial 14 bold", width=5) 
ent4.place(x=450, y=180)

lb5 = tk.Label(window, text="0-10 Arasındaki sayıya en yakın sayıyı giren ilk zar atacak kişi olur.", fg="black", bg="white", font="italic 18")
lb5.place(x=155,y=300)

lb6 = tk.Label(window, text="", fg="black", bg="white", font="italic 14" )
lb6.place(x=155, y=350)
lb8 = tk.Label(window, text="", fg="black", bg="white", font="italic 14" )
lb8.place(x=155, y=400)
lb7 = tk.Label(window, text="", fg="black", bg="white", font="italic 40" )
lb7.place(x=470, y=350)

def zar():
    number =random.randint(0,11)
    while True:
        
        number1 = int(ent3.get())
        number2 = int(ent4.get())
        if(number1>10 or number1<0):
            lb5["text"] = "Hatalı giriş yaptınız!! Tekrar Deneyiniz"
            lb5["fg"] = "red"
            break
        if(number2>10 or number2<0):
            lb5["text"] = "Hatalı giriş yaptınız!! Tekrar Deneyiniz"
            lb5["fg"] = "red"
            break
            
        if(abs(number1-number) > abs(number2-number)):
            lb5["text"] = "İlk Başlayan " + ent2.get() 
            atis(ent2.get(), ent1.get())
            break
        elif(abs(number1-number) < abs(number2-number)):
            lb5["text"] = "İlk başlayan " + ent1.get() 
            atis(ent1.get(), ent2.get())
            break
        elif(abs(number1-number) == abs(number2-number)):
            lb5["text"] = "Berabere tekrar çekiliş yapın"
            break
        else:
            lb5["text"] = "Hatalı giriş yaptınız!! Tekrar Deneyiniz"
            break
        
def atis(namex, namey):
    atis1 = random.randint(1,7)
    lb6["text"] = (f"{namex} {atis1} değerini attı.")
    atis2 = random.randint(1,7)
    lb8["text"] = (f"{namey} {atis2} değerini attı.")
    if(atis1 > atis2):
        lb7["text"] = (f"{namex} Kazandı ")
        lb7["fg"] = "orange"
        lb6["fg"] = "green"
        lb8["fg"] = "red"
    elif(atis1 < atis2):
        lb7["text"] = (f"{namey} Kazandı ")
        lb7["fg"] = "orange"
        lb6["fg"] = "red"
        lb8["fg"] = "green"
    elif(atis1 == atis2):
        lb7["text"] = ("Durum berabere")
        lb7["fg"] = "orange" 
        lb6["fg"] = "blue"
        lb8["fg"] = "blue"


def finish():
    window.destroy() 
    
bt1 = tk.Button(window, text="Zar At", fg="white", bg="navy", font="arial 12", command=zar)
bt1.place(x=470, y=220)
bt2 = tk.Button(window, text="Çıkış", fg="white", bg="navy", font="arial 12", command=finish)
bt2.place(x=550, y=220)
     

window.mainloop()         


