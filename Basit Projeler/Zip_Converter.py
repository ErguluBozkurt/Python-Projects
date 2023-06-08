"""
Aşağıdaki uygulama dosya ve klasörleri zip haline getirmek için yapılmıştır. Arayüze sahiptir.
"""

import tkinter as tk
from tkinter import filedialog as fd
import zipfile
import os

window = tk.Tk()
window.title("Zip Conversion")
window.geometry("500x500+600+100")
window.resizable(False,False)

# Dosya
def file_add():
	try:
		import_filename = fd.askopenfilename()
		with zipfile.ZipFile('dosya.zip', 'w') as myzip:
			dosya_adresi = os.path.abspath(import_filename)
			myzip.write(dosya_adresi)
			lb1 = tk.Label(window, text="Sıkıştırma Başarılı   ", font="arial 14", fg="green")
			lb1.place(x=120, y=320)
	except:
		lb1 = tk.Label(window, text="Sıkıştırma Başarısız", font="arial 14", fg="red")
		lb1.place(x=120, y=320)
 
# Klasör
def klasor_add():

	def zipp():
		try:
			path = ent.get()
			zipf = zipfile.ZipFile('dosya.zip', 'w', zipfile.ZIP_DEFLATED)
			for root, files in os.walk(path):
				for file in files:
					zipf.write(os.path.join(root, file))
			zipf.close()
			lb1 = tk.Label(window, text="Sıkıştırma Başarılı   ", font="arial 14", fg="green")
			lb1.place(x=120, y=400)
		except:
			lb1 = tk.Label(window, text="Sıkıştırma Başarısız", font="arial 14", fg="red")
			lb1.place(x=120, y=400)
			

	lb = tk.Label(window, text="Dosya yolu", font="arial 11")
	lb.place(x=120, y=290)
	ent = tk.Entry(window, font="arial 12")
	ent.place(x=120, y=320)
	button3 = tk.Button(window, text="Çevir", font="italic 12 bold", fg="white", bg="navy", command=zipp)
	button3.place(x=180, y=350)


button1 = tk.Button(window, text="Dosya Ekle", width=20, height=2, bg="navy",fg="white", font="itaic 12 bold", command=file_add)
button1.place(x=120, y=120)

button2 = tk.Button(window, text="Klasör Ekle", width=20, height=2, bg="navy", fg="white", font="italic 12 bold", command=klasor_add)
button2.place(x=120, y=220)

window.mainloop()


