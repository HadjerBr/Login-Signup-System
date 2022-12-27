from cgitb import text
from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

def clear():
    email_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    cPassword_entry.delete(0,END)
    ch_var.set(0)

def connect_database():
    if email_entry.get() == "" or password_entry.get() == "" or username_entry.get() == "" or cPassword_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif password_entry.get( ) != cPassword_entry.get():
        messagebox.showerror("Error", "Pasword missmatch!")
    elif ch_var.get() == 0:
        messagebox.showerror("Error", "Please accept terms & conditions!")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Cilekreceli1#")
            mycursor = con.cursor()  # for queries ( actions ) related to database
        except:
            messagebox.showerror("Error", "Not connected to database!")
            return
        try:
            query = "create database userInfo"
            mycursor.execute(query)
            query = "use userInfo"
            mycursor.execute(query)
            query = "create table user(id int auto_increment primary key not null, email varchar(50), username varchar(50), password varchar(100))"
            mycursor.execute(query)
        except:
            mycursor.execute("use userInfo")
        query = "select * from user where username = %s"
        mycursor.execute(query, (username_entry.get()))
        row = mycursor.fetchone()
        if row!= None:
            messagebox.showerror("Error", "Username already exists!")
            clear()
            
        else:
            query = "insert user(email, username, password) values(%s,%s,%s)"
            mycursor.execute(query, (email_entry.get(), username_entry.get(), password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Account created")
            clear()

def go_to_login():
    root1.destroy()
    import login_page


root1 = Tk()
root1.title("Sign up")
root1.geometry("1080x681")
root1.resizable(0, 0)
background_image = ImageTk.PhotoImage(file = "images/bg.jpg")
label1 = Label(root1, image = background_image)
label1.place(x=0, y=0)
title = Label(root1, text="CREATE NEW ACCOUNT", font=("Arial", 21, "bold"), bg="#A6D7DB", fg="white")
title.place(x = 629, y = 80 )

email_label = Label(root1, text="Email", font=("Arial", 15), bg="#A6D7DB", fg="white" )
email_label.place(x=630, y=150)
email_entry = Entry(root1, width = 30, font=("Arial", 15), fg="black", bd=0, bg = "white")
email_entry.place(x = 635, y = 180)

username_label = Label(root1, text="Username", font=("Arial", 15), bg="#A6D7DB", fg="white" )
username_label.place(x=630, y=225)
username_entry = Entry(root1, width = 30, font=("Arial", 15), fg="black", bd=0, bg = "white")
username_entry.place(x = 635, y = 255)

password_label = Label(root1, text="Password", font=("Arial", 15), bg="#A6D7DB", fg="white" )
password_label.place(x=630, y=300)
password_entry = Entry(root1, width = 30, font=("Arial", 15), fg="black", bd=0, bg = "white")
password_entry.place(x = 635, y = 330)

cPassword_label = Label(root1, text="Confirm Password", font=("Arial", 15), bg="#A6D7DB", fg="white" )
cPassword_label.place(x=630, y=375)
cPassword_entry = Entry(root1, width = 30, font=("Arial", 15), fg="black", bd=0, bg = "white")
cPassword_entry.place(x = 635, y = 405)

ch_var = IntVar()
check = Checkbutton(root1, text="I agree to the terms & conditions",font=("Arial", 13, "bold"), fg="white", bg ="#A6D7DB", activebackground="#A6D7DB", selectcolor= "black", activeforeground="white", cursor="hand2", variable = ch_var )
check.place(x=635, y= 450)

register_button = Button(root1, text="Signup", bg = "white", fg = "#007FFF", font=("Arial", 15, "bold"), activebackground="white", activeforeground="#007FFF", width = 27, bd=0, cursor="hand2", command = connect_database)
register_button.place(x=635, y=495)

da_label = Label(root1, text="Already have an account?", font=("Arial", 11, "bold"), bg="#A6D7DB", fg="white" )
da_label.place(x = 675, y= 560)

ca_button = Button(root1, text="Login", bg = "#A6D7DB", fg = "blue", font=("Arial", 11, "underline"), activebackground="#A6D7DB", activeforeground="blue", bd=0, cursor="hand2", command=go_to_login)
ca_button.place(x=865 , y=558)



root1.mainloop()