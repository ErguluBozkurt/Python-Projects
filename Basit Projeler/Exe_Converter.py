"""
Dosyalar aynı klasör içersinde yer alması gerekir.
setup.py adında bir python dosyası oluşturun ve içerisine aşağıdaki kodu kopyalayın.
Burada dosya_adi yazan yere exe yapmak istediğiniz dosyanın adını yazın ve aşağıdaki kodu terminal ekranında çalıştırın.
python setup.py build
"""
from cx_Freeze import setup, Executable

setup(
    name="uygulama-adi",
    version="0.1",
    description="Uygulama açıklaması",
    executables=[Executable("dosya_adi.py")],
)

