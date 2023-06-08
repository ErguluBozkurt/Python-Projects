"""
Yaş ve Eğitims seviyesine göre ehliyet alıp alamama sonucunu elde edilir.
"""

name = input("İsim=")
age = int(input("Yaş="))
if(age>=18):
    education = input("Eğitim Seviyesi(Lise or Üniversite)=")
    if((education=="Lise") or (education=="Üniversite")):
       print(f"{name} ehliyet alabilirsin.")
    else:
       print("Uygun şartları sağlamıyorsunuz.")
else:
    print("Uygun şartları sağlamıyorsunuz.")
    
