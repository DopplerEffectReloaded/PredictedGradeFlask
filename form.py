from flask import Flask, request, render_template

password_data = {}
with open("password.txt") as data:
    for line in data:
        name, var = line.partition("=")[::2]
        password_data[name.strip()] = var


PE1_WEIGHTAGE = 0.1
PE2_WEIGHTAGE = 0.1
PE3_WEIGHTAGE = 0.3
PEY_WEIGHTAGE = 0.4
# Cases to handle: hindiHL, spanishABHL, frenchABHL, spanishBHL, frenchBHL, ESS
englishHL = [12, 25, 35, 49, 61, 76, 100]
englishSL = [9, 22, 34, 45, 59, 76, 100]
spanishBSL = [5, 11, 24, 40, 56, 74, 100]
frenchBSL = [9, 20, 32, 48, 64, 79, 100]
hindiBSL = [8, 19, 34, 48, 63, 78, 100]
spanishABSL = [11, 22, 34, 49, 62, 77, 100]
frenchABSL = [10, 22, 36, 52, 65, 81, 100]
math_aaHL = [3, 11, 23, 37, 52, 68, 100]
math_aiHL = [3, 9, 18, 32, 46, 61, 100]
math_aaSL = [3, 11, 22, 39, 57, 71, 100]
math_aiSL = [3, 12, 24, 38, 54, 69, 100]
physicsHL = [13, 19, 28, 38, 53, 68, 100]
physicsSL = [9, 14, 25, 36, 49, 62, 100]
chemistryHL = [14, 19, 34, 49, 66, 79, 100]
chemistrySL = [4, 9, 23, 45, 60, 75, 100]
biologyHL = [15, 23, 33, 46, 58, 75, 100]
biologySL = [11, 21, 30, 43, 58, 74, 100]
psychologyHL = [7, 16, 28, 41, 52, 65, 100]
psychologySL = [5, 11, 18, 35, 49, 65, 100]
digital_societiesHL = [29, 39, 49, 59, 71, 84, 100]
digital_societiesSL = [29, 39, 49, 59, 71, 84, 100]
global_politicsHL = [9, 19, 28, 39, 50, 61, 100]
global_politicsSL = [6, 18, 28, 37, 48, 58, 100]
visual_artsHL = [7, 17, 33, 47, 62, 76, 100]
visual_artsSL = [8, 17, 31, 45, 62, 76, 100]
economicsHL = [8, 17, 26, 39, 53, 66, 100]
economicsSL = [9, 19, 30, 43, 58, 71, 100]
business_managementHL = [10, 24, 33, 45, 54, 64, 100]
business_managementSL = [9, 17, 26, 39, 53, 66, 100]
computer_scienceHL = [10, 15, 21, 34, 48, 62, 100]
computer_scienceSL = [5, 10, 26, 36, 48, 61, 100]
essSL = [29, 39, 49, 59, 71, 84, 100]
essHL = [29, 39, 49, 59, 71, 84, 100]

def Predictor(PE1, PE2, PE3, PE_Y2, sub_grade, weightagePE1, weightagePE2, weightagePE3, weightagePE1Y2):
    '''This function takes your marks as input and then predicts 
    how many marks you need to obtain in your next exam to get the next grade according to the 
    IB grade boundaries for all the exams'''
    
    if PE2 is None:

        current_grade = 1           
        for i in range(0, 7):
            
            d = sub_grade[i]

            if weightagePE1*PE1 >= weightagePE1*d:
                current_grade += 1

        future_grade  = current_grade + 1
        if (future_grade - 7) >= 1:
            future_grade = 7

            
        boundary = sub_grade[future_grade-2]
        future_marks = ((boundary*(weightagePE1+weightagePE2))-weightagePE1*PE1)/weightagePE2
        return ([current_grade, future_grade, round(future_marks, 1)])

    elif PE3 is None:
        y = weightagePE1*PE1 + weightagePE2*PE2   
        current_grade = 1
        for i in range(0, 7):

            f = sub_grade[i]

            if (weightagePE1*PE1 + weightagePE2*PE2) >= (weightagePE1*f) + (weightagePE2*f):
                current_grade += 1

        future_grade  = current_grade + 1
        if (future_grade - 7) >= 1:
            future_grade = 7
        
        boundary = sub_grade[future_grade-2]
        future_marks = ((boundary*(weightagePE1+weightagePE2+weightagePE3)) - y)/weightagePE3
        return ([current_grade, future_grade, round(future_marks, 1)])
    
    elif PE_Y2 is None:
        z = weightagePE1*PE1 + weightagePE2*PE2 + weightagePE3*PE3
        current_grade = 1
        for i in range(0, 7):

            j = sub_grade[i]

            if z >= (weightagePE1*j) + (weightagePE2*j) + (weightagePE3*j):
                current_grade += 1

        future_grade  = current_grade + 1
        if (future_grade - 7) >= 1:
            future_grade = 7
        
        boundary = sub_grade[future_grade-2]
        future_marks = ((boundary*(weightagePE1+weightagePE2+weightagePE3+weightagePE1Y2)) - z)/weightagePE1Y2
        return ([current_grade, future_grade, round(future_marks, 1)])
    else:
        z = weightagePE1*PE1 + weightagePE2*PE2 + weightagePE3*PE3 + weightagePE1Y2*PE_Y2
        current_grade = 1
        for i in range(0, 7):

            j = sub_grade[i]

            if z >= (weightagePE1*j) + (weightagePE2*j) + (weightagePE3*j) + (weightagePE1Y2*j):
                current_grade += 1
            future_grade = 'N/A, all exams have been taken'
            future_marks = 'N/A, all exams have been taken'
        return ([current_grade, future_grade, future_marks])



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
   return render_template('index.html')


@app.route('/newAccount', methods = ['GET', 'POST'])
def newAccount():
    return render_template('newAccount.html')


@app.route('/accountDone', methods = ['GET', 'POST'])
def accountDone():
    email = request.form['email']
    password = request.form['password']
    print(password)
    # cursor.execute(f'')

    if (request.form['password'] != request.form['password_confirm']):
        return render_template('newAccount.html', message = "The two passwords do not match")

    try:
        dummy = password_data[email]
        return render_template('newAccount.html', message = "This account already exists")
        
    except:

        if (email[-12:] == 'chirec.ac.in'):

            with open('password.txt', 'a') as data:
                data.write(f'\n{email}={password}')
            with open("password.txt") as data:
                for line in data:
                    name, var = line.partition("=")[::2]
                    password_data[name.strip()] = var
            return render_template('accountDone.html')
        else:
            return render_template('newAccount.html', message = "Please use an official CHIREC email id to register")
    
    # for i in data:
    #     em, pwd = i.split('=') 
    #     if em == email:
    #         return render_template('newAccount.html', message = "This account already exists")
    #     else:
    #         data.write(f'{email}={password}\n')
    #         return render_template('accountDone.html')
            
    # try:
        
        
    #     cursor.execute(f'insert into password (Email, Password) values(\'{str(email)}\', \'{str(password)}\')')
    #     db.commit()
    #     return render_template('accountDone.html')
    # except mysql.connector.IntegrityError:
        # return render_template('newAccount.html', message = "This account already exists")



