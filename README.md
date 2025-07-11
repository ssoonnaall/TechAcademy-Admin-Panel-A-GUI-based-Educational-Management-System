# Project Title: TechAcademy Admin Panel – A GUI-based Educational Management System
## 📌 Introduction: 
TechAcademy Admin Panel is a desktop-based Python application developed using Tkinter for GUI and MySQL for backend storage. It is designed to help educational institutes manage their admin users, mentors, students, and courses in an efficient and user-friendly manner.
## 🎯 Objective:
To create a centralized GUI system where an administrator can:
-	Register themselves securely
-	Login with credentials
-	Add and manage students, mentors, and courses
## 🧑‍💼 Who Can Use This Project?
This project is useful for:
-	Coaching institutes and training centers
-	Online education platforms
-	Administrative personnel managing course enrollment and faculty
## 🛠️ Technologies Used:
- Programming Language	 Python 3.x
- GUI Library	           Tkinter
- Database	             MySQL (via PyMySQL)
## 📂 Modules Overview:
### 1. Admin Registration
-	First-time registration of an admin user.
-	Validates fields like email, contact number, etc.
-	Stores credentials securely in the database.
### 2. Login Page
-	Admin can log in with previously registered credentials.
-	Invalid login attempts are handled gracefully.
-	Show/Hide password feature is provided.
### 3. Homepage
- **Dashboard with buttons to navigate to:**
  - Student Registration
  - Mentor Registration
  - Add Courses
  - Mentor Display
  - Courses Display
### 4. Student Registration
#### 	Allows admin to register new students.
- **Includes:**
- Auto age calculator based on DOB  
- Input validations for phone number and email  
- Dropdowns for state and gender selection
### 5. Mentor Registration
#### 	A dedicated form to register mentors.
- **Inputs include**:
-	Mentor name, contact, email
-	Qualification and experience
-	Assigned course and mode (Online/Offline)
### 6. Add Course
#### •	Admin can add new courses into the system.
- **Fields include:**
-	Course name, fee, duration
-	Time slot, mentor name, and mode of delivery
## 🚀 How to Run:
1.	Start with registration.py to register the admin.
2.	Then run login.py to log into the system.
3.	After login, homepage.py provides access to other features.
4.	Use respective buttons to open:
-	Student Registration
-	Mentor Registration
-	Course Management
