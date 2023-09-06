"""
Arayüze sahip bir hesap makinesi yapılmıştır. tkinter ve math kütüphanesi kullanılmıştır. 

"""
# Kütüphaneler
import tkinter as tk
import math

# Arayüz penceresi
window = tk.Tk()
window.geometry("340x520+1000+100")
window.title("Hesap Makinesi")
window.resizable(False, False)

# Ekran
lb1 = tk.Label(window, text="0.0", fg="black", font="arial 30 bold")
lb1.place(x=20,y=20)

# Değişkenler
num1 = str()
num2 = str()
is_n = True
value = str()

# Fonksiyonlar
def number0():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "0"
    else:
        num2 = str(num2) + "0"
def number1():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "1"
    else:
        num2 = str(num2) + "1"
def number2():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "2"
    else:
        num2 = str(num2) + "2"
def number3():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "3"
    else:
        num2 = str(num2) + "3"
def number4():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "4"
    else:
        num2 = str(num2) + "4"
def number5():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "5"
    else:
        num2 = str(num2) + "5"
def number6():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "6"
    else:
        num2 = str(num2) + "6"
def number7():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "7"
    else:
        num2 = str(num2) + "7"
def number8():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "8"
    else:
        num2 = str(num2) + "8"
def number9():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "9"
    else:
        num2 = str(num2) + "9"
def point():
    global num1, num2
    if(is_n):
        num1 = str(num1) + "."
    else:
        num2 = str(num2) + "."
def square_root():
    global num1
    num1 = math.sqrt(int(num1))
    lb1["text"] = num1
def square():
    global num1
    num1 = int(num1)**2
    lb1["text"] = num1
def all_delete():
    global num1, num2, is_n, value
    num1 = str()
    num2 = str()
    is_n = True
    value = str()
def delete():
    global num1, num2
    if(is_n):
        num1 = str(num1)[:-1]
    else:
        num2 = str(num2)[:-1]
def percentage():
    global num1
    num1 = float(num1)/100.0
    lb1["text"] = num1
def cos():
    global num1
    num1 = math.cos(float(num1))
    lb1["text"] = num1
def sin():
    global num1
    num1 = math.sin(float(num1))
    lb1["text"] = num1
def tan():
    global num1
    num1 = math.tan(float(num1))
    lb1["text"] = num1
def cot():
    global num1
    num1 = 1/(math.tan(float(num1)))
    lb1["text"] = num1
def adder():
    global value, is_n
    value = "add"
    is_n = False 
def subtract():
    global value, is_n
    value = "subtract"
    is_n = False 
def multiplication():
    global value, is_n
    value = "multiplication"
    is_n = False 
def division():
    global value, is_n
    value = "division"
    is_n = False 
def equal():
    global value, num1, num2
    if(value=="add"):
        num1 = float(num1) + float(num2)
        lb1["text"] = num1
        num2 = ""
        value = ""
    elif(value=="subtract"):
        num1 = float(num1) - float(num2)
        lb1["text"] = num1
        num2 = ""
        value = ""
    elif(value=="multiplication"):
        num1 = float(num1) * float(num2)
        lb1["text"] = num1
        num2 = ""
        value = ""
    elif(value=="division"):
        num1 = float(num1) / float(num2)
        lb1["text"] = num1
        num2 = ""
        value = ""
    else:
        lb1["text"] = "Geçersiz İşlem"


# Düğmeler
bt1 = tk.Button(window, text="Cos", fg="black", bg="white", activeforeground="gray", font="arial 15", command=cos)
bt1.place(x=20, y=120, width=70, height=50)

bt2 = tk.Button(window, text="Sin", fg="black", bg="white", activeforeground="gray", font="arial 15", command=sin)
bt2.place(x=95, y=120, width=70, height=50)

bt3 = tk.Button(window, text="Tan", fg="black", bg="white", activeforeground="gray", font="arial 15", command=tan)
bt3.place(x=170, y=120, width=70, height=50)

bt4 = tk.Button(window, text="Cot", fg="black", bg="white", activeforeground="gray", font="arial 15", command=cot)
bt4.place(x=245, y=120, width=70, height=50)

bt5 = tk.Button(window, text="%", fg="black", bg="white", activeforeground="gray", font="arial 15", command=percentage)
bt5.place(x=20, y=175, width=70, height=50)

bt6 = tk.Button(window, text="1/x", fg="black", bg="lightgray", activeforeground="gray", font="arial 15")
bt6.place(x=20, y=230, width=70, height=50)

bt7 = tk.Button(window, text="7", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number7)
bt7.place(x=20, y=285, width=70, height=50)

bt8 = tk.Button(window, text="4", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number4)
bt8.place(x=20, y=340, width=70, height=50)

bt9 = tk.Button(window, text="1", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number1)
bt9.place(x=20, y=395, width=70, height=50)

bt10 = tk.Button(window, text="+/-", fg="black", bg="white", activeforeground="gray", font="arial 15")
bt10.place(x=20, y=450, width=70, height=50)

bt11 = tk.Button(window, text="CE", fg="black", bg="white", activeforeground="gray", font="arial 15")
bt11.place(x=95, y=175, width=70, height=50)

bt12 = tk.Button(window, text="X^2", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=square)
bt12.place(x=95, y=230, width=70, height=50)

bt13 = tk.Button(window, text="8", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number8)
bt13.place(x=95, y=285, width=70, height=50)

bt14 = tk.Button(window, text="5", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number5)
bt14.place(x=95, y=340, width=70, height=50)

bt15 = tk.Button(window, text="2", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number2)
bt15.place(x=95, y=395, width=70, height=50)

bt16 = tk.Button(window, text="0", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number0)
bt16.place(x=95, y=450, width=70, height=50)

bt17 = tk.Button(window, text="C", fg="black", bg="white", activeforeground="gray", font="arial 15", command=all_delete)
bt17.place(x=170, y=175, width=70, height=50)

bt18 = tk.Button(window, text="√x", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=square_root)
bt18.place(x=170, y=230, width=70, height=50)

bt19 = tk.Button(window, text="9", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number9)
bt19.place(x=170, y=285, width=70, height=50)

bt20 = tk.Button(window, text="6", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number6)
bt20.place(x=170, y=340, width=70, height=50)

bt21 = tk.Button(window, text="3", fg="black", bg="white", activeforeground="gray", font="arial 15", command=number3)
bt21.place(x=170, y=395, width=70, height=50)

bt22 = tk.Button(window, text=".", fg="black", bg="white", activeforeground="gray", font="arial 15", command=point)
bt22.place(x=170, y=450, width=70, height=50)

bt17 = tk.Button(window, text="<<=", fg="black", bg="white", activeforeground="gray", font="arial 15", command=delete)
bt17.place(x=245, y=175, width=70, height=50)

bt18 = tk.Button(window, text="÷", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=division)
bt18.place(x=245, y=230, width=70, height=50)

bt19 = tk.Button(window, text="x", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=multiplication)
bt19.place(x=245, y=285, width=70, height=50)

bt20 = tk.Button(window, text="-", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=subtract)
bt20.place(x=245, y=340, width=70, height=50)

bt21 = tk.Button(window, text="+", fg="black", bg="lightgray", activeforeground="gray", font="arial 15", command=adder)
bt21.place(x=245, y=395, width=70, height=50)

bt22 = tk.Button(window, text="=", fg="black", bg="lightblue", activeforeground="gray", font="arial 15", command=equal)
bt22.place(x=245, y=450, width=70, height=50)


window.mainloop()