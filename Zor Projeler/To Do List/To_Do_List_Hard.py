"""
Bu kod bir to-do-list kodudur.Kod içerisinde SQLite ve tkinter kütüphaneleri yoğun olarak kullanılmıştır.
Kodu çalıştırdığınızda da görebileceğiniz gibi önünüze 4 seçenek çıkacaktır. Bunlar sırası ile listeye bakma
not ekleme, notu güncelleme ve notu silme şeklindedir. 5 Adet görev kaydı ekleyebilirsiniz isterseniz arttırabilirsiniz.
Kod içerisinde gerekli kodların açıklaması yapılmıştır. Kayıt alanına notunuzun açıklaması ve hangi gün yapılacağı 
hakkında bilgiler tutulur. Koda ek olarak saat ve istenilen parametrelerde eklenebilir. Ayrıca kayıtlı olan görevi 
sesli şekilde okuyabilmektedir.

"""
# Kütüphanler Tanımlandı
import sqlite3 as sql
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from gtts import gTTS
import pygame
import time

# Tkinter ile bir arayüz ekranı oluşturuldu.
window = tk.Tk()
window.title("Yardımcı Asistan")
window.geometry("800x600+700+70")
window.resizable(False, False)

# SQLite ile bir database oluşturuldu.
db = sql.connect("task.sqlite")
imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
imlec.execute("SELECT * FROM Duty")
infos = imlec.fetchall()
lenght = len(infos)

# Daha önceden database de ki kayıt adedi.
if(lenght==1):
    number = int(infos[0][2])
elif(lenght==2):
    number = int(infos[1][2])
elif(lenght==3):
    number = int(infos[2][2])
elif(lenght==4):
    number = int(infos[3][2])
elif(lenght==5):
    number = int(infos[4][2])
else:
    number = 0
    
# Ekranın bir parçasını beyaz tema yapmak için kullanıldı.
img = tk.PhotoImage(file="Beyaz.png")
lb = tk.Label(window, image=img)
lb.place(x=35, y=20, width=500, height=550)

# Kayıt göster
def show_info():
    global img, lb
    t = 0
    img = tk.PhotoImage(file="Beyaz.png")
    lb = tk.Label(window, image=img)
    lb.place(x=35, y=20, width=500, height=550)
    
    db = sql.connect("task.sqlite")
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
    imlec.execute("SELECT * FROM Duty")
    infos = imlec.fetchall()
    lenght = len(infos)
    
    # Kayıtların gösterilmesi 
    if(lenght>=1):
        lb5 = tk.Label(window, text=" Görev 1 - " + infos[0][1], font="arial 13 bold", bg="white")
        lb5.place(x=40, y=100)
        lb6 = tk.Label(window, text=infos[0][0], font="arial 12", bg="white")
        lb6.place(x=40, y=130)
    
        if(lenght>=2):
            lb7 = tk.Label(window, text="Görev 2 - " + infos[1][1], font="arial 13 bold", bg="white")
            lb7.place(x=40, y=180)
            lb8 = tk.Label(window, text=infos[1][0], font="arial 12", bg="white")
            lb8.place(x=40, y=210)
        
            if(lenght>=3):        
                lb9 = tk.Label(window, text="Görev 3 - " + infos[2][1], font="arial 13 bold", bg="white")
                lb9.place(x=40, y=260)
                lb10 = tk.Label(window, text=infos[2][0], font="arial 12", bg="white")
                lb10.place(x=40, y=290)
        
                if(lenght>=4):        
                    lb11 = tk.Label(window, text="Görev 4 - " + infos[3][1], font="arial 13 bold", bg="white")
                    lb11.place(x=40, y=340)
                    lb12 = tk.Label(window, text=infos[3][0], font="arial 12", bg="white")
                    lb12.place(x=40, y=370)
        
                    if(lenght==5):        
                        lb13 = tk.Label(window, text="Görev 5 - " + infos[4][1], font="arial 13 bold", bg="white")
                        lb13.place(x=40, y=420)
                        lb14 = tk.Label(window, text=infos[4][0], font="arial 12", bg="white")
                        lb14.place(x=40, y=450)

                        if(lenght>5):   
                            lb5 = tk.Label(window, text="Çok Fazla Görev Girdiniz", font="arial 16 bold", fg="black", bg="white")
                            lb5.place(x=150, y=200)
    else:
        lb5 = tk.Label(window, text="Her Hangi Bir Göreviniz Yok", font="arial 16 bold", fg="black", bg="white")
        lb5.place(x=150, y=200)
    
    # Sesli Oynatmai
    try:
        if(lenght>=1):
            def oynat():
                pygame.init()
                file = "oku" + str(t) + ".mp3"
                pygame.mixer.music.load(file)
                pygame.mixer_music.play()

            for i in infos:
                t = t + 1
                yazi = "Görev " + str(t) + i[0]
                cikti = gTTS(text=yazi, lang="tr", slow=False )
                
                cikti.save("oku" + str(t) + ".mp3")
                oynat()
                time.sleep(7)
    except:
        messagebox.showwarning(title="Bilgi", message="Sesli Oynatma Başarısız.İnternet Bağlantısının Olduğuna Dikkat Edin!!")
    
    db.commit()
    db.close()

