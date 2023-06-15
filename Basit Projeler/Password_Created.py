"""
Bu kod büyük-küçük harf,rakam ve sembol kullanarak 10 basamaklı güçlü bir şifre oluşturmaktadır.
"""

import random

lower = "qwertyuopasdfghjklzxcvbnmi"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
mark = "!^+%&/()=?*_-|][}{]$#£><.,:;"
total = lower + upper + number + mark

password = random.choices(total, k=10)
password = "".join(password) # gelen değer liste şeklinde olduğu için onları birleştirdik
print(password)