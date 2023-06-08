"""
Boy ve kilo bilgilerini alarak indeks hesaplayan bir arayüz projesidir.
"""

import tkinter as tk

window = tk.Tk()
window.title("Endexmatik")
window.geometry("400x600+800+100")
window.resizable(False, False)

#LOGO
l1 = tk.Label(window, text="ENDEXMATİK", font="arial 14 italic bold")
l1.pack(pady=50)

#BOY
l2 = tk.Label(window, text="Boyunuz(cm)", font="arial 12 italic")
l2.place(x=50, y=100)
e1 = tk.Entry(window, font="arial 12")
e1.place(x=180, y=100)

#KİLO
l3 = tk.Label(window, text="Kilonuz", font="arial 12 italic")
l3.place(x=50, y=150)
e2 = tk.Entry(window, font="arial 12")
e2.place(x=180, y=150)

#SONUÇ
l4 = tk.Label(window, text="", font="arial 16 italic")
l4.pack(pady=100)
l5 = tk.Label(window, text="", font="arial 48 italic")
l5.pack()
l6 = tk.Label(window,text="", font="arial 14")
l6.pack()

#BUTON
def hesapla():
    boy = float(e1.get())/100
    kilo = float(e2.get())
    sonuc = round(kilo/pow(boy,2),2)
    l4["text"] = "Boy-Kilo Endeksiniz"
    l5["text"] = str(sonuc)
    if(sonuc<19):
        l6["text"] = "Zayıfsınız"
        l6["fg"] = "orange"
    elif(sonuc<25):
        l6["text"] = "İdeal Kilodasınz"
        l6["fg"] = "green"
    else:
        l6["text"] = "Kilolusunuz"
        l6["fg"] = "red"
    
    
b1 = tk.Button(window, text="Hesapla", bg="green", fg="white", font="arial 12 bold", command=hesapla)
b1.place(x=290, y=160)


window.mainloop()