# Kayıt güncelle
def update_info():
    global img, lb
    
    img = tk.PhotoImage(file="Beyaz.png")
    lb = tk.Label(window, image=img)
    lb.place(x=35, y=20, width=500, height=550)
    
    lb16 = tk.Label(window, text="", font="arial 14 bold", bg="white")
    lb16.place(x=40, y=170)
    
    db = sql.connect("task.sqlite")
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
    imlec.execute("SELECT * FROM Duty")
    infos = imlec.fetchall()
    lenght = len(infos)
    
        
    def update():
        global img, lb
        img = tk.PhotoImage(file="Beyaz.png")
        lb = tk.Label(window, image=img)
        lb.place(x=35, y=20, width=500, height=550)
        
        # Görev güncelle
        def gorev_mi():
            img = tk.PhotoImage(file="Beyaz.png")
            lb = tk.Label(window, image=img)
            lb.place(x=35, y=20, width=500, height=550)
            
            lbx = tk.Label(window, text="Yeni Görev Nedir?", font="arial 12 bold underline", bg="white")
            lbx.place(x=40, y=30)
            ent2 = tk.Entry(window, font="arial 12")
            ent2.place(x=40, y=60, width=490, height=30)
            
            def change1():
                imlec.execute(f"UPDATE Duty SET Task='{ent2.get()}' WHERE No={combo1.get()}")
                db.commit()
                db.close()
            bt5 = tk.Button(window, text="    Güncelle     ", fg="white", bg="navy", font="italic 13 bold", command=change1)
            bt5.place(x=250, y=250)
        
        # Gün güncelle
        def gun_mu():
            global img, lb, string
            img = tk.PhotoImage(file="Beyaz.png")
            lb = tk.Label(window, image=img)
            lb.place(x=35, y=20, width=500, height=550)
            string = ""
            def day_one():
                global string
                string = "Pazartesi / " + string
            def day_two():
                global string
                string = "Salı / " + string
            def day_three():
                global string
                string = "Çarşamba / " + string
            def day_four():
                global string
                string = "Perşembe / " + string
            def day_five():
                global string
                string = "Cuma / " + string
            def day_six():
                global string
                string = "Cumartesi / " + string
            def day_seven():
                global string
                string = "Pazar / " + string
            def today():
                global string
                string = "Bugün / " + string  
            
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
            day8 = tk.IntVar()
            day8.set(0)
            
            checkbox1 = tk.Checkbutton(window, text="Pazartesi", variable=day1, font="arial 14", bg="white", command=day_one)
            checkbox1.place(x=40, y=200)
            
            checkbox2 = tk.Checkbutton(window, text="Salı", variable=day2, font="arial 14", bg="white", command=day_two)
            checkbox2.place(x=40, y=230)
            
            checkbox3 = tk.Checkbutton(window, text="Çarşamba", variable=day3, font="arial 14", bg="white", command=day_three)
            checkbox3.place(x=40, y=260)
            
            checkbox4 = tk.Checkbutton(window, text="Perşembe", variable=day4, font="arial 14", bg="white", command=day_four)
            checkbox4.place(x=230, y=200)
            
            checkbox5 = tk.Checkbutton(window, text="Cuma", variable=day5, font="arial 14", bg="white", command=day_five)
            checkbox5.place(x=230, y=230)
            
            checkbox6 = tk.Checkbutton(window, text="Cumartesi", variable=day6, font="arial 14", bg="white", command=day_six)
            checkbox6.place(x=230, y=260)
            
            checkbox7 = tk.Checkbutton(window, text="Pazar", variable=day7, font="arial 14", bg="white", command=day_seven)
            checkbox7.place(x=410, y=200)
            
            checkbox8 = tk.Checkbutton(window, text="Bugün", variable=day8, font="arial 14", bg="white", command=today)
            checkbox8.place(x=410, y=230)
            
            def change2():
            
                imlec.execute(f"UPDATE Duty SET Day='{string}' WHERE No={combo1.get()}")   
                db.commit()
                db.close()  
            bt5 = tk.Button(window, text="    Güncelle     ", fg="white", bg="navy", font="italic 13 bold", command=change2)
            bt5.place(x=250, y=350)
            
        gorev_m = tk.IntVar()
        gorev_m.set(0)  
        gun_m = tk.IntVar()
        gun_m.set(0)  
        
        checkbox1 = tk.Checkbutton(window, text="Görev mi?", variable=gorev_m, font="arial 14", bg="white", command=gorev_mi)
        checkbox1.place(x=40, y=200)
        checkbox2 = tk.Checkbutton(window, text="Gün mü?", variable=gun_m, font="arial 14", bg="white", command=gun_mu)
        checkbox2.place(x=40, y=230)
        
    
    # Kayıt seçimi
    if(lenght==1):
        lb16["text"] = "1 Adet Görev Var, Seçiminizi Yapın"
        number = [1]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
        bt5 = tk.Button(window, text="Seçimi Onayla", fg="white", bg="navy", font="italic 13 bold", command=update)
        bt5.place(x=250, y=250)
    elif(lenght==2):
        lb16["text"] = "2 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
        bt5 = tk.Button(window, text="Seçimi Onayla", fg="white", bg="navy", font="italic 13 bold", command=update)
        bt5.place(x=250, y=250)
    elif(lenght==3):
        lb16["text"] = "3 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
        bt5 = tk.Button(window, text="Seçimi Onayla", fg="white", bg="navy", font="italic 13 bold", command=update)
        bt5.place(x=250, y=250)
    elif(lenght==4):
        lb16["text"] = "4 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3,4]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
        bt5 = tk.Button(window, text="Seçimi Onayla", fg="white", bg="navy", font="italic 13 bold", command=update)
        bt5.place(x=250, y=250)
    elif(lenght==5):
        lb16["text"] = "5 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3,4,5]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
        bt5 = tk.Button(window, text="Seçimi Onayla", fg="white", bg="navy", font="italic 13 bold", command=update)
        bt5.place(x=250, y=250)
        
    else:
        lb16["text"] = "Güncellenecek Göreviniz Yok"

