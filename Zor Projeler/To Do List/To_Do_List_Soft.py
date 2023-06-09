"""
Basit bir to do list uygulamasıdır. tkinter ile arayüz, sqlite ile database oluşturulmuştur.
Maksimum 5 görev eklenebilir dilerseniz arttırabilirsiniz.
"""

# Kütüphanler eklendi
import tkinter as tk
import sqlite3 as sql
from tkinter.ttk import Combobox


number = 0
def ana_fonksiyon():
    window = tk.Tk()
    window.title("To Do List")
    window.geometry("600x600+900+70")
    window.resizable(False,False)

    lb1 = tk.Label(window, text="Ergülü Bozkurt'un Yapılacaklar Listesi", font="italic 14 bold")
    lb1.pack(pady=50)

    db = sql.connect("task.sqlite")
    imlec = db.cursor()
    
    # Kaydı göster
    def show_info():
        
        img = tk.PhotoImage(file="gri.png")
        lb4 = tk.Label(window, image=img)
        lb4.place(x=30, y=160)
        
        imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
        imlec.execute("SELECT * FROM Duty")
        infos = imlec.fetchall()
        lenght = len(infos)
        
        if(lenght==1):
            lb5 = tk.Label(window, text="1." + infos[0][1], font="arial 13 bold")
            lb5.place(x=50, y=200)
            lb6 = tk.Label(window, text=infos[0][0], font="arial 12")
            lb6.place(x=50, y=230)
        
        elif(lenght==2):
            lb5 = tk.Label(window, text="1." + infos[0][1], font="arial 13 bold")
            lb5.place(x=50, y=200)
            lb6 = tk.Label(window, text=infos[0][0], font="arial 12")
            lb6.place(x=50, y=230)
            
            lb7 = tk.Label(window, text="2." + infos[1][1], font="arial 13 bold")
            lb7.place(x=50, y=280)
            lb8 = tk.Label(window, text=infos[1][0], font="arial 12")
            lb8.place(x=50, y=310)
        
        elif(lenght==3):
            lb5 = tk.Label(window, text="1." + infos[0][1], font="arial 13 bold")
            lb5.place(x=50, y=200)
            lb6 = tk.Label(window, text=infos[0][0], font="arial 12")
            lb6.place(x=50, y=230)
            
            lb7 = tk.Label(window, text="2." + infos[1][1], font="arial 13 bold")
            lb7.place(x=50, y=280)
            lb8 = tk.Label(window, text=infos[1][0], font="arial 12")
            lb8.place(x=50, y=310)
            
            lb9 = tk.Label(window, text="3." + infos[2][1], font="arial 13 bold")
            lb9.place(x=50, y=360)
            lb10 = tk.Label(window, text=infos[2][0], font="arial 12")
            lb10.place(x=50, y=390)
            
        elif(lenght==4):
            lb5 = tk.Label(window, text="1." + infos[0][1], font="arial 13 bold")
            lb5.place(x=50, y=200)
            lb6 = tk.Label(window, text=infos[0][0], font="arial 12")
            lb6.place(x=50, y=230)
            
            lb7 = tk.Label(window, text="2." + infos[1][1], font="arial 13 bold")
            lb7.place(x=50, y=280)
            lb8 = tk.Label(window, text=infos[1][0], font="arial 12")
            lb8.place(x=50, y=310)
            
            lb9 = tk.Label(window, text="3." + infos[2][1], font="arial 13 bold")
            lb9.place(x=50, y=360)
            lb10 = tk.Label(window, text=infos[2][0], font="arial 12")
            lb10.place(x=50, y=390)
            
            lb11 = tk.Label(window, text="4." + infos[3][1], font="arial 13 bold")
            lb11.place(x=50, y=440)
            lb12 = tk.Label(window, text=infos[3][0], font="arial 12")
            lb12.place(x=50, y=470)
            
        elif(lenght==5):
            lb5 = tk.Label(window, text="1." + infos[0][1], font="arial 13 bold")
            lb5.place(x=50, y=200)
            lb6 = tk.Label(window, text=infos[0][0], font="arial 12")
            lb6.place(x=50, y=230)
            
            lb7 = tk.Label(window, text="2." + infos[1][1], font="arial 13 bold")
            lb7.place(x=50, y=280)
            lb8 = tk.Label(window, text=infos[1][0], font="arial 12")
            lb8.place(x=50, y=310)
            
            lb9 = tk.Label(window, text="3." + infos[2][1], font="arial 13 bold")
            lb9.place(x=50, y=360)
            lb10 = tk.Label(window, text=infos[2][0], font="arial 12")
            lb10.place(x=50, y=390)
            
            lb11 = tk.Label(window, text="4." + infos[3][1], font="arial 13 bold")
            lb11.place(x=50, y=440)
            lb12 = tk.Label(window, text=infos[3][0], font="arial 12")
            lb12.place(x=50, y=470)
            
            lb13 = tk.Label(window, text="5." + infos[4][1], font="arial 13 bold")
            lb13.place(x=50, y=520)
            lb14 = tk.Label(window, text=infos[4][0], font="arial 12")
            lb14.place(x=50, y=550)
        
        elif(lenght>5):
            lb5 = tk.Label(window, text="Çok Fazla Görev Girdiniz \nLütfen Biraz Siliniz", font="arial 14 bold", fg="orange")
            lb5.place(x=150, y=200)
        
        else:
            lb5 = tk.Label(window, text="Her Hangi Bir Göreviniz Yok", font="arial 14 bold", fg="orange")
            lb5.place(x=150, y=200)
        
    # Kaydet
    def write_info():
        
        img = tk.PhotoImage(file="gri.png")
        lb4 = tk.Label(window, image=img)
        lb4.place(x=30, y=160)
        
        my_list = list()
        lb2 = tk.Label(window, text="Görev Nedir?", font="arial 12")
        lb2.place(x=50, y=170)
        ent1 = tk.Entry(window, font="arial 12")
        ent1.place(x=50, y=200, width=500, height=30)
        
        lb3 = tk.Label(window, text="Hangi Gün Yapılacak?", font="arial 12")
        lb3.place(x=50, y=250)
        
        def day_one():
            my_list.append(("Pazartesi"))
        def day_two():
            my_list.append("Salı")
        def day_three():
            my_list.append("Çarşamba")
        def day_four():
            my_list.append("Perşembe")
        def day_five():
            my_list.append("Cuma")
        def day_six():
            my_list.append("Cumartesi")
        def day_seven():
            my_list.append("Pazar")
            
        
        day1 = tk.IntVar()
        day1.set(0)  
        day2 = tk.IntVar()
        day2.set(0)  
        day3 = tk.IntVar()
        day3.set(0)  
        day4 = tk.IntVar()
        day4.set(0)  
        day5 = tk.IntVar()
        day5.set(0)  
        day6 = tk.IntVar()
        day6.set(0)  
        day7 = tk.IntVar()
        day7.set(0)
        
        checkbox1 = tk.Checkbutton(window, text="Pazartesi", variable=day1, font="arial 12", command=day_one)
        checkbox1.place(x=50, y=280)
        
        checkbox2 = tk.Checkbutton(window, text="Salı", variable=day2, font="arial 12", command=day_two)
        checkbox2.place(x=50, y=310)
        
        checkbox3 = tk.Checkbutton(window, text="Çarşamba", variable=day3, font="arial 12", command=day_three)
        checkbox3.place(x=50, y=340)
        
        checkbox4 = tk.Checkbutton(window, text="Perşembe", variable=day4, font="arial 12", command=day_four)
        checkbox4.place(x=230, y=280)
        
        checkbox5 = tk.Checkbutton(window, text="Cuma", variable=day5, font="arial 12", command=day_five)
        checkbox5.place(x=230, y=310)
        
        checkbox6 = tk.Checkbutton(window, text="Cumartesi", variable=day6, font="arial 12", command=day_six)
        checkbox6.place(x=230, y=340)
        
        checkbox7 = tk.Checkbutton(window, text="Pazar", variable=day7, font="arial 12", command=day_seven)
        checkbox7.place(x=410, y=280)
        
        def save():
            global number
            number = number + 1
            print(number)
            tpl = (str(ent1.get()), str(my_list), number)

            imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
            imlec.execute("INSERT INTO Duty VALUES(?,?,?)",tpl)
            db.commit()
            
            
            

        bt4 = tk.Button(window, text="Kaydet", fg="white", bg="navy", font="italic 12 bold", command=save)
        bt4.place(x=450, y=400)
    
    # Kaydı Sil
    def delete_info():
        
        img = tk.PhotoImage(file="gri.png")
        lb4 = tk.Label(window, image=img)
        lb4.place(x=30, y=160)
        
        lb15 = tk.Label(window, text="Hangi Numaralı Notu Sileceksiniz?", font="arial 12")
        lb15.place(x=50, y=170)
        
        number = [1,2,3,4,5]
        combo1 = Combobox(window, values=number)
        combo1.current(0)
        combo1.place(x=50, y=200)
        
        
        def delete():
            global number
            number = number - 1
            print(number)
            imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
            imlec.execute(f"DELETE FROM Duty WHERE No={combo1.get()}")
            imlec.execute(f"UPDATE Duty SET No={number}")
            imlec.execute("SELECT * FROM Duty")
            infos = imlec.fetchall()
            print(infos)
            db.commit()
            
        
        bt5 = tk.Button(window, text="Sil", fg="white", bg="navy", font="italic 12 bold", width=10, command=delete)
        bt5.place(x=100, y=250)



    bt1 = tk.Button(window, text="Görevleri Göster", fg="white", bg="navy", font="italic 12 bold", command=show_info)
    bt1.place(x=50, y=100)

    bt2 = tk.Button(window, text="Yeni Görev Gir", fg="white", bg="navy", font="italic 12 bold", command=write_info)
    bt2.place(x=260, y=100)

    bt3 = tk.Button(window, text="Görev Sil", fg="white", bg="navy", font="italic 12 bold", command=delete_info)
    bt3.place(x=450, y=100)

    
    window.mainloop()
ana_fonksiyon()
