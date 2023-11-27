import tkinter as tk
import Paremeter_list
from termcolor import colored

window = tk.Tk()
window.title("Menü")
window.geometry("310x800+1550+70")
window.resizable(False,False)


def motor_servo():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x750+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.motor_servo.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    lb8 = tk.Label(window1, text=text[8], font="arial 14 bold", bg="red", fg="black")
    lb8.place(x=10,y=570, height=65)
    lb9 = tk.Label(window1, text=text[9], font="arial 14 bold", fg="black")
    lb9.place(x=10,y=640, height=65)

    window1.mainloop()
    
def telemetry():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x750+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.telemetry.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    lb8 = tk.Label(window1, text=text[8], font="arial 14 bold", bg="red", fg="black")
    lb8.place(x=10,y=570, height=65)
    lb9 = tk.Label(window1, text=text[9], font="arial 14 bold", fg="black")
    lb9.place(x=10,y=640, height=65)
    
    window1.mainloop()
    
def camera():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x750+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.camera.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    lb8 = tk.Label(window1, text=text[8], font="arial 14 bold", bg="red", fg="black")
    lb8.place(x=10,y=570, height=65)
    lb9 = tk.Label(window1, text=text[9], font="arial 14 bold", fg="black")
    lb9.place(x=10,y=640, height=65)
    
    window1.mainloop()
    
def move_speed():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x550+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.move_speed.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)

    window1.mainloop()
    
def move_road():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x600+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.move_road.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)

    window1.mainloop()
    
def fail_safe():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x600+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.fail_safe.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    
    window1.mainloop()
    
def battery():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x300+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.battery.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    
    window1.mainloop()
    
def kumanda():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x200+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.kumanda.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    
    window1.mainloop()
    
def memory():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x100+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.memory.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)

    window1.mainloop()
    
def gps():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x600+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.gps.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)

    window1.mainloop()
    
def eksen():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x1000+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.eksen.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    lb8 = tk.Label(window1, text=text[8], font="arial 14 bold", bg="grey", fg="black")
    lb8.place(x=10,y=570, height=65)
    lb9 = tk.Label(window1, text=text[9], font="arial 14 bold", bg="green", fg="black")
    lb9.place(x=10,y=640, height=65)
    lb10 = tk.Label(window1, text=text[10], font="arial 14 bold",bg="red" , fg="black")
    lb10.place(x=10,y=710, height=65)
    lb11 = tk.Label(window1, text=text[11], font="arial 14 bold", fg="black")
    lb11.place(x=10,y=780, height=65)
    lb12 = tk.Label(window1, text=text[12], font="arial 14 bold", bg="yellow", fg="black")
    lb12.place(x=10,y=850, height=65)
    lb13 = tk.Label(window1, text=text[13], font="arial 14 bold", bg="green", fg="black")
    lb13.place(x=10,y=920, height=65)

    window1.mainloop()
def take_off():
    global window1
    window1.destroy()
    window1 = tk.Tk()
    window1.title("Açıklamalar")
    window1.geometry("1500x800+1+1")
    window1.resizable(False,False)
    window1.configure(bg="white")
    
    text = Paremeter_list.take_off.split(".")
    
    lb0 = tk.Label(window1, text=text[0], font="arial 14 bold", bg="grey", fg="black")
    lb0.place(x=10,y=10, height=65)
    lb1 = tk.Label(window1, text=text[1], font="arial 14 bold", bg="green", fg="black")
    lb1.place(x=10,y=80, height=65)
    lb2 = tk.Label(window1, text=text[2], font="arial 14 bold",bg="red" , fg="black")
    lb2.place(x=10,y=150, height=65)
    lb3 = tk.Label(window1, text=text[3], font="arial 14 bold", fg="black")
    lb3.place(x=10,y=220, height=65)
    lb4 = tk.Label(window1, text=text[4], font="arial 14 bold", bg="yellow", fg="black")
    lb4.place(x=10,y=290, height=65)
    lb5 = tk.Label(window1, text=text[5], font="arial 14 bold", bg="green", fg="black")
    lb5.place(x=10,y=360, height=65)
    lb6 = tk.Label(window1, text=text[6], font="arial 14 bold",  bg="grey", fg="black")
    lb6.place(x=10,y=430, height=65)
    lb7 = tk.Label(window1, text=text[7], font="arial 14 bold", bg="orange", fg="black")
    lb7.place(x=10,y=500, height=65)
    lb8 = tk.Label(window1, text=text[8], font="arial 14 bold", bg="grey", fg="black")
    lb8.place(x=10,y=570, height=65)
    lb9 = tk.Label(window1, text=text[9], font="arial 14 bold", bg="green", fg="black")
    lb9.place(x=10,y=640, height=65)
    
    window1.mainloop()

bt1 = tk.Button(window, text="Motor ve Servo", font="arial 14 bold", bg="navy", fg="white", command=motor_servo)
bt1.place(x=30,y=30, width=250)
bt2 = tk.Button(window, text="Hareket Hızı", font="arial 14 bold", bg="navy", fg="white", command=move_speed)
bt2.place(x=30,y=80, width=250)
bt3 = tk.Button(window, text="Hareket Yolu", font="arial 14 bold", bg="navy", fg="white", command=move_road)
bt3.place(x=30,y=130, width=250)
bt4 = tk.Button(window, text="Hafıza", font="arial 14 bold", bg="navy", fg="white", command=memory)
bt4.place(x=30,y=180, width=250)
bt5 = tk.Button(window, text="Batarya", font="arial 14 bold", bg="navy", fg="white", command=battery)
bt5.place(x=30,y=230, width=250)
bt6 = tk.Button(window, text="GPS", font="arial 14 bold", bg="navy", fg="white", command=gps)
bt6.place(x=30,y=280, width=250)
bt7 = tk.Button(window, text="Kalkış", font="arial 14 bold", bg="navy", fg="white", command=take_off)
bt7.place(x=30,y=330, width=250)
bt8 = tk.Button(window, text="Telemetri", font="arial 14 bold", bg="navy", fg="white", command=telemetry)
bt8.place(x=30,y=380, width=250)
bt9 = tk.Button(window, text="Fail Safe", font="arial 14 bold", bg="navy", fg="white", command=fail_safe)
bt9.place(x=30,y=430, width=250)
bt10 = tk.Button(window, text="Eksenler(AHRS)", font="arial 14 bold", bg="navy", fg="white", command=eksen)
bt10.place(x=30,y=480, width=250)
bt11 = tk.Button(window, text="Kamera", font="arial 14 bold", bg="navy", fg="white", command=camera)
bt11.place(x=30,y=530, width=250)
bt12 = tk.Button(window, text="Kumanda", font="arial 14 bold", bg="navy", fg="white", command=kumanda)
bt12.place(x=30,y=580, width=250)


window1 = tk.Tk()
window1.title("Açıklamalar")
window1.geometry("1500x1000+1+1")
window1.resizable(False,False)
window1.configure(bg="white")

def out():
    window1.destroy()
    window.destroy()  
    
bt16 = tk.Button(window, text="Çıkış", font="arial 14 bold", fg="white", bg="black", command=out)
bt16.place(x=30, y=720, width=250)


window1.mainloop() 
window.mainloop() 