# Kaydet
def write_info():
    global img, lb,string
    img = tk.PhotoImage(file="Beyaz.png")
    lb = tk.Label(window, image=img)
    lb.place(x=35, y=20, width=500, height=550)
    
    lb1 = tk.Label(window, text="Görev Nedir?", font="arial 12 bold underline", bg="white")
    lb1.place(x=40, y=30)
    ent1 = tk.Entry(window, font="arial 12")
    ent1.place(x=40, y=60, width=490, height=30)
    
    string = ""
    
    lb2 = tk.Label(window, text="Hangi Gün Yapılacak?", font="arial 12 bold underline", bg="white")
    lb2.place(x=40, y=150)
    
    def day_one():
        global string
        string = "Pazartesi " + string
    def day_two():
        global string
        string = "Salı " + string
    def day_three():
        global string
        string = "Çarşamba " + string
    def day_four():
        global string
        string = "Perşembe " + string
    def day_five():
        global string
        string = "Cuma " + string
    def day_six():
        global string
        string = "Cumartesi " + string
    def day_seven():
        global string
        string = "Pazar " + string
    def today():
        global string
        string = "Bugün " + string      
    
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
    day8 = tk.IntVar()
    day8.set(0)
    
    
    checkbox1 = tk.Checkbutton(window, text="Pazartesi", variable=day1, font="arial 14", bg="white", command=day_one)
    checkbox1.place(x=40, y=200)
    
    checkbox2 = tk.Checkbutton(window, text="Salı", variable=day2, font="arial 14", bg="white", command=day_two)
    checkbox2.place(x=40, y=230)
    
    checkbox3 = tk.Checkbutton(window, text="Çarşamba", variable=day3, font="arial 14", bg="white", command=day_three)
    checkbox3.place(x=40, y=260)
    
    checkbox4 = tk.Checkbutton(window, text="Perşembe", variable=day4, font="arial 14", bg="white", command=day_four)
    checkbox4.place(x=230, y=200)
    
    checkbox5 = tk.Checkbutton(window, text="Cuma", variable=day5, font="arial 14", bg="white", command=day_five)
    checkbox5.place(x=230, y=230)
    
    checkbox6 = tk.Checkbutton(window, text="Cumartesi", variable=day6, font="arial 14", bg="white", command=day_six)
    checkbox6.place(x=230, y=260)
    
    checkbox7 = tk.Checkbutton(window, text="Pazar", variable=day7, font="arial 14", bg="white", command=day_seven)
    checkbox7.place(x=410, y=200)
    
    checkbox8 = tk.Checkbutton(window, text="Bugün", variable=day8, font="arial 14", bg="white", command=today)
    checkbox8.place(x=410, y=230)
    
    def save():
        global number
        
        # Database
        db = sql.connect("task.sqlite")
        imlec = db.cursor()
        imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
        imlec.execute("SELECT * FROM Duty")
        infos = imlec.fetchall()
        lenght = len(infos) 
        
        if(lenght > 4):
            messagebox.showwarning(title="HATA!", message="Çok Fazla Görev Girdiniz!             ")
        else:
            number = number + 1
            tpl = (str(ent1.get()), string, number)
            imlec.execute("INSERT INTO Duty VALUES(?,?,?)",tpl)
            db.commit()
            db.close()
            
                    
    bt5 = tk.Button(window, text="Kaydet", fg="white", bg="navy", font="italic 13 bold", command=save)
    bt5.place(x=250, y=330)
 
# Kayıt sil   
def delete_info():
    global img, lb
    
    img = tk.PhotoImage(file="Beyaz.png")
    lb = tk.Label(window, image=img)
    lb.place(x=35, y=20, width=500, height=550)
    
    lb15 = tk.Label(window, text="", font="arial 14 bold", bg="white")
    lb15.place(x=40, y=170)
    
    db = sql.connect("task.sqlite")
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
    imlec.execute("SELECT * FROM Duty")
    infos = imlec.fetchall()
    lenght = len(infos)
    
    # Kayıt seçimi
    if(lenght==1):
        lb15["text"] = "1 Adet Görev Var, Seçiminizi Yapın"
        number = [1]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
    elif(lenght==2):
        lb15["text"] = "2 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
    elif(lenght==3):
        lb15["text"] = "3 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
    elif(lenght==4):
        lb15["text"] = "4 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3,4]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
    elif(lenght==5):
        lb15["text"] = "5 Adet Görev Var, Seçiminizi Yapın"
        number = [1,2,3,4,5]
        combo1 = Combobox(window, values=number, width=10)
        combo1.current(0)
        combo1.place(x=40, y=200)
    else:
        lb15["text"] = "Silinecek Göreviniz Yok"
        
    # Silme fonksiyonu
    def delete():
        global number
        if(number >= 0):
            number = number - 1
            db = sql.connect("task.sqlite")
            imlec = db.cursor()
            imlec.execute("CREATE TABLE IF NOT EXISTS Duty(Task TEXT, Day TEXT, No INTEGER)")
            imlec.execute(f"DELETE FROM Duty WHERE No={combo1.get()}")
            imlec.execute("SELECT * FROM Duty")
            infos = imlec.fetchall()
            lenght = len(infos)
            if(lenght==1):
                imlec.execute(f"UPDATE Duty SET No=1 WHERE No={infos[0][2]}")
            elif(lenght==2):
                imlec.execute(f"UPDATE Duty SET No=1 WHERE No={infos[0][2]}")
                imlec.execute(f"UPDATE Duty SET No=2 WHERE No={infos[1][2]}")
            elif(lenght==3):
                imlec.execute(f"UPDATE Duty SET No=1 WHERE No={infos[0][2]}")
                imlec.execute(f"UPDATE Duty SET No=2 WHERE No={infos[1][2]}")
                imlec.execute(f"UPDATE Duty SET No=3 WHERE No={infos[2][2]}")
            elif(lenght==4):
                imlec.execute(f"UPDATE Duty SET No=1 WHERE No={infos[0][2]}")
                imlec.execute(f"UPDATE Duty SET No=2 WHERE No={infos[1][2]}")
                imlec.execute(f"UPDATE Duty SET No=3 WHERE No={infos[2][2]}")
                imlec.execute(f"UPDATE Duty SET No=4 WHERE No={infos[3][2]}")
            
            db.commit()
            db.close()
    
    bt5 = tk.Button(window, text="Sil", fg="white", bg="navy", font="italic 12 bold", width=10, command=delete)
    bt5.place(x=240, y=350)


# Ana ekrandaki giriş butonları
bt1 = tk.Button(window, text="Görev Göster", fg="white", bg="blue", font="italic 16 bold", command=show_info)
bt1.place(x=570, y=20, height=100, width=175)

bt2 = tk.Button(window, text="Görev Güncelle", fg="white", bg="green", font="italic 16 bold", command=update_info)
bt2.place(x=570, y=150, height=100)

bt3 = tk.Button(window, text="Görev Ekle", fg="white", bg="orange", font="italic 16 bold", command=write_info)
bt3.place(x=570, y=280, height=100, width=175)

bt4 = tk.Button(window, text="Görev Sil", fg="white", bg="red", font="italic 16 bold", command=delete_info)
bt4.place(x=570, y=410, height=100, width=175)
    
    

window.mainloop() # Arayüzün sürekli açık kalması için