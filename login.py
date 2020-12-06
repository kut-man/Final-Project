from tkinter import *
from random import choice
import os


class LoginWindow:
    def login_success(self):
        self.login_win = Toplevel()
        self.login_win.iconbitmap("b.ico")
        self.login_win.title("Student Information")
        self.login_win.geometry("1465x800")
        self.login_win.configure(bg="#a1c4cc")
        self.photo2 = PhotoImage(file="0.png")
        self.photo = Label(self.login_win, image=self.photo2)
        self.photo.grid()


p1 = LoginWindow()


def register_user():
    global username
    global password
    global username_entry
    global password_entry
    global register_win

    register_win = Toplevel(root)
    register_win.title("Sign Up")
    register_win.geometry("265x400+866+100")
    register_win.resizable(False, False)
    register_win.iconbitmap("b.ico")
    register_win.configure(bg="#a1c4cc")
    Label(register_win, text="Sign Up", font=("Arial Rounded MT bold", 15),
          bg="#3285a8").place(x=10, y=10)
    Label(register_win, text="Want to sign up fill out this form!",
          font=("arial cyr", 9), fg="#918d8d",
          bg="#a1c4cc").place(x=10, y=40)
    Label(register_win, text="___________________________________"
                             "____________________",
          fg="#918d8d", bg="#a1c4cc").place(x=-5, y=60)
    Label(register_win, text="Student Number", bg="#3285a8",
          font=("arial", 9)).place(x=20, y=100)
    username_entry = Entry(register_win, width=15, font=("arial", 20),
                           relief="solid", bg="#999966")
    username_entry.place(x=20, y=123)
    Label(register_win, text="Password", bg="#3285a8",
          font=("arial", 9)).place(x=20, y=180)
    password_entry = Entry(register_win, width=15, font=("arial", 20),
                           relief="solid", bg="#999966")
    password_entry.place(x=20, y=203)
    Button(register_win, text="Sign Up", command=register_file, padx=34,
           pady=5, bg="#52dfff", activebackground="#a1c4cc").place(x=20, y=290)
    Button(register_win, text="Generate Password", command=generate, pady=5,
           bg="#52dfff", activebackground="#a1c4cc").place(x=137, y=290)
    Label(register_win, text="I accept the terms of use", bg="#a1c4cc",
          font=("arial", 9)).place(x=40, y=250)
    var = StringVar()
    Checkbutton(register_win, variable=var, bg="#a1c4cc",
                activebackground="#a1c4cc").place(x=15, y=249)


def register_file():
    username_info = username_entry.get()
    password_info = password_entry.get()
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    chek = 0
    for k in range(len(alphabet)):
        if alphabet[k] in username_info.upper():
            chek = chek + 1
    if username_info == "" or password_info == "":
        empty = Label(register_win, text="Empty blanc!", fg="green",
                      font=("verdana", 11))
        empty.place(x=80, y=330)
        register_win.after(1000, empty.destroy)
    elif len(username_info) > 9 or len(username_info) < 9:
        len_error = Label(register_win, fg="green", font=("verdana", 11),
                          text="Length of Student Number \n should be 9",)
        len_error.place(x=30, y=330)
        register_win.after(1000, len_error.destroy)

    elif len(password_info) > 15:
        len_error1 = Label(register_win, text="Too long password", fg="green",
                           font=("verdana", 11))
        len_error1.place(x=55, y=330)
        register_win.after(1000, len_error1.destroy)
    elif chek > 0:
        type_error = Label(register_win, fg="green", font=("verdana", 11),
                           text="Use only numbers \n in username!")
        type_error.place(x=55, y=330)
        register_win.after(1000, type_error.destroy)
    else:
        try:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()
        except FileNotFoundError:
            pass
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(register_win, text="Successfully Registered", fg="green",
              font=("verdana", 11)).place(x=43, y=330)
        register_win.after(1000, lambda: register_win.destroy())


def login_verify():
    global login_entry_main
    global password_entry_main
    username1 = login_entry_main.get()
    password1 = password_entry_main.get()
    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            LoginWindow.login_success(p1)

        else:
            error_label1 = Label(root, text="Login or Password is incorrect."
                                            "\n Try again!", bg="#3285a8",
                                 fg="white", font=("permanent marker", 10))
            error_label1.place(x=30, y=475)
            root.after(1000, error_label1.destroy)
    elif username1 == "":
        error_label2 = Label(root, text="Student number is empty", fg="white",
                             bg="#3285a8", font=("permanent marker", 12))
        error_label2.place(x=35, y=475)
        root.after(1000, error_label2.destroy)
    elif password1 == "":
        error_label3 = Label(root, text="Password is empty", fg="white",
                             bg="#3285a8", font=("permanent marker", 12))
        error_label3.place(x=60, y=475)
        root.after(1000, error_label3.destroy)
    else:
        error_label5 = Label(root, text="Login or Password is incorrect."
                                        "\n Try again!", fg="white",
                             bg="#3285a8", font=("permanent marker", 10))
        error_label5.place(x=30, y=475)
        root.after(1000, error_label5.destroy)


def toggle_password():
    if password_entry_main.cget('show') == '':
        password_entry_main.config(show='*')
        show_btn.config(image=eye_photo2)
    else:
        password_entry_main.config(show='')
        show_btn.config(image=eye_photo)


def low():
    password_entry.delete(0, END)

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    paswrd = ""

    for i in range(0, 10):
        paswrd = paswrd + choice(upper)
    return paswrd


def generate():
    password1 = low()
    password_entry.insert(0, password1)


root = Tk()
root.resizable(False, False)
root.title("Sign In")
root.geometry("265x520+600+100")
root.iconbitmap("b.ico")
root.configure(bg="#3285a8")

photo2 = PhotoImage(file="b.png")
photo = Label(root, image=photo2, bg="#999966")
eye_photo = PhotoImage(file=r"D:\Final-Project\p.png")
eye_photo2 = PhotoImage(file=r"D:\Final-Project\rsz_3o.png")

sign_in_lbl = Label(root, text="Sign In", bg="#3285a8",
                    font=("bungee inline", 20))

login_entry_main = Entry(root, borderwidth=4, relief="solid", bg="#393f40",
                         width=16, font=("cabin sketch", 15), fg="white")
password_entry_main = Entry(root, borderwidth=4, relief="solid", bg="#393f40",
                            width=16, font=("cabin sketch", 15), fg="white")

login_btn = Button(root, text="Login", font=("doppio one", 15),
                   command=login_verify, bg="#677882",
                   activebackground="#31484f", padx=27)
register_btn = Button(root, text="Register", font=("doppio one", 15),
                      command=register_user, bg="#677882",
                      activebackground="#31484f", padx=8)
show_btn = Button(root, text="👁", image=eye_photo, bg="#586466",
                  activebackground="#31484f", command=toggle_password)

AlaToo_lbl = Label(root, text="Ala-Too International University 2020",
                   font=("Dubai Medium", 10), bg="#3285a8")

photo.grid()
sign_in_lbl.grid()
login_entry_main.place(x=16, y=320)
login_entry_main.insert(0, "Student Number")
login_entry_main.bind("<FocusIn>",
                      lambda args: login_entry_main.delete('0', 'end'))
password_entry_main.place(x=16, y=360)
password_entry_main.insert(0, "Password")
password_entry_main.bind("<FocusIn>",
                         lambda args: password_entry_main.delete('0', 'end'))
login_btn.place(x=15, y=400)
register_btn.place(x=140, y=400)
show_btn.place(x=221, y=364)

AlaToo_lbl.place(x=30, y=450)

root.mainloop()
