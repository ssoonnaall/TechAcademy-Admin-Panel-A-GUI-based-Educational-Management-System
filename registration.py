from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox
import pymysql as sql

top = Tk()
top.title('Admin Registration')
top.geometry('1500x700')  # adjusted to fit on screen
top.resizable(True, True)

# Functions

def exit_app():
    top.destroy()

def clear_fields():
# Clear Entry fields
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')

# Reset gender selection (radio buttons)
    var.set('')  # or var.set('Male') or any default you prefer

# Reset state dropdown
    c.set('')    # or c.set('Select State') or your default option

def show_password():
    if e5.cget('show') == "*":
        e5.config(show='')
    else:
        e5.config(show='*')



def calculate_age(*args):
    dob = cal.get_date()
    today = datetime.date.today()
    # Calculate age
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    #Display the result
    e4.delete(0, END)
    e4.insert(0, str(age))


def insert():
    firstname = e1.get()
    lastname = e2.get()
    contact = e3.get()
    age = e4.get()
    email = e6.get()
    password = e5.get()
    gender = var.get()
    state = c.get()

#  Contact number validation
    if not contact.isdigit() or len(contact) != 10:
        messagebox.showerror("Invalid Contact", "Contact number must be exactly 10 digits.")
        return
#  Short Email validation
    if "@" not in email or "." not in email or email.startswith("@") or email.endswith("@"):
        messagebox.showerror("Invalid Email", "Enter a valid email address.")
        return

    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    query = "INSERT INTO reg_schema VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (firstname, lastname, contact, age, email,password, gender, state)
    result = cur.execute(query, values)
    db.commit()

    if result > 0:
        messagebox.showinfo("Success", "Record inserted successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Failed", "Insert failed.")

    for entry in (e1, e2, e3, e4, e5, e6):
        entry.delete(0, END)

def update():
    firstname = e1.get()
    lastname = e2.get()
    contact = e3.get()
    age = e4.get()
    email = e6.get()
    password = e5.get()
    gender = var.get()
    state = c.get()
    if not all([firstname, lastname, contact, age, email,password, gender, state]):
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return

    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    query = """UPDATE reg_schema SET  firstname=%s ,lastname=%s, contact=%s, age=%s, password=%s, gender=%s, state=%s WHERE email=%s """
    values = (firstname,lastname, contact, age, password, gender, state,email )
    result = cur.execute(query, values)
    db.commit()

    if result > 0:
        messagebox.showinfo("Success", "Record updated successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Failed", "No record updated.")

def delete():
    firstname = e1.get()
    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    result = cur.execute("DELETE FROM reg_schema WHERE firstname=%s", (firstname,))
    db.commit()

    if result > 0:
        messagebox.showinfo("Success", "Record deleted successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Failed", "No record found.")

def open_login():
    top.destroy()
    import login

# Background
bg_path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
img = ImageTk.PhotoImage(Image.open(bg_path))
bg_label = Label(top, image=img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Heading
Label(top, text='Admin Registration', bg='white', fg='black', font=('Arial', 30, 'bold')).place(x=450, y=30)

# Input Fields
Label(top, text='First Name', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=100)
e1 = Entry(top, font=('Arial 20'))
e1.place(x=320, y=100)

Label(top, text='Last Name', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=150)
e2 = Entry(top, font=('Arial 20'))
e2.place(x=320, y=150)

Label(top, text='Contact', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=200)
e3 = Entry(top, font=('Arial 20'))
e3.place(x=320, y=200)

Label(top, text='Select DOB', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=250)
cal = DateEntry(top, width=19, bg='powderblue', fg='black', font=('Arial', 20), year=2000,date_pattern='yyyy/mm/dd')
cal.place(x=320, y=250)
cal.bind("<<DateEntrySelected>>", calculate_age)

Label(top, text='Age', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=300)
e4 = Entry(top, font=('Arial 20'))
e4.place(x=320, y=300)


Label(top, text='Email', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=350)
e6 = Entry(top, font=('Arial 20'))  # new Entry for email
e6.place(x=320, y=350)

Label(top, text='Password', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=400)
e5 = Entry(top, font=('Arial 20'), show='*')
e5.place(x=320, y=400)
Checkbutton(top, command=show_password).place(x=660, y=405)

Label(top, text='Gender', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=450)
var = StringVar()
Radiobutton(top, text='Male', value='Male', variable=var, font=('Arial 18')).place(x=320, y=450)
Radiobutton(top, text='Female', value='Female', variable=var, font=('Arial 18')).place(x=410, y=450)
Radiobutton(top, text='Other', value='Other', variable=var, font=('Arial 18')).place(x=527, y=450)

Label(top, text='State', bg='white', fg='black', font=('Arial 20 bold')).place(x=150, y=500)
states = ['Select', 'Delhi', 'UttarPradesh', 'Haryana', 'Hyderabad', 'Rajasthan']
c = ttk.Combobox(top, values=states, font=('Arial 19'))
c.place(x=320, y=500)
c.current(0)


# Buttons
Button(top, text='Submit', font=('Arial 18 bold'), command=insert).place(x=320, y=537)
Button(top, text='Delete', font=('Arial 18 bold'), command=delete).place(x=540, y=537)
Button(top, text='Update', font=('Arial 18 bold'), command=update).place(x=430, y=537)
Button(top, text='Close', font=('Arial 18 bold'), command=exit_app).place(x=430, y=590)
Button(top, text='Login', font=('Arial 18 bold'), command=open_login).place(x=320, y=590)

top.config(bg='powderblue')
top.mainloop()
