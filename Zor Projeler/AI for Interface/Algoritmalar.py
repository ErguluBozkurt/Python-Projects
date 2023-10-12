import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import seaborn as sns
import tkinter as tk
from sklearn.impute import SimpleImputer
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.svm import SVC, SVR
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.pipeline import Pipeline


def data():
    global datas
    with open("save.txt", "r") as file:
        url = file.read()
    url = str(url)
    if(url[-3:] == "csv"):
        datas = pd.read_csv(url)
    else:
        datas = pd.read_excel(url)
data()
    
def ilk():
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("1100x170+300+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.head(), font="arial 12", fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()
         
def son():
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("1100x170+300+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.tail(), font="arial 12", fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()
               
def min_max():
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("1100x200+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=datas.describe(), font="arial 12", fg="black", bg="white")
    lb1.place(x=20, y=20)
    window1.mainloop()

def infos():
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("500x270+400+70")
    window1.resizable(False,False)
    missing_values = datas.isnull().sum()
    data_types = datas.dtypes
    df = pd.DataFrame({'Sutunlar':"",
                        '   Eksik_Degerler    ': missing_values,
                        '   Veri_Tipleri      ': data_types})
    
    lb1 = tk.Label(window1, text=df.head(20), font="arial 14", fg="black", bg="white")
    lb1.place(x=5, y=5)
    window1.mainloop()
    
def ridiculous():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("400x200+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Anlamsız Veri Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    def outt():
        global datas
        datas = datas.drop([ent1.get()], axis=1)
        lb2 = tk.Label(window1, text="Çıkarıldı", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    bt1 = tk.Button(window1, text="Çıkar", font="arial 12 bold", fg="white", bg="navy", command=outt)
    bt1.place(x=150, y=120)
    window1.mainloop()
######################################################
def bar_graph():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    def circle():
        global value_list, n
        value_list.append(ent1.get())
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def bar_plot(variable):
        var = datas[variable] 
        var_value = var.value_counts() 
        plt.figure(figsize = (6,3))
        plt.bar(var_value.index, var_value)
        plt.ylabel("Frequency")
        plt.title(variable)
        plt.show()    
    
    def send():
        category = value_list 
        for i in category:
            bar_plot(i)
        
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=send)
    bt2.place(x=200, y=160)
    
    window1.mainloop()

def pie_graph(): 
    global value_list
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def pie():
        data_set = datas[ent1.get()].value_counts().reset_index()
        fig = px.pie(data_set, values="index", names=str(ent1.get()))
        fig.show()
    
    bt1 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=pie)
    bt1.place(x=150, y=100)
    
    window1.mainloop()
    
def sun_burst():
    global value_list, n
    value_list = list()
    n = 0
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı (Son Değişken Sayısal)", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    def circle():
        global value_list, n
        value_list.append(ent1.get())
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def sunburst():
        sun = datas.groupby(value_list[:-1])[value_list[-1]].count().reset_index()
        fig = px.sunburst(sun, path = [value_list[:-1]], values = value_list[-1])
        fig.show()
        
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=sunburst)
    bt2.place(x=200, y=160)
    
    window1.mainloop()
######################################################
def hist_graph():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(ent1.get())
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def plot_hist(variable):
        plt.figure(figsize=(7,3))
        plt.hist(datas[variable], bins = 30)
        plt.xlabel(variable)
        plt.ylabel("Frequency")
        plt.title(f"Graphic of {variable}")
        plt.show()
        
    def send():
        for i in value_list:
            plot_hist(i)
            
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=send)
    bt2.place(x=200, y=160)
    
    window1.mainloop()
######################################################
def grouph():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("800x350+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı ve Bağımlı Değişken", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def group_by():
        s = (datas[[value_list[0], value_list[1]]].groupby([value_list[0]]).mean().sort_values(by=value_list[1])[::-1])
        lb2 = tk.Label(window1, text=s, font="arial 12", fg="black")
        lb2.place(x=400, y=20)
        
        
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=150)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=group_by)
    bt2.place(x=200, y=150)
######################################################
def pair_plot():
    colum = datas.columns
    sns.pairplot(datas[colum[:5]])  
    plt.show() 
    sns.pairplot(datas[colum[5:]])  
    plt.show() 
    
def box_plot(): 
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def plot_box():
        sns.boxplot(data = datas.loc[:, value_list], orient = "v", palette = "Set1")
        plt.show()
             
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=plot_box)
    bt2.place(x=200, y=160)
    
    window1.mainloop()
    
def count_plot():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Kategorik Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def plot_count():
        sns.countplot(data = datas, x = str(ent1.get())) # Aynı değişkenden ne kadar veri var? 
        plt.xticks(rotation = 60) # Yazıların 60 derecelik eğimle yazılmasını sağlıyor
        plt.show()
    bt1 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=plot_count)
    bt1.place(x=100, y=160)    

    window1.mainloop()
    
def bar_plot():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı (Sayısal + Kategorik)", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def plot_bar():
        sns.barplot(x = value_list[0], y = value_list[1], data = datas, palette = "coolwarm")
        plt.show()
             
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=plot_bar)
    bt2.place(x=200, y=160)
    
    window1.mainloop()
    
def kde_plot():
    global value_list, n
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı (Sayısal + Kategorik)", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def plot_kde():
        plt.figure(figsize = (15, 8)) 
        sns.kdeplot(data = datas, x = value_list[0], hue = value_list[1], fill = True, linewidth=2)
        plt.show()
             
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=plot_kde)
    bt2.place(x=200, y=160)
    
    window1.mainloop()

######################################################
def all_corelation():
    plt.figure(figsize=(6, 6)) 
    sns.heatmap(datas.corr(), annot=True, fmt=".2f")
    plt.show() 
         
def one_corelation():
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("800x250+400+70")
    window1.resizable(False,False)
    corr_matrix = datas.corr()
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        value = str(ent1.get())
        s = corr_matrix[value].sort_values(ascending=False)
        lb2 = tk.Label(window1, text=s, font="arial 12", fg="black", bg="white")
        lb2.place(x=400, y=10)
        
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()
   
######################################################
def all_delete():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False) 
    
    datas.fillna(method="ffill", inplace=True)
    lb1 = tk.Label(window1, text="Başarılı", font="arial 12", fg="green", bg="white")
    lb1.place(x=100, y=80)
    
    window1.mainloop()
    
def categoric_mod():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False) 
    
    imp = SimpleImputer(strategy="most_frequent") 
    imp.fit_transform(datas)
    lb1 = tk.Label(window1, text="Başarılı", font="arial 12", fg="green", bg="white")
    lb1.place(x=100, y=80)
    
    window1.mainloop()

def numeric_mean():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        global datas
        value = str(ent1.get())
        datas[value] = datas[value].fillna(datas[value].mean())
        lb2 = tk.Label(window1, text="Ortalama Başarılı", font="arial 12", fg="green", bg="white")
        lb2.place(x=100, y=80)
        
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()
    
def numeric_median():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        global datas
        value = str(ent1.get())
        datas[value].fillna(datas[value].median(), inplace=True)
        lb2 = tk.Label(window1, text="Medyan Başarılı", font="arial 12", fg="green", bg="white")
        lb2.place(x=100, y=80)
        
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()

def numeric_mod():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        global datas
        value = str(ent1.get())
        datas[value].fillna(datas[value].mod(), inplace=True)
        lb2 = tk.Label(window1, text="Medyan Başarılı", font="arial 12", fg="green", bg="white")
        lb2.place(x=100, y=80)
        
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()
    
######################################################
def label_encoder(): 
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        global datas
        value = str(ent1.get())
        label_encoder = LabelEncoder()
        datas[value] = label_encoder.fit_transform(datas[value])
        lb2 = tk.Label(window1, text="Label Encoder Başarılı", font="arial 12", fg="green", bg="white")
        lb2.place(x=100, y=80)
        
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()
    
def onehot_encoder():
    global datas
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x400+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 14")
    ent1.place(x=100, y=40)
    def values():
        global datas
        value = str(ent1.get())
        datas = pd.get_dummies(datas,columns=[value]) 
        lb2 = tk.Label(window1, text="One Hot Encoder Başarılı", font="arial 12", fg="green", bg="white")
        lb2.place(x=100, y=80)
        print(datas.head())
    bt1 = tk.Button(window1, text="Tamam", font="arial 14 bold", fg="white", bg="navy", command=values)
    bt1.place(x=100, y=160)  
    
    window1.mainloop()    

######################################################
def outlier():
    global value_list, n, datas
    n = 0
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text="Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        n += 1
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
    
    def start():
        global datas
        def detect_outlier(df_, features):
            outlier_indices = []
            for i in features:
                q1 = np.percentile(df_[i], 25)
                q3 = np.percentile(df_[i], 75)
                iqr = q3 - q1
                outlier_step = iqr * 1.5
                outlier_list = df_[(df_[i] < q1 - outlier_step) | (df_[i] > q3 + outlier_step)].index
                outlier_indices.extend(outlier_list)
            return(outlier_indices)
        outliers = detect_outlier(datas, value_list)
        datas = datas.drop(outliers, axis=0).reset_index(drop=True) 

        
             
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=start)
    bt2.place(x=200, y=160)
    
    window1.mainloop()

######################################################
n = "Bağımsız"
def standart_scaler():
    global value_list, n, X, y, datas
    value_list = list()
    window1 = tk.Tk()
    window1.title("Yapay Zeka")
    window1.geometry("600x300+400+70")
    window1.resizable(False,False)
    lb1 = tk.Label(window1, text=f"{n} Değişken Adı", font="arial 12", fg="black")
    lb1.place(x=100, y=10)
    ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
    ent1.place(x=100, y=40)
    
    
    def circle():
        global value_list, n
        value_list.append(str(ent1.get()))
        lb2 = tk.Label(window1, text=f"{n}. Değişken Kaydedildi \nYeni Değişken Girebilirsiniz \nİşlem Bitiminde Tamam'a Basınız", font="arial 12", fg="green")
        lb2.place(x=100, y=80)
        n = "Bağımlı"
    
    def start():
        global X, y
        X = np.array(datas[value_list[0]]).reshape(-1,1)
        y = np.array(datas[value_list[1]]).reshape(-1,1)
        sc = StandardScaler()
        X = sc.fit_transform(X)
        y = sc.fit_transform(y)

             
    bt1 = tk.Button(window1, text="Kaydet", font="arial 12 bold", fg="white", bg="navy", command=circle)
    bt1.place(x=100, y=160)    
        
    bt2 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=start)
    bt2.place(x=200, y=160)
    
    window1.mainloop()

######################################################
def model():
    global X, y, datas, n
    if(n == "Bağımlı"):
        window1 = tk.Tk()
        window1.title("Yapay Zeka")
        window1.geometry("600x800+400+20")
        window1.resizable(False,False)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        # Modelleri ve ilgili hiperparametre aralıklarını tanımlayın
        models = [
            {
                'name': 'DecisionTreeClassifier',
                'model': DecisionTreeClassifier(),
                'params': {
                    'criterion': ['gini','entropy'],
                    "max_depth": range(1,20,2),
                }
            },
            {
                'name': 'DecisionTreeRegressor',
                'model': DecisionTreeRegressor(),
                'params': {
                    'criterion': ['mse', 'friedman_mse', 'mae', 'poisson'],
                    "max_depth": range(1,20,2),
                }
            },
            {
                'name': 'SVC',
                'model': SVC(),
                'params': {
                    "gamma": [0.001, 0.01, 0.1, 1],
                    'C': [1,10,50,100,200,300,1000],
                    'kernel': ['rbf'],
                }
            },
            {
                'name': 'SVR',
                'model': SVR(),
                'params': {
                    "gamma": [0.001, 0.01, 0.1, 1],
                    'C': [1,10,50,100,200,300,1000],
                    'kernel': ['rbf'],
                }
            },
            {
                'name': 'RandomForestClassifier',
                'model': RandomForestClassifier(),
                'params': {
                    "max_features": [1,3,10],
                    "min_samples_split":[2,3,10],
                    "min_samples_leaf":[1,3,10],
                    "bootstrap":[False],
                    'n_estimators': [100, 200, 300],
                    'criterion': ['gini','entropy'],
                }
            },
            {
                'name': 'RandomForestRegressor',
                'model': RandomForestRegressor(),
                'params': {
                    'n_estimators': [100, 200, 300],
                    'criterion': ['mse', 'friedman_mse', 'mae', 'poisson'],
                }
            },
            {
                'name': 'LogisticRegression',
                'model': LogisticRegression(),
                'params': {
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'penalty': ['l1', 'l2'],
                }
            },
            {
                'name': 'KNeighborsClassifier',
                'model': KNeighborsClassifier(),
                'params': {
                    'n_neighbors': [2,3,4,5,6,7,9,11,13,15,17,19],
                    'weights': ['uniform', 'distance'],
                    "metric":["euclidean","manhattan"]
                }
            },
            {
                'name': 'KNeighborsRegressor',
                'model': KNeighborsRegressor(),
                'params': {
                    'n_neighbors': [2,3,4,5,6,7,9,11,13,15,17,19],
                    'weights': ['uniform', 'distance'],
                }
            },
            {
                'name': 'PolynomialFeatures+LinearRegression',
                'model': Pipeline([
                    ('poly', PolynomialFeatures()),
                    ('linear', LinearRegression())
                ]),
                'params': {
                    'poly__degree': [2,3,4,5,6,7],
                }
            },
        ]

        # GridSearchCV için döngü başlatın ve en iyi sonuçları bulun
        best_models = []
        for model_info in models:
            if 'Pipeline' in model_info['name']:
                param_grid = {
                    'poly__degree': model_info['params']['poly__degree']
                }
            else:
                param_grid = model_info['params']

            grid_search = GridSearchCV(model_info['model'], param_grid, cv=5, n_jobs=-1)
            grid_search.fit(X_train, y_train)  # Eğitim verileriyle uyumlu hale getirildi
            best_models.append({
                'name': model_info['name'],
                'best_model': grid_search.best_estimator_,
                'best_params': grid_search.best_params_,
                'best_score': grid_search.best_score_
            })

        # En iyi sonuçları yazdırın
        for best_model in best_models:
            s = (f"Model: {best_model['name']} \nBest Parameters: {best_model['best_params']} \nBest Score: {round(best_model['best_score'], 2)}%")
            lb2 = tk.Label(window1, text=s, font="arial 12", fg="green")
            lb2.place(x=10, y=20)

        model_names = []
        model_scores = []
        for best_model in best_models:
            score = best_model['best_score']
            if score >= 0:
                model_names.append(best_model['name'])
                model_scores.append(score)

        plt.figure(figsize=(12, 6))
        plt.bar(model_names, model_scores, color='skyblue')
        plt.xlabel('Model Score')
        plt.title('Model Performansı')
        plt.gca().invert_yaxis()  # Model isimlerini y ekseninde
        plt.show()

        window1.mainloop()

    else:
        window1 = tk.Tk()
        window1.title("Yapay Zeka")
        window1.geometry("600x300+400+70")
        window1.resizable(False,False)
        lb1 = tk.Label(window1, text="Bağımlı Değişken Adı", font="arial 12", fg="black")
        lb1.place(x=100, y=10)
        ent1 = tk.Entry(window1, font="arial 12", fg="black", bg="white")
        ent1.place(x=100, y=40)
        
        def start():
            bound = str(ent1.get())
            lenght = len(datas)
            train = datas[:lenght]
            X = train.drop(labels = bound, axis = 1)
            y = train[bound]

            # Veriyi eğitim ve test alt kümelerine bölelim
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
            
            # Modelleri ve ilgili hiperparametre aralıklarını tanımlayın
            models = [
                {
                    'name': 'DecisionTreeClassifier',
                    'model': DecisionTreeClassifier(),
                    'params': {
                        'criterion': ['gini','entropy'],
                        "max_depth": range(1,20,2),
                    }
                },
                {
                    'name': 'DecisionTreeRegressor',
                    'model': DecisionTreeRegressor(),
                    'params': {
                        'criterion': ['mse', 'friedman_mse', 'mae', 'poisson'],
                        "max_depth": range(1,20,2),
                    }
                },
                {
                    'name': 'SVC',
                    'model': SVC(),
                    'params': {
                        "gamma": [0.001, 0.01, 0.1, 1],
                        'C': [1,10,50,100,200,300,1000],
                        'kernel': ['rbf'],
                    }
                },
                {
                    'name': 'SVR',
                    'model': SVR(),
                    'params': {
                        "gamma": [0.001, 0.01, 0.1, 1],
                        'C': [1,10,50,100,200,300,1000],
                        'kernel': ['rbf'],
                    }
                },
                {
                    'name': 'RandomForestClassifier',
                    'model': RandomForestClassifier(),
                    'params': {
                        "max_features": [1,3,10],
                        "min_samples_split":[2,3,10],
                        "min_samples_leaf":[1,3,10],
                        "bootstrap":[False],
                        'n_estimators': [100, 200, 300],
                        'criterion': ['gini','entropy'],
                    }
                },
                {
                    'name': 'RandomForestRegressor',
                    'model': RandomForestRegressor(),
                    'params': {
                        'n_estimators': [100, 200, 300],
                        'criterion': ['mse', 'friedman_mse', 'mae', 'poisson'],
                    }
                },
                {
                    'name': 'LogisticRegression',
                    'model': LogisticRegression(),
                    'params': {
                        'C': [0.001, 0.01, 0.1, 1, 10, 100],
                        'penalty': ['l1', 'l2'],
                    }
                },
                {
                    'name': 'KNeighborsClassifier',
                    'model': KNeighborsClassifier(),
                    'params': {
                        'n_neighbors': [2,3,4,5,6,7,9,11,13,15,17,19],
                        'weights': ['uniform', 'distance'],
                        "metric":["euclidean","manhattan"]
                    }
                },
                {
                    'name': 'KNeighborsRegressor',
                    'model': KNeighborsRegressor(),
                    'params': {
                        'n_neighbors': [2,3,4,5,6,7,9,11,13,15,17,19],
                        'weights': ['uniform', 'distance'],
                    }
                },
                {
                    'name': 'PolynomialFeatures+LinearRegression',
                    'model': Pipeline([
                        ('poly', PolynomialFeatures()),
                        ('linear', LinearRegression())
                    ]),
                    'params': {
                        'poly__degree': [2,3,4,5,6,7],
                    }
                },
            ]

            # GridSearchCV için döngü başlatın ve en iyi sonuçları bulun
            best_models = []
            for model_info in models:
                if 'Pipeline' in model_info['name']:
                    param_grid = {
                        'poly__degree': model_info['params']['poly__degree']
                    }
                else:
                    param_grid = model_info['params']

                grid_search = GridSearchCV(model_info['model'], param_grid, cv=5, n_jobs=-1)
                grid_search.fit(X_train, y_train)  # Eğitim verileriyle uyumlu hale getirildi
                best_models.append({
                    'name': model_info['name'],
                    'best_model': grid_search.best_estimator_,
                    'best_params': grid_search.best_params_,
                    'best_score': grid_search.best_score_
                })

            # En iyi sonuçları yazdırın
            for best_model in best_models:
                s = (f"Model: {best_model['name']} \nBest Parameters: {best_model['best_params']} \nBest Score: {round(best_model['best_score'], 2)}%")
                lb2 = tk.Label(window1, text=s, font="arial 12", fg="green")
                lb2.place(x=10, y=20)

            model_names = []
            model_scores = []
            for best_model in best_models:
                score = best_model['best_score']
                if score >= 0:
                    model_names.append(best_model['name'])
                    model_scores.append(score)

            plt.figure(figsize=(12, 6))
            plt.bar(model_names, model_scores, color='skyblue')
            plt.xlabel('Model Score')
            plt.title('Model Performansı')
            plt.gca().invert_yaxis()  # Model isimlerini y ekseninde
            plt.show()
                
        bt1 = tk.Button(window1, text="Tamam", font="arial 12 bold", fg="white", bg="navy", command=start)
        bt1.place(x=200, y=160)
        
        window1.mainloop()
        
    
        