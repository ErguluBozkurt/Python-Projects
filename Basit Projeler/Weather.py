"""
Bu proje bulunduğunuz güne dair hava durumunu sizlere sunar ayrıca sizlere ne yapmanız gerektiği hakkında küçük öneriler vermektedir.
"""



from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Corum"
driver.get(url)
driver.minimize_window()

sicaklik= driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[1]").text
ruzgar = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/section/div[5]/div[2]/div[2]/div[2]/div[2]").text
durum = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[2]/div[2]").text
yagis = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[3]/div[2]/div[2]").text

print("#"*40)
print(f"  Hava Bugün {durum}  ".center(40,"#"))
print("#"*40)
print(f"  * Hava Sıcaklığı {sicaklik} Derce")
print(f"  * Rüzgar Hızı Yaklaşık {ruzgar}km/sa Hız İle Esmektedir")
if(int(ruzgar)<15):
    print("  * Sakin Bir Hava Hakim")
elif(int(ruzgar)>15 and int(ruzgar)<20):
    print("  * Ruzgarlı Bir Hava Hakim")
elif(int(ruzgar)>20 ):
    print("  * Çok Ruzgarlı Bir Hava Hakim")
print(f"  * Ortalama Yağış Miktarı {yagis}")
if(int(yagis)>15):
    print("DİKKAT!!!")
    if(int(ruzgar)<20):
        print("      * Bugün Yağmurlu Bir Hava Var! \nŞemsiye Alabilirsiniz")
    else:
        print("      * Bugün Yağmurlu ve Rüzgarlı Bir Hava Bekleniyor!! \nLütfen Gerekli Önleminizi Alınız")   
    
driver.close()
