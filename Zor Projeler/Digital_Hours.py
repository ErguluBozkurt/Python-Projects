
"""
Aşağıdaki proje farklı ülkelere ait saat ve tarihleri açılan pencere vasıtasıyla sizlere göstermektedir. 
"""

import tkinter as tk
import pytz
import datetime

window = tk.Tk()
window.title("Dijital Saat")
window.geometry("800x600+600+100")
window.resizable(False, False)
window.configure(bg="black")

saat_formatiT = "%H:%M:%S"
saat_formati = "%H:%M:%S\n%Y-%m-%d"
zaman_dilimleri = {
      "Türkiye": "Europe/Istanbul",
      "ABD": "America/New_York",
      "İngiltere": "Europe/London",
      "Japonya": "Asia/Tokyo",
      "Azerbaycan": "Asia/Baku",
      "Mısır": "Africa/Cairo",
      "Çin": "Asia/Shanghai",
      "Rusya": "Europe/Moscow",
      "Almanya": "Europe/Berlin"
      # İstediğiniz diğer ülkeleri buraya ekleyebilirsiniz
  }


lb1 = tk.Label(window, text="Türkiye", font="arial 20 bold", fg="white", bg="#363636")
lb1.place(x=330, y=5, width=150)
lb1x = tk.Label(window, text="", font="Arial 25 bold", foreground= "white", background="#363636")
lb1x.place(x=330, y=40, width=150)

lb2 = tk.Label(window, text="Azerbaycan", font="arial 15 bold", fg="white", bg="#363636")
lb2.place(x=100, y=150, width=150)
lb2x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb2x.place(x=100, y=180, width=150)

lb3 = tk.Label(window, text="Amerika", font="arial 15 bold", fg="white", bg="#363636")
lb3.place(x=100, y=250, width=150)
lb3x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb3x.place(x=100, y=280, width=150)

lb4 = tk.Label(window, text="Çin", font="arial 15 bold", fg="white", bg="#363636")
lb4.place(x=100, y=350, width=150)
lb4x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb4x.place(x=100, y=380, width=150)

lb5 = tk.Label(window, text="İngiltere", font="arial 15 bold", fg="white", bg="#363636")
lb5.place(x=100, y=450, width=150)
lb5x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb5x.place(x=100, y=480, width=150)

lb6 = tk.Label(window, text="Japonya", font="arial 15 bold", fg="white", bg="#363636")
lb6.place(x=550, y=150, width=150)
lb6x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb6x.place(x=550, y=180, width=150)

lb7 = tk.Label(window, text="Mısır", font="arial 15 bold", fg="white", bg="#363636")
lb7.place(x=550, y=250, width=150)
lb7x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb7x.place(x=550, y=280, width=150)

lb8 = tk.Label(window, text="Rusya", font="arial 15 bold", fg="white", bg="#363636")
lb8.place(x=550, y=350, width=150)
lb8x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb8x.place(x=550, y=380, width=150)

lb9 = tk.Label(window, text="Almanya", font="arial 15 bold", fg="white", bg="#363636")
lb9.place(x=550, y=450, width=150)
lb9x = tk.Label(window, text="", font="Arial 15 bold", foreground= "white", background="#363636")
lb9x.place(x=550, y=480, width=150)


def turkey():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Türkiye"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formatiT)
  lb1x["text"] = anlik_zaman
  lb1x.after(1000,turkey)
turkey()

def azerbaijan():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Azerbaycan"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb2x["text"] = anlik_zaman
  lb2x.after(1000,azerbaijan)
azerbaijan()

def abd():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["ABD"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb3x["text"] = anlik_zaman
  lb3x.after(1000,abd)
abd()

def china():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Çin"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb4x["text"] = anlik_zaman
  lb4x.after(1000,china)
china()

def england():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["İngiltere"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb5x["text"] = anlik_zaman
  lb5x.after(1000,england)
england()

def japan():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Japonya"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb6x["text"] = anlik_zaman
  lb6x.after(1000,japan)
japan()

def egypt():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Mısır"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb7x["text"] = anlik_zaman
  lb7x.after(1000,egypt)
egypt()

def russia():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Rusya"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb8x["text"] = anlik_zaman
  lb8x.after(1000,russia)
russia()

def germany():
  zaman_dilimi = pytz.timezone(zaman_dilimleri["Almanya"])
  anlik_zaman = datetime.datetime.now(zaman_dilimi).strftime(saat_formati)
  lb9x["text"] = anlik_zaman
  lb9x.after(1000,germany)
germany()
window.mainloop()