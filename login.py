from tkinter import *
from random import choice
import os


def login_success():
    root.deiconify()
    root.destroy()


def register_user():
    global username
    global password
    global username_entry
    global password_entry
    global register_win

    register_win = Toplevel(root)
    register_win.title("Register")
    register_win.geometry("265x200+866+100")
    register_win.resizable(False, False)
    register_win.iconbitmap("b.ico")
    Label(register_win, text="Enter details below").pack()
    Label(register_win, text="").pack()
    Label(register_win, text="Username * ").pack()
    username_entry = Entry(register_win)
    username_entry.pack()
    Label(register_win, text="Password * ").pack()
    password_entry = Entry(register_win)
    password_entry.pack()
    Button(register_win, text="Register", command=register_file).pack()
    Button(register_win, text="Generate Password", command=generate).pack()


def register_file():
    username_info = username_entry.get()
    password_info = password_entry.get()
    try:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    except FileNotFoundError:
        pass
    if username_info == "" or password_info == "":
        empty = Label(register_win, text="Empty blanc!", fg="green",
                      font=("verdana", 11))
        empty.pack()
        register_win.after(1000, empty.destroy)
    elif len(username_info) > 13:
        len_error = Label(register_win, text="Too long username", fg="green",
                          font=("verdana", 11))
        len_error.pack()
        register_win.after(1000, len_error.destroy)
    elif len(password_info) > 13:
        len_error1 = Label(register_win, text="Too long password", fg="green",
                           font=("verdana", 11))
        len_error1.pack()
        register_win.after(1000, len_error1.destroy)
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(register_win, text="Successfully Registered", fg="green",
              font=("verdana", 11)).pack()
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
            login_success()

        else:
            error_label1 = Label(root, text="Login or Password is incorrect."
                                            "\n Try again!",
                                 fg="green", font=("verdana", 9))
            error_label1.place(x=30, y=445)
            root.after(1000, error_label1.destroy)
    elif username1 == "":
        error_label2 = Label(root, text="Student number is empty", fg="green",
                             font=("verdana", 11))
        error_label2.place(x=35, y=455)
        root.after(1000, error_label2.destroy)
    elif password1 == "":
        error_label3 = Label(root, text="Password is empty", fg="green",
                             font=("verdana", 11))
        error_label3.place(x=60, y=455)
        root.after(1000, error_label3.destroy)
    else:
        error_label4 = Label(root, text="Login or Password is incorrect."
                                        "\n Try again!",
                             fg="green", font=("verdana", 9))
        error_label4.place(x=30, y=455)
        root.after(1000, error_label4.destroy)


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
root.title("LOGIN SCREEN")
root.geometry("265x490+600+100")
root.iconbitmap("b.ico")
root.configure(bg="white")

photo2 = PhotoImage(file="b.png")
photo = Label(root, image=photo2, bg="#999966")
eye_photo = PhotoImage(file=r"D:\Final-Project\p.png")
eye_photo2 = PhotoImage(file=r"D:\Final-Project\rsz_3o.png")

sign_in_lbl = Label(root, text="Sign In", font=("Helvetica", 20))

password_entry_main = Entry(root, borderwidth=6)
login_entry_main = Entry(root, borderwidth=6)

login_btn = Button(root, text="Login", command=login_verify, padx=46)
register_btn = Button(root, text="Register", command=register_user, padx=40)
show_btn = Button(root, text="👁", image=eye_photo, command=toggle_password)

AlaToo_lbl = Label(root, text="Ala-Too International University 2020",
                   font=("Arial", 9))

photo.grid()
sign_in_lbl.grid()
login_entry_main.grid()
login_entry_main.insert(0, "Student Number")
login_entry_main.bind("<FocusIn>",
                      lambda args: login_entry_main.delete('0', 'end'))
password_entry_main.grid()
password_entry_main.insert(0, "Password")
password_entry_main.bind("<FocusIn>",
                         lambda args: password_entry_main.delete('0', 'end'))
login_btn.grid()
register_btn.place(x=67, y=385)
show_btn.place(x=195, y=327)

AlaToo_lbl.place(x=30, y=420)

root.mainloop()
