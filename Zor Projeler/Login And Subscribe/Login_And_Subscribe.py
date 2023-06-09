"""
Bu proje abone olup giriş yapılabilen arayüz ile desteklenen bir site giriş örneğidir. Yoğun database ve tkinter kullanılmıştır.


"""

import tkinter as tk
import random
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3 as sql
import webbrowser

def ana_fonksiyon():
    window1 = tk.Tk()
    window1.title("Giriş")
    window1.geometry("800x600+700+100")
    window1.configure(bg="white")
    window1.minsize(800,600)

    #LOGO
    img = tk.PhotoImage(file="mainscreen.png")
    lb1 = tk.Label(window1, image=img)
    lb1.pack()
    lb4 = tk.Label(window1, text="HOŞ GELDİNİZ", fg="black", font="italic 18 bold")
    lb4.place(relx = 0.4, rely = 0.06)
    lb5 = tk.Label(window1, text="ERGÜLÜ BOZKURT", fg="black", font="italic 14")
    lb5.place(relx = 0.01, rely = 0.01)

    #Email
    lb2 = tk.Label(window1, text="Email", fg="black", font="arial 12")
    lb2.place(relx = 0.4, rely = 0.2)
    ent1 = tk.Entry(window1, font="italic 13 bold", fg="black")
    ent1.place(relx=0.4, rely=0.24)

    #Password
    lb3 = tk.Label(window1, text="Hesap No", fg="black", font="arial 12")
    lb3.place(relx = 0.4, rely = 0.3)
    ent2 = tk.Entry(window1, font="italic 13 bold", fg="black", width=15, show="*")
    ent2.place(relx=0.4, rely=0.34)

    #Button
    def giris():
        email = str(ent1.get())
        password = str(ent2.get())
        
        tpl1 = tuple()
        tpl1 = (email, password)
        
        db = sql.connect("databese.sqlite")
        imlec =db.cursor()
        imlec.execute("CREATE TABLE IF NOT EXISTS Users(name TEXT, surname TEXT, email_no TEXT, hesap_no TEXT)")
        imlec.execute("SELECT email_no, hesap_no FROM Users")
        listeler = imlec.fetchall()
        for liste in listeler:
            if(liste==tpl1):
                webbrowser.open('https://www.linkedin.com/in/erg%C3%BCl%C3%BC-bozkurt-82345323b/', new=2)
                break
        db.commit()
        db.close()
        
    def kayit():
        window1.destroy()
        window2 = tk.Tk()
        window2.title("Kayıt")
        window2.geometry("800x600+700+100")
        window2.configure(bg="white")
        window2.minsize(800,600)

        #LOGO
        img1 = tk.PhotoImage(file="mainscreen.png")
        lb4 = tk.Label(window2, image=img1)
        lb4.pack()
        lb14 = tk.Label(window2, text="ERGÜLÜ BOZKURT", fg="black", font="italic 14")
        lb14.place(relx = 0.01, rely = 0.01)
        
        #İller 
        iller = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", 
                "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce",
                "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul",
                "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya",
                "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", 
                "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"]
        
        lb11 = tk.Label(window2, text="İl", fg="black", font="arial 12")
        lb11.place(relx = 0.1, rely = 0.1)
        combo2 = Combobox(window2, values=iller, height=10)
        combo2.current(0)
        combo2.place(relx=0.1, rely=0.14)
        
        # Doğum Tarihi
        lb12 = tk.Label(window2, text="Doğum Yılı", fg="black", font="arial 12")
        lb12.place(relx = 0.1, rely = 0.2)
        ent7 = tk.Entry(window2, font="italic 10 bold", fg="black")
        ent7.place(relx=0.1, rely=0.24)
        
        ay = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
        lb10 = tk.Label(window2, text="Doğum Ayı", fg="black", font="arial 12")
        lb10.place(relx = 0.1, rely = 0.3)
        combo1 = Combobox(window2, values=ay, height=6)
        combo1.current(0)
        combo1.place(relx=0.1, rely=0.34)
        
        gun = ["1","2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        lb13 = tk.Label(window2, text="Doğum Günü", fg="black", font="arial 12")
        lb13.place(relx = 0.1, rely = 0.4)
        combo3 = Combobox(window2, values=gun, height=6)
        combo3.current(0)
        combo3.place(relx=0.1, rely=0.44)
        
        #Ad
        lb7 = tk.Label(window2, text="Ad", fg="black", font="arial 12")
        lb7.place(relx = 0.4, rely = 0.1)
        ent5 = tk.Entry(window2, font="italic 13 bold", fg="black")
        ent5.place(relx=0.4, rely=0.14)

        #Soyad
        lb8 = tk.Label(window2, text="Soyad", fg="black", font="arial 12")
        lb8.place(relx = 0.4, rely = 0.2)
        ent6 = tk.Entry(window2, font="italic 13 bold", fg="black")
        ent6.place(relx=0.4, rely=0.24)
        

        #Email
        lb5 = tk.Label(window2, text="Email(@gmail.com)", fg="black", font="arial 12")
        lb5.place(relx = 0.4, rely = 0.3)
        ent3 = tk.Entry(window2, font="italic 13 bold", fg="black")
        ent3.place(relx=0.4, rely=0.34)

        #Hesap No
        lb6 = tk.Label(window2, text="Aşağıda bulunan hesap numarası ile giriş yapabilirsiniz \nNOT: Hesap Numarasını Lütfen Not Alın", fg="black", font="arial 12")
        lb6.place(relx = 0.4, rely = 0.5)
        
        
        #Duyuru
        lb9 = tk.Label(window2, text="", fg="green", font="arial 15")
        lb9.place(relx = 0.4, rely = 0.6)
        
        
        def kayit_islemi():
            global tpl 
            
            new_name = str(ent5.get())
            if(new_name.isalpha()):
                new_surname = str(ent6.get())
                if(new_surname.isalpha()):
                    new_email_no = str(ent3.get())
                    if(new_email_no[-10:]=="@gmail.com"):
                        yes_no = messagebox.askquestion(title="ONAY", message="Girdiğiniz Veriler Kaydedilsin mi?")
                        if(yes_no =="yes"):
                            # aynı eposta ile kayıtlı alıcı var ise kaydetme işlemini iptal etsin
                            db = sql.connect("databese.sqlite")
                            imlec = db.cursor()
                            imlec.execute("CREATE TABLE IF NOT EXISTS Users(name TEXT, surname TEXT, email_no TEXT, hesap_no TEXT)")
                            imlec.execute("SELECT email_no FROM Users")
                            tpl2 = tuple()
                            tpl2 = (new_email_no,)
                            listeler = imlec.fetchall()
                            for liste in listeler:
                                if(liste == tpl2):
                                    lb9["text"] = "Aynı Email Adına Başka Bir Hesap Vardır!! \nLütfen Başka Bir Email Giriniz."
                                    lb9["fg"] =  "red"
                                    break
                                
                            else:
                                hesap_no = random.randint(1000000000,9999999999)
                                lb9["text"] = str(hesap_no)
                                lb9["fg"] = "green"
                                new_hesap_no = str(hesap_no)
                                
                                # Databese
                                db = sql.connect("databese.sqlite")
                                imlec = db.cursor()
                                imlec.execute("CREATE TABLE IF NOT EXISTS Users(name TEXT, surname TEXT, email_no TEXT, hesap_no TEXT)")
                                tpl = tuple()
                                tpl = (new_name, new_surname, new_email_no,new_hesap_no)
                                imlec.execute("INSERT INTO Users VALUES(?,?,?,?)",tpl)
                                db.commit()                        
                                db.close()
                                    
                        
                        else:
                            messagebox.showwarning(title="Bilgi", message="Bilgiler Kaydedilmedi")
                
                    else:
                        messagebox.showwarning(title="HATA!", message="Hatalı Email Adresi!!")
                        
                else:
                    messagebox.showwarning(title="HATA!", message="Hatalı Soyad!")
            else:  
                messagebox.showwarning(title="HATA!", message="Hatalı Ad!")
            
            
            
            
        def tekrar_giris():
            window2.destroy() 
            ana_fonksiyon()
        
        
        b3 = tk.Button(window2, text=" Kaydol ", fg="white", bg="navy", command=kayit_islemi)
        b3.place(relx=0.50, rely=0.4)
        
        b4 = tk.Button(window2, text=" Giriş Yap ", fg="white", bg="navy", command=tekrar_giris)
        b4.place(relx=0.60, rely=0.4)

        
        window2.mainloop()
        
        

            
    b1 = tk.Button(window1, text="Giriş Yap", fg="white", bg="navy", command=giris)
    b1.place(relx=0.4, rely=0.4)

    b2 = tk.Button(window1, text=" Kaydol ", fg="white", bg="navy", command=kayit)
    b2.place(relx=0.50, rely=0.4)


    window1.mainloop() 

ana_fonksiyon()