"""
Yapay zekada kullanılan başlıca metodlar ve hazır fonksiyonları tek bir çatı altında toplanmıştır. Arayüz ile kullanımı kolay bir hale getirilerek
arka planda kodların çalışması sağlanmıştır.
"""

import tkinter as tk
import Algoritmalar

window = tk.Tk()
window.title("Yapay Zeka")
window.geometry("1000x600+500+70")
window.resizable(False,False)


def search():
    def notx():
        listem = list()
        window2 = tk.Tk()
        window2.title("Yapay Zeka")
        window2.geometry("500x400+100+70")
        window2.resizable(False,False)
        window2.configure(bg="white")
        strx = str(ent2.get())
        strx = strx.replace(".", "\n")
        listem.append(strx)
        lb4 = tk.Label(window2, text=listem, font="arial 14", bg="white")
        lb4.place(x=20,y=20)
        window2.mainloop()
        
        
    bt5 = tk.Button(window, text="   İlk 5 Değer   ", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.ilk)
    bt5.place(x=90,y=100)
    bt6 = tk.Button(window, text="   Son 5 Değer   ", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.son)
    bt6.place(x=85,y=150)
    bt7 = tk.Button(window, text="  Min-Max Değer  ", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.min_max)
    bt7.place(x=80,y=200)
    lb3 = tk.Label(window, text="Not Ekle", font="italic 12")
    lb3.place(x=20, y=300)
    ent2 = tk.Entry(window, font="arial 14")
    ent2.place(x=20,y=330)
    bt22 = tk.Button(window, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=notx)
    bt22.place(x=60, y=370)  
    
def korelasyon():
    bt8 = tk.Button(window, text="Korelasyon Isı Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.korelasyon_ısı)
    bt8.place(x=310,y=100)
    bt9 = tk.Button(window, text="Seçili Eleman Üzerindeki\nKorelasyon", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.korelasyon_num)
    bt9.place(x=300,y=150)
    
def graph():
    bt10 = tk.Button(window, text="Değişkenler Arası\nGrafik", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.values_graph)
    bt10.place(x=550,y=100)
    bt11 = tk.Button(window, text="Değişkenlerin Kendi\nGrafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.value_graph)
    bt11.place(x=540,y=170)
    bt12 = tk.Button(window, text="Tek Değişken Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.one_graph)
    bt12.place(x=540,y=240)
    
    
def model_select():
    bt13 = tk.Button(window, text="Lineer Regresyon", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.lineer)
    bt13.place(x=785,y=100)
    bt14 = tk.Button(window, text="Polinomal Regresyon", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.polinomal)
    bt14.place(x=770,y=150)
    bt15 = tk.Button(window, text="Çoklu Regresyon", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.coklu)
    bt15.place(x=785,y=200)
    bt16 = tk.Button(window, text="SVM Algoritması", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.svm)
    bt16.place(x=789,y=250)
    bt17 = tk.Button(window, text="SVR Algoritması", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.svr)
    bt17.place(x=789,y=300)
    
def csv():
    with open("Try/save.txt", "w") as file:
        file.write(ent1.get())
        lb2 = tk.Label(window, text="Yükleme Başarılı", font="italic 12", fg="green")
        lb2.place(x=450,y=470)

bt1 = tk.Button(window, text="  Verilere Genel Bakış  ", font="arial 14 bold", bg="blue", fg="white", command=search)
bt1.place(x=40,y=30)
bt2 = tk.Button(window, text="     Korelasyona Bak     ", font="arial 14 bold", bg="orange", fg="white", command=korelasyon)
bt2.place(x=280,y=30)
bt3 = tk.Button(window, text="       Grafik Oluştur      ", font="arial 14 bold", bg="green", fg="white", command=graph)
bt3.place(x=520,y=30)
bt4 = tk.Button(window, text="Eğitilecek Modeli Seç", font="arial 14 bold", bg="red", fg="white", command=model_select)
bt4.place(x=750,y=30)

lb1 = tk.Label(window, text="Dosya Uzantısı", font="italic 12")
lb1.place(x=400, y=350)
ent1 = tk.Entry(window, font="arial 14")
ent1.place(x=400, y=370)
bt18 = tk.Button(window, text="Çalıştır", font="arial 14 bold", fg="white", bg="navy", command=csv)
bt18.place(x=470, y=420)  


window.mainloop() 