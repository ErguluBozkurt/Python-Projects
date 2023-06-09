"""
Bu proje class yapısı dikkate alınarak gerçekleştirilen bir bankamatik örneğidir. 
Bankamatikde gerçekleştirilen bazı işlemler kodlar ile yapılmıştır.
"""
import time

class Bank():
    def __init__(self, name, surname, count_no, password,money):
        self.name = name
        self.surname = surname
        self.count_no = count_no
        self.password = password
        self.money = money
    
    
    
    def view_info(self):
        print("*"*20)
        print(f"{self.name} {self.surname}: \nCount No:{self.count_no} \nYour Money:{self.money} ")
        time.sleep(2)
    
    
    def take_money(self, money):
        if(self.money >= money):
            self.money = self.money - money
            print("You can take your money...")
            time.sleep(2)
            self.view_info()
            time.sleep(2)
        else:
            print("You haven't enough money !!")
            time.sleep(2)    
        
    
    
    def put_money(self, money1):
        self.money = self.money + money1
        print("You can put your money...")
        time.sleep(2)
        self.view_info()
        time.sleep(2)
        
        
    def send_money(self, iban, ad):
        money2 = int(input("How much money you enter its:"))
        if(self.money >= money2):
            print(f"it had send to {ad}, iban:{iban}")
            self.money = self.money - money2
            
            
# isim, soyisim, hesap no, şifre
kisi = Bank("Admin", "Nimda", "235894", "11111", 15000)     
        
        
i = 0            
while(i<3):
    
    your_account = input("You enter your account no, please: ")
    your_password = input("You enter your password, please :")

    if(your_password==kisi.password and your_account == kisi.count_no):
        print(f"  WELCOME {kisi.name.upper()} {kisi.surname.upper()}  ".center(62, "#"))
        print()
        time.sleep(3)
        
        while True:
            choice = int(input("""You enter to you want choices
                            
                            if you want to look your account     : 1
                            if you want to take your money       : 2
                            if you want to put your money        : 3
                            if you want to send money to someone : 4
                            if you want to exit              : 0
                            Choice : """))
            if(choice == 1):
                kisi.view_info()

            elif(choice == 2):
                money = int(input("How much you want to take money:"))
                kisi.take_money(money)

            elif(choice == 3):
                money1 = int(input("How much you want to put money:"))
                kisi.put_money(money1)
                
            elif(choice == 4):
                hesap_no = input("You enter its IBAN no:")
                name = input("You enter its name:")
                kisi.send_money(hesap_no, name)
                
            elif(choice == 0):
                i = 4
                break
            
            else:
                print("You enter to click wrong!!")
                time.sleep(2)
                        
    else:
        if(your_password != kisi.password):
            print("You enter wrong your password !!")
            time.sleep(2)
        if(your_account != kisi.count_no):    
            print("You enter wrong your account no !!")
            time.sleep(2)
        
        i = i + 1
        if(i==3):
            print("The bankmatic took in your card ")
            time.sleep(2)
            
