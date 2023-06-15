"""
Bu kod sizi önce dinler daha sonra söylediklerinizi yazı haline getirip txt dosyasında saklayacaktır.

"""


import speech_recognition as sr
import tkinter as tk


window = tk.Tk()
window.title("Ses Dinleme")
window.geometry("400x200+550+150")
window.resizable(False, False)

lb1 = tk.Label(window, text="Konuşmaya Başlayın...", fg="black", font="arial 14")
lb1.pack(pady=30)

def ses():
    rec = sr.Recognizer()

    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Konuşmaya Başlayın...")
        audio = rec.listen(mic)
        
        
        try:
            print("Senin Söylemek İstediğin: " + rec.recognize_google(audio))
        except:
            print("Hata --> " + str(Exception))
        with open("oku.txt", "w", encoding="utf-8") as file:
            file.write(audio.get_wav_data())
            print("Ses Kaydedildi")


bt1 = tk.Button(window, text="Başla", fg="white", bg="navy", activebackground="white", activeforeground="navy", font="arial 12", width=10, command=ses)
bt1.pack()

window.mainloop()

