"""
Bu proje içersinde makine öğrenimi projelerinde sıklıkla kullanılan yöntemleri bir araya getirerek arayüz aracılığı ile
kullanımı kolay bir çalışma tasarlanmıştır.
Projede Hangi Yöntemler Yer Alıyor?
    Veriyi tanımız için kullanılan hazır fonksiyonlar.
    Görselleştirme için grafikler
    Korelasyon incelemeleri
    Sayısal eksik verilerin düzenlenmesi
    Kategorik eksik verilerin düzenlenmesi
    Ayrık verilerin analizi
    Özellik ölçeklendirme
    Model uygulanması
    Model sonuçlarının incelenmesi

Önemli Uyarılar:
Veri setini klasör içerisine eklemeyi unutmayın.
Değişiklikler veri seti üzerinde olduğu için verinizin bir kopyasını oluşturmayı unutmayın.

"""

import tkinter as tk


def get_url():
    window = tk.Tk()
    window.title("Yapay Zeka")
    window.geometry("300x150+420+70")
    window.resizable(False,False)    
    def csv():
        with open("save.txt", "w") as file:
            if(len(ent1.get()) > 0):
                file.write(ent1.get())
                lb2 = tk.Label(window, text="Yükleme Başarılı   ", font="italic 12", fg="green")
                lb2.place(x=450,y=470)
                window.destroy()
            else:
                lb2 = tk.Label(window, text="Yükleme Başarısız", font="italic 12", fg="red")
                lb2.place(x=450,y=470)
        
    lb1 = tk.Label(window, text="Dosya Uzantısı", font="italic 12")
    lb1.place(x=10, y=10)
    ent1 = tk.Entry(window, font="arial 14")
    ent1.place(x=10, y=30)
    bt14 = tk.Button(window, text="Çalıştır", font="arial 14 bold", fg="white", bg="navy", command=csv)
    bt14.place(x=100, y=80)  


    window.mainloop()
get_url()

import Algoritmalar
window = tk.Tk()
window.title("Yapay Zeka")
window.geometry("1100x600+420+70")
window.resizable(False,False)

result_number = 0       
describe = ""
def search():
   
        
    bt17 = tk.Button(window, text="İlk 5 Değer", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.ilk)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="Son 5 Değer", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.son)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="Min-Max Değer", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.min_max)
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="Bilgi", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.infos)
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="Anlamsız Verileri Çıkart", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.ridiculous)
    bt21.place(x=870,y=250, width=200)

def categorical_analysis():
    bt17 = tk.Button(window, text="Bar Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.bar_graph)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="Pie Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.pie_graph)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="Sunburst Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.sun_burst)
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)
    
def numerical_analysis():
    bt17 = tk.Button(window, text="Histogram", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.hist_graph)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)
    
def relationship_analysis():
    bt17 = tk.Button(window, text="Groupby", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.grouph)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def visualization():
    bt17 = tk.Button(window, text="Pairplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.pair_plot)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="Boxplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.box_plot)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="Countplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.count_plot)
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="Barplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.bar_plot)
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="Kdeplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.kde_plot)
    bt21.place(x=870,y=250, width=200)
    
def discrete_value():
    bt17 = tk.Button(window, text="Boxplot Grafiği", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.box_plot)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)
    
def corelation():
    bt17 = tk.Button(window, text="Isı Korelasyon Tablosu", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.all_corelation)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="Tek Değişken Korelasyon", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.one_corelation)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def size_reduction():
    bt17 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def missing_data():
    bt17 = tk.Button(window, text="Boş Verileri Sil", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.all_delete)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="Kategorikleri Mod Doldur", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.categoric_mod)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="Sayısalları Ortalama Doldur", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.numeric_mean)
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="Sayısalları Medyan Doldur", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.numeric_median)
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="Sayısalları Mod Doldur", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.numeric_mod)
    bt21.place(x=870,y=250, width=200)

def categorical_data_edit():
    bt17 = tk.Button(window, text="Label Encoder", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.label_encoder)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="One Hot Encoder", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.onehot_encoder)
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def discrete_data_edit():
    bt17 = tk.Button(window, text="Label Encoder", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.outlier)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def scaler():
    bt17 = tk.Button(window, text="Standart Scaler", font="arial 12 bold", bg="black", fg="white", command=Algoritmalar.standart_scaler)
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)

def features_engineer():
    bt17 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt17.place(x=30,y=250, width=200)
    bt18 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt18.place(x=240,y=250, width=200)
    bt19 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt19.place(x=450,y=250, width=200)
    bt20 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt20.place(x=660,y=250, width=200)
    bt21 = tk.Button(window, text="", font="arial 12 bold", bg="black", fg="white")
    bt21.place(x=870,y=250, width=200)
    


bt1 = tk.Button(window, text="Verileri İncele", font="arial 14 bold", bg="blue", fg="white", command=search)
bt1.place(x=30,y=30, width=225)
bt2 = tk.Button(window, text="Kategorik Veri Analizi", font="arial 14 bold", bg="orange", fg="white", command=categorical_analysis)
bt2.place(x=270,y=30, width=260)
bt3 = tk.Button(window, text="Sayısal Veri Analizi", font="arial 14 bold", bg="green", fg="white", command=numerical_analysis)
bt3.place(x=545,y=30, width=215)
bt4 = tk.Button(window, text="Değişkenler Arası İlişki Analizi", font="arial 14 bold", bg="red", fg="white", command=relationship_analysis)
bt4.place(x=775,y=30)
bt5 = tk.Button(window, text="Görselleştir", font="arial 14 bold", bg="blue", fg="white", command=visualization)
bt5.place(x=30,y=80, width=225)
bt6 = tk.Button(window, text="Ayrık Değerleri İncele", font="arial 14 bold", bg="orange", fg="white", command=discrete_value)
bt6.place(x=270,y=80, width=260)
bt7 = tk.Button(window, text="Korelasyona Bak", font="arial 14 bold", bg="green", fg="white", command=corelation)
bt7.place(x=545,y=80, width=215)
bt8 = tk.Button(window, text="Boyut Azaltma", font="arial 14 bold", bg="red", fg="white", command=size_reduction)
bt8.place(x=775,y=80, width=295)
bt9 = tk.Button(window, text="Eksik Verilerin Tespiti", font="arial 14 bold", bg="blue", fg="white", command=missing_data)
bt9.place(x=30,y=130)
bt10 = tk.Button(window, text="Kategorik Verileri Düzenle", font="arial 14 bold", bg="orange", fg="white", command=categorical_data_edit)
bt10.place(x=270,y=130)
bt11 = tk.Button(window, text="Ayrık Verileri Düzenle", font="arial 14 bold", bg="green", fg="white", command=discrete_data_edit)
bt11.place(x=545,y=130)
bt12 = tk.Button(window, text="Özellik Ölçeklendirme", font="arial 14 bold", bg="red", fg="white", command=scaler)
bt12.place(x=775,y=130, width=295)
bt13 = tk.Button(window, text="Yeni Veriler Üret", font="arial 14 bold", bg="blue", fg="white", command=features_engineer)
bt13.place(x=150,y=180, width= 250)
bt14 = tk.Button(window, text="Modeli Eğit", font="arial 14 bold", bg="red", fg="white", command=Algoritmalar.model)
bt14.place(x=650,y=180, width=250)


window2 = tk.Tk()
window2.title("Notlar")
window2.geometry("500x800+1+1")
window2.resizable(False,False)
window2.configure(bg="white")
def notx():
    global describe, result_number
    result_number += 1 
    describe = describe + f"SONUÇ {result_number} : " +  str(ent2.get()) + "\n"
    lb4 = tk.Label(window2, text=describe, font="arial 14", bg="white")
    lb4.place(x=1,y=1)
    
lb3 = tk.Label(window, text="Not Ekle : ", font="italic 12")
lb3.place(x=240, y=450)
ent2 = tk.Entry(window, font="arial 14")
ent2.place(x=240,y=470)
bt15 = tk.Button(window, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=notx)
bt15.place(x=300, y=520)
def out():
    window.destroy()
    window2.destroy()    
bt16 = tk.Button(window, text="Çıkış", font="arial 14 bold", fg="white", bg="navy", command=out)
bt16.place(x=700, y=520, width=250)

window2.mainloop()
window.mainloop() 
