"""
Proje gizli tutmak istediğiniz dosyaları kilitleyerek başka kişilerin bilgilere ulaşmasını önlemek amacı ile yazılmış bir projedir. 
Proje sadece örnek bir çalışmadır. Dosyalarınıza zarar gelmemesi için öncelikle boş bir dosya ile deneme yaptıktan sonra kullanınız.
Projenin doğru şekilde çalışması için dosya yolu doğru ayarlanmalıdır.
"""
import tkinter as tk
import pyAesCrypt
import os


def main_function():
    global url, password
    window = tk.Tk()
    window.geometry("1000x700+500+50")
    window.title("Kilit")
    window.resizable(False, False)

    
 
    # Duyuru
    lb1 = tk.Label(window, text="Kilitlendi", font="arial 20", fg="gray", bg="navy")
    lb1.place(x=400, y=220, width=245, height=50)

    lb2 = tk.Label(window, text="Açıldı", font="arial 20", fg="gray", bg="navy")
    lb2.place(x=655, y=220, width=245, height=50)

    # Dosya uzantısı
    lb3 = tk.Label(window, text="Dosya Uzantısı", font="arial 20", fg="white", bg="navy")
    lb3.place(x=100, y=160, width=250, height=50)

    ent1 = tk.Entry(window, font="arial 16", fg="white", bg="navy")
    ent1.place(x=400, y=160, width=500, height=50)
    
    # Şifre
    lb0xy = tk.Label(window, text="Şifre", font="arial 20", fg="white", bg="navy")
    lb0xy.place(x=100, y=100, width=250, height=50)

    ent2 = tk.Entry(window, font="arial 16", fg="white", bg="navy")
    ent2.place(x=400, y=100, width=250, height=50)

    url = str() 
    def key_locked(): 
        global url, password
        url = str(ent1.get())
        password = str(ent2.get())
        with open(url, "r") as file:
            read_list = file.readlines()
            password1 = read_list[-1]
            
        if(password==password1):
            buffer_size = 512*1024
            try:
                pyAesCrypt.encryptFile(str(url), str(url[:-4]) + ".aes", password, buffer_size)
                url = url[:-4] + ".aes"
                os.remove("gizli_bilgi.txt")
                lb1["fg"] = "red"
                lb1["text"] = "Kilitlendi"
                lb2["fg"] = "gray"
            except:
                lb1["text"] = "Hatalı Kod!"
                lb1["fg"] = "orange"
        
        else:
            lb1["text"] = "Hatalı Şifre!"
            lb1["fg"] = "orange"
            
    def key_open():
        global url, password
        if(len(url)>0):
            buffer_size = 512*1024
            try:
                pyAesCrypt.decryptFile(str(url), str(url[:-4]) + ".txt", password, buffer_size)
                url = url[:-4] + ".txt"
                os.remove("gizli_bilgi.aes")
                lb2["fg"] = "green"
                lb2["text"] = "Açıldı"
                lb1["fg"] = "gray"
            except:
                lb2["text"] = "Hatalı Kod!"
                lb2["fg"] = "orange"
        else:
            url = str(ent1.get())
            buffer_size = 512*1024
            try:
                pyAesCrypt.decryptFile(str(url), str(url[:-4]) + ".txt", password, buffer_size)
                url = url[:-4] + ".txt"
                os.remove("gizli_bilgi.aes")
                lb2["fg"] = "green"
                lb1["fg"] = "gray"
            except:
                lb2["text"] = "Hatalı Kod!"
                lb2["fg"] = "orange"
                
    def out():
        window.destroy()
            
    # Kilitle
    bt1 = tk.Button(window, text="Dosyayı Kilitle", font="arial 20", fg="white", bg="navy", command=key_locked)
    bt1.place(x=100, y=320, width=300, height=50)
    # Aç
    bt2 = tk.Button(window, text="Dosyayı Kilidini Aç", font="arial 20", fg="white", bg="navy", command=key_open)
    bt2.place(x=600, y=320, width=300, height=50)
    # Çıkış
    bt3 = tk.Button(window, text="Çıkış", font="arial 20", fg="white", bg="navy", command=out)
    bt3.place(x=350, y=420, width=300, height=50)


    window.mainloop()


window1 = tk.Tk()
window1.geometry("600x400+500+50")
window1.title("Kilit Şifre Belirleme")
window1.resizable(False, False)


# Şifre
lb0 = tk.Label(window1, text="Şifre", font="arial 20", fg="white", bg="navy")
lb0.place(x=50, y=50, width=200, height=50)

lb0x = tk.Label(window1, text="Doğrula", font="arial 20", fg="white", bg="navy")
lb0x.place(x=50, y=110, width=200, height=50)

ent3 = tk.Entry(window1, font="arial 16", fg="white", bg="navy")
ent3.place(x=270, y=50, width=280, height=50)

ent4 = tk.Entry(window1, font="arial 16", fg="white", bg="navy")
ent4.place(x=270, y=110, width=280, height=50)

lb0y = tk.Label(window1, text="", font="arial 20", fg="white")
lb0y.place(x=50, y=190, width=500, height=50)

def passwords():
    global url
    password1 = ent3.get()
    password2 = ent4.get()
    if(password1 == password2):
        with open("gizli_bilgi.txt", "a+") as file:
            file.write("\n\nKeys:\n" + password1)
        window1.destroy()
        main_function()
        
    else:
        lb0y["text"] = "Hatalı Şifre"
        lb0y["bg"]="red"
        
bt4 = tk.Button(window1, text="Kaydet", font="arial 20", fg="white", bg="navy", command=passwords)
bt4.place(x=200, y=270, width=200, height=50)

window1.mainloop()