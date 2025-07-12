from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
import pymysql as sql
import subprocess
import sys
from config import DB_PASSWORD


top = Tk()
top.title('Mentor Registration')


# Background image
path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
img = ImageTk.PhotoImage(Image.open(path))
L12 = Label(top, image=img)
L12.pack()

# FUNCTIONS

def exit_app():
    top.destroy()


def back():
    top.destroy()
    subprocess.Popen([sys.executable, 'homepage.py'])


def clear_fields():
    e_id.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e_email.delete(0, END)
    c2.set("Select")
    c3.set("Select")
    c4.set("Select")
    gender_var.set("Male")

def insert():
    k1 = e1.get()
    k2 = e2.get()
    k3 = e3.get()
    k4 = e4.get()
    email = e_email.get()
    qualification = c2.get()
    gender = gender_var.get()
    subject = c3.get()
    experience = c4.get()

    if not (k1 and k2 and k3 and k4 and email and qualification != "Select" and gender and subject != "Select" and experience != "Select"):
        messagebox.showwarning("Incomplete", "Please fill all the fields correctly.")
        return

    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    query = "INSERT INTO Mentors(Firstname, Lastname, Contact, Age, Email, Qualification, Gender, Subject, Experience) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (k1, k2, k3, k4, email, qualification, gender, subject, experience)
    result = cur.execute(query, values)
    db.commit()

    cur.execute("SELECT LAST_INSERT_ID()")
    mentor_id = cur.fetchone()[0]
    mentor_id_var.set(mentor_id)

    if result > 0:
        messagebox.showinfo("Success", "Record inserted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e_email.delete(0, END)
        c2.set("Select")
        c3.set("Select")
        c4.set("Select")
        gender_var.set("Male")
    else:
        messagebox.showerror("Error", "Failed to insert record.")
def update_mentor():
    mentor_id = e_id.get()
    if not mentor_id:
        messagebox.showwarning("Input Needed", "Please enter Mentor ID to update.")
        return

    values = ( e1.get(), e2.get(), e3.get(), e4.get(),e_email.get(), c2.get(), gender_var.get(), c3.get(), c4.get(), mentor_id )

    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    query = "UPDATE Mentors SET Firstname=%s, Lastname=%s, Contact=%s, Age=%s, Email=%s, Qualification=%s, Gender=%s, Subject=%s, Experience=%s WHERE MentorID=%s"
    result = cur.execute(query, values)
    db.commit()
    if result > 0:
        messagebox.showinfo("Updated", "Mentor record updated.")
        clear_fields()
    else:
        messagebox.showerror("Error", "Mentor ID not found or no change made.")
    db.close()

def delete_mentor():
    mentor_id = e_id.get()
    if not mentor_id:
        messagebox.showwarning("Input Needed", "Please enter Mentor ID to delete.")
        return

    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this mentor?")
    if confirm:
        db = sql.connect(host='localhost', user='root', password='Rama@1234', db='project')
        cur = db.cursor()
        cur.execute("DELETE FROM Mentors WHERE MentorID=%s", (mentor_id,))
        db.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Deleted", "Mentor record deleted.")
            clear_fields()
        else:
            messagebox.showerror("Error", "Mentor ID not found.")
        db.close()

# WIDGETS

Label(top, text='Mentor Registration', bg='white', fg='black', font='Arial 30 bold').place(x=500, y=30)

Label(top, text='Mentor ID', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=100)
mentor_id_var = StringVar()
e_id = Entry(top, font='Arial 20', textvariable=mentor_id_var)
e_id.place(x=400, y=100)

Label(top, text='First Name', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=150)
e1 = Entry(top, font='Arial 20')
e1.place(x=400, y=150)

Label(top, text='Last Name', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=200)
e2 = Entry(top, font='Arial 20')
e2.place(x=400, y=200)

Label(top, text='Contact', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=250)
e3 = Entry(top, font='Arial 20')
e3.place(x=400, y=250)

Label(top, text='Age', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=300)
e4 = Entry(top, font='Arial 20')
e4.place(x=400, y=300)

Label(top, text='Email ID', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=350)
e_email = Entry(top, font='Arial 20')
e_email.place(x=400, y=350)

Label(top, text='Qualification', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=400)
qualifications = ['Select', 'B.A', 'B.Tech', 'B.Sc', 'BBA', 'B.C.A', 'M.A', 'M.C.A', 'M.Tech', 'M.Sc', 'MBA', 'PHD']
c2 = ttk.Combobox(top, values=qualifications, font='Arial 20')
c2.place(x=400, y=400)
c2.current(0)

Label(top, text='Gender', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=450)
gender_var = StringVar(value='Male')

Radiobutton(top, text='Male', value='Male', variable=gender_var, font='Arial 14').place(x=400, y=450, height=40, width=70)
Radiobutton(top, text='Female', value='Female', variable=gender_var, font='Arial 14').place(x=480, y=450, height=40, width=90)
Radiobutton(top, text='Other', value='Other', variable=gender_var, font='Arial 14').place(x=580, y=450, height=40, width=80)

Label(top, text='Subject', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=500)
subjects = ['Select', 'Data Science', 'Machine Learning', 'Data Analytics', 'Generative AI','Linux Training']
c3 = ttk.Combobox(top, values=subjects, font='Arial 20 bold')
c3.place(x=400, y=500)
c3.current(0)

Label(top, text='Experience', bg='white', fg='black', font='Arial 20 bold').place(x=200, y=550)
experience_years = ['Select', 'No Experience', '1-2', '3-4', '4-5', '>5']
c4 = ttk.Combobox(top, values=experience_years, font='Arial 20 bold')
c4.place(x=400, y=550)
c4.current(0)


#Buttons
Button(top, text='Submit',font='Arial 16 bold', command=insert).place(x=200, y=592)
Button(top, text='Update', font='Arial 16 bold', command=update_mentor).place(x=300, y=592)
Button(top, text='Delete', font='Arial 16 bold', command=delete_mentor).place(x=400, y=592)
Button(top, text='Clear', font='Arial 16 bold', command=clear_fields).place(x=490, y=592)
Button(top, text='Back', font='Arial 16 bold', command=back).place(x=570, y=592)
Button(top, text='Exit', font='Arial 16 bold', command=exit_app).place(x=650, y=592)

top.config(bg='lightgreen')
top.mainloop()
