
"""
Aşağıda yer alan kod resimleri jpg-png ve png-jpg formatına çevirebilen arayüze sahip bir çalışmadır. Arayüz için tkinter kütüphanesi
kullanılmıştır.
"""
# Kütüphaneler tanımlandı
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox

# Arayüz ekranı oluşturuldu
window = tk.Tk()
window.title("Image Conversion App")
window.geometry("500x500+600+100")
window.resizable(False,False)

# jpg formatından png formatına çevirme 
def jpg_to_png():
	global im1
	import_filename = fd.askopenfilename()
	if(import_filename.endswith(".jpg") == True):

		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".png")
		im1.save(export_filename)
		messagebox.showinfo("Success", "Your Image Converted to Png")
	else:

		messagebox.showerror("Fail!!", "Something Went Wrong...")

# png formatından jpg formatına çevirme
def png_to_jpg():
	global im1
	import_filename = fd.askopenfilename()
	if(import_filename.endswith(".png") == True):
		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".jpg")
		im1.save(export_filename)
		messagebox.showinfo("Success ", "Your Image Converted to jpg ")
	else:

		messagebox.showerror("Fail!!", "Something Went Wrong...")

# Butonlar
button1 = tk.Button(window, text="JPG to PNG", width=20, height=2, bg="navy",fg="white", font="itaic 12 bold", command=jpg_to_png)
button1.place(x=120, y=120)

button2 = tk.Button(window, text="PNG to JPEG", width=20, height=2, bg="navy", fg="white", font="italic 12 bold", command=png_to_jpg)
button2.place(x=120, y=220)

window.mainloop() # Arayüzün sürekli açık kalması için