@app.route('/input', methods = ['GET', 'POST'])
def input():
    if request.method == 'POST':
        email = str(request.form['email'])
        # cursor.execute(f'select Password from password where email=\'{(str(email))}\'')
        # res = str(cursor.fetchall())
        # res = res[3:-4]
        try:
            file_pass = password_data[email]
        except:
            return render_template('index.html', message = "Login failed, try again")


        if (str(request.form['password']) == file_pass):
            # insert form prepopulation logic - EXAMPLE
            # form_values = {
            #     'name': 'John Doe',
            #     'email': 'johndoe@gmail.com',
            #     'phone': '123-456-7890'
            # }
            # return render_template('form.html', form=form_values)


            return render_template('inputForm.html')
        else:
            return render_template('index.html', message = "Login failed, try again")



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
    pe3_2 = int(request.form.get('Subject 2 PE3')) if request.form.get('Subject 3 PE3') else None
    pey_2 = int(request.form.get('Subject 2 PEY2')) if request.form.get('Subject 3 PEY2') else None

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
    pe3_4 = int(request.form.get('Subject 4 PE3')) if request.form.get('Subject 4 PE2') else None
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
    
    # subject1 = request.form['Subject 1'] if request.form['Subject 1'] else None
    # level1 = request.form['Subject 1 Level'] if request.form['Subject 1 Level'] else None
    # pe1_1 = int(request.form['Subject 1 PE1']) if request.form['Subject 1 PE1'] else None
    # pe2_1 = int(request.form['Subject 1 PE2']) if request.form['Subject 1 PE2'] else None
    # pe3_1 = int(request.form['Subject 1 PE3']) if request.form['Subject 1 PE3'] else None
    # pey_1 = int(request.form['Subject 1 PEY2']) if request.form['Subject 1 PEY2'] else None
    # print(request.form['Subject 2'])
    # subject2 = request.form['Subject 2'] if request.form['Subject 2'] else None
    # print(subject2)
    # level2 = request.form['Subject 2 Level'] if request.form['Subject 2 Level'] else None
    # pe1_2 = int(request.form['Subject 2 PE1']) if request.form['Subject 2 PE1'] else None
    # pe2_2 = int(request.form['Subject 2 PE2']) if request.form['Subject 2 PE2'] else None
    # pe3_2 = int(request.form['Subject 2 PE3']) if request.form['Subject 2 PE3'] else None
    # pey_2 = int(request.form['Subject 2 PEY2']) if request.form['Subject 2 PEY2'] else None
    # subject3 = request.form['Subject 3'] if request.form['Subject 3'] else None
    # level3 = request.form['Subject 3 Level'] if request.form['Subject 3 Level'] else None
    # pe1_3 = int(request.form['Subject 3 PE1']) if request.form['Subject 3 PE1'] else None
    # pe2_3 = int(request.form['Subject 3 PE2']) if request.form['Subject 3 PE2'] else None
    # pe3_3 = int(request.form['Subject 3 PE3']) if request.form['Subject 3 PE3'] else None
    # pey_3 = int(request.form['Subject 3 PEY2']) if request.form['Subject 3 PEY2'] else None
    # subject4 = request.form['Subject 4'] if request.form['Subject 4'] else None
    # level4 = request.form['Subject 4 Level'] if request.form['Subject 4 Level'] else None
    # pe1_4 = int(request.form['Subject 4 PE1']) if request.form['Subject 4 PE1'] else None
    # pe2_4 = int(request.form['Subject 4 PE2']) if request.form['Subject 4 PE2'] else None
    # pe3_4 = int(request.form['Subject 4 PE3']) if request.form['Subject 4 PE3'] else None
    # pey_4 = int(request.form['Subject 4 PEY2']) if request.form['Subject 4 PEY2'] else None
    # subject5 = request.form['Subject 5'] if request.form['Subject 5'] else None
    # level5 = request.form['Subject 5 Level'] if request.form['Subject 5 Level'] else None
    # pe1_5 = int(request.form['Subject 5 PE1']) if request.form['Subject 5 PE1'] else None
    # pe2_5 = int(request.form['Subject 5 PE2']) if request.form['Subject 5 PE2'] else None
    # pe3_5 = int(request.form['Subject 5 PE3']) if request.form['Subject 5 PE3'] else None
    # pey_5 = int(request.form['Subject 5 PEY2']) if request.form['Subject 5 PEY2'] else None
    # subject6 = request.form['Subject 6'] if request.form['Subject 6'] else None
    # level6 = request.form['Subject 6 Level'] if request.form['Subject 6 Level'] else None
    # pe1_6 = int(request.form['Subject 6 PE1']) if request.form['Subject 6 PE1'] else None
    # pe2_6 = int(request.form['Subject 6 PE2']) if request.form['Subject 6 PE2'] else None
    # pe3_6 = int(request.form['Subject 6 PE3']) if request.form['Subject 6 PE3'] else None
    # pey_6 = int(request.form['Subject 6 PEY2']) if request.form['Subject 6 PEY2'] else None


    form_values = {}

    # SUBJECT 1
    if ((subject1 and level1 and pe1_1)):
        key = subject1 + level1
        temp = Predictor(pe1_1, pe2_1, pe3_1, pey_1, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        print(temp)
        form_values['subject_1'] = f'{subject1} {level1}'
        form_values['sub_1_grade'] = temp[0]
        form_values['sub1_nextGrade'] = temp[1]
        form_values['sub1_nextMarks'] = temp[2]
    else:
        form_values['subject_1'] = 'Incomplete information provided'
        form_values['sub_1_grade'] = 'Incomplete information provided'
        form_values['sub1_nextGrade'] = 'Incomplete information provided'
        form_values['sub1_nextMarks'] = 'Incomplete information provided'
    
    # SUBJECT 2
    if ((subject2 and level2 and pe1_2)):
        key = subject2 + level2
        temp = Predictor(pe1_2, pe2_2, pe3_2, pey_2, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_2'] = f'{subject2} {level2}'
        form_values['sub_2_grade'] = temp[0]
        form_values['sub2_nextGrade'] = temp[1]
        form_values['sub2_nextMarks'] = temp[2]
    else:
        form_values['subject_2'] = 'Incomplete information provided'
        form_values['sub_2_grade'] = 'Incomplete information provided'
        form_values['sub2_nextGrade'] = 'Incomplete information provided'
        form_values['sub2_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 3
    if ((subject3 and level3 and pe1_3)):
        key = subject3 + level3
        temp = Predictor(pe1_3, pe2_3, pe3_3, pey_3, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_3'] = f'{subject3} {level3}'
        form_values['sub_3_grade'] = temp[0]
        form_values['sub3_nextGrade'] = temp[1]
        form_values['sub3_nextMarks'] = temp[2]
    else:
        form_values['subject_3'] = 'Incomplete information provided'
        form_values['sub_3_grade'] = 'Incomplete information provided'
        form_values['sub3_nextGrade'] = 'Incomplete information provided'
        form_values['sub3_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 4
    if ((subject4 and level4 and pe1_4)):
        key = subject4 + level4
        temp = Predictor(pe1_4, pe2_4, pe3_4, pey_4, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_4'] = f'{subject4} {level4}'
        form_values['sub_4_grade'] = temp[0]
        form_values['sub4_nextGrade'] = temp[1]
        form_values['sub4_nextMarks'] = temp[2]
    else:
        form_values['subject_4'] = 'Incomplete information provided'
        form_values['sub_4_grade'] = 'Incomplete information provided'
        form_values['sub4_nextGrade'] = 'Incomplete information provided'
        form_values['sub4_nextMarks'] = 'Incomplete information provided'


    # SUBJECT 5
    if ((subject5 and level5 and pe1_5)):
        key = subject5 + level5
        temp = Predictor(pe1_5, pe2_5, pe3_5, pey_5, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_5'] = f'{subject5} {level5}'
        form_values['sub_5_grade'] = temp[0]
        form_values['sub5_nextGrade'] = temp[1]
        form_values['sub5_nextMarks'] = temp[2]
    else:
        form_values['subject_5'] = 'Incomplete information provided'
        form_values['sub_5_grade'] = 'Incomplete information provided'
        form_values['sub5_nextGrade'] = 'Incomplete information provided'
        form_values['sub5_nextMarks'] = 'Incomplete information provided'

    # SUBJECT 6 finally :)
    if ((subject6 and level6 and pe1_6)):
        key = subject6 + level6
        temp = Predictor(pe1_6, pe2_6, pe3_6, pey_6, globals().get(key), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
        form_values['subject_6'] = f'{subject6} {level6}'
        form_values['sub_6_grade'] = temp[0]
        form_values['sub6_nextGrade'] = temp[1]
        form_values['sub6_nextMarks'] = temp[2]

    else:
        form_values['subject_6'] = 'Incomplete information provided'
        form_values['sub_6_grade'] = 'Incomplete information provided'
        form_values['sub6_nextGrade'] = 'Incomplete information provided'
        form_values['sub6_nextMarks'] = 'Incomplete information provided'
        
    return render_template('result.html', form = form_values) 
    
    
    # return f'Subject 1: {subject1} ({level1}) \n PE1: {pe1_1} \n PE2: {pe2_1} \n PE3: {pe3_1} \n PEY2: {pey_1} \n Subject 2: {subject2} ({level2}) \n PE1: {pe1_2} \n PE2: {pe2_2} \n PE3: {pe3_2} \n PEY2: {pey_2} \n Subject 3: {subject3} ({level3}) \n PE1: {pe1_3} \n PE2: {pe2_3} \n PE3: {pe3_3} \n PEY2: {pey_3} \n Subject 4: {subject4} ({level4}) \n PE1: {pe1_4} \n PE2: {pe2_4} \n PE3: {pe3_4} \n PEY2: {pey_4} \n Subject 5: {subject5} ({level5}) \n PE1: {pe1_5} \n PE2: {pe2_5} \n PE3: {pe3_5} \n PEY2: {pey_5} \n Subject 6: {subject6} ({level6}) \n PE1: {pe1_6} \n PE2: {pe2_6} \n PE3: {pe3_6} \n PEY2: {pey_6} \n'
    

if __name__ == '__main__':
  app.run()
