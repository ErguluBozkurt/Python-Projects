"""
Bu proje örnek bir bankamatiğin sık kullanılan işlemlerin gerçekleştirilmesi üzerine yazılmıştır.
"""

import time

hesap={
    "name": "Admin",
    "hesap_no":"1111",
    "bakiye": 7000,
    "ek_hesap":3000,
    "askeri_borc":2500
}

while True:
    print(f"Welcome {hesap['name']}")
    no = input("You enter your account number:")
    
    if(no==hesap["hesap_no"]):
        choice = int(input("If you want to invest money, you can click on (1) = \nIf you want to take money, you can click on (2) = \nIf you want to pay owe, you can click on (3) = \nchoice = "))

        if(choice==2):
            print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
            def para_cek(hesap, miktar):
   
                toplam = hesap["bakiye"] + hesap["ek_hesap"]
                if(hesap["bakiye"]>=miktar):
                    print("You can take money")
                    time.sleep(5)
                    hesap["bakiye"] -= miktar
                    print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
    
                elif((hesap["bakiye"]<miktar) and (toplam>=miktar)):
                    x = input("Do you want to make add account(e/h)=")
                    if(x == "e"):
                        print("You can take money")
                        time.sleep(5)
                        y = miktar - hesap["bakiye"]
                        hesap["bakiye"] = 0
                        hesap["ek_hesap"] = hesap["ek_hesap"] - y
                        print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
                else:
                    print("You haven't enough money")
    
            i=0
            while(i==0):
                para_cek(hesap, int(input("How much will you take money=")))  
                again = input("Do you want to take money again(e/h)=")
                if(again=="h"):
                    i=1       
    
        if(choice==3):
            print(f"You have owe = {hesap['askeri_borc']}")
            print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
            def borc_ode(hesap, miktar):
                toplam = hesap["bakiye"] + hesap["ek_hesap"]
                if(hesap["bakiye"]>=miktar):
                    print("Paid owe")
                    time.sleep(5)
                    hesap["bakiye"] -= miktar
                    print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
                    hesap['askeri_borc'] = hesap['askeri_borc'] - miktar
                    print(f"You have owe = {hesap['askeri_borc']}")
                elif((hesap["bakiye"]<miktar) and (toplam>=miktar)):
                    x = input("Do you want to make add account(e/h)=")
                    if(x == "e"):
                        print("Paid owe")
                        time.sleep(5)
                        y = miktar - hesap["bakiye"]
                        hesap["bakiye"] = 0
                        hesap["ek_hesap"] = hesap["ek_hesap"] - y
                        print(f"You have account={hesap['bakiye']} and add account={hesap['ek_hesap']}")
                        hesap['askeri_borc'] = hesap['askeri_borc'] - miktar 
                        print(f"You have owe = {hesap['askeri_borc']}")
                else:
                    print("You haven't enough money")
    
            borc_ode(hesap, int(input("How much will you pay owe=")))
    
        if(choice==1):
            while True:
                
                if(hesap["askeri_borc"]>0):
                    yatir = int(input("How much money you invest="))
                    print("Your money is invested, wait for please!")
                    time.sleep(5)
                    hesap["bakiye"] += yatir
                    print("Your money is invested.")
                    print(f"You have account={hesap['bakiye']}")
                    add_money = input("Would you like to add momey(e/h)=")
                    if(add_money=="h"):
                        break
                else:
                    print("You don't have owe.")
        
    
       
        x = input("Do you want to finish(e/h)=")
        if(x=="e"):
            print("THANK YOU!!")
            time.sleep(3)
            break  
         
    else:
        print("You enter wrong number!!!")
