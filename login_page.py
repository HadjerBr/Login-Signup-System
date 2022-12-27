from cgitb import text
from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql


def forget_password():

    def clear():
        user_name_entry.delete(0,END)
        new_password_entry.delete(0,END)
        c_password_entry.delete(0,END)

    def reset_password():

        if new_password_entry.get() == "" or c_password_entry.get() == "" or user_name_entry.get() == "" :
            messagebox.showerror("Error", "All fields requiered!", parent = window)
        elif new_password_entry.get() != c_password_entry.get():
            messagebox.showerror("Error", "Password mismatch", parent = window)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Cilekreceli1#")
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "Not connected to database! Try again", parent = window)
                return
            query = "use userInfo"
            mycursor.execute(query)
            query = "select * from user where username = %s"
            mycursor.execute(query, (user_name_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Unvalid username!", parent = window)
            else:
                query = "UPDATE user SET password =%s WHERE username =%s"
                mycursor.execute(query, (new_password_entry.get(), user_name_entry.get()))
                con.commit() # since we are updating
                messagebox.showinfo("Success", "Password updated", parent = window)
                window.destroy()

    def onclick(event):
        if user_name_entry.get() == "Username":
            user_name_entry.delete(0, END)

    def onclick2(event):
        if new_password_entry.get() == "New Password":
            new_password_entry.delete(0, END)

    def onclick3(event):
        if c_password_entry.get() == "Confirm Password":
            c_password_entry.delete(0, END)

    window = Toplevel()
    window.title("Rest Password")
    background_image = ImageTk.PhotoImage(file = "images/forget.jpg")
    label1 = Label(window, image = background_image)
    label1.grid()
    window.resizable(0, 0)

    forgot = Label(window, text="REST PASSWORD", font=("Arial", 18, "bold"), fg="violet", bg="white")
    forgot.place(x = 490, y = 60 )

    user_name_entry = Entry(window, width = 18, font=("Arial", 15), fg="violet", bd=0, bg = "white")
    user_name_entry.place(x = 490, y = 120)
    user_name_entry.insert(0, "Username")
    user_name_entry.bind("<FocusIn>", onclick)
    line1 = Frame(window, height=2, width=230, bg = "violet")
    line1.place(x = 490, y = 150)

    new_password_entry = Entry(window, width = 18, font=("Arial", 15), fg="violet", bd=0, bg = "white")
    new_password_entry.place(x = 490, y = 200)
    new_password_entry.insert(0, "New Password")
    new_password_entry.bind("<FocusIn>", onclick2)
    line1 = Frame(window, height=2, width=230, bg = "violet")
    line1.place(x = 490, y = 230)

    c_password_entry = Entry(window, width = 18, font=("Arial", 15), fg="violet", bd=0, bg = "white")
    c_password_entry.place(x = 490, y = 280)
    c_password_entry.insert(0, "Confirm Password")
    c_password_entry.bind("<FocusIn>", onclick3)
    line1 = Frame(window, height=2, width=230, bg = "violet")
    line1.place(x = 490, y = 310)

    submit_button = Button(window, text="Submit", bg = "violet", fg = "white", font=("Arial", 15, "bold"), activebackground="violet", activeforeground="white", width = 18, bd=0, cursor="hand2", command= reset_password)
    submit_button.place(x=490, y=360)



    window.mainloop()

def clear():
    user_name_entry.delete(0,END)
    password_entry.delete(0,END)

def connect_to_database():
    if user_name_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error", "All fields are requiered!")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Cilekreceli1#")
            mycursor = con.cursor()  # for queries ( actions ) related to database
        except:
            messagebox.showerror("Error", "Not connected to database!")
            return
        query = "use userInfo"
        mycursor.execute(query)
        
        query = "select * from user where username = %s and password = %s"
        mycursor.execute(query, (user_name_entry.get(), password_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Wrong username or password!")
            clear()
        else:
            messagebox.showinfo("Welcome", "Login is successful")
            clear()
        



def go_to_register():
    root.destroy()
    import registration_page

def onclick(event):
    if user_name_entry.get() == "Username":
        user_name_entry.delete(0, END)

def onclick2(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, END)

def hide():
    open_eye.config(file = "images/icons8-blind-48.png")
    password_entry.config(show="*")
    open_eye_button.config(command = show)

def show():
    open_eye.config(file = "images/icons8-eye-48.png")
    password_entry.config(show="")
    open_eye_button.config(command = hide)



root = Tk()
root.title("Login")
root.geometry("1080x681")
root.resizable(0, 0)
background_image = ImageTk.PhotoImage(file = "images/bg.jpg")
label1 = Label(root, image = background_image)
label1.place(x=0, y=0)
root.wm_attributes("-transparentcolor", 'grey')
login = Label(root, text="USER LOGIN", font=("Arial", 30, "bold"), bg="#A6D7DB", fg="white")
login.place(x = 680, y = 100 )

user_name_entry = Entry(root, width = 25, font=("Arial", 15), fg="black", bd=0, bg = "#A6D7DB")
user_name_entry.place(x = 665, y = 200)
user_name_entry.insert(0, "Username")
user_name_entry.bind("<FocusIn>", onclick)
line1 = Frame(root, height=2, width=280, bg = "white")
line1.place(x = 665, y = 230)

password_entry = Entry(root, width = 25, font=("Arial", 15), fg="black", bd=0, bg = "#A6D7DB")
password_entry.place(x = 665, y = 290)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", onclick2)
line1 = Frame(root, height=2, width=280, bg = "white")
line1.place(x = 665, y = 320)


open_eye = PhotoImage(file = "images/icons8-eye-48.png")
open_eye_button = Button(root, image = open_eye, bd=0, bg = "#A6D7DB", height= 30, width=40, activebackground="#A6D7DB", cursor="hand2", command = hide)
open_eye_button.place(x = 900, y= 287 )

f_password = Button(root, text="frogot password?", bd=0, bg="#A6D7DB", fg="white", font=("Arial", 12), activebackground="#A6D7DB", activeforeground="white", cursor="hand2", command = forget_password)
f_password.place(x=823, y = 335)

login_button = Button(root, text="LOGIN", bg = "white", fg = "#007FFF", font=("Arial", 15, "bold"), activebackground="white", activeforeground="#007FFF", width = 23, bd=0, cursor="hand2", command = connect_to_database)
login_button.place(x=665, y=400)

or_label = Label(root, text="----------------OR--------------", font=("Arial", 18), bg="#A6D7DB", fg="white" )
or_label.place(x = 663, y= 450)

facebook = PhotoImage(file="images/facebook.png")
fLabel = Label(image=facebook, bg="#A6D7DB")
fLabel.place(x=750, y = 495)

google = PhotoImage(file="images/google.png")
gLabel = Label(image=google, bg="#A6D7DB")
gLabel.place(x=795, y = 495)

twitter = PhotoImage(file="images/twitter.png")
tLabel = Label(image=twitter, bg="#A6D7DB")
tLabel.place(x=840, y = 495)

da_label = Label(root, text="Don't have an account?", font=("Arial", 11, "bold"), bg="#A6D7DB", fg="white" )
da_label.place(x = 665, y= 560)

ca_button = Button(root, text="Create new one", bg = "#A6D7DB", fg = "blue", font=("Arial", 11, "underline"), activebackground="#A6D7DB", activeforeground="blue", bd=0, cursor="hand2", command= go_to_register)
ca_button.place(x=835 , y=558)

root.mainloop()