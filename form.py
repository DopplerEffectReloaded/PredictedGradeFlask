from flask import Flask, request, render_template
import openpyxl
from additional import *


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
   return render_template('index.html')
    
@app.route('/input', methods = ['GET', 'POST'])
def input():
    if request.method == 'POST':
        email = str(request.form['uid'])
        password = str(request.form['password'])
        # Check if account details match admin account
        admin = is_admin(email, password)
        if admin == 0: # Admin login incorrect password
            return render_template('index.html', message = "Password is incorrect")
        elif admin == 1: # Admin login correct password
            return render_template('adminHome.html')
        else:
            # Check for student login
            if is_student(email, password):
                return render_template('result.html', form = parse_db(email), name = email)
            else:
                return render_template('index.html', message = 'The username or password is incorrect')
        
@app.route('/manage_grades', methods=['GET', 'POST'])
def manage_grades():
    if request.method == 'POST':
        return render_template('manageBoundary.html')

@app.route('/view_grades', methods=['GET', 'POST'])
def view_grades_menu():
    if request.method == 'POST':
        return render_template('gradeSelect.html')
    return render_template('gradeSelect.html')

@app.route('/view_grade_subject', methods = ['GET', 'POST'])
def view_grades():
    if request.method == 'POST':
        return render_template('gradeViewSelect.html')

@app.route('/view_grades/subject', methods=['GET', 'POST'])
def view_grades_subject():
    if request.method == 'POST':
        subject = request.form['subject']
        return render_template('gradeView.html', subject = f'{subName[subject[:-2]]} {subject[-2:]}', data = get_grades(subject))

@app.route('/view_grades/all', methods = ['GET', 'POST'])
def view_all_grades():
    if request.method == 'POST':
        return render_template('grade_Students.html', data = get_final_grades())


@app.route('/boundary_set', methods=['GET', 'POST'])
def boundary_set():
    if request.method == 'POST':
        subject = request.form['subject']
        if not request.form['grade_2'] or not request.form['grade_3'] or not request.form['grade_4'] or not request.form['grade_5'] or not request.form['grade_6'] or not request.form['grade_7']:
            boundary = globals().get(subject)
            message = f'Boundary for {subName[subject[:-2]]} {subject[-2:]} updated to 2023 grade boundaries.'
            
        else:
            boundary = [int(request.form['grade_2']) - 1, int(request.form['grade_3']) - 1, int(request.form['grade_4']) - 1, int(request.form['grade_5']) - 1, int(request.form['grade_6']) - 1, int(request.form['grade_7']) - 1, 100]
            for i in range(len(boundary) - 1):
                if boundary[i] >= boundary[i+1]:
                    return render_template('boundarySet.html', subject_name = f'{subName[subject[:-2]]} {subject[-2:]}', subject = subject, message = 'Invalid grade boundaries entered.')
            message = f'Boundaries for {subName[subject[:-2]]} {subject[-2:]} updated'
        
        #  Save boundaries to mySQL table
        set_boundary(subject, boundary)
        return render_template('adminHome.html', message = message)

@app.route('/upload_grades', methods = ['GET', 'POST'])
def upload_grades():
    if request.method == 'POST':
        return render_template('upload_grades.html')
    
@app.route('/upload_grades/finish', methods = ['GET', 'POST'])
def finish():
    if request.method == 'POST':
        file = request.files['excel-file']
        xls = openpyxl.load_workbook(file)
        data = xls.active
        
        try:
            student_grade(data)
            return render_template('adminHome.html', message = 'Grades entered successfully')
        except:
            return render_template('adminHome.html', message = 'There was an error. Please check the format and contents of your excel file again.')
    
@app.route('/back', methods = ['GET', 'POST'])
def back():
    if request.method == 'POST':
        return render_template('adminHome.html')

@app.route('/subject', methods=['GET', 'POST'])
def subject():
    if request.method == 'POST':
        curr_subject = request.form['subject']
        boundary = get_boundary(curr_subject)[:-1]
        for i in range(len(boundary)): boundary[i] += 1
        return render_template('boundarySet.html', subject_name = f'{subName[curr_subject[:-2]]} {curr_subject[-2:]}', subject = curr_subject, current_boundaries = boundary)  

if __name__ == '__main__':
  app.run()
