
"""
Bu kod bir kapı kilit şifresini yazma süresini hesaplamaktadır.
Tuşlama takımında rakamların yeri değişmektedir. Burada kullanılan tuşlama takımı aşağıdaki gibidir;
        2 4 7
        3 1 8
        5 6 9 



"""

x1,x2,x3,x4,x5,x6,x7,x8,x9 = ("2","4","7","3","1","8","5","6","9") # Tuşlama takımı
time = 0
securty_kod = input("Güvenlik Kodu:")
sayac1 = 1
for i in securty_kod:
    sayac1 +=1 
    sayac2 = 0
    if(i==x1):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="1" or j=="3" or j=="4"):
                    time += 1
                elif(j=="2"):
                    pass
                else:
                    time += 2
            
                
    elif(i==x2):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="2" or j=="3" or j=="8"or j=="1" or j=="7"):
                    time += 1
                elif(j=="4"):
                    pass
                else:
                    time += 2
    

    elif(i==x3):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="4" or j=="8"or j=="1"):
                    time += 1
                elif(j=="7"):
                    pass
                else:
                    time += 2
    

    elif(i==x4):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="2" or j=="4" or j=="6"or j=="1" or j=="5"):
                    time += 1
                elif(j=="3"):
                    pass
                else:
                    time += 2
            
    elif(i==x5):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="2" or j=="4" or j=="6"or j=="7" or j=="5"or j=="3" or j=="8"or j=="7" or j=="9"):
                    time += 1
                elif(j=="1"):
                    pass
                else:
                    time += 2
    elif(i==x6):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="7" or j=="4" or j=="6"or j=="1" or j=="9"):
                    time += 1
                elif(j=="8"):
                    pass
                else:
                    time += 2
        
    elif(i==x7):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="3" or j=="6"or j=="1"):
                    time += 1
                elif(j=="5"):
                    pass
                else:
                    time += 2
            
    elif(i==x8):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="5" or j=="3" or j=="8"or j=="1" or j=="9"):
                    time += 1
                elif(j=="6"):
                    pass
                else:
                    time += 2
        
    elif(i==x9):
        for j in securty_kod:
            sayac2 +=1
            if(sayac1==sayac2):
                if(j=="8" or j=="6"or j=="1"):
                    time += 1
                elif(j=="9"):
                    pass
                else:
                    time += 2
print(f"Zaman:{time}")