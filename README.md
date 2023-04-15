# Predicted Grade Management System
### This is a flask application that IBDP schools can use to manage predicted grade calculations. 
### Access the test version [here](https://predictedgradetest.pythonanywhere.com) using the below credentials.
- Note: Not much student data is available here as it is a sample version. 
- Sample login for Admin:
  - UID = Admin
  - password = AdminTest
 - Sample login for Student:
  - UID = Student1
  - password = StudentTest
### Features
- It includes a login system that allows both students and teachers to log in.
- Students can view their grades for each subject upon logging in. Additionally, they can view what their current predicted grade is (based on grade boundaries, and weighted averages of the exams they have taken so far). The students' grades are saved in a hosted database, from which they are accessed.
- When teachers (or admins) log in, they are presented with 3 options:
  - **Manage Grade boundaries**: This option allows admins to individually modify the grade boundaries for each subject, at both Higher and Standard levels separately. After changing the grade boundaries, the updated grade boundaries are saved to the hosted database for future use.
  - **View Students' grades**: This option allows admins to view the Students' grades. Admins can either choose to view all students' total grades out of 42, or view individual grades for each subject.
  - **Upload grades**: This option allows admins to upload an excel file of a specific format containing student information (such as name, subject, and marks). The excel file is parsed, and student marks for each subject are saved to the hosted database. These are then visible through the **View Students' Grades** option.
  
