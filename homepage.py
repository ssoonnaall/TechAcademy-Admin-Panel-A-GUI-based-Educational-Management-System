from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql as sql
from config import DB_PASSWORD


top = Tk()
top.title('Home Page')
top.geometry('1500x700')
top.resizable(True, True)

# Load and place background image
path = r"C:\Users\lanos\Downloads\python assignment\tech46-3.jpg"
bg_image = Image.open(path)
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(top, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def student():
    top.destroy()
    import student

def course():
    top.destroy()
    import course

def mentor():
    top.destroy()
    import mentor

def show_mentor():
    global tv
    tv = ttk.Treeview(top,height=18)
    tv['columns'] = ()
    tv['columns'] = ('MentorID','First Name', 'Last Name', 'Contact', 'Age', 'Email Id', 'Qualification', 'Subject', 'Experience', 'Gender')
    tv.column('#0', width=0, stretch=NO)
    tv.column('MentorID', anchor=CENTER, width=60)
    tv.column('First Name', anchor=CENTER, width=120)
    tv.column('Last Name', anchor=CENTER, width=120)
    tv.column('Contact', anchor=CENTER, width=120)
    tv.column('Age', anchor=CENTER, width=100)
    tv.column('Email Id', anchor=CENTER, width=150)
    tv.column('Qualification', anchor=CENTER, width=130)
    tv.column('Subject', anchor=CENTER, width=150)
    tv.column('Experience', anchor=CENTER, width=110)
    tv.column('Gender', anchor=CENTER, width=100)

    tv.heading('MentorID', text='ID', anchor=CENTER)
    tv.heading('First Name', text='First Name', anchor=CENTER)
    tv.heading('Last Name', text='Last Name', anchor=CENTER)
    tv.heading('Contact', text='Contact', anchor=CENTER)
    tv.heading('Age', text='Age', anchor=CENTER)
    tv.heading('Email Id', text='Email Id', anchor=CENTER)
    tv.heading('Qualification', text='Qualification', anchor=CENTER)
    tv.heading('Subject', text='Subject', anchor=CENTER)
    tv.heading('Experience', text='Experience', anchor=CENTER)
    tv.heading('Gender', text='Gender', anchor=CENTER)
    tv.place(x=50, y=250)
    for i in tv.get_children():
        tv.delete(i)
    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    cur.execute("SELECT MentorID,Firstname, Lastname, Contact, Age, Email, Qualification,Subject,Experience,Gender FROM mentors")
    result = cur.fetchall()
    for col in result:
        MentorID=col[0]
        Firstname = col[1]
        Lastname = col[2]
        Contact = col[3]
        Age = col[4]
        EmailId = col[5]
        Qualification = col[6]
        Subject= col[7]
        Experience= col[8]
        Gender= col[9]
        tv.insert("", "end", values=(MentorID,Firstname, Lastname, Contact, Age, EmailId, Qualification,Subject,Experience,Gender))

def Search():
    s7 = e6.get()
    for i in tv.get_children():
        tv.delete(i)
    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    s = "select * from mentors where Firstname=%s"
    cur.execute(s, s7)
    result = cur.fetchall()
    for col in result:
        Firstname = col[0]
        Lastname = col[1]
        Contact = col[2]
        Age = col[3]
        EmailId = col[4]
        Qualification = col[5]
        Subject= col[6]
        Experience= col[7]
        Gender= col[8]
        tv.insert("", "end", values=(Firstname, Lastname, Contact, Age, EmailId, Qualification,Subject,Experience,Gender))

def Search2():
    s7=e6.get()
    for i in tv.get_children():
        tv.delete(i)
    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    s="select * from courses where Course_name=%s"
    cur.execute(s,s7)
    result = cur.fetchall()
    for col in result:
        CourseName = col[0]
        TuitionFee = col[1]
        Duration = col[2]
        MentorName = col[3]
        TimeSlot = col[4]
        CourseMode = col[5]
        tv.insert("", 'end', values=(CourseName, TuitionFee, Duration, MentorName, TimeSlot, CourseMode))

def show_courses():
    global tv
    tv=ttk.Treeview(top,height=18)
    for i in tv.get_children():
        tv.delete(i)
    tv['columns'] = ('Course Name', 'Tuition Fee', 'Duration', 'Mentor Name', 'Time Slot', 'Course Mode')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Course Name', anchor=CENTER, width=200)
    tv.column('Tuition Fee', anchor=CENTER, width=200)
    tv.column('Duration', anchor=CENTER, width=200)
    tv.column('Mentor Name', anchor=CENTER, width=200)
    tv.column('Time Slot', anchor=CENTER, width=160)
    tv.column('Course Mode', anchor=CENTER, width=200)

    tv.heading('Course Name', text='Course Name', anchor=CENTER)
    tv.heading('Tuition Fee', text='Tuition Fee', anchor=CENTER)
    tv.heading('Duration', text='Duration', anchor=CENTER)
    tv.heading('Mentor Name', text='Mentor Name', anchor=CENTER)
    tv.heading('Time Slot', text='Time Slot', anchor=CENTER)
    tv.heading('Course Mode', text='Course Mode', anchor=CENTER)
    tv.place(x=50, y=250)


    db = sql.connect(host='localhost', user='root', password='DB_PASSWORD', db='project')
    cur = db.cursor()
    cur.execute("SELECT Course_name, Course_fee, Duration, Mentor, Time_slot, Course_mode FROM courses")
    result = cur.fetchall()
    for col in result:
        CourseName = col[0]
        TuitionFee = col[1]
        Duration=col[2]
        MentorName=col[3]
        TimeSlot=col[4]
        CourseMode=col[5]
        tv.insert("",'end',values=(CourseName, TuitionFee, Duration, MentorName, TimeSlot, CourseMode))
    db.close()

# Page Label
Label(top, text='Home Page', bg='white', fg='black', font=('Arial', 30, 'bold')).place(x=550, y=30)

# Buttons
Button(top, text='Mentor Registration', font=('Arial 18 bold'),command=mentor).place(x=50, y=100)
Button(top, text='Student Registration', font=('Arial 18 bold'),command=student).place(x=310, y=100)
Button(top, text='Courses', font=('Arial 18 bold'),command=show_courses).place(x=590, y=100)
Button(top, text='Add Course', font=('Arial 18 bold'),command=course).place(x=720, y=100)
Button(top, text='Show Mentor', font=('Arial 18 bold'),command=show_mentor).place(x=900, y=100)
Button(top, text='Close', font=('Arial 18 bold'), command=top.quit).place(x=1090, y=100)
Button(top, text='Search Mentor',font=('Arial 15 bold'), command=Search).place(x=370, y=200)
Button(top, text='Search Course',font=('Arial 15 bold'), command=Search2).place(x=540, y=200)


# Search section
e6= Entry(top, font=('Arial',20))
e6.place(x=50, y=200)

top.mainloop()
