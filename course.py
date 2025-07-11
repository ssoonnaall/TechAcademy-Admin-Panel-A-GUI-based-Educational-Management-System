from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys

def insert_course():
    name = e1.get()
    fee = e2.get()
    duration = e3.get()
    instructor = e4.get()
    slot = e5.get()
    mode = c.get()

    if name == "" or fee == "" or duration == "" or instructor == "" or slot == "" or mode == "Select":
        messagebox.showerror("Error", "Please fill all fields")
        return

    import pymysql as sql
    db = sql.connect(host="localhost", user="root", password="Rama@1234", db="project")
    cur = db.cursor()
    cur.execute("INSERT INTO courses VALUES (%s, %s, %s, %s, %s, %s)", (name, fee, duration, instructor, slot, mode))
    db.commit()
    db.close()
    messagebox.showinfo("Success", "Course added successfully")
    clear()

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    c.set("Select")


def go_back():
    top.destroy()
    subprocess.Popen([sys.executable, 'homepage.py'])


# Main Window
top = Tk()
top.title("Add Course")
top.geometry("700x500")
top.config(bg='powderblue')

# Background Image
path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
img = ImageTk.PhotoImage(Image.open(path))
L12 = Label(top, image=img)
L12.pack()

# Heading
Label(top, text="Add New Course", font=('"Arial" 18 bold'), bg="white").place(x=270, y=30)

# Input Fields
Label(top, text="Course Name", font=('"Arial" 18 bold'), bg="white").place(x=100, y=100)
e1 = Entry(top, font=("Arial", 16))
e1.place(x=350, y=100)

Label(top, text="Course Fee", font=('"Arial" 18 bold'), bg="white").place(x=100, y=140)
e2 = Entry(top, font=("Arial", 16))
e2.place(x=350, y=140)

Label(top, text="Duration", font=('"Arial" 18 bold'), bg="white").place(x=100, y=180)
e3 = Entry(top, font=("Arial", 16))
e3.place(x=350, y=180)

Label(top, text="Mentor", font=('"Arial" 18 bold'), bg="white").place(x=100, y=220)
e4 = Entry(top, font=("Arial", 16))
e4.place(x=350, y=220)

Label(top, text="Time Slot", font=('"Arial" 18 bold'), bg="white").place(x=100, y=260)
e5 = Entry(top, font=("Arial", 16))
e5.place(x=350, y=260)

Label(top, text="Course Mode", font=('"Arial" 18 bold'), bg="white").place(x=100, y=300)
c = StringVar()
drop = ttk.Combobox(top, textvariable=c, font=('"Arial" 18 '), values=["Select", "Online", "Offline"])
drop.place(x=350, y=300)
drop.current(0)

# Buttons
Button(top, text="Add", font=('"Arial" 18 bold'), fg="black", width=8, command=insert_course).place(x=350, y=350)
Button(top, text="Back", font=('"Arial" 18 bold'), fg="black", width=8, command=go_back).place(x=500, y=350)

top.mainloop()
