from tkinter import *
import os


def login_success():
    root.deiconify()
    root.destroy()


def register_user():
    global username
    global password
    global username_entry
    global password_entry
    global screen1

    screen1 = Toplevel(root)
    screen1.title("Register")
    screen1.geometry("265x172+866+100")
    screen1.resizable(False, False)
    screen1.iconbitmap("b.ico")
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Button(screen1, text="Register", width=10, height=1,
           command=register_file).pack()


def register_file():
    username_info = username.get()
    password_info = password.get()
    try:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    except FileNotFoundError:
        pass
    if username_info == "" or password_info == "":
        empty = Label(screen1, text="Empty blanc", fg="green",
                      font=("verdana", 11))
        empty.pack()
        screen1.after(1000, empty.destroy)
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green",
              font=("verdana", 11)).pack()
        screen1.after(1000, lambda: screen1.destroy())


def login_verify():

    username1 = login_entry.get()
    password1 = password_entry.get()

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            myLabel = Label(root, text="Login or Password is incorrect",
                            fg="green", font=("verdana", 11)).pack()
            myLabel.pack()
            root.after(1000, myLabel.destroy)
    elif username1 == "":
        mylbl = Label(root, text="Student number is empty", fg="green",
                      font=("verdana", 11))
        mylbl.pack()
        root.after(1000, mylbl.destroy)
    elif password1 == "":
        mylbl1 = Label(root, text="Password is empty", fg="green",
                       font=("verdana", 11))
        mylbl1.pack()
        root.after(1000, mylbl1.destroy)
    else:
        myLabel1 = Label(root, text="Login or Password is incorrect",
                         fg="green", font=("verdana", 11))
        myLabel1.pack()
        root.after(1000, myLabel1.destroy)


root = Tk()
root.resizable(False, False)
root.title("LOGIN SCREEN")
root.geometry("265x439+600+100")
root.iconbitmap("b.ico")
root.configure(bg="white")
photo2 = PhotoImage(file="b.png")
photo = Label(root, image=photo2, bg="#999966")
username_lbl = Label(root, text="Student number:", font=("Helvetica", 10))
login_entry = Entry(root)
password_lbl = Label(root, text="Password:", font=("Helvetica", 10))
password_entry = Entry(root, show="*")
login_btn = Button(root, text="Login", command=login_verify)
register_btn = Button(root, text="Register", command=register_user)
AlaToo_lbl = Label(root, text="Ala-Too International University 2020",
                   font=("Arial", 9))

photo.pack()
username_lbl.pack()
login_entry.pack()
password_lbl.pack()
password_entry.pack()
login_btn.pack(ipadx=42)
register_btn.pack(ipadx=36)

AlaToo_lbl.pack(side=BOTTOM)

root.mainloop()
