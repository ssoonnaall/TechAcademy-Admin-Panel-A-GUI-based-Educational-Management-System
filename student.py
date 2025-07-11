from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
import pymysql as sql
import subprocess
import sys


top = Tk()
top.title('Student Registration')
top.geometry('2000x1100')
top.config(bg='green')

# Background Image
path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
img = ImageTk.PhotoImage(Image.open(path))
Label(top, image=img).pack()

# Exit and Back
def exit_app():
    top.destroy()


def back():
    top.destroy()
    subprocess.Popen([sys.executable, 'homepage.py'])


def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    cal.set_date(datetime.date.today())
    c2.current(0)  # Reset Qualification
    gender_var.set('Male')  # Reset Gender
    c3.current(0)  # Reset Course
    c4.current(0)  # Reset State


def search():
    global tv
    tv = ttk.Treeview(top)
    Firstname = e1.get()
    for i in tv.get_children():
        tv.delete(i)
    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    cur.execute("SELECT * FROM students WHERE Firstname = %s", (Firstname,))
    result = cur.fetchall()

    for row in result:
        tv.insert("", 'end', values=row)

# Submit
def insert():
    stid = student_id_entry.get()
    k1 = e1.get()
    k2 = e2.get()
    k3 = e3.get()
    k4 = e4.get()
    k5 = cal.get()
    date = datetime.datetime.strptime(k5, '%m/%d/%y')
    reg_date = date.strftime('%Y-%m-%d')
    k6 = c2.get()
    k7 = gender_var.get()
    k8 = c3.get()
    k9 = c4.get()

    if "" in (stid,k1, k2, k3, k4) or k6 == "Select" or k8 == "Select" or k9 == "Select State":
        messagebox.showerror("Error", "Please fill all fields")
        return
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    query = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (stid,k1, k2, int(k3), int(k4), reg_date, k6, k7, k8, k9)
    result = cur.execute(query, values)
    db.commit()
    db.close()

    if result > 0:
        messagebox.showinfo("Success", "Record inserted successfully")
    else:
        messagebox.showinfo("Error", "Record not inserted")


def update():
    stid = student_id_entry.get()
    Firstname = e1.get()
    Lastname = e2.get()
    Contact = e3.get()
    Age = e4.get()
    RegDate = cal.get()
    Qualification = c2.get()
    Gender = gender_var.get()
    Course = c3.get()
    State = c4.get()

    if not all([stid,Firstname, Lastname, Contact, Age, RegDate, Qualification, Gender, Course, State]):
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return

    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    query = """UPDATE students SET Firstname=%s,Lastname=%s, Contact=%s, Age=%s, Reg_date=%s, Qualification=%s, Gender=%s, Course=%s, state=%s WHERE StudentID=%s"""
    values = (Firstname,Lastname, Contact, Age, RegDate, Qualification, Gender, Course, State, stid)
    result = cur.execute(query, values)
    db.commit()

    if result > 0:
        messagebox.showinfo("Success", "Record updated successfully.")
        show_students()
    else:
        messagebox.showwarning("Failed", "No record updated.")


def delete_student():
    selected = tv.selection()
    if not selected:
        messagebox.showwarning("Select", "Please select a record to delete.")
        return

    record = tv.item(selected)['values']
    stid = record[0]  # student id is unique

    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    cur.execute("DELETE FROM students WHERE Firstname=%s", (fname,))
    db.commit()

    messagebox.showinfo("Deleted", f"Student '{fname}' deleted.")
    show_students()

def show_students():
    for i in tv.get_children():
        tv.delete(i)
    db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
    cur = db.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    for row in data:
        tv.insert("", END, values=row)

# Heading
Label(top, text='Student Registration', bg='white', fg='black', font=('Arial', 30)).place(x=500, y=30)

# Input Fields
Label(top, text='Student ID', bg='white', fg='black', font=("'Arial' 18 bold")).place(x=80, y=100)
student_id_entry = Entry(top, font=('Arial', 18))
student_id_entry.place(x=235, y=100)


Label(top, text='Firstname', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=150)
e1 = Entry(top, font=('Arial', 18))
e1.place(x=235, y=150)

Label(top, text='Lastname', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=200)
e2 = Entry(top, font=('Arial', 18))
e2.place(x=235, y=200)

Label(top, text='Contact', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=250)
e3 = Entry(top, font=('Arial', 18))
e3.place(x=235, y=250)

Label(top, text='Age', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=300)
e4 = Entry(top, font=('Arial', 18))
e4.place(x=235, y=300)

Label(top, text='RegDate', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=350)
cal = DateEntry(top, width=18, bg='white', fg='black', font=('Arial', 14), year=2025)
cal.place(x=235, y=350)

Label(top, text='Qualification', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=400)
c2 = ttk.Combobox(top, values=['Select', '12th', '10th', 'B.A', 'B.Tech', 'B.Sc', 'B.C.A', 'M.Tech', 'M.Sc'], font=('Arial', 16))
c2.place(x=235, y=400)
c2.current(0)

Label(top, text='Gender', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=450)
gender_var = StringVar()
Radiobutton(top, text='Male', value='Male', variable=gender_var, font=('Arial', 14)).place(x=235, y=450)
Radiobutton(top, text='Female', value='Female', variable=gender_var, font=('Arial', 14)).place(x=315, y=450)
Radiobutton(top, text='Other', value='Other', variable=gender_var, font=('Arial', 14)).place(x=425, y=450)
gender_var.set('Male')

Label(top, text='Course', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=500)
c3 = ttk.Combobox(top, values=['Select', 'Data Analytics', 'Buisness Analytics', 'Machine Learning', 'Mern Full Stack', 'Digital Marketing'], font=('Arial', 16))
c3.place(x=235, y=500)
c3.current(0)

Label(top, text='State', bg='white', fg='black', font=('"Arial" 18 bold')).place(x=80, y=550)
c4 = ttk.Combobox(top, values=['Select', 'Delhi', 'UttarPradesh', 'Haryana', 'Hyderabad', 'Rajasthan'], font=('Arial', 16))
c4.place(x=235, y=550)
c4.current(0)

# Treeview for data display
tv = ttk.Treeview(top)
tv['columns'] = ('Student ID','First name', 'Last name', 'Contact', 'Age', 'Reg Date', 'Qualification', 'Gender','Course', 'State')
tv.column('#0', width=0, stretch=NO)
tv.column('Student ID', anchor=CENTER, width=80)
tv.column('First name', anchor=CENTER, width=75)
tv.column('Last name', anchor=CENTER, width=65)
tv.column('Contact', anchor=CENTER, width=90)
tv.column('Age', anchor=CENTER, width=50)
tv.column('Reg Date', anchor=CENTER, width=80)
tv.column('Qualification', anchor=CENTER, width=75)
tv.column('Gender', anchor=CENTER, width=55)
tv.column('Course', anchor=CENTER, width=85)
tv.column('State', anchor=CENTER, width=85)

tv.heading('Student ID', text='Student ID', anchor=CENTER)
tv.heading('First name', text='First name', anchor=CENTER)
tv.heading('Last name', text='Last name', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('Reg Date', text='Reg Date', anchor=CENTER)
tv.heading('Qualification', text='Qualification', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.heading('Course', text='Course', anchor=CENTER)
tv.heading('State', text='State', anchor=CENTER)
tv.place(x=520,y=100)


# Buttons
Button(top, text='Submit', fg="black", font=('Arial 16 bold'), command=insert).place(x=80, y=590)
Button(top, text='Delete', font=('Arial 16 bold'), command= delete_student).place(x=180, y=590)
Button(top, text='Show', font=('Arial 16 bold'),command=show_students).place(x=270, y=590)
Button(top, text='Clear', font=('Arial 16 bold'), command=clear_fields).place(x=350, y=590)
Button(top, text='Update', font=('Arial 16 bold'), command=update).place(x=430, y=590)
Button(top, text='Back', fg="black", font=('Arial 16 bold'), command=back).place(x=1100, y=590)
Button(top, text='Exit', fg="black", font=('Arial 16 bold'), command=exit_app).place(x=1180, y=590)


top.mainloop()
