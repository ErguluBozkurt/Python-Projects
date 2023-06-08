"""
Bu proje her hangi bir siteye girerken ki giriş bilgilerinden esinlenmiştir. Girilen kullanıcı adı ve şifrenin doğrululuğunu 
kontrol etmektedir.
"""

import tkinter as tk

window = tk.Tk()
window.geometry("1000x600+450+150")
window.title("Login Ekranı")
window.resizable(False, False)

l1 = tk.Label(window, text="Şirket Ekranı", fg="purple", font="arial 24 italic underline bold")
l1.pack(pady=100)

#username
l2 = tk.Label(window,text="Kullanıcı Adı", fg="purple", font="arial 18")
l2.place(x=300, y=200)
e1 = tk.Entry(window, font="arial 18 italic")
e1.place(x=450, y=200)

#password
l3 = tk.Label(window,text="Şifre", fg="purple", font="arial 18")
l3.place(x=300, y=260)
e2 = tk.Entry(window, font="arial 18 italic", show="*") #yazının yıldızlı olmasını sağlıyor
e2.place(x=450, y=260)

#Label
l4 = tk.Label(window,text="", fg="purple", font="arial 18")
l4.place(x=300, y=450)

#button
def login():
    username = e1.get()
    password = e2.get()
    if(username=="admin" and password=="102030"):
        l4["text"] = "Kullanıcı Adı ve Şifre Doğru"
        l4["fg"] = "green"
    else:
        l4["text"] =  "Kullanıcı Adı ve Şifre Yanlış"
        l4["fg"] = "red"

b1 = tk.Button(window, text="Giriş", bg="purple", fg="white", font="arial 18", command=login)#command ile fonksiyona yollamamız lazım
b1.place(x=590, y=320, width=120)


window.mainloop()
