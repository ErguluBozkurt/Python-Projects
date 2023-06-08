"""
Aşağıdaki kod girilen sayının asal sayı olup olmadığını buluyor.
"""

sayi = int(input("sayi="))
asal_mi = True
if(sayi == 1):
    asal_mi = False
for i in range(2, sayi):
    if(sayi % i == 0):
        asal_mi = False 
        break
if asal_mi:
    print("Asal sayi")
else:
    print("Asal sayi değildir")
    
