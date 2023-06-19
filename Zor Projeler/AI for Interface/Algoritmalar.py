import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import seaborn as sns
import tkinter as tk
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
import operator
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score

def data():
    global datas
    with open("Try/save.txt", "r") as file:
        url = file.read()
    url = str(url)
    if(url[-3:] == "csv"):
        datas = pd.read_csv(url)
    else:
        datas = pd.read_excel(url)

def ilk():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("900x300+500+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.head(), fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()
         
def son():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("900x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.tail(), fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()
               
def min_max():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("900x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.describe(), fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()


######################################################
def korelasyon_ısı():
    data()
    plt.figure(figsize=(6, 6)) # sıcaklık tablosu oluşturur korelasyon katsayısı ilişkisini daha net görebilmek için
    heatmap = sns.heatmap(datas.corr(), vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
    plt.show() # Sıcaklık tablosunu gösterdi
         
def korelasyon_num():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x500+500+70")
    window1.resizable(False,False)
    corr_matrix = datas.corr()
    lb1 = tk.Label(window1, text="Değişken Adı", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    def values():
        global value
        value = str(ent1.get())
        lb1 = tk.Label(window1, text=corr_matrix[value], font="10", fg="black", bg="white")
        lb1.place(x=20, y=100)
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()
   

######################################################
def values_graph():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+900+70")
    window1.resizable(False,False)
    sutunlar = list(datas.columns)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=20)
    
    def val():
        dependent_variable = ent1.get()
        num_plots = len(sutunlar)
        num_rows = 6
        current_plot = 0

        while current_plot < num_plots:
            fig, axes = plt.subplots(num_rows, 1, figsize=(10, 8*num_rows))

            for i in range(num_rows):
                if current_plot >= num_plots:
                    break
                variable = sutunlar[current_plot]
                sns.scatterplot(x=variable, y=dependent_variable, data=datas, ax=axes[i])
                axes[i].set_xlabel(variable)
                axes[i].set_ylabel(dependent_variable)
                axes[i].set_title(f'{variable} vs {dependent_variable}')
                current_plot += 1

            plt.tight_layout()
            plt.show()
            plt.close(fig)
        
    but1 = tk.Button(window1, text="Tamam", font="italic 12 bold", fg="white", bg="navy", command=val)
    but1.place(x=50, y=60)
    
                            
    window1.mainloop()    
def value_graph():
    data()
    datas.hist(bins=50, figsize=(20,15)) 
    plt.show()
def one_graph():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+500+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    def values():
        global value
        value = str(ent1.get())
        sns.distplot(datas[value]) 
        plt.show()
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()

######################################################
def lineer():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+900+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Bağımlı Değişken", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    lb2 = tk.Label(window1, text="Bağımsız Değişken", font="5", fg="black")
    lb2.place(x=20, y=100)
    ent2 = tk.Entry(window1, font="arial 14")
    ent2.place(x=20, y=130)
    def values():
        global value1, value2
        value1 = str(ent1.get())
        value2 = str(ent2.get())
        X = datas[value2].values 
        y = datas[value1].values            
        uzunluk = len(X) 
        X = X.reshape((uzunluk,1))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 
        lm = LinearRegression() 
        lm.fit(X_train,y_train)
        scorem = lm.score(X_test, y_test) 
        lb3 = tk.Label(window1, text=f"Regrasyon Scoru : {round(scorem, 2)}", font="10", fg="black", bg="white")
        lb3.place(x=20, y=200)
        plt.scatter(X_train, y_train, color = 'red') 
        plt.plot(X_train, lm.predict(X_train), color = 'blue')
        plt.show()
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()
    
def polinomal():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+900+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Bağımlı Değişken", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    lb2 = tk.Label(window1, text="Bağımsız Değişken", font="5", fg="black")
    lb2.place(x=20, y=100)
    ent2 = tk.Entry(window1, font="arial 14")
    ent2.place(x=20, y=130)
    lb3 = tk.Label(window1, text="Polinom Derecesi", font="5", fg="black")
    lb3.place(x=20, y=180)
    ent3 = tk.Entry(window1, font="arial 14")
    ent3.place(x=20, y=210)
    def values():
        global value1, value2
        value1 = str(ent1.get())
        value2 = str(ent2.get())
        value3 = int(ent3.get())
        X = np.array(datas[value2]).reshape(-1, 1) 
        y = np.array(datas[value1]).reshape(-1, 1) 

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=80)
        poli_reg = PolynomialFeatures(degree = value3) 
        transform_poli = poli_reg.fit_transform(X_train) 
        dogrusal_reg = LinearRegression() 
        dogrusal_reg.fit(transform_poli,y_train)
        poli_tahmin = dogrusal_reg.predict(transform_poli)
        r2 = r2_score(poli_tahmin, y_train)
        lb4 = tk.Label(window1, text=f"Regrasyon Scoru : {r2}", font="10", fg="black", bg="white")
        lb4.place(x=20, y=240)
        plt.scatter(X_train, y_train) 
        sort_axis = operator.itemgetter(0) 
        sorted_zip = sorted(zip(X_train,poli_tahmin), key=sort_axis)
        X_train, poli_tahmin = zip(*sorted_zip)
        plt.plot(X_train, poli_tahmin, color='r', label = 'Polinom Regresyon')
        plt.xlabel('heta') 
        plt.ylabel('Sıcaklık') 
        plt.legend()
        plt.show()
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()
    
def coklu():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+900+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Bağımlı Değişken", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    lb2 = tk.Label(window1, text="Bağımsız Değişkenler(ex:['dsg1', 'sdb2'])", font="5", fg="black")
    lb2.place(x=20, y=100)
    ent2 = tk.Entry(window1, font="arial 14")
    ent2.place(x=20, y=130)
    def values():
        global value1, value2
        value1 = str(ent1.get())
        value2 = ent2.get()
        X = datas[value2].values 
        y = datas[value1].values   

        X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=42) 
        coklu_regresyon = LinearRegression()
        coklu_regresyon.fit(X_train, y_train)
        y_pred = coklu_regresyon.predict(X_test)
        scorem = coklu_regresyon.score(X_test, y_test)
        lb3 = tk.Label(window1, text=f"Regrasyon Scoru : {round(scorem, 2)}", font="10", fg="black", bg="white")
        lb3.place(x=20, y=200)
        plt.plot(y_test, label='gerçek')
        plt.plot(y_pred, label='tahmin')
        plt.legend()
        plt.show()
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()
    
def svm():
    pass
def svr():
    data()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x300+900+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Bağımlı Değişken", font="5", fg="black")
    lb1.place(x=20, y=20)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=20, y=50)
    lb2 = tk.Label(window1, text="Bağımsız Değişken", font="5", fg="black")
    lb2.place(x=20, y=100)
    ent2 = tk.Entry(window1, font="arial 14")
    ent2.place(x=20, y=130)
    def values():
        global value1, value2
        value1 = str(ent1.get())
        value2 = str(ent2.get())
        X = np.array(datas[value2]).reshape(-1, 1)
        y = np.array(datas[value1]).reshape(-1, 1)
        sc_X = StandardScaler()
        sc_y = StandardScaler()
        X = sc_X.fit_transform(X)
        y = sc_y.fit_transform(y)
        regressor = SVR(kernel ="rbf")
        regressor.fit(X,y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        scorem = regressor.score(X_test, y_test) # Sayısal hali
        lb3 = tk.Label(window1, text=f"Regrasyon Scoru : {round(scorem, 2)}", font="10", fg="black", bg="white")
        lb3.place(x=20, y=200)
        plt.scatter(X_test,y_test, color="red")
        plt.plot(X_test, regressor.predict(X_test), color="blue")
        plt.title("SVR")
        plt.xlabel("Pozisyon")
        plt.ylabel("Maaş")
        plt.show()
        window1.destroy()
    bt1 = tk.Button(window1, text="Uygula", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=300, y=20)  
    window1.mainloop()
    
    
