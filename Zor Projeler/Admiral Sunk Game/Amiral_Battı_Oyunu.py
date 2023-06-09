"""
Bu proje amiral battı oyunun dan esinlenerek geliştirilmiştir. Tkinter ile görsel arayüz geliştirilmiştir.
"""

import random
import tkinter as tk
from tkinter.ttk import Combobox

window = tk.Tk()
window.title("Amiral Battı")
window.geometry("600x600+600+100")
window.resizable(False, False)

img = tk.PhotoImage(file="amiral2.png")
lb1 = tk.Label(window, image=img)
lb1.place(x=0, y=0)

lb2 = tk.Label(window, text="", font="arial 14 bold", fg="white", bg="#282834")
lb2.place(x=170,y=90)

lb3 = tk.Label(window,text="", font="arial 14", bg="#282834")
lb3.place(x=170,y=40)

board = list()
location = list()
my_list = list()
score = 1000
heart = 10
sayac = 0
value = ["1","2","3","4","5"]

def main_function():
    
    def destroyy():
        window.destroy()

    for i in range(0,5):
        board.append(["0"]*5)
        
    def board_see():
        matrix = f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}".replace(',','')
        lb2["text"] = " ".join(matrix)
    board_see()
    
    def wrong_result():
        board[x-1][y-1] = "x"
        board_see()

    def true_result():
        board[x-1][y-1] = "/"
        board_see()
        
    def game():
        global location
        for j in range(0,5):
            ship1 = random.randint(1,5)
            ship2 = random.randint(1,5)
            location.append([ship1,ship2])
            
    game()
    
    combo1 = Combobox(window, values=value, height=5)
    combo1.place(x=170,y=250, width=70)
    combo2 = Combobox(window, values=value, height=5)
    combo2.place(x=250,y=250, width=70)
    def proces():
        
        global stop, t, x, y, sayac, location, score
        x = int(combo1.get())
        y = int(combo2.get())
        my_list.append([x,y])
        sayac += 1
        t = 0
        stop = 0
        
        for i in range(0,5):
            if(location[i][0]==x and location[i][1]==y and stop==0):
                
                lb3["text"] = f"Tebrikler Bildiniz \nScorunuz: {score}"
                lb3["fg"] = "green"
                true_result()
                stop=1
                break
            t = t + 1
            if(t==5 and stop==0):
                score = score - 100
                lb3["text"] = f"Yanlış Cevap!! \nScorunuz: {score}"
                lb3["fg"] = "red"
                wrong_result()
                stop = 1
                break
            if(sayac>1 and stop==0):
                for i in range(0,sayac-1):
                    if(my_list[i][0]==x and my_list[i][1]==y):
                        lb3["text"] = f"Lütfen Farklı Değer Giriniz!!"
                        lb3["fg"] = "orange"
                        score = score - 100
                        stop = 1
                        break
                                
        if(sayac==heart):
            lb3["text"] = f"Scorunuz: {score} \nCanınız Bitti. Tekrar Oynamak İstermisiniz?"
            lb3["fg"] = "red"
            bt2 = tk.Button(window, text="Evet", font="italic 14 bold", command=main_function)
            bt2.place(x=200,y=300)
            bt3 = tk.Button(window, text="Hayır", font = "italic 14 bold", command=destroyy)
            bt3.place(x=350,y=300)
                
    bt1 = tk.Button(window, text="Onayla", font="italic 14 bold", fg="white", bg="navy", command=proces)
    bt1.place(x=260, y=400)    
bt1 = tk.Button(window, text="Başla", font="italic 14 bold", fg="white", bg="navy", command=main_function)
bt1.place(x=260, y=400)

window.mainloop()

