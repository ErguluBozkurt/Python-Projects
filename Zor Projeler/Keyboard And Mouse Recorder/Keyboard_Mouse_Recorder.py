"""
Aşağıda yer alan kodu çalıştırdığınızda bilgisayar ekranın da hangi tuşlamaları hangi maus hareketlerini 
yapıyorsanız kayıt altına alır ve istediğinizde bu kaydı kullanarak bilgisayarın sizinle aynı işlemleri
yapmasını sağlayabilirsiniz. Dosya yolunun uygun şekilde değiştirilmesi gerektiğini unutmayın.
"""
# Kütüphaneler eklendi
from pynput import mouse, keyboard
import time
import json
import pyautogui
import pyperclip

mouse_listener = None
start_time = None
last_coordinate = [0,0]
threshold = 200 # maus hassasiyeti 
up_to_now = 0
events = []

# Kayıt
def record():
    
    def save_json():
        with open("kayit.json","w") as event:
            json.dump(events,event, indent=4)

    ######### Klavye #######
    def on_press(key):
        try:
            save_event(current_time=round(time.time(),2), action=0, key = key.char)
            print(f"Alphanumerik rakam {key.char}")
            
        except:
            save_event(current_time=round(time.time(),2), action=0, key = str(key))
            print(f"Alphanumerik rakam {key}")
            
            
    def on_release(key):
        try:
            print(f"{key} Serbest bırakıldı")
            if(key == keyboard.Key.esc): # ESC bastığında kayıt durur
                print(time.time()-start_time)
                mouse_listener.stop()
                save_json()
                print("Maus ve klavye durduruldu")
                return False
            save_event(current_time=round(time.time(),2), action=1, key = key.char)
        except:
            save_event(current_time=round(time.time(),2), action=1, key = str(key))
            
    ########################

    ######### Maus #########

    def on_move(x,y):
        save_event(current_time=round(time.time(),2), action=2, coordinate = [x,y])
        print(f"Maus hareketi {(x,y)}")

    def on_click(x, y, button, pressed):
        if(pressed):
            save_event(current_time=round(time.time(),2), action=3, coordinate = [x,y])
            print('{0} {1}'.format('Tıklandı' if pressed else 'Serpest bıraktı',(x, y)))
            
    def on_scroll(x, y, dx, dy):
        save_event(current_time=round(time.time(),2), action=4, coordinate=[x,y], direction = ('Aşağı' if dy < 0 else 'Yukarı'))
        print('Kaydırıldı {0} at {1}'.format('Aşağı' if dy < 0 else 'Yukarı',(x, y)))

    ########################

    class ActionTypes():
        KEYPRESS = 0
        KEYRELEASE = 1
        MOUSEMOVE = 2
        MOUSECLICK = 3
        MOUSESCROLL = 4
        
    ######### Kayıt Dosyası #########
    def save_event(current_time, action, key='', coordinate=[], direction = 'up'):
        global up_to_now
        elapsed_time = current_time-start_time
        theduration = round(elapsed_time - up_to_now, 2)
        if action == ActionTypes.KEYPRESS:
            info = {
                'time': theduration,
                'action': ActionTypes.KEYPRESS,
                'key': key
            }
        elif action == ActionTypes.KEYRELEASE:
            info = {
                'time': theduration,
                'action': ActionTypes.KEYRELEASE,
                'key': key
            }
        elif action == ActionTypes.MOUSEMOVE:
            global last_coordinate
            if abs(coordinate[0] - last_coordinate[0]) > threshold or abs(coordinate[1] - last_coordinate[1]) > threshold:
                info = {
                    'time': 0,
                    'action': ActionTypes.MOUSEMOVE,
                    'coordinate': coordinate
                }
                last_coordinate = coordinate
                events.append(info)
            return
        elif action == ActionTypes.MOUSECLICK:
            info = {
                'time': theduration,
                'action': ActionTypes.MOUSECLICK,
                'coordinate': coordinate
            }
        elif action == ActionTypes.MOUSESCROLL:
            info = {
                'time': theduration,
                'action': ActionTypes.MOUSESCROLL,
                'coordinate': coordinate,
                'direction': direction
            }
        up_to_now = elapsed_time
        events.append(info)
    ##########################

    ######### Maus Hassasiyet Ayarı #############
    def settingUpMouseSensitive():
        global threshold
        while True:
            response = input('Maus hassasiyeti 200 de değiştirmek ister misin?\n(Dikkat:Hassasiyet Arttıkça Daha Yavaş Çalışır)\nCevap(y/n):').lower()
            if response == 'y':
                try:
                    sensitive = int(input('Hassasiyet Girin (0-300):'))
                    if 0 <= sensitive <= 300:
                        threshold = sensitive
                        print(f'Hassasiyet Değişti. ({sensitive})')
                        break
                    else:
                        print('Lütfen Seçili Aralıkda Bir Değer Girin.')
                except:
                    print('Lütfen Seçili Aralıkda Bir Değer Girin.')
            elif response == 'n':
                print(f'Hassasiyet {threshold}')
                break
    #########################################
    
    ############# Kayıt Başlat ################
    def run():
        global start_time
        settingUpMouseSensitive()
        print("Kaydı Durdurmak için ESC'ye Basınız")
        input('Kaydı Başlatmak İçin Enter a Basınız...')
        for x in range(4, -1, -1):
            print(x+1)
            time.sleep(1)
        print('Kaydediliyor...')
        start_time = round(time.time(),2)
        print(f"Başlama Zamanı: {start_time}")

        events.append({'time': 0, 'action': 'Recording Started'})
        global mouse_listener

        
        keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

        keyboard_listener.start()
        mouse_listener.start()

        keyboard_listener.join()
        mouse_listener.join()

        print(events)

    if __name__ == '__main__':
        run()

    ###################################
    


def move():

    CHANGE_LETTERS = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'caps_lock': 'capslock',
        'media_volume_down': 'volumedown',
        'media_volume_up': 'volumeup',
        'print_screen': 'printscreen',
        'num_lock': 'numlock',
        'scroll_lock': 'scrolllock'
    }

    UTF_CHARACTERS = ['ç','ı', 'ö', 'ş', 'ğ', 'ü', '@', 'İ']

    def ConvertToProperKeys(key):

        properKey = key.replace('Key.', '')

        if properKey in CHANGE_LETTERS.keys():
            return CHANGE_LETTERS[properKey]
        elif properKey in UTF_CHARACTERS:
            pyperclip.copy(properKey)
            pyautogui.hotkey('ctrl', 'v')
            return ''

        return properKey


    def load_json():
        global events
        with open('kayit.json', 'r') as event:
            events = json.load(event)

    def play():
        global SCROLL_SENSITIVE
        for x, y in enumerate(events[1:]):
            p = y['time'] -0.1 
            time.sleep(p if p > 0 else 0)
            if y['action'] == 0:
                pyautogui.keyDown(ConvertToProperKeys(y['key']))
            elif y['action'] == 1:
                pyautogui.keyUp(ConvertToProperKeys(y['key']))
            elif y['action'] == 2:
                pyautogui.moveTo(x = y['coordinate'][0], y = y['coordinate'][1])
            elif y['action'] == 3:
                pyautogui.click(x = y['coordinate'][0], y = y['coordinate'][1])
            elif y['action'] == 4:
                pyautogui.scroll(clicks=(SCROLL_SENSITIVE if y['direction'] == 'up' else -SCROLL_SENSITIVE), x = y['coordinate'][0], y = y['coordinate'][1])

    def run():
        load_json()
        print('Kayıt 5 Saniye içinde Oynatılacak')
        for x in range(4, -1, -1):
            print(x+1)
            time.sleep(1)
        play()
        pyautogui.keyUp('esc')
    if __name__ == '__main__':
        run()


while True:
    choice = input("Kayıt Başlatmak için 'kayıt' \nKaydı Oynatmak için 'oynat' \nÇıkış Yapmak için 'çıkış' Yazınız:").lower()
    if(choice=="kayıt"):
        record()
    elif(choice=="oynat"):
        events = None
        SCROLL_SENSITIVE = 110  
        move()
    elif(choice =="çıkış"):
        print("Uygulama Kapatıldı")
        break
    else:
        print("Hatalı Giriş!!, Tekrar Deneyiniz.")
        
        
