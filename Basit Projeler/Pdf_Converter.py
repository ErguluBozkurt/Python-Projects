"""
Aşağıdaki kod bir resmi pdf formatına çevirmede kullanılır. Arayüze sahiptir.
Dosya yolu belirtilmelidir.
"""

from fpdf import FPDF
import tkinter as tk

window = tk.Tk()
window.geometry("500x500+600+100")
window.title("PDF Çevir")
window.resizable(False, False)

lb = tk.Label(window, text="Dosya Yolu", font="arial 12") 
lb.place(x=120, y=100)
ent = tk.Entry(window, font="italic 12")
ent.place(x=120, y=130)

def resmi_pdfye_donustur():
    try:
        resim_yolu = ent.get()
        pdf = FPDF()
        pdf.add_page()
        pdf.image(resim_yolu, x=10, y=10, w=190)
        pdf.output("new.pdf")
        lb1 = tk.Label(window, text="PDF Oluşturuldu       ", font="arial 12", fg="green")
        lb1.place(x=150, y=250)
    except:
        lb1 = tk.Label(window, text="PDF Oluşturulamadı", font="arial 12", fg="red")
        lb1.place(x=150, y=250)


bt = tk.Button(window, text="Çevir", font="arial 12 bold", fg="white", bg="navy", command=resmi_pdfye_donustur)
bt.place(x=180, y=180)

window.mainloop()