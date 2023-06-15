"""
Aşağıdaki kod Tv lerde sıklıkla görülen grafiksel ve görsel yöntemler göz önüne alınarak tasarlanmış basit bir projedir.
"""



import numpy as np
import matplotlib.pyplot as plt

toplam_test = int(input("Toplam Yapılan Test Sayısı:"))
toplam_hasta_num = int(input("Toplam Hasta Sayısı:"))
toplam_vefat_num = int(input("Toplam Vefat Eden Kişi Sayısı:"))
toplam_iyilesen_num = int(input("Toplam iyileşen Kişi Sayısı:"))

test_num = int(input("Bugünkü Yapılan Test Sayısı:"))
hasta_num = int(input("Bugünkü Hasta Sayısı:"))
vefat_num = int(input("Bugünkü Vefat Eden Kişi Sayısı:"))
iyilesen_num = int(input("Bugünkü iyileşen Kişi Sayısı:"))
gun = input("Günün Tarihini giriniz:")

listem1 = [toplam_test,toplam_hasta_num,toplam_vefat_num, toplam_iyilesen_num]
listem2 = [test_num, hasta_num, vefat_num, iyilesen_num]
remark = ["Test \nSayısı","Hasta \nSayısı","Vefat \nSayısı","İyileşen \nSayısı"]
plt.subplot(1,2,1)
plt.bar(x=remark, height=listem1)
plt.title("Toplam Korona Vürüs Hasta \nBilgileri")

plt.subplot(1,2,2)
plt.bar(x=remark, height=listem2)
plt.title(f"Günlük Korana Virüs Tablosu \n{gun}")

plt.show()
