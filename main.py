import tkinter
from tkinter import *
from PIL import ImageTk, Image
import time
import requests
from tkcalendar import *


root = Tk()
# root.configure(bg="White")
root.geometry("1280x720")
root.title("DAV Login")
root.resizable(width=False, height=True)
root.iconbitmap("LOGO.ico")
# title frame
frame1 = LabelFrame(root, bg="Red")
frame1.pack()
# teacher frame
teachFrame = Frame(root, bg="White")
teachFrame.pack(fill='both')
teachFrame.pack_forget()
# student frame
studentFrame = Frame(root, bg="White")
studentFrame.pack(fill='both')
studentFrame.pack_forget()
# login frame
loginFrame = LabelFrame(root, bg="White", width="18", labelanchor="n")
loginFrame.pack(pady=200, ipadx=10, ipady=10)

# Title image
img = ImageTk.PhotoImage(Image.open("LOGO.png"))
my_img_lbl = Label(frame1, image=img, bg="Red")
my_img_lbl.grid(row=0, column=1)
# Title
title = Label(frame1, text="D.A.V International School, Kharghar", font=("Times New Roman", 30, 'bold'), fg="White", width=38, bg="Red")
title.grid(row=0, column=2)
# clock
label = Label(frame1, font=("Times New Roman", 30, 'bold'), bd=30, fg="White", bg="Red")
label.grid(row=0, column=3)


def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()
# clock end
# Login part
userid = Label(loginFrame, text="Login ID:", width=20, font=("Times New Roman", 10, 'bold'), fg="Black", bg="White")
userid.grid(row=2, column=1, pady=(20, 10))


def clear_login_insert(var):
    user.delete(0, tkinter.END)


def clear_pass_insert(var):
    password.delete(0, tkinter.END)


def studentlog():
    global logine
    logine = "student"


def teacherlog():
    global logine
    logine = "teacher"


def login():
    resp = requests.post('https://cs-project-database-connection.herokuapp.com/login/' + logine + '/' + user.get() + '/' + password.get()).text
    if resp == "Success":
        loginFrame.pack_forget()
        if logine == "teacher":
            teachFrame.pack()
        elif logine == "student":
            studentFrame.pack()
    elif resp == "Email or password Not Found":
        respon = Label(loginFrame, text="User or password Not Found", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)
    elif resp == "User not found, Please enter a valid user":
        respon = Label(loginFrame, text="User not found, Please enter a valid user", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)
    elif resp == "Incorrect Password":
        respon = Label(loginFrame, text="Incorrect Password", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)
    else:
        respon = Label(loginFrame, text="Backend Error", bg="White", width=30, fg="Red")
        respon.grid(row=1, column=1, columnspan=2)


r = IntVar()
sel_stud = Radiobutton(loginFrame, text="Student Login", variable=r, bg="White", value=1, command=studentlog)
sel_stud.grid(row=0, column=1)
sel_teach = Radiobutton(loginFrame, text="Teacher Login", variable=r, bg="White", value=2, command=teacherlog)
sel_teach.grid(row=0, column=2)


user = Entry(loginFrame, width=40, font=("Times New Roman", 10, 'bold'))
user.insert(0, "Enter your user ID / Email ID")
user.grid(row=2, column=2, pady=(20, 10))
user.bind("<Button-1>", clear_login_insert)

passtxt= Label(loginFrame, text="Password", width=20, font=("Times New Roman", 10, 'bold'), fg="Black", bg="White")
passtxt.grid(row=3, column=1, pady=(10, 10))
password = Entry(loginFrame, width=40, font=("Times New Roman", 10, 'bold'), show="*")
password.grid(row=3, column=2)
password.insert(0, "Enter Password")
password.bind("<Button-1>", clear_pass_insert)


login_button = Button(loginFrame, text="Login", command=login, fg="Red", bg="white")
login_button.grid(row=4, column=1, columnspan=2, pady=(10, 20))


root.mainloop()
