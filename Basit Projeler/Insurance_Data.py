"""
İstenilen yıl aralığında her hangi bir şeyin sigortasının hangi yılda olduğunu bulan basit bir alıştma kodudur.
Örnek kod 3 yıl aralıkda sigortaya sahip durumlar için yapılmıştır.
"""

import datetime

days = 0
date =list()
date = input("Sigorta Tarihini Giriniz(year/month/day)=")
new_date = date.split("/")
year_ = int(new_date[0])
month_ = int(new_date[1])
day_ = int(new_date[2])

now = datetime.datetime.now()
year = now.year
month = now.month
day =now.day

new_year = year - year_
x = 365 * new_year
days = days + x
new_month = month - month_
y = new_month * 30
days = days + y
days = days + (day - day_)
if(days<=365):
    print("Birinci Yıl")
elif(days<=(365*2)):
    print("İkinci Yıl")
elif(days<=(365*3)):
    print("Üçüncü Yıl")
else:
    print("Bilgi Bulunamadı")
 
