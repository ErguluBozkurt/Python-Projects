"""
Bu projede PyQt5 kütüphanesini kullanarak basit bir hesap makinesi yapılmıştır.
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys 


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Calculator") 
        self.setGeometry(200,200,400,400) 
  
        self.gui()


    def gui(self):
        # Birinci sayı 
        self.lb1 = QLabel(self)
        self.lb1.setText("İlk Sayı : ")
        self.lb1.move(10,10)

        self.ent1 = QLineEdit(self)
        self.ent1.move(70,10)
        self.ent1.resize(100,32)

        # İkinci sayı
        self.lb2 = QLabel(self)
        self.lb2.setText("İkinci Sayı : ")
        self.lb2.move(10,80)

        self.ent2 = QLineEdit(self)
        self.ent2.move(70,80)
        self.ent2.resize(100,32)

        # Button
        self.btn1 = QPushButton(self)
        self.btn1.setText("Toplama")
        self.btn1.move(70, 130)
        self.btn1.clicked.connect(self.calculator)

        self.btn2 = QPushButton(self)
        self.btn2.setText("Çıkarma")
        self.btn2.move(70, 170)
        self.btn2.clicked.connect(self.calculator)

        self.btn3 = QPushButton(self)
        self.btn3.setText("Çarpma")
        self.btn3.move(70, 210)
        self.btn3.clicked.connect(self.calculator)

        self.btn4 = QPushButton(self)
        self.btn4.setText("Bölme")
        self.btn4.move(70, 250)
        self.btn4.clicked.connect(self.calculator)
        
        # Sonuç
        self.lb3 = QLabel(self)
        self.lb3.move(250,50)


    def calculator(self):
        sender = self.sender() # hangi butona basarsak onu işaret eder
        result = 0
        if(sender.text()=="Toplama"):
            result = int(self.ent1.text()) + int(self.ent2.text())
        elif(sender.text()=="Çıkarma"):
            result = int(self.ent1.text()) - int(self.ent2.text())
        elif(sender.text()=="Çarpma"):
            result = int(self.ent1.text()) * int(self.ent2.text())
        elif(sender.text()=="Bölme"):
            result = int(self.ent1.text()) / int(self.ent2.text())

        self.lb3.setText(f"Sonuç : {result}")
        

def wimdow(): 
    app = QApplication(sys.argv)
    win = MyWindow() 

    win.show() 
    sys.exit(app.exec_()) 

wimdow()