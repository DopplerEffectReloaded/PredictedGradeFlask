from flask import Flask, request, render_template
from additional import *


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
   return render_template('index.html')

# @app.route('/newAccount', methods = ['GET', 'POST'])
# def newAccount():
#     return render_template('newAccount.html')

# @app.route('/accountDone', methods = ['GET', 'POST'])
# def accountDone():
#     email = request.form['email']
#     password = request.form['password']
#     if (('=' in email) or ('=' in password)):
#         return render_template('newAccount.html', message = "You cannot have '=' in your email id or password")

#     if (request.form['password'] != request.form['password_confirm']):
#         return render_template('newAccount.html', message = "The two passwords do not match")

#     try:
#         dummy = password_data[email]
#         return render_template('newAccount.html', message = "This account already exists")
        
#     except:

#         if (email[-12:] == 'chirec.ac.in'):

#             with open('password.txt', 'a') as data:
#                 data.write(f'\n{email}={password}')
#             with open("password.txt") as data:
#                 for line in data:
#                     name, var = line.partition("=")[::2]
#                     password_data[name.strip()] = var.strip()
#             return render_template('accountDone.html')
#         else:
#             return render_template('newAccount.html', message = "Please use an official CHIREC email id to register")
    
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
                return render_template('result.html', form = parse_db(email))
            else:
                return render_template('index.html', message = 'The username or password is incorrect')
        
@app.route('/manage_grades', methods=['GET', 'POST'])
def manage_grades():
    return render_template('manageBoundary.html')

@app.route('/view_grades', methods=['GET', 'POST'])
def view_grades():
    return render_template('gradeView.html')

@app.route('/boundary_set', methods=['GET', 'POST'])
def boundary_set():
    subject = request.form['subject']
    print(subject)
    if not request.form['grade_2'] or not request.form['grade_3'] or not request.form['grade_4'] or not request.form['grade_5'] or not request.form['grade_6'] or not request.form['grade_7']:
        boundary = globals().get(subject)
        message = f'Boundary for {subName[subject[:-2]]} {subject[-2:]} updated to 2019 grade boundaries.'
        
    else:
        boundary = [int(request.form['grade_2']) - 1, int(request.form['grade_3']) - 1, int(request.form['grade_4']) - 1, int(request.form['grade_5']) - 1, int(request.form['grade_6']) - 1, int(request.form['grade_7']) - 1, 100]
        for i in range(len(boundary) - 1):
            if boundary[i] >= boundary[i+1]:
                return render_template('boundarySet.html', subject_name = f'{subName[subject[:-2]]} {subject[-2:]}', subject = subject, message = 'Invalid grade boundaries entered.')
        message = f'Boundaries for {subName[subject[:-2]]} {subject[-2:]} updated'
    
    #  Save boundaries to mySQL table
    set_boundary(subject, boundary)
    return render_template('adminHome.html', message = message)

@app.route('/subject', methods=['GET', 'POST'])
def subject():
    curr_subject = request.form['subject']
    return render_template('boundarySet.html', subject_name = f'{subName[curr_subject[:-2]]} {curr_subject[-2:]}', subject = curr_subject)

@app.route('/result', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    
    subject1 = (request.form.get('Subject 1'))
    level1 = (request.form.get('Subject 1 Level'))
    pe1_1 = int(request.form.get('Subject 1 PE1')) if request.form.get('Subject 1 PE1') else None
    pe2_1 = int(request.form.get('Subject 1 PE2')) if request.form.get('Subject 1 PE2') else None
    pe3_1 = int(request.form.get('Subject 1 PE3')) if request.form.get('Subject 1 PE3') else None
    pey_1 = int(request.form.get('Subject 1 PEY2')) if request.form.get('Subject 1 PEY2') else None

    subject2 = (request.form.get('Subject 2'))
    level2 = (request.form.get('Subject 2 Level'))
    pe1_2 = int(request.form.get('Subject 2 PE1')) if request.form.get('Subject 2 PE1') else None
    pe2_2 = int(request.form.get('Subject 2 PE2')) if request.form.get('Subject 2 PE2') else None
    pe3_2 = int(request.form.get('Subject 2 PE3')) if request.form.get('Subject 2 PE3') else None
    pey_2 = int(request.form.get('Subject 2 PEY2')) if request.form.get('Subject 2 PEY2') else None

    subject3 = (request.form.get('Subject 3'))
    level3 = (request.form.get('Subject 3 Level'))
    pe1_3 = int(request.form.get('Subject 3 PE1')) if request.form.get('Subject 3 PE1') else None
    pe2_3 = int(request.form.get('Subject 3 PE2')) if request.form.get('Subject 3 PE2') else None
    pe3_3 = int(request.form.get('Subject 3 PE3')) if request.form.get('Subject 3 PE3') else None
    pey_3 = int(request.form.get('Subject 3 PEY2')) if request.form.get('Subject 3 PEY2') else None

    subject4 = (request.form.get('Subject 4'))
    level4 = (request.form.get('Subject 4 Level'))
    pe1_4 = int(request.form.get('Subject 4 PE1')) if request.form.get('Subject 4 PE1') else None
    pe2_4 = int(request.form.get('Subject 4 PE2')) if request.form.get('Subject 4 PE2') else None
    pe3_4 = int(request.form.get('Subject 4 PE3')) if request.form.get('Subject 4 PE3') else None
    pey_4 = int(request.form.get('Subject 4 PEY2')) if request.form.get('Subject 4 PEY2') else None

    subject5 = (request.form.get('Subject 5'))
    level5 = (request.form.get('Subject 5 Level'))
    pe1_5 = int(request.form.get('Subject 5 PE1')) if request.form.get('Subject 5 PE1') else None
    pe2_5 = int(request.form.get('Subject 5 PE2')) if request.form.get('Subject 5 PE2') else None
    pe3_5 = int(request.form.get('Subject 5 PE3')) if request.form.get('Subject 5 PE3') else None
    pey_5 = int(request.form.get('Subject 5 PEY2')) if request.form.get('Subject 5 PEY2') else None

    subject6 = (request.form.get('Subject 6'))
    level6 = (request.form.get('Subject 6 Level'))
    pe1_6 = int(request.form.get('Subject 6 PE1')) if request.form.get('Subject 6 PE1') else None
    pe2_6 = int(request.form.get('Subject 6 PE2')) if request.form.get('Subject 6 PE2') else None
    pe3_6 = int(request.form.get('Subject 6 PE3')) if request.form.get('Subject 6 PE3') else None
    pey_6 = int(request.form.get('Subject 6 PEY2')) if request.form.get('Subject 6 PEY2') else None

    # NO HL SUBJECTS : spanishB, frenchB, hindiB, spanishAB, frenchAB
    if ((subject1 == 'spanishB' or subject1 == 'frenchB' or subject1 == 'hindiB' or subject1 == 'spanishAB' or subject1 == 'frenchAB') and (level1 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 1")

    if ((subject2 == 'spanishB' or subject2 == 'frenchB' or subject2 == 'hindiB' or subject2 == 'spanishAB' or subject2 == 'frenchAB') and (level2 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 2")
    
    if ((subject3 == 'spanishB' or subject3 == 'frenchB' or subject3 == 'hindiB' or subject3 == 'spanishAB' or subject3 == 'frenchAB') and (level3 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 3")

    if ((subject4 == 'spanishB' or subject4 == 'frenchB' or subject4 == 'hindiB' or subject4 == 'spanishAB' or subject4 == 'frenchAB') and (level4 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 4")

    if ((subject5 == 'spanishB' or subject5 == 'frenchB' or subject5 == 'hindiB' or subject5 == 'spanishAB' or subject5 == 'frenchAB') and (level5 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 5")

    if ((subject6 == 'spanishB' or subject6 == 'frenchB' or subject6 == 'hindiB' or subject6 == 'spanishAB' or subject6 == 'frenchAB') and (level6 == 'HL')):
        return render_template('inputForm.html', message = "Invalid subject-level combination entered in subject 6")
    
    form_values = {}

    # SUBJECT 1
    if ((subject1 and level1 and pe1_1)):
        key = subject1 + level1
        temp = Predictor(pe1_1, pe2_1, pe3_1, pey_1, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_1'] = f'{subName[subject1]} {level1}'
        form_values['sub1_grade'] = temp[0]
        form_values['sub1_nextGrade'] = temp[1]
        form_values['sub1_nextMarks'] = temp[2]
    else:
        form_values['subject_1'] = 'Incomplete information provided'
        form_values['sub1_grade'] = 'Incomplete information provided'
        form_values['sub1_nextGrade'] = 'Incomplete information provided'
        form_values['sub1_nextMarks'] = 'Incomplete information provided'
    
    # SUBJECT 2
    if ((subject2 and level2 and pe1_2)):
        key = subject2 + level2
        temp = Predictor(pe1_2, pe2_2, pe3_2, pey_2, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_2'] = f'{subName[subject2]} {level2}'
        form_values['sub2_grade'] = temp[0]
        form_values['sub2_nextGrade'] = temp[1]
        form_values['sub2_nextMarks'] = temp[2]
    else:
        form_values['subject_2'] = 'Incomplete information provided'
        form_values['sub2_grade'] = 'Incomplete information provided'
        form_values['sub2_nextGrade'] = 'Incomplete information provided'
        form_values['sub2_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 3
    if ((subject3 and level3 and pe1_3)):
        key = subject3 + level3
        temp = Predictor(pe1_3, pe2_3, pe3_3, pey_3, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_3'] = f'{subName[subject3]} {level3}'
        form_values['sub3_grade'] = temp[0]
        form_values['sub3_nextGrade'] = temp[1]
        form_values['sub3_nextMarks'] = temp[2]
    else:
        form_values['subject_3'] = 'Incomplete information provided'
        form_values['sub3_grade'] = 'Incomplete information provided'
        form_values['sub3_nextGrade'] = 'Incomplete information provided'
        form_values['sub3_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 4
    if ((subject4 and level4 and pe1_4)):
        key = subject4 + level4
        temp = Predictor(pe1_4, pe2_4, pe3_4, pey_4, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_4'] = f'{subName[subject4]} {level4}'
        form_values['sub4_grade'] = temp[0]
        form_values['sub4_nextGrade'] = temp[1]
        form_values['sub4_nextMarks'] = temp[2]
    else:
        form_values['subject_4'] = 'Incomplete information provided'
        form_values['sub4_grade'] = 'Incomplete information provided'
        form_values['sub4_nextGrade'] = 'Incomplete information provided'
        form_values['sub4_nextMarks'] = 'Incomplete information provided'


    # SUBJECT 5
    if ((subject5 and level5 and pe1_5)):
        key = subject5 + level5
        temp = Predictor(pe1_5, pe2_5, pe3_5, pey_5, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_5'] = f'{subName[subject5]} {level5}'
        form_values['sub5_grade'] = temp[0]
        form_values['sub5_nextGrade'] = temp[1]
        form_values['sub5_nextMarks'] = temp[2]
    else:
        form_values['subject_5'] = 'Incomplete information provided'
        form_values['sub5_grade'] = 'Incomplete information provided'
        form_values['sub5_nextGrade'] = 'Incomplete information provided'
        form_values['sub5_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 6
    if ((subject6 and level6 and pe1_6)):
        key = subject6 + level6
        temp = Predictor(pe1_6, pe2_6, pe3_6, pey_6, get_boundary(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_6'] = f'{subName[subject6]} {level6}'
        form_values['sub6_grade'] = temp[0]
        form_values['sub6_nextGrade'] = temp[1]
        form_values['sub6_nextMarks'] = temp[2]

    else:
        form_values['subject_6'] = 'Incomplete information provided'
        form_values['sub6_grade'] = 'Incomplete information provided'
        form_values['sub6_nextGrade'] = 'Incomplete information provided'
        form_values['sub6_nextMarks'] = 'Incomplete information provided'
        
    return render_template('result.html', form = form_values) 
    

if __name__ == '__main__':
  app.run()
