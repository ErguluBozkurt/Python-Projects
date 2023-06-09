"""
2,3,4 ve 5 kişilik bir şans oyunudur. Gelen renge göre kimin seçildiği belirtilir. 
İki kişilik için kod çalışır durumdadır. Dilerseniz sizler 3 veya daha fazla kişi için güncelleyebilirsiniz.

"""

import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import random


window = tk.Tk()
window.geometry("900x700+600+60")
window.title("Şans Oyunu")
window.resizable(False,False)

# Seçim
lb1 = tk.Label(window, text="Kişi Sayısı", fg="black", font="italic 12")
lb1.place(x=20, y=20)
people = [2,3,4,5]
combo1 = Combobox(window, values=people, width=10)
combo1.current(0)
combo1.place(x=130, y=25)

foto_list = list()
img1 = tk.PhotoImage(file="kırmızı.png")
img2 = tk.PhotoImage(file="mavi.png")
img3 = tk.PhotoImage(file="siyah.png")
img4 = tk.PhotoImage(file="ws.png")
img5 = tk.PhotoImage(file="yesil.png")

# Renk Listesi
color_list = ["Kırmızı ", "Mavi       ", "Turuncu ", "Siyah     ", "Yeşil     "]

# Kişi Sayısı
def human_many():
    if(int(combo1.get())==2):
    
        lb2 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb2.place(x=20, y=100)
        ent1 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent1.place(x=20, y=125)

        lb3 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb3.place(x=200, y=100)
        ent2 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent2.place(x=200, y=125)
        
        lb4 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb4.place(x=380, y=100)
        lb4 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb4.place(x=380, y=125)
        
        lb5 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb5.place(x=560, y=100)
        lb5 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb5.place(x=560, y=125)
        
        lb6 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb6.place(x=740, y=100)
        lb6 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb6.place(x=740, y=125)
        
    elif(int(combo1.get())==3):
        
        lb2 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb2.place(x=20, y=100)
        ent1 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent1.place(x=20, y=125)

        lb3 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb3.place(x=200, y=100)
        ent2 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent2.place(x=200, y=125)

        lb4 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb4.place(x=380, y=100)
        ent3 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent3.place(x=380, y=125)
        
        lb5 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb5.place(x=560, y=100)
        lb5 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb5.place(x=560, y=125)
        
        lb6 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb6.place(x=740, y=100)
        lb6 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb6.place(x=740, y=125)
    
    elif(int(combo1.get())==4):
        
        lb2 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb2.place(x=20, y=100)
        ent1 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent1.place(x=20, y=125)

        lb3 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb3.place(x=200, y=100)
        ent2 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent2.place(x=200, y=125)

        lb4 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb4.place(x=380, y=100)
        ent3 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent3.place(x=380, y=125)

        lb5 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb5.place(x=560, y=100)
        ent4 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent4.place(x=560, y=125)
        
        lb6 = tk.Label(window, text="                 ", fg="black", font="italic 13")
        lb6.place(x=740, y=100)
        lb6 = tk.Label(window, text="                              ", fg="black", font="italic 13")
        lb6.place(x=740, y=125)
    
    elif(int(combo1.get())==5):
        
        lb2 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb2.place(x=20, y=100)
        ent1 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent1.place(x=20, y=125)

        lb3 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb3.place(x=200, y=100)
        ent2 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent2.place(x=200, y=125)

        lb4 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb4.place(x=380, y=100)
        ent3 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent3.place(x=380, y=125)

        lb5 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb5.place(x=560, y=100)
        ent4 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent4.place(x=560, y=125)

        lb6 = tk.Label(window, text="Kişi Adı", fg="black", font="italic 13")
        lb6.place(x=740, y=100)
        ent5 = tk.Entry(window, font="arial 12 bold", fg="black", width=15)
        ent5.place(x=740, y=125)
    
    else:
        messagebox.showwarning(title="HATALI GİRİŞ", message="         Hatalı Kişi Sayısı                           ")
    
    # Renk seçimi
    def luck_start():
        
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)
        while(color1==color2):
            color2 = random.choice(color_list)
        color3 = random.choice(color_list)
        while(color1==color3 or color2==color3):
            color3 = random.choice(color_list)
        color4 = random.choice(color_list)
        while(color1==color4 or color2==color4 or color3==color4):
            color4 = random.choice(color_list)
        color5 = random.choice(color_list)
        while(color1==color5 or color2==color5 or color3==color5 or color4==color5):
            color5 = random.choice(color_list)


        
        if(int(combo1.get())==2):
            lb7 = tk.Label(window, text=color1, font="italic 13")
            lb7.place(x=20, y=150)
            
            lb8 = tk.Label(window, text=color2, font="italic 13")
            lb8.place(x=200, y=150)
            
            if(color1=="Kırmızı " and color2=="Mavi       ") or (color1=="Mavi       " and color2=="Kırmızı "):
                foto_list.append(img1)
                foto_list.append(img2)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
                
            elif(color1=="Turuncu " and color2=="Kırmızı ") or (color2=="Turuncu " and color1=="Kırmızı ")  :
                foto_list.append(img1)
                foto_list.append(img4)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
            elif(color1=="Yeşil     " and color2=="Kırmızı ") or (color2=="Yeşil     " and color1=="Kırmızı "):
                foto_list.append(img1)
                foto_list.append(img5)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
                
                
            elif(color1=="Siyah     " and color2=="Kırmızı ") or (color2=="Siyah     " and color1=="Kırmızı "):
                foto_list.append(img1)
                foto_list.append(img3)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
            
            elif(color1=="Siyah     " and color2=="Mavi       ") or (color2=="Siyah     " and color1=="Mavi       "):
                foto_list.append(img2)
                foto_list.append(img3)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
                
            elif(color1=="Siyah     " and color2=="Turuncu ") or (color2=="Siyah     " and color1=="Turuncu "):
                foto_list.append(img4)
                foto_list.append(img3)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
                
            elif(color1=="Siyah     " and color2=="Yeşil     ") or (color2=="Siyah     " and color1=="Yeşil     "):
                foto_list.append(img5)
                foto_list.append(img3)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
                
            elif(color2=="Mavi       " and color1=="Yeşil     ") or (color1=="Mavi       " and color2=="Yeşil     "):
                foto_list.append(img5)
                foto_list.append(img2)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
            
            elif(color1=="Mavi       " and color2=="Turuncu ") or (color2=="Mavi       " and color1=="Turuncu "):
                foto_list.append(img2)
                foto_list.append(img4)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
            
            elif(color1=="Yeşil     " and color2=="Turuncu ") or (color2=="Yeşil     " and color1=="Turuncu "):
                foto_list.append(img5)
                foto_list.append(img4)
                img = random.choice(foto_list)
                lb12 = tk.Label(window, image=img)
                lb12.place(x=400, y=400)
                foto_list.pop()
                foto_list.pop()
        
    
        elif(int(combo1.get())==3):
            lb7 = tk.Label(window, text=color1, font="italic 13")
            lb7.place(x=20, y=150)
            
            lb8 = tk.Label(window, text=color2, font="italic 13")
            lb8.place(x=200, y=150)
            
            lb9 = tk.Label(window, text=color3, font="italic 13")
            lb9.place(x=380, y=150)
            
         
        elif(int(combo1.get())==4):
            lb7 = tk.Label(window, text=color1, font="italic 13")
            lb7.place(x=20, y=150)
            
            lb8 = tk.Label(window, text=color2, font="italic 13")
            lb8.place(x=200, y=150)
            
            lb9 = tk.Label(window, text=color3, font="italic 13")
            lb9.place(x=380, y=150)
            
            lb10 = tk.Label(window, text=color4, font="italic 13")
            lb10.place(x=560, y=150)
            
    
        elif(int(combo1.get())==5):
            lb7 = tk.Label(window, text=color1, font="italic 13")
            lb7.place(x=20, y=150)
            
            lb8 = tk.Label(window, text=color2, font="italic 13")
            lb8.place(x=200, y=150)
            
            lb9 = tk.Label(window, text=color3, font="italic 13")
            lb9.place(x=380, y=150)
            
            lb10 = tk.Label(window, text=color4, font="italic 13")
            lb10.place(x=560, y=150)
            
            lb11 = tk.Label(window, text=color5, font="italic 13")
            lb11.place(x=740, y=150)
        
        
        if(int(combo1.get())==2):    
            if(color1=="Kırmızı "):
                lb7["fg"] = "red"
            elif(color1=="Mavi       "):
                lb7["fg"] = "blue"
            elif(color1=="Turuncu "):
                lb7["fg"] = "orange"
            elif(color1=="Yeşil     "):
                lb7["fg"] = "green"
            elif(color1=="Siyah     "):
                lb7["fg"] = "black"
            
            if(color2=="Kırmızı "):
                lb8["fg"] = "red"
            elif(color2=="Mavi       "):
                lb8["fg"] = "blue"
            elif(color2=="Turuncu "):
                lb8["fg"] = "orange"
            elif(color2=="Yeşil     "):
                lb8["fg"] = "green"
            elif(color2=="Siyah     "):
                lb8["fg"] = "black"
        
        if(int(combo1.get())==3): 
            if(color1=="Kırmızı "):
                lb7["fg"] = "red"
            elif(color1=="Mavi       "):
                lb7["fg"] = "blue"
            elif(color1=="Turuncu "):
                lb7["fg"] = "orange"
            elif(color1=="Yeşil     "):
                lb7["fg"] = "green"
            elif(color1=="Siyah     "):
                lb7["fg"] = "black"
            
            if(color2=="Kırmızı "):
                lb8["fg"] = "red"
            elif(color2=="Mavi       "):
                lb8["fg"] = "blue"
            elif(color2=="Turuncu "):
                lb8["fg"] = "orange"
            elif(color2=="Yeşil     "):
                lb8["fg"] = "green"
            elif(color2=="Siyah     "):
                lb8["fg"] = "black"
                
            if(color3=="Kırmızı "):
                lb9["fg"] = "red"
            elif(color3=="Mavi       "):
                lb9["fg"] = "blue"
            elif(color3=="Turuncu "):
                lb9["fg"] = "orange"
            elif(color3=="Yeşil     "):
                lb9["fg"] = "green"
            elif(color3=="Siyah     "):
                lb9["fg"] = "black"
                
        if(int(combo1.get())==4): 
            if(color1=="Kırmızı "):
                lb7["fg"] = "red"
            elif(color1=="Mavi       "):
                lb7["fg"] = "blue"
            elif(color1=="Turuncu "):
                lb7["fg"] = "orange"
            elif(color1=="Yeşil     "):
                lb7["fg"] = "green"
            elif(color1=="Siyah     "):
                lb7["fg"] = "black"
            
            if(color2=="Kırmızı "):
                lb8["fg"] = "red"
            elif(color2=="Mavi       "):
                lb8["fg"] = "blue"
            elif(color2=="Turuncu "):
                lb8["fg"] = "orange"
            elif(color2=="Yeşil     "):
                lb8["fg"] = "green"
            elif(color2=="Siyah     "):
                lb8["fg"] = "black"
                
            if(color3=="Kırmızı "):
                lb9["fg"] = "red"
            elif(color3=="Mavi       "):
                lb9["fg"] = "blue"
            elif(color3=="Turuncu "):
                lb9["fg"] = "orange"
            elif(color3=="Yeşil     "):
                lb9["fg"] = "green"
            elif(color3=="Siyah     "):
                lb9["fg"] = "black"
                
            if(color4=="Kırmızı "):
                lb10["fg"] = "red"
            elif(color4=="Mavi       "):
                lb10["fg"] = "blue"
            elif(color4=="Turuncu "):
                lb10["fg"] = "orange"
            elif(color4=="Yeşil     "):
                lb10["fg"] = "green"
            elif(color4=="Siyah     "):
                lb10["fg"] = "black"
        
        if(int(combo1.get())==5): 
            if(color1=="Kırmızı "):
                lb7["fg"] = "red"
            elif(color1=="Mavi       "):
                lb7["fg"] = "blue"
            elif(color1=="Turuncu "):
                lb7["fg"] = "orange"
            elif(color1=="Yeşil     "):
                lb7["fg"] = "green"
            elif(color1=="Siyah     "):
                lb7["fg"] = "black"
            
            if(color2=="Kırmızı "):
                lb8["fg"] = "red"
            elif(color2=="Mavi       "):
                lb8["fg"] = "blue"
            elif(color2=="Turuncu "):
                lb8["fg"] = "orange"
            elif(color2=="Yeşil     "):
                lb8["fg"] = "green"
            elif(color2=="Siyah     "):
                lb8["fg"] = "black"
                
            if(color3=="Kırmızı "):
                lb9["fg"] = "red"
            elif(color3=="Mavi       "):
                lb9["fg"] = "blue"
            elif(color3=="Turuncu "):
                lb9["fg"] = "orange"
            elif(color3=="Yeşil     "):
                lb9["fg"] = "green"
            elif(color3=="Siyah     "):
                lb9["fg"] = "black"
                
            if(color4=="Kırmızı "):
                lb10["fg"] = "red"
            elif(color4=="Mavi       "):
                lb10["fg"] = "blue"
            elif(color4=="Turuncu "):
                lb10["fg"] = "orange"
            elif(color4=="Yeşil     "):
                lb10["fg"] = "green"
            elif(color4=="Siyah     "):
                lb10["fg"] = "black"
                
            if(color5=="Kırmızı "):
                lb11["fg"] = "red"
            elif(color5=="Mavi       "):
                lb11["fg"] = "blue"
            elif(color5=="Turuncu "):
                lb11["fg"] = "orange"
            elif(color5=="Yeşil     "):
                lb11["fg"] = "green"
            elif(color5=="Siyah     "):
                lb11["fg"] = "black"
          
 
    bt2 = tk.Button(window, text="Oyna", fg="white", bg="navy", font="arial 12", command=luck_start)
    bt2.place(x=400, y=200)

bt1 = tk.Button(window, text="Başla", fg="white", bg="navy", font="arial 12", command=human_many)
bt1.place(x=250, y=20)

window.mainloop()