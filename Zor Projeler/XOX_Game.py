"""
Bu projede bir XOX oyunu yapılmıştır. Bilgisayar ile karşılıklı oynayabileceğiniz zevkli bir oyundur.

"""


oyun_tahtasi = [' ' for x in range(10)]

def ekran_goster():
    print(' ' + oyun_tahtasi[1] + ' ' + '|' + ' ' + oyun_tahtasi[2] + ' ' + '|' + ' ' + oyun_tahtasi[3])
    print("----------------")
    print(' ' + oyun_tahtasi[4] + ' ' + '|' + ' ' + oyun_tahtasi[5] + ' ' + '|' + ' ' + oyun_tahtasi[6])
    print("----------------")
    print(' ' + oyun_tahtasi[7] + ' ' + '|' + ' ' + oyun_tahtasi[8] + ' ' + '|' + ' ' + oyun_tahtasi[9])
    
def harf_koy(harf, konum):
    oyun_tahtasi[konum] = harf
    
def alan_bosmu(konum):
    return(oyun_tahtasi[konum] == ' ')

def tahta_dolu():
    if(oyun_tahtasi.count(' ')>1):
        return(False)
    else:
        return(True)
    
def kazanan(oyuntahtasi, harf):
    
    return(oyun_tahtasi[1] == harf and oyun_tahtasi[2] == harf and oyun_tahtasi[3] == harf and oyun_tahtasi[4] == harf and oyun_tahtasi[5] == harf and oyun_tahtasi[6] == harf and oyun_tahtasi[7] == harf and oyun_tahtasi[8] == harf and oyun_tahtasi[9] == harf and oyun_tahtasi[1] == harf and oyun_tahtasi[4] == harf and oyun_tahtasi[7] == harf and oyun_tahtasi[2] == harf and oyun_tahtasi[5] == harf and oyun_tahtasi[8] == harf and oyun_tahtasi[3] == harf and oyun_tahtasi[6] == harf and oyun_tahtasi[9] == harf and oyun_tahtasi[1] == harf and oyun_tahtasi[5] == harf and oyun_tahtasi[9] == harf and oyun_tahtasi[3] == harf and oyun_tahtasi[5] == harf and oyun_tahtasi[7] == harf)
    
def oyuncu_hareketi():
    konum = int(input("1-9 arasında bir konum giriniz:"))
    if(alan_bosmu(konum)):
        harf_koy('X', konum)
        if(kazanan(oyun_tahtasi, 'X')):
            ekran_goster()
            print("Tebrikler Kazandınız")
            exit()
            
        ekran_goster()
    else:
        print("Girdiğiniz Konum Dolu, Tekrar Konum Giriniz")
        oyuncu_hareketi()
        
def bilgisayar_hareket():
    import random
    musait_konumlar = [konum for konum, harf in enumerate(oyun_tahtasi) if harf == ' ' and konum != 0]
    
    
    hareket = 0
    
    for harf in ['O','X']:
        for i in musait_konumlar:
            kopya_tahta = oyun_tahtasi[:]
            kopya_tahta[i] = harf
            if kazanan(kopya_tahta, harf):
                hareket = i
                return(hareket)
    koseler = []
    for i in musait_konumlar:
        if i in[1,3,7,9]:
            koseler.append(i)
            
    if(len(koseler)>0):
        hareket = random.choice(koseler)
        return(hareket)
    
    if(len(koseler)>0):
        hareket = random.choice(koseler)
        return(hareket)
    
    if 5 in musait_konumlar:
        hareket = 5
        return(hareket)
    
    icerisi = []
    
    for i in musait_konumlar:
        if i in[2,4,6,8]:
            icerisi.append(i)
            
            
    if len(icerisi)>0:
        hareket = random.choice(icerisi)
        return(hareket)
    

def oyun():
    print("XOX Oyununa Hoşgeldin")
    ekran_goster()
    
    while not tahta_dolu():
        oyuncu_hareketi()
        if tahta_dolu():
            print("Oyun Berabere Bitti, Kazanan Yok!")
            exit()
            
        print("---------------------------------")
        bilgisayarhareket = bilgisayar_hareket()
        harf_koy('O', bilgisayarhareket)
        if kazanan(oyun_tahtasi, 'O'):
            ekran_goster()
            print("Bilgisayar Kazandı, Tekrardan Denemeye Hazırmısın!!")
            exit()
        
        ekran_goster()
        if(tahta_dolu()):
            print("Oyun Berabere Bitti, Kazanan Yok")
            exit()
        print("-----------------------------------")
            
oyun()
    