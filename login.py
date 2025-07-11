from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql as sql

top = Tk()
top.title('Admin Login')
top.geometry('1000x600')
top.resizable(True, True)

# Background Image
path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
img = ImageTk.PhotoImage(Image.open(path))
bg_label = Label(top, image=img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Show/Hide Password Toggle
def show():
    if e2.cget('show') == "*":
        e2.config(show='')
    else:
        e2.config(show='*')

# Login Function
def Login():
    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    cur.execute("SELECT * FROM reg_schema WHERE email=%s AND  password=%s", (e1.get(), e2.get()))
    row = cur.fetchone()

    if row is None:
        messagebox.showerror("Error", "Invalid Email or Password")
    else:
        top.destroy()
        import homepage

# Labels and Entries
Label(top, text='Admin Login', bg='white', fg='black', font=('Arial', 30, 'bold')).place(x=500, y=30)

Label(top, text='Email', bg='white', fg='black', font=('Arial', 20, 'bold')).place(x=200, y=150)
e1 = Entry(top, font=('Arial', 20, 'bold'))
e1.place(x=350, y=150)

Label(top, text='Password', bg='white', fg='black', font=('Arial', 20, 'bold')).place(x=200, y=200)
e2 = Entry(top, font=('Arial', 20, 'bold'), show='*')
e2.place(x=350, y=200)

# Buttons
Button(top, text='Login', font=('Arial 18 bold'), command=Login).place(x=440, y=260)


# Show password check
Checkbutton(top, command=show, text="Show Password", bg='white', font=('Arial 12')).place(x=670, y=210)

top.config(bg='powderblue')
top.mainloop()
