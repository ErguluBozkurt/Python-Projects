"""
Bu proje basit bir sudoku oyunudur. Diğer yazdığım projelere bakarak geliştirebilirsiniz.
"""


import numpy as np
import random
import tkinter as tk
from tkinter.ttk import Combobox  


def main():
    window = tk.Tk()
    window.title("Sudoku")
    window.geometry("800x600+650+60")
    window.resizable(False, False)
    number = [1,2,3,4,5,6,7,8,9]

    zeros = np.zeros((9,9))

    for i in range(35):
        rd = random.randint(1,9)
        
        matriks_x = random.randint(0,8)
        matriks_y = random.randint(0,8)
        zeros[matriks_x, matriks_y] = rd
        
    lb1 = tk.Label(window, text=zeros, font="arial 20", fg="red", bg="black")
    lb1.place(x=250, y=50)
    lb2 = tk.Label(window, text="Satır Numarası", font="arial 14")
    lb2.place(x=200, y=370)
    lb3 = tk.Label(window, text="Sutün Numarası", font="arial 14")
    lb3.place(x=200, y=430)
    lb4 = tk.Label(window, text="Sayı", font="arial 14")
    lb4.place(x=400, y=370)
    lb5 = tk.Label(window, text="    1    2    3    4    5    6    7    8    9", font="arial 14", fg="black")
    lb5.place(x=250, y=20)     
    
    # Duyuru
    lb6 = tk.Label(window, text="", font="arial 20", fg="orange")
    lb6.place(x=50, y=50)

    combo1 = Combobox(window, values=number, height=9)
    combo1.place(x=200, y = 400)
    combo2 = Combobox(window, values=number, height=9)
    combo2.place(x=200, y=460)
    combo3 = Combobox(window, values=number, height=9)
    combo3.place(x=400, y=400)
    
    def add():
        satir = int(combo1.get()) - 1
        sutun = int(combo2.get()) - 1
        try:
            value = int(zeros[satir,sutun])
            if(zeros[satir,sutun] == 0):
                zeros[satir, sutun] = int(combo3.get())
                lb1["text"] = zeros
                lb6["text"] = ""
            else:
                lb6["text"] = "Seçtiğiniz Yer \nDolu!!"
        except:
            lb6["text"] = "Lütfen Sayı \nGiriniz!!"
        
    def again():
        window.destroy()
        main()
            
    bt1 = tk.Button(window, text="Ekle", font="arial 14", fg="white", bg="navy", command=add)
    bt1.place(x=400, y=450)
    bt2 = tk.Button(window, text="Tekrar Başla", font="arial 14", fg="white", bg="navy", command=again)
    bt2.place(x=500, y=450)

    window.mainloop()
main()
