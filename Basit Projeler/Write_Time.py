"""
Klavye ile yazma hızınızı ölçen bir projedir. Ekran da gösterilen yazıyı yazın, onaylayın ve yazma hızınızı görün.

"""


import datetime
import time


print("Hazır olun!")
for i in range(3,0,-1):
    print(f"{i}...")
    time.sleep(1)

print("başarı tesadüf değildir.")

now = datetime.datetime.now()
saniye = str(now.second)
mikro_saniye = now.microsecond
mikro_saniye = str(mikro_saniye)
mikro_saniye = mikro_saniye[0:2]

value = input("Yazın :")

now1 = datetime.datetime.now()
saniye1 = str(now1.second)
mikro_saniye1 = now1.microsecond
mikro_saniye1 = str(mikro_saniye1)
mikro_saniye1 = mikro_saniye1[0:2]
result1 = int(saniye1) - int(saniye)
result2 = int(mikro_saniye1) - int(mikro_saniye)
result = str(result1) + "." + str(result2)
print(f"Yazma süreniz: {result} ")



