"""
Bu projede kim milyoner olmak ister yarışması üzerinden kurgulanılarak yapılmıştır. 10 adet soru sorulmakta. Tüm sorular
doğru bilindiğinde büyük ödülü kazanmış olursunuz. 2. ve 7. sorular baraj sorularını temsil etmektedir.  
"""
import tkinter as tk
import random
from tkinter import messagebox



def program():
    global num, score
    
    questions = [["1. Hangisi Türkiye'nin başkenti olan bir şehirdir?", "1. Hangisi Türkiye'deki en uzun nehirdir?", "1. Hangisi Türkiye'nin en kalabalık şehridir?"],
                ["2. Hangi gezegen Güneş Sistemi'ndeki en büyük gezegendir?", "2. Hangi gezegen Güneş Sistemi'ndeki en hızlı dönme hareketine sahiptir?", "2. Hangi gezegen Güneş Sistemi'ndeki en küçük gezegendir?"],
                ["3. Hangisi dünyadaki en yüksek dağlardan biridir?", "3. Hangisi insan vücudunda bulunan en büyük iç organı temsil eder?", "3. Hangisi dünyadaki en uzun nehirden biridir?"],
                ["4. Hangisi bir Nobel ödülü kategorisidir?", "4. Hangisi 'Harry Potter' kitap serisindeki yazarın adıdır?", "4. Hangisi bir Amerikan başkanının adıdır?"],
                ["5. Hangisi renkli bir gemidir?", "5. Hangisi bir müzik türüdür?", "5. Hangisi ünlü bir ressamdır?"],
                ["6. Hangisi Türkiye'nin en büyük gölüdür?", "6. Hangisi İngiltere'nin başkenti olan bir şehirdir?", "6. Hangisi Türkiye'nin en yüksek dağıdır?"],
                ["7. Hangisi bir müzik notasıdır?", "7. Hangi renk, trafik ışıklarında durmaya işaret eder?", "7. Hangisi bir meyve değildir?"],
                ["8. Hangisi bir futbol kulübüdür?", "8. Hangisi bir dans türüdür?", "8. Hangi yıl İkinci Dünya Savaşı sona ermiştir?"],
                ["9. Hangisi bir açlık oyunları karakteridir?", "9. Hangisi bir Hayao Miyazaki filmidir?", "9. Hangisi ünlü bir film yönetmenidir?"],
                ["10. Hangisi İtalya'nın bir şehridir?", "10. Hangisi Mısır'ın başkenti olan bir şehirdir?", "10. Hangisi İspanya'nın başkenti olan bir şehirdir?"]]

    answers_true = [["Ankara", "Fırat Nehri", "İstanbul"],
                    ["Jüpiter", "Venüs", "Merkür"],
                    ["Everest", "Karaciğer", "Nil Nehri"],
                    ["Nobel Barış Ödülü", "J.K. Rowling", "Barack Obama"],
                    ["Beyaz gemi", "Hip-hop", "Pablo Picasso"],
                    ["Van Gölü", "Londra", "Ağrı Dağı"],
                    ["Do", "Kırmızı", "Patates"],
                    ["Real Madrid", "Salsa", "1945"],
                    ["Katniss Everdeen", "Prenses Mononoke", "Martin Scorsese"],
                    ["Roma", "Kahire", "Madrid"]]

    answers_false = [[["İstanbul","İzmir", "Bursa"], ["Sakarya Nehri", "Kızılırmak", "Çoruh Nehri"], ["Ankara", "İzmir", "Bursa"]],
                    [["Mars","Venüs","Neptün"], ["Merkür","Mars","Jüpiter"], ["Mars", "Venüs", "Neptün"]],
                    [["Mont Blanc", "Kilimanjaro", "K2"], ["Beyin", "Kalp", "Akciğer"], ["Amazon Nehri", "Yangtze Nehri", "Kongo Nehri"]],
                    [["Altın Ayı Ödülü", "Oscar Ödülü", "Grammy Ödülü"], ["Stephenie Meyer", "Suzanne Collins", "George R.R. Martin"], ["Angela Merkel", "Emmanuel Macron", "Vladimir Putin"]],
                    [["Mavi gemi", "Yeşil gemi", "Kırmızı gemi"], ["Futbol", "Basketbol", "Voleybol"], ["Albert Einstein", "William Shakespeare", "Marie Curie"]],
                    [["Tuz Gölü", "İznik Gölü", "Eğirdir Gölü"], ["Paris", "Berlin", "Roma"], ["Erciyes Dağı", "Uludağ", "Süphan Dağı"]],
                    [["Sesi", "Sol", "Fa"], ["Yeşil", "Mavi", "Turuncu"], ["Elma", "Portakal", "Mandalina"]],
                    [["Los Angeles Lakers", "New York Yankees", "Boston Bruins"], ["Buz hokeyi", "Eskrim", "Bateri"], ["1943", "1947", "1950"]],
                    [["Hermione Granger", "Bella Swan", "Arya Stark"], ["Aslan Kral", "Hükümet Kadın", "La La Land"], ["Justin Bieber", "Serena Williams", "Elon Musk"]],
                    [["Barselona", "Atina", "Londra"], ["İstanbul", "Nairobi", "Madrid"], ["Barselona", "Lizbon", "Roma"]]]

    # Kazanılan miktar değişkeni
    score = 0
    num = 0
    
    
    window = tk.Tk()
    window.title("Kim Milyoner Olmak İster")
    window.geometry("900x700+600+60")
    window.resizable(False, False)
    window.configure(bg="#02549c")

    img = tk.PhotoImage(file="kim_milyoner.png")
    lb = tk.Label(window, image=img, bg="#02549c")
    lb.place(x=330,y=20)

    lb4 = tk.Label(window, text=name, font="arial 20", fg="white", bg="navy")
    lb4.place(x=30,y=20, width=250)

    
    def main_function():
        
        # Soru ve cevap seçimi
        def question_random():
            global example, num, false1, false2, false3, answer
            num = num + 1
            if(num==1):
                example = random.choice(questions[0])
                indexx = questions[0].index(example)
                answer = answers_true[0][indexx]
                false1 = answers_false[0][indexx][0]
                false2 = answers_false[0][indexx][1]
                false3 = answers_false[0][indexx][2]
            elif(num==2):
                example = random.choice(questions[1])
                indexx = questions[1].index(example)
                answer = answers_true[1][indexx]
                false1 = answers_false[1][indexx][0]
                false2 = answers_false[1][indexx][1]
                false3 = answers_false[1][indexx][2]
            elif(num==3):
                example = random.choice(questions[2])
                indexx = questions[2].index(example)
                answer = answers_true[2][indexx]
                false1 = answers_false[2][indexx][0]
                false2 = answers_false[2][indexx][1]
                false3 = answers_false[2][indexx][2]
            elif(num==4):
                example = random.choice(questions[3])
                indexx = questions[3].index(example)
                answer = answers_true[3][indexx]
                false1 = answers_false[3][indexx][0]
                false2 = answers_false[3][indexx][1]
                false3 = answers_false[3][indexx][2]
            elif(num==5):
                example = random.choice(questions[4])
                indexx = questions[4].index(example)
                answer = answers_true[4][indexx]
                false1 = answers_false[4][indexx][0]
                false2 = answers_false[4][indexx][1]
                false3 = answers_false[4][indexx][2]
            elif(num==6):
                example = random.choice(questions[5])
                indexx = questions[5].index(example)
                answer = answers_true[5][indexx]
                false1 = answers_false[5][indexx][0]
                false2 = answers_false[5][indexx][1]
                false3 = answers_false[5][indexx][2]
            elif(num==7):
                example = random.choice(questions[6])
                indexx = questions[6].index(example)
                answer = answers_true[6][indexx]
                false1 = answers_false[6][indexx][0]
                false2 = answers_false[6][indexx][1]
                false3 = answers_false[6][indexx][2]
            elif(num==8):
                example = random.choice(questions[7])
                indexx = questions[7].index(example)
                answer = answers_true[7][indexx]
                false1 = answers_false[7][indexx][0]
                false2 = answers_false[7][indexx][1]
                false3 = answers_false[7][indexx][2]
            elif(num==9):
                example = random.choice(questions[8])
                indexx = questions[8].index(example)
                answer = answers_true[8][indexx]
                false1 = answers_false[8][indexx][0]
                false2 = answers_false[8][indexx][1]
                false3 = answers_false[8][indexx][2]
            elif(num==10):
                example = random.choice(questions[9])
                indexx = questions[9].index(example)
                answer = answers_true[9][indexx]
                false1 = answers_false[9][indexx][0]
                false2 = answers_false[9][indexx][1]
                false3 = answers_false[9][indexx][2]
            else:
                print("Soru seçmede Hata")
        
        # Cevap tepkileri
        def true():
            global score
            btA["text"] = "Doğru"
            btA["bg"] = "green"
            if(num==1):
                score = 1000
            elif(num==2):
                score = 5000
                yes_no = messagebox.askquestion(title="ONAY", message="Çekilmek İster Misiniz?             ")
                if(yes_no =="yes"):
                    messagebox.showwarning(title="BİLDİRİ", message="5.000TL Çekinizi Alabilirsiniz              ")
                    window.destroy()
                    yes_no = messagebox.askquestion(title="ONAY", message="Tekrar Oynamak İster Misiniz?             ")
                    if(yes_no =="yes"):
                        info_contestent()
            elif(num==3):
                score = 15000
            elif(num==4):
                score = 30000
            elif(num==5):
                score = 60000
            elif(num==6):
                score = 120000
            elif(num==7):
                score = 200000
                yes_no = messagebox.askquestion(title="ONAY", message="Çekilmek İster Misiniz?             ")
                if(yes_no =="yes"):
                    messagebox.showwarning(title="BİLDİRİ", message="200.000TL Çekinizi Alabilirsiniz              ")
                    window.destroy()
                    yes_no = messagebox.askquestion(title="ONAY", message="Tekrar Oynamak İster Misiniz?             ")
                    if(yes_no =="yes"):
                        info_contestent()
            elif(num==8):
                score = 300000
            elif(num==9):
                score = 500000
            elif(num==10):
                messagebox.showwarning(title="BİLDİRİ", message="Büyük Ödül 1.000.000TL Kazandınız Tebrik Ederim:))             ")
                
        def falseB():
            btB["text"] = "Yanlış"
            btB["bg"] = "red"
            if(num<3):
                messagebox.showwarning(title="BİLDİRİ", message="Kaybettiniz!! Şansınızı Bir Daha Deneyin     ")
                window.destroy()
                yes_no = messagebox.askquestion(title="ONAY", message="Tekrar Oynamak İster Misiniz?             ")
                if(yes_no =="yes"):
                    info_contestent()
            if(num==3):
                messagebox.showwarning(title="BİLDİRİ", message="5.000TL Çekinizi Alabilirsiniz              ")
            elif(num==8):
                messagebox.showwarning(title="BİLDİRİ", message="200.000TL Çekinizi Alabilirsiniz            ")
            
        def falseC():
            btC["text"] = "Yanlış"
            btC["bg"] = "red"
            if(num<3):
                messagebox.showwarning(title="BİLDİRİ", message="Kaybettiniz!! Şansınızı Bidaha Deneyin     ")
                window.destroy()
                yes_no = messagebox.askquestion(title="ONAY", message="Tekrar Oynamak İster Misiniz?             ")
                if(yes_no =="yes"):
                    info_contestent()
            if(num==3):
                messagebox.showwarning(title="BİLDİRİ", message="5.000TL Çekinizi Alabilirsiniz              ")
            elif(num==8):
                messagebox.showwarning(title="BİLDİRİ", message="200.000TL Çekinizi Alabilirsiniz            ")
        def falseD():
            btD["text"] = "Yanlış"
            btD["bg"] = "red"
            if(num<3):
                messagebox.showwarning(title="BİLDİRİ", message="Kaybettiniz!! Şansınızı Bidaha Deneyin     ")
                window.destroy()
                yes_no = messagebox.askquestion(title="ONAY", message="Tekrar Oynamak İster Misiniz?             ")
                if(yes_no =="yes"):
                    info_contestent()
            if(num==3):
                messagebox.showwarning(title="BİLDİRİ", message="5.000TL Çekinizi Alabilirsiniz              ")
            elif(num==8):
                messagebox.showwarning(title="BİLDİRİ", message="200.000TL Çekinizi Alabilirsiniz            ")
                
                
        question_random()
        
        
        # Soru   
        lb1 = tk.Label(window, text=example, font="arial 16", fg="white", bg="navy")
        lb1.place(x=50,y=330, width=800)
        
        # Şıkların yer değiştirmesi
        choices = [[50,400], [500,400], [50,450], [500,450]]
        s1 = random.choice(choices)
        s2 = random.choice(choices)
        while(s1==s2):
            s2 = random.choice(choices)
        s3 = random.choice(choices)
        while(s3==s2 or s3==s1):
            s3 = random.choice(choices)
        s4 = random.choice(choices)
        while(s4== s3 or s4==s2 or s4==s1):
            s4 = random.choice(choices)
        
                        
        # Şıklar
        btA = tk.Button(window, text=f"{answer}", font="arial 16", fg="white", bg="navy", command=true)
        btA.place(x=s1[0],y=s1[1], width=350)
        btB = tk.Button(window, text=f"{false1}", font="arial 16", fg="white", bg="navy", command=falseB)
        btB.place(x=s2[0],y=s2[1], width=350)
        btC = tk.Button(window, text=f"{false2}", font="arial 16", fg="white", bg="navy", command=falseC)
        btC.place(x=s3[0],y=s3[1], width=350)
        btD = tk.Button(window, text=f"{false3}", font="arial 16", fg="white", bg="navy", command=falseD)
        btD.place(x=s4[0],y=s4[1], width=350)

        lb2 = tk.Label(window, text=f"Kazanılan \n{score}", font="arial 16", fg="white", bg="navy")
        lb2.place(x=700, y=50)


    # Yeni soru geçişi
    bt1 = tk.Button(window, text="Yeni Soru >", font="arial 16", fg="white", bg="navy", command=main_function)
    bt1.place(x=720,y=280)
    window.mainloop()
    
    

def info_contestent():
    window1 = tk.Tk()
    window1.title("Kim Milyoner Olmak İster")
    window1.geometry("600x500+600+60")
    window1.resizable(False, False)
    window1.configure(bg="#02549c")

    
    lb0 = tk.Label(window1, text="Ad-Soyad", font="arial 12", fg="white", bg="#02549c")
    lb0.place(x=30,y=20)
    ent0 = tk.Entry(window1, font="arial 14 bold", fg="black", bg="white")
    ent0.place(x=30,y=45)
    
    lb1 = tk.Label(window1, text="Yaş", font="arial 12", fg="white", bg="#02549c")
    lb1.place(x=30,y=95)
    ent1 = tk.Entry(window1, font="arial 14 bold", fg="black", bg="white")
    ent1.place(x=30,y=120)
    
    lb2 = tk.Label(window1, text="Doğum Yeri", font="arial 12", fg="white", bg="#02549c")
    lb2.place(x=30,y=170)
    ent2 = tk.Entry(window1, font="arial 14 bold", fg="black", bg="white")
    ent2.place(x=30,y=195)
    
    lb3 = tk.Label(window1, text="Meslek", font="arial 12", fg="white", bg="#02549c")
    lb3.place(x=30,y=245)
    ent3 = tk.Entry(window1, font="arial 14 bold", fg="black", bg="white")
    ent3.place(x=30,y=280)
    
    
    def dest():
        global name
        name = str(ent0.get())
        window1.destroy()
        program()

    save = tk.Button(window1, text="Onayla", font="arial 14 bold", fg="white", bg="navy", command=dest)
    save.place(x=100, y=320)
    window1.mainloop()

info_contestent()
   