"""
Bu projede sıklıkla merak ettiğiniz bilgisayarınız hakkında bilgilere(ram, hafıza, işlemci vb.) hızlı bir şekilde arayüz kullanılarak ulaşmamızı sağlamaktadır.
"""
from __future__ import print_function
import sys
import psutil
import os
import platform
import tkinter as tk
import threading



# İşlemci bilgisi
def processor_view():
  window1 = tk.Tk()
  window1.geometry("300x100+10+590")
  window1.resizable(False, False)
  window1.title("Processor Information")
  window1.configure(bg="#363636")
  processor_info = platform.processor().split()
  
  lb1 = tk.Label(window1, text=f"İşlemci : {processor_info[0]} {processor_info[1]} {processor_info[2]} {processor_info[3]} {processor_info[4]}              \n{processor_info[5]} {processor_info[6]} {processor_info[7]}", font="arial 12 bold", fg="white", bg="#363636")
  lb1.place(x=10, y=10)
  lb2 = tk.Label(window1, text=f"Sistem : {os.name}", font="arial 12 bold", fg="white", bg="#363636")
  lb2.place(x=10, y=70)
  window1.mainloop()


# Ram bilgisi
def bytes1(n):
  symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
  prefix = {}
  for i, s in enumerate(symbols):
      prefix[s] = 1 << (i + 1) * 10
  for s in reversed(symbols):
      if n >= prefix[s]:
          value = float(n) / prefix[s]
          return '%.1f%s' % (value, s)
  return "%sB" % n
def pprint_ntuple(nt):
  global my_list1
  my_list1 = list()
  for name in nt._fields:
      value = getattr(nt, name)
      if name != 'percent':
          value = bytes1(value)
      my_list1.append('%-10s : %7s' % (name.capitalize(), value))

def processor():
  window2 = tk.Tk()
  window2.geometry("300x300+10+10")
  window2.resizable(False, False)
  window2.title("Ram Information")
  window2.configure(bg="#363636")
  pprint_ntuple(psutil.virtual_memory())
  lb1 = tk.Label(window2, text=f"MEMORY : {my_list1[0]}B\t      \n{my_list1[1]}B \n{my_list1[2]}% \n{my_list1[3]}B \n{my_list1[4]}B", font="arial 12 bold", fg="white", bg="#363636")
  lb1.place(x=10, y=10)
  
  pprint_ntuple(psutil.swap_memory())
  lb2 = tk.Label(window2, text=f"SWAP : {my_list1[0]}Hz\t            \n{my_list1[1]}Hz  \n{my_list1[2]}Hz   \n{my_list1[3]}%\n{my_list1[4]}\n{my_list1[5]}", font="arial 12 bold", fg="white", bg="#363636")
  lb2.place(x=10, y=140)
  window2.mainloop()


# Hafıza bilgisi
def ram():
  
  window3 = tk.Tk()
  window3.geometry("300x200+10+350")
  window3.resizable(False, False)
  window3.title("Disk Information")
  window3.configure(bg="#363636")

  for part in psutil.disk_partitions(all=False):
      if os.name == 'nt':
          if 'cdrom' in part.opts or part.fstype == '':
              continue
      usage = psutil.disk_usage(part.mountpoint)
      lb1 = tk.Label(window3, text=f"Device : {part.device}   \nTotal : {bytes1(usage.total)}B \nUsed : {bytes1(usage.used)}B\nFree : {bytes1(usage.free)}B\nType : {part.fstype}\nMount : {part.mountpoint}", font="arial 12 bold", fg="white", bg="#363636")
      lb1.place(x=10, y=10)
  window3.mainloop()


# Batarya bilgisi
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    tt, hh = divmod(hh, 60)
    return "%d:%2d:%2d" % (hh, mm, ss)
  
def battery():
  window4 = tk.Tk()
  window4.geometry("300x160+350+10")
  window4.resizable(False, False)
  window4.title("Battery information")
  window4.configure(bg="#363636")
  
  if not hasattr(psutil, "sensors_battery"):
    return sys.exit("platform not supported")
  batt = psutil.sensors_battery()
  if batt is None:
    return sys.exit("no battery is installed")

  if batt.power_plugged:
    lb1 = tk.Label(window4, text=f"CHARGE : {round(batt.percent, 2)}                   \n\nSTATUS : {('It s charging' if batt.percent < 100 else 'battery full')}\n\nPLUGG IN : Yes\t      ", font="arial 12 bold", fg="white", bg="#363636")
    lb1.place(x=10, y=10)
  else:
    lb1 = tk.Label(window4, text=f" CHARGE : {round(batt.percent, 2)}\t\t\n\nREMAINING TIME : {secs2hours(batt.secsleft)}\n\nSTATUS : It's not charging\n\nPLUGG IN : No\t             ", font="arial 12 bold", fg="white", bg="#363636")
    lb1.place(x=10, y=10)
  window4.mainloop()


# Thread'lerin aynı anda çalışmasını sağlamak için
def start_threads():
    thread1 = threading.Thread(target=processor_view)
    thread2 = threading.Thread(target=processor)
    thread3 = threading.Thread(target=ram)
    thread4 = threading.Thread(target=battery)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

# Tüm pencerelerin aynı anda açılması için
start_threads()
