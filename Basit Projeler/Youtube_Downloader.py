"""
Aşağıda yer alan uygulama youtube dan video indirmek için yapılmıştır. Arayüze sahiptir.
"""

from pytube import YouTube
import tkinter as tk


window = tk.Tk()
window.title("Image Conversion App")
window.geometry("500x500+600+100")
window.resizable(False,False)

lb = tk.Label(window, text="URL Gir", font="arial 12")
lb.place(x=120, y=100)

ent = tk.Entry(window, font="italic 12", width=25)
ent.place(x=120, y=125)

def downloadd():
    lb1 = tk.Label(window, text="Downloading...", font="arial 14", fg="orange")
    lb1.place(x=150, y=200)
    try:
        lb2 = tk.Label(window, text="Download", font="arial 14", fg="green")
        lb2.place(x=150, y=200)
        video_url = ent.get()
        yt = YouTube(video_url)
        stream = yt.streams.first()
        stream.download()
    except:
        lb2 = tk.Label(window, text="Not Downloading", font="arial 14", fg="red")
        lb2.place(x=150, y=200)
        

bt = tk.Button(window, text="İndir", font="arial 12 bold", fg="white", bg="navy", command=downloadd)
bt.place(x=200, y=170)

window.mainloop()