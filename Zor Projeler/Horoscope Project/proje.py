"""
Bu proje burcunuzun ne olduğunu sizlere söylediği gibi genel anlamını da sizlere göstermektedir. 
Aynı zamanda burcunuzun diğer burçlar ile uyumu hakkında bilgi vermektedir.

"""

import tkinter as  tk
from tkinter.ttk import Combobox
from tkinter import messagebox 
import burc
import uyum


def ana_fonksiyon():
    window = tk.Tk()
    window.title("Burç Öğren")
    window.state("zoom")
    window.configure(bg="#051628")
    window.resizable(False, False)
    
    #LOGO
    img1 = tk.PhotoImage(file="Resimler\indir.png")
    lb1 = tk.Label(window, image=img1, bg="#051628")
    lb1.pack(pady=250)
    lb2 = tk.Label(window, text="HOŞ GELDİNİZ", fg="white", bg="#051628" ,font="italic 25 bold")
    lb2.place(relx = 0.425, rely = 0.06)
    

# Doğum Tarihi
    my_list = list()
    for i in range(1900,2024):
        my_list.append(i)
    my_list.reverse()
    lb3 = tk.Label(window, text="Doğum Yılı", fg="white", bg="#051628", font="arial 14")
    lb3.place(relx = 0.1, rely = 0.2)
    combo1 = Combobox(window, values=my_list, height=10, font="12", width=10)
    combo1.current(0)
    combo1.place(relx=0.1, rely=0.24)
    
    ay = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
    lb4 = tk.Label(window, text="Doğum Ayı", fg="white", bg="#051628", font="arial 14")
    lb4.place(relx = 0.1, rely = 0.3)
    combo2 = Combobox(window, values=ay, height=6, font="12", width=10)
    combo2.current(0)
    combo2.place(relx=0.1, rely=0.34)
    
    gun = ["1","2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    lb5 = tk.Label(window, text="Doğum Günü", fg="white", bg="#051628", font="arial 14")
    lb5.place(relx = 0.1, rely = 0.4)
    combo3 = Combobox(window, values=gun, height=6, font="12", width=10)
    combo3.current(0)
    combo3.place(relx=0.1, rely=0.44)
    
    lb6 = tk.Label(window, text="Burcun uyumunu öğrenmek için", fg="white", bg="#051628", font="arial 15")
    lb6.place(relx = 0.25, rely = 0.45)
    
    # Element
    lb9 = tk.Label(window, text="", fg="white", bg="#051628", font="arial 20")
    lb9.place(relx = 0.27, rely = 0.18)
    lb7 = tk.Label(window, text="", fg="white", bg="#051628", font="arial 25")
    lb7.place(relx = 0.28, rely = 0.25)
    
    # Açıklama
    lb8 = tk.Label(window, text="", fg="white", bg="#051628", font="arial 14")
    lb8.place(relx = 0.6, rely = 0.4)
    
    
    # Resim
    img2 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 112544.png")
    img3 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113045.png")
    img4 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113115.png")
    img5 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113132.png")
    img6 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113155.png")
    img7 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113215.png")
    img8 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113236.png")
    img9 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113303.png")
    img10 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113321.png")
    img11 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113347.png")
    img12 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113409.png")
    img13 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113429.png")
    img0 = tk.PhotoImage(file="Resimler\sıfır.png")
    
    def burc_info():
        year = str(combo1.get())
        if(year.isdigit()):
            if(int(combo1.get())>=1900 and int(combo1.get())<=2023 ):
                num = str(combo3.get())
                if(num.isdigit()):
                    
                    lb9["text"] = "Burcunun Elementi"
                    # Koç
                    if((combo2.get()=="Mart" and int(combo3.get())>=20 and int(combo3.get())<32) or (combo2.get()=="Nisan" and int(combo3.get())<=19)):
                        lb8["text"] = burc.koc
                        lb10 = tk.Label(window, image=img2, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)
                        lb2["text"] ="Koç Burcu"
                        lb2["fg"] = "red"
                        lb7["text"] = burc.koc_element
                        lb7["fg"] = "red"

                    # Boğa
                    elif((combo2.get()=="Nisan" and int(combo3.get())>=20 and int(combo3.get())<32) or (combo2.get()=="Mayıs" and int(combo3.get())<=20)):
                        lb8["text"] = burc.boga   
                        lb10 = tk.Label(window, image=img3, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)  
                        lb2["text"] ="Boğa Burcu"
                        lb2["fg"] = "orange" 
                        lb7["text"] = burc.boga_element
                        lb7["fg"] = "orange" 
                        
                    # İkizler
                    elif((combo2.get()=="Mayıs" and int(combo3.get())>=21 and int(combo3.get())<32) or (combo2.get()=="Haziran" and int(combo3.get())<=20)):
                        lb8["text"] = burc.ikizler
                        lb10 = tk.Label(window, image=img4, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)  
                        lb2["text"] ="İkizler Burcu"
                        lb2["fg"] = "#ffaa56" 
                        lb7["text"] = burc.ikizler_element
                        lb7["fg"] = "#ffaa56" 

                    # Yengeç
                    elif((combo2.get()=="Haziran" and int(combo3.get())>=21 and int(combo3.get())<32) or (combo2.get()=="Temmuz" and int(combo3.get())<=22)):
                        lb8["text"] = burc.yengec
                        lb10 = tk.Label(window, image=img5, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)   
                        lb2["text"] ="Yengeç Burcu"
                        lb2["fg"] = "#ffff7f" 
                        lb7["text"] = burc.yengec_element
                        lb7["fg"] = "#ffff7f"
                        
                    # Aslan
                    elif((combo2.get()=="Temmuz" and int(combo3.get())>=23 and int(combo3.get())<32) or (combo2.get()=="Ağustos" and int(combo3.get())<=22)):
                        lb8["text"] = burc.aslan
                        lb10 = tk.Label(window, image=img6, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1) 
                        lb2["text"] ="Aslan Burcu"
                        lb2["fg"] = "yellow"
                        lb7["text"] = burc.aslan_element
                        lb7["fg"] = "yellow"    
                    
                    # Başak
                    elif((combo2.get()=="Ağustos" and int(combo3.get())>=23 and int(combo3.get())<32) or (combo2.get()=="Eylül" and int(combo3.get())<=22)):
                        lb8["text"] = burc.basak
                        lb10 = tk.Label(window, image=img7, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1) 
                        lb2["text"] ="Başak Burcu"
                        lb2["fg"] = "green"  
                        lb7["text"] = burc.basak_element
                        lb7["fg"] = "green"
                        
                    # Terazi
                    elif((combo2.get()=="Eylül" and int(combo3.get())>=23 and int(combo3.get())<32) or (combo2.get()=="Ekim" and int(combo3.get())<=22)):
                        lb8["text"] = burc.terazi
                        lb10 = tk.Label(window, image=img8, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)  
                        lb2["text"] ="Terazi Burcu"
                        lb2["fg"] = "#00f5ff" 
                        lb7["text"] = burc.terazi_element
                        lb7["fg"] = "#00f5ff"   
                        
                    # Akrep
                    elif((combo2.get()=="Ekim" and int(combo3.get())>=24 and int(combo3.get())<32) or (combo2.get()=="Kasım" and int(combo3.get())<=23)):
                        lb8["text"] = burc.akrep
                        lb10 = tk.Label(window, image=img9, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)   
                        lb2["text"] ="Akrep Burcu"
                        lb2["fg"] = "#009acd"
                        lb7["text"] = burc.akrep_element
                        lb7["fg"] = "#009acd"  
                        
                    # Yay
                    elif((combo2.get()=="Kasım" and int(combo3.get())>=22 and int(combo3.get())<32) or (combo2.get()=="Aralık" and int(combo3.get())<=21)):
                        lb8["text"] = burc.yay
                        lb10 = tk.Label(window, image=img10, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1) 
                        lb2["text"] ="Yay Burcu"
                        lb2["fg"] = "#4876ff"   
                        lb7["text"] = burc.yay_element
                        lb7["fg"] = "#4876ff"
                    
                    # Oğlak
                    elif((combo2.get()=="Aralık" and int(combo3.get())>=22 and int(combo3.get())<32) or (combo2.get()=="Ocak" and int(combo3.get())<=19)):
                        lb8["text"] = burc.oglak
                        lb10 = tk.Label(window, image=img11, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)    
                        lb2["text"] ="Oğlak Burcu"
                        lb2["fg"] = "#7a67ee"   
                        lb7["text"] = burc.oglak_element
                        lb7["fg"] = "#7a67ee"
                    
                    # Kova
                    elif((combo2.get()=="Ocak" and int(combo3.get())>=21 and int(combo3.get())<32) or (combo2.get()=="Şubat" and int(combo3.get())<=18)):
                        lb8["text"] = burc.kova
                        lb10 = tk.Label(window, image=img12, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1)   
                        lb2["text"] ="Kova Burcu"
                        lb2["fg"] = "#ff56ff"
                        lb7["text"] = burc.kova_element
                        lb7["fg"] = "#ff56ff"    
                    
                    # Balık
                    elif((combo2.get()=="Şubat" and int(combo3.get())>=19 and int(combo3.get())<32) or (combo2.get()=="Mart" and int(combo3.get())<=20)):
                        lb8["text"] = burc.balik
                        lb10 = tk.Label(window, image=img13, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.1) 
                        lb2["text"] ="Balık Burcu"
                        lb2["fg"] = "magenta"
                        lb7["text"] = burc.balik_element
                        lb7["fg"] = "magenta"    
                        
                    else:
                        lb2["text"] ="HOŞ GELDİNİZ"
                        lb2["fg"] = "white"
                        lb8["text"] = ""
                        lb9["text"] = ""
                        lb10 = tk.Label(window, image=img0, bg="#051628")
                        lb10.place(relx = 0.7, rely = 0.05) 
                        lb7["text"] = ""
                        messagebox.showwarning(title="HATA!", message="Hatalı Ay Girişi!!")
                        
                else:
                    lb2["text"] ="HOŞ GELDİNİZ"
                    lb2["fg"] = "white"
                    lb8["text"] = ""
                    lb9["text"] = ""
                    lb10 = tk.Label(window, image=img0, bg="#051628")
                    lb10.place(relx = 0.7, rely = 0.05) 
                    lb7["text"] = ""
                    messagebox.showwarning(title="HATA!", message=" Hatalı Gün Girişi!!                                ")
            
            else:      
                lb2["text"] ="HOŞ GELDİNİZ"
                lb2["fg"] = "white"
                lb8["text"] = ""
                lb9["text"] = ""
                lb10 = tk.Label(window, image=img0, bg="#051628")
                lb10.place(relx = 0.7, rely = 0.05) 
                lb7["text"] = ""
                messagebox.showwarning(title="HATA!", message=" Hatalı Yıl Girişi!!                                ")
        
        
        else:
            lb2["text"] ="HOŞ GELDİNİZ"
            lb2["fg"] = "white"
            lb8["text"] = ""
            lb9["text"] = ""
            lb10 = tk.Label(window, image=img0, bg="#051628")
            lb10.place(relx = 0.7, rely = 0.05) 
            lb7["text"] = ""
            messagebox.showwarning(title="HATA!", message=" Hatalı Yıl Girişi!!                                      ")
        
            
    def burc_uyum():
        window.destroy()
        window1 = tk.Tk()
        window1.title("Burç Uyumu")
        window1.state("zoom")
        window1.configure(bg="#051628")
        window1.resizable(False, False)
        
        #LOGO
        img1 = tk.PhotoImage(file="Resimler\indir.png")
        lb12 = tk.Label(window1, image=img1, bg="#051628")
        lb12.pack(pady=250)
        
        # Başlık
        lb13 = tk.Label(window1, text="BURÇ UYUMU", fg="white", bg="#051628" ,font="italic 25 bold")
        lb13.place(relx = 0.425, rely = 0.06)
        
        lb15 = tk.Label(window1, text="Burcunu öğrenmek için", fg="white", bg="#051628", font="arial 16")
        lb15.place(relx = 0.1, rely = 0.555)
        
        # Açıklama
        lb14 = tk.Label(window1, text="", fg="white", bg="#051628", font="arial 14")
        lb14.place(relx = 0.6, rely = 0.4)
        
        # Burç Uyumu
        burclar = ["Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"]
        lb10 = tk.Label(window1, text="Burç", fg="white", bg="#051628", font="arial 14")
        lb10.place(relx = 0.2, rely = 0.2)
        combo4 = Combobox(window1, values=burclar, height=6, font="12", width=10)
        combo4.current(0)
        combo4.place(relx=0.2, rely=0.24)
        
        
        lb11 = tk.Label(window1, text="Burç", fg="white", bg="#051628", font="arial 14")
        lb11.place(relx = 0.2, rely = 0.3)
        combo5 = Combobox(window1, values=burclar, height=6, font="12", width=10)
        combo5.current(0)
        combo5.place(relx=0.2, rely=0.34)
        
        # Resim
        img2 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 112544.png")
        img3 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113045.png")
        img4 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113115.png")
        img5 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113132.png")
        img6 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113155.png")
        img7 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113215.png")
        img8 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113236.png")
        img9 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113303.png")
        img10 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113321.png")
        img11 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113347.png")
        img12 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113409.png")
        img13 = tk.PhotoImage(file="Resimler\Ekran görüntüsü 2023-03-18 113429.png")
        img0 = tk.PhotoImage(file="Resimler\sıfır.png")
        
        
        def uyum_info():
    
            if(combo4.get()=="Koç" and combo5.get()=="Koç"):
                lb14["text"] = uyum.koc_koc
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                
            elif((combo4.get()=="Koç" and combo5.get()=="Boğa") or (combo4.get()=="Boğa" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img3, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="İkizler") or (combo4.get()=="İkizler" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_ikizler
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img4, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Yengeç") or (combo4.get()=="Yengeç" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img5, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Aslan") or (combo4.get()=="Aslan" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_aslan
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img6, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Başak") or (combo4.get()=="Başak" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img7, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Koç")):
                lb14["text"] = uyum.oglak_koc
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Koç")):
                lb14["text"] = uyum.koc_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Koç" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Koç")):
                lb14["text"] = uyum.balik_koc
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img2, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif(combo4.get()=="Boğa" and combo5.get()=="Boğa"):
                lb14["text"] = uyum.boga_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Boğa" and combo5.get()=="İkizler") or (combo4.get()=="İkizler" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.ikizler_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img4, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)  

            elif((combo4.get()=="Boğa" and combo5.get()=="Yengeç") or (combo4.get()=="Yengeç" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.boga_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img5, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Aslan") or (combo4.get()=="Aslan" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.aslan_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img6, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Başak") or (combo4.get()=="Başak" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.basak_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img7, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.terazi_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.akrep_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.yay_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.oglak_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.kova_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Boğa" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Boğa")):
                lb14["text"] = uyum.balik_boga
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img3, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="İkizler" and combo5.get()=="İkizler"):
                lb14["text"] = uyum.ikizler_ikizler
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="İkizler" and combo5.get()=="Yengeç") or (combo4.get()=="Yengeç" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img5, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Aslan") or (combo4.get()=="Aslan" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_aslan
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img6, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Başak") or (combo4.get()=="Başak" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img7, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 
                
            elif((combo4.get()=="İkizler" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.oglak_ikizler
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.ikizler_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="İkizler" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="İkizler")):
                lb14["text"] = uyum.balik_ikizler
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img4, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="Yengeç" and combo5.get()=="Yengeç"):
                lb14["text"] = uyum.yengec_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Yengeç" and combo5.get()=="Aslan") or (combo4.get()=="Aslan" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.aslan_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img6, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Başak") or (combo4.get()=="Başak" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.basak_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img7, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.terazi_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.akrep_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.yay_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.oglak_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.kova_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Yengeç" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Yengeç")):
                lb14["text"] = uyum.balik_yengec
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img5, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="Aslan" and combo5.get()=="Aslan"):
                lb14["text"] = uyum.aslan_aslan
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
            

            elif((combo4.get()=="Aslan" and combo5.get()=="Başak") or (combo4.get()=="Başak" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.aslan_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img7, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.aslan_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.aslan_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.aslan_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.oglak_aslan
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.aslan_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Aslan" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Aslan")):
                lb14["text"] = uyum.balik_aslan
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img6, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="Başak" and combo5.get()=="Başak"):
                lb14["text"] = uyum.basak_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Başak" and combo5.get()=="Terazi") or (combo4.get()=="Terazi" and combo5.get()=="Başak")):
                lb14["text"] = uyum.terazi_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img8, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Başak" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Başak")):
                lb14["text"] = uyum.basak_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Başak" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Başak")):
                lb14["text"] = uyum.yay_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Başak" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Başak")):
                lb14["text"] = uyum.oglak_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Başak" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Başak")):
                lb14["text"] = uyum.kova_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Başak" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Başak")):
                lb14["text"] = uyum.balik_basak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img7, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="Terazi" and combo5.get()=="Terazi"):
                lb14["text"] = uyum.terazi_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Terazi" and combo5.get()=="Akrep") or (combo4.get()=="Akrep" and combo5.get()=="Terazi")):
                lb14["text"] = uyum.terazi_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img9, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Terazi" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Terazi")):
                lb14["text"] = uyum.terazi_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Terazi" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Terazi")):
                lb14["text"] = uyum.oglak_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Terazi" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Terazi")):
                lb14["text"] = uyum.kova_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Terazi" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Terazi")):
                lb14["text"] = uyum.balik_terazi
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img8, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif(combo4.get()=="Akrep" and combo5.get()=="Akrep"):
                lb14["text"] = uyum.akrep_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img9, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Akrep" and combo5.get()=="Yay") or (combo4.get()=="Yay" and combo5.get()=="Akrep")):
                lb14["text"] = uyum.yay_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img9, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img10, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Akrep" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Akrep")):
                lb14["text"] = uyum.oglak_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img9, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1) 

            elif((combo4.get()=="Akrep" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Akrep")):
                lb14["text"] = uyum.kova_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img9, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif((combo4.get()=="Akrep" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Akrep")):
                lb14["text"] = uyum.balik_akrep
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img9, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif(combo4.get()=="Yay" and combo5.get()=="Yay"):
                lb14["text"] = uyum.yay_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img10, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Yay" and combo5.get()=="Oğlak") or (combo4.get()=="Oğlak" and combo5.get()=="Yay")):
                lb14["text"] = uyum.oglak_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img10, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img11, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif((combo4.get()=="Yay" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Yay")):
                lb14["text"] = uyum.kova_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img10, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif((combo4.get()=="Yay" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Yay")):
                lb14["text"] = uyum.balik_yay
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img10, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif(combo4.get()=="Oğlak" and combo5.get()=="Oğlak"):
                lb14["text"] = uyum.oglak_oglak
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img11, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Oğlak" and combo5.get()=="Kova") or (combo4.get()=="Kova" and combo5.get()=="Oğlak")):
                lb14["text"] = uyum.oglak_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img11, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img12, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif((combo4.get()=="Oğlak" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Oğlak")):
                lb14["text"] = uyum.oglak_balik
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img11, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif(combo4.get()=="Kova" and combo5.get()=="Kova"):
                lb14["text"] = uyum.kova_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img12, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                

            elif((combo4.get()=="Kova" and combo5.get()=="Balık") or (combo4.get()=="Balık" and combo5.get()=="Kova")):
                lb14["text"] = uyum.balik_kova
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.05)
                lb16 = tk.Label(window1, image=img12, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.1)
                lb17 = tk.Label(window1, image=img13, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.1)

            elif(combo4.get()=="Balık" and combo5.get()=="Balık"):
                lb14["text"] = uyum.balik_balik
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb16 = tk.Label(window1, image=img13, bg="#051628")
                lb16.place(relx = 0.7, rely = 0.1)
                
            else:
                lb16 = tk.Label(window1, image=img0, bg="#051628")
                lb16.place(relx = 0.6, rely = 0.05)
                lb17 = tk.Label(window1, image=img0, bg="#051628")
                lb17.place(relx = 0.8, rely = 0.05) 
                lb14["text"] = ""
                lb13["text"] = "BURÇ UYUMU"
                messagebox.showwarning(title="HATA!", message="   Hatalı Burç Girişi!!                                     ")
                
            
        def tekrar_giris():
            window1.destroy() 
            ana_fonksiyon()
        
        b3 = tk.Button(window1, text="Uyumu Öğren", fg="white", bg="orange", font="13", command=uyum_info)
        b3.place(relx=0.29, rely=0.4)
        
        b4 = tk.Button(window1, text="Tıklayınız", fg="white", bg="orange", font="13", command=tekrar_giris)
        b4.place(relx=0.245, rely=0.55)
    
        window1.mainloop()
    
    
    b1 = tk.Button(window, text="Burcunu Öğren", fg="white", bg="orange", font="13", command=burc_info)
    b1.place(relx=0.1, rely=0.5)

    b2 = tk.Button(window, text="Tıklayınız", fg="white", bg="orange", font="13", command=burc_uyum)
    b2.place(relx=0.3, rely=0.5)
    
    window.mainloop()
    
      
ana_fonksiyon()   
    
    