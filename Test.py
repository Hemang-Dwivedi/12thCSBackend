import pyautogui as p
import time
import webbrowser as we
from tkinter import messagebox
import tkinter as tk
import requests

print("Program status :", end=' ')
start = time.time()
try:
    req = requests.get('https://web.whatsapp.com/')
    end = time.time()
    print("Successful")
    tyme = end - start
    if (tyme >= 3):
        messagebox.showwarning("Warning!", "Net is slow, the message may not be delivered.")
except:
    errmsg = "PLEASE CHECK INTERNET CONNECTION!"
    print("ERROR")
    print(errmsg)
    messagebox.showerror("ERROR", errmsg)
    exit()


def break_it():
    exit()


def send_message():
    s = int(e3.get())
    c = int(e4.get())
    x = e1.get()
    y = e2.get()
    msg = "The message '%s' will be sent to '%s' at %s:%s" % (y, x, s, c)
    print(msg)
    messagebox.showinfo("SeWaMe", msg)
    q = s
    if (s == 00):
        q = 24
    if (c == 00):
        c = 60
        s = q - 1
    while True:
        l = time.localtime()
        if (l.tm_hour == s) & (l.tm_min == (c - 1)):
            we.open('https://web.whatsapp.com/send?phone=' + x + '&text=' + y)
            time.sleep(60)
            p.press('enter')
            master.mainloop()


master = tk.Tk()
master.title("SeWaMe")
master.geometry("290x150")
tk.Label(master, text="Receiver's name : ").grid(row=0)
tk.Label(master, text="Message : ").grid(row=1)
tk.Label(master, text="Hour : ").grid(row=2, column=0)
tk.Label(master, text="Minutes : ").grid(row=3, column=0)

e1 = tk.Entry(master)
e2 = tk.Entry(master, width=30)
e3 = tk.Spinbox(master, from_=00, to=23, width=5)
e4 = tk.Spinbox(master, from_=00, to=59, width=5)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

tk.Button(master, text='Cancel', command=break_it).grid(row=4, column=0)  # ,sticky=tk.W,pady=4)
tk.Button(master, text='SEND MESSAGE', command=send_message).grid(row=4, column=1)  # ,sticky=tk.W,pady=1)
master.mainloop()
