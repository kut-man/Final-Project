# Python Tutorial (Login System)

In this tutorial, we will learn how to create login system by writing some Python GUI examples using the Tkinter
package.

Tkinter package is shipped with Python as a standard package, so we don’t need to install anything to use it.

#### You need to have:

* Python 3.9.
* IDE
* Tkinter, random, os libraries
* Creativity

## Getting Started

### Designing Main Screen

First, we will import Tkinter package and create a window and set its title:

```
from tkinter import *
from random import choice
import os

root = Tk()
root.resizable(False, False)
root.title("Sign In")
root.geometry("265x520+600+100")
root.iconbitmap("b.ico")
root.configure(bg="#3285a8")


root.mainloop()
```

You can also customize the design of main screen as per your choice and make it more attractive. So let’s see the output
of this code:

![Screenshot 2020-12-09 220820](https://user-images.githubusercontent.com/73386100/101654825-22853900-3a6b-11eb-80b5-41da979ea7a3.png)

Then add some pictures:

```
photo2 = PhotoImage(file="b.png")
photo = Label(root, image=photo2, bg="#999966")

photo.grid()
```

Create Entry and Labels:

```
sign_in_lbl = Label(root, text="Sign In", bg="#3285a8",
                    font=("bungee inline", 20))

login_entry_main = Entry(root, borderwidth=4, relief="solid", bg="#393f40",
                         width=16, font=("cabin sketch", 15), fg="white")
pass_entr_main = Entry(root, borderwidth=4, relief="solid", bg="#393f40",
                       width=16, font=("cabin sketch", 15), fg="white")
laToo_lbl = Label(root, text="Ala-Too International University 2020",
                   font=("Dubai Medium", 10), bg="#3285a8")
sign_in_lbl.grid()            
login_entry_main.place(x=16, y=320)
pass_entr_main.place(x=16, y=360)
AlaToo_lbl.place(x=30, y=450)
```

The result will be like this:

![qwertyuio](https://user-images.githubusercontent.com/73386100/101727987-c27caa00-3adf-11eb-8a0a-d7dd804dae5b.png)

## Now we will create register window:

That means if a user press register button on the main screen, new window will appear where users have to enter a
username and password. This way they can register themselves. So let’s see how to do that.

```
def register_user():
    global username
    global password
    global username_entry
    global pass_entr
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
    pass_entr = Entry(register_win, width=15, font=("arial", 20),
                      relief="solid", bg="#999966")
    pass_entr.place(x=20, y=203)
    but = Button(register_win, text="Sign Up", padx=34,
           pady=5, bg="#52dfff", activebackground="#a1c4cc")
    but.place(x=20, y=290)

```

###### Create Register Button in root(main) window and bind it to the register function with command:

```
register_btn = Button(root, text="Register", font=("doppio one", 15),
                      command=register_user(), bg="#677882",
                      activebackground="#31484f", padx=8)


register_btn.place(x=140, y=400)
```

When you press to the register button it will call register function and new window will appear The result will be like
this:

![qqqqqqqqqqqqqqq](https://user-images.githubusercontent.com/73386100/101728152-14253480-3ae0-11eb-9027-4cb57ccf9e2c.png)

OK now add the button in registration window which will create a random password with length 10. It will, useful if user
want to create a strong password. To do this first we need to crate function which will generate Password.

```
# Add this button↓ to the register window.
Button(register_win, text="Generate Password", command=generate, pady=5,
           bg="#52dfff", activebackground="#a1c4cc").place(x=137, y=290)


def generate():
    pass_entr.delete(0, END)
    password1 = password_creator()
    pass_entr.insert(0, password1)


def password_creator():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    paswrd = ""

    for i in range(0, 10):
        paswrd = paswrd + choice(upper)
    return paswrd


```

If you want, you can make passwords more strong. Just add numbers and symbols in upper variable.

### We created Register button in register window, but it did not work. To make it we will create register_file function.

This function will create files with names which we input in username entry. After that we can get all list of files and
chek is this file in our computer. Also, we should add some limitations for registration. For instance: If user will
enter strings in username entry we will return massage that the username should be only numbers. You can create
limitations by your see. Be sure that you put limitations before the creating file, otherwise it will register even if
it is incorrect

```
def register_file():
    list_of_users = os.listdir()
    username_info = username_entry.get()
    password_info = pass_entr.get()
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
                          text="Length of Student Number \n should be 9")
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
    elif var.get() == 0:
        agreement_error = Label(register_win, fg="green", font=("verdana", 11),
                                text="Put mark on agreement"
                                     "\npolicy to sign up!")
        agreement_error.place(x=38, y=330)
        register_win.after(1000, agreement_error.destroy)
    elif username_info in list_of_users:
        clone_error = Label(register_win, fg="green", font=("verdana", 11),
                            text="This Student Number\nis already exist!")
        clone_error.place(x=50, y=330)
        register_win.after(1000, clone_error.destroy)
    else:
        try:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()
        except FileNotFoundError:
            pass
        username_entry.delete(0, END)
        pass_entr.delete(0, END)
        Label(register_win, text="Successfully Registered", fg="green",
              font=("verdana", 11)).place(x=43, y=330)
        register_win.after(1000, lambda: register_win.destroy())

```

Do not forget to bind this function with our register button in registration window

```
but = Button(register_win, text="Sign Up", command=register_file, padx=34,
           pady=5, bg="#52dfff", activebackground="#a1c4cc")
    but.place(x=20, y=290)
```

Congratulations we finished with registration window! You can add some features, it depends on your imagination. For
example: you can add chek button with agreement policy or make function which will hide password etc.

### Now create login button in root(main) window

```
login_btn = Button(root, text="Login", font=("doppio one", 15),
                   command=login_verify, bg="#677882",
                   activebackground="#31484f", padx=27)
      
login_btn.place(x=15, y=400)
```

Result:

![ppppppppppppppppppppp](https://user-images.githubusercontent.com/73386100/101728321-70885400-3ae0-11eb-80c4-55ccf179d710.png)

When user see this window there will be some question: where to write a username and where password? Therefore, we will
create placeholders. This placeholder will disappear when user will click on it.

```
login_entry_main.insert(0, "Student Number")
login_entry_main.bind("<FocusIn>",
                      lambda args: login_entry_main.delete('0', 'end'))
                  
pass_entr_main.insert(0, "Password")
pass_entr_main.bind("<FocusIn>",
                    lambda args: pass_entr_main.delete('0', 'end'))
```

## Login Verification Process

In this section we will verify the username and password for the login. So let’s start

#### Defining Verification function

```
def login_verify():
    global login_entry_main
    global pass_entr_main
    
    #get username and password
    
    username1 = login_entry_main.get()
    password1 = pass_entr_main.get()
    
    #The method listdir() returns a list containing the names of the entries in the directory
    
    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            LoginWindow.login_success(p1) # This class we will created below

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

```

### Designing Login Success Window

Now we will define a function that will show a window for a successful login. If user has entered the valid entries then
this window will appear. So let’s see how to do it.

```
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

```

I just put one image in success window, you can do it what you want.




\
We should create hide button which will hide password when user writing. For this we can use show method.
```
def hide_password():
    if pass_entr_main.cget('show') == '':
        pass_entr_main.config(show='*')
        show_btn.config(image=eye_photo2)
    else:
        pass_entr_main.config(show='')
        show_btn.config(image=eye_photo)
```
We created function, now create a button. Do not forget to bind with our function!

```
show_btn = Button(root, text="👁", image=eye_photo, bg="#586466",
                  activebackground="#31484f", command=hide_password)
```

## Final Result:

![final look](https://user-images.githubusercontent.com/73386100/101783927-0e9e0d80-3b25-11eb-84b6-2263cbe2eef3.png)

## Complete Code For Python GUI Login

```
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
    global pass_entr
    global register_win
    global var

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
    pass_entr = Entry(register_win, width=15, font=("arial", 20),
                      relief="solid", bg="#999966")
    pass_entr.place(x=20, y=203)
    but = Button(register_win, text="Sign Up", command=register_file, padx=34,
           pady=5, bg="#52dfff", activebackground="#a1c4cc", state=DISABLED)
    but.place(x=20, y=290)
    Button(register_win, text="Generate Password", command=generate, pady=5,
           bg="#52dfff", activebackground="#a1c4cc").place(x=137, y=290)
    Label(register_win, text="I accept the terms of use", bg="#a1c4cc",
          font=("arial", 9)).place(x=40, y=250)
    def enable():
        if var.get():
            but['state'] = 'normal'
        else:
            but['state'] = 'disabled'  # disable it
    var = IntVar()
    cb = Checkbutton(register_win, variable=var, bg="#a1c4cc",
                activebackground="#a1c4cc", command=enable)
    cb.place(x=15, y=249)


def register_file():
    list_of_users = os.listdir()
    username_info = username_entry.get()
    password_info = pass_entr.get()
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
                          text="Length of Student Number \n should be 9")
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
    elif var.get() == 0:
        agreement_error = Label(register_win, fg="green", font=("verdana", 11),
                                text="Put mark on agreement"
                                     "\npolicy to sign up!")
        agreement_error.place(x=38, y=330)
        register_win.after(1000, agreement_error.destroy)
    elif username_info in list_of_users:
        clone_error = Label(register_win, fg="green", font=("verdana", 11),
                            text="This Student Number\nis already exist!")
        clone_error.place(x=50, y=330)
        register_win.after(1000, clone_error.destroy)
    else:
        try:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()
        except FileNotFoundError:
            pass
        username_entry.delete(0, END)
        pass_entr.delete(0, END)
        Label(register_win, text="Successfully Registered", fg="green",
              font=("verdana", 11)).place(x=43, y=330)
        register_win.after(1000, lambda: register_win.destroy())


def login_verify():
    global login_entry_main
    global pass_entr_main
    username1 = login_entry_main.get()
    password1 = pass_entr_main.get()
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


def hide_password():
    if pass_entr_main.cget('show') == '':
        pass_entr_main.config(show='*')
        show_btn.config(image=eye_photo2)
    else:
        pass_entr_main.config(show='')
        show_btn.config(image=eye_photo)


def generate():
    pass_entr.delete(0, END)
    password1 = password_creator()
    pass_entr.insert(0, password1)


def password_creator():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    paswrd = ""

    for i in range(0, 10):
        paswrd = paswrd + choice(upper)
    return paswrd


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
pass_entr_main = Entry(root, borderwidth=4, relief="solid", bg="#393f40",
                       width=16, font=("cabin sketch", 15), fg="white")

login_btn = Button(root, text="Login", font=("doppio one", 15),
                   command=login_verify, bg="#677882",
                   activebackground="#31484f", padx=27)
register_btn = Button(root, text="Register", font=("doppio one", 15),
                      command=register_user, bg="#677882",
                      activebackground="#31484f", padx=8)
show_btn = Button(root, text="👁", image=eye_photo, bg="#586466",
                  activebackground="#31484f", command=hide_password)

AlaToo_lbl = Label(root, text="Ala-Too International University 2020",
                   font=("Dubai Medium", 10), bg="#3285a8")

photo.grid()
sign_in_lbl.grid()
login_entry_main.place(x=16, y=320)
login_entry_main.insert(0, "Student Number")
login_entry_main.bind("<FocusIn>",
                      lambda args: login_entry_main.delete('0', 'end'))
pass_entr_main.place(x=16, y=360)
pass_entr_main.insert(0, "Password")
pass_entr_main.bind("<FocusIn>",
                    lambda args: pass_entr_main.delete('0', 'end'))
login_btn.place(x=15, y=400)
register_btn.place(x=140, y=400)
show_btn.place(x=221, y=364)

AlaToo_lbl.place(x=30, y=450)

root.mainloop()

```

So this was Python GUI Login tutorial. I hope you have understood this very well. If you found it helpful then please
share with others. Thanks for Your Time.
