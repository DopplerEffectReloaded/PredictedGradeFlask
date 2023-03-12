from secret import db
cursor = db.cursor()

PE1_WEIGHTAGE = 0.1
PE2_WEIGHTAGE = 0.1
PE3_WEIGHTAGE = 0.3
PEY_WEIGHTAGE = 0.4

englishHL = [12, 28, 45, 58, 68, 82, 100]
englishSL = [12, 28, 44, 58, 68, 82, 100]
spanishBSL = [13, 29, 48, 61, 73, 86, 100]
frenchBSL = [14, 29, 46, 59, 72, 85, 100]
hindiBSL = [8, 19, 34, 48, 63, 78, 100]
spanishABSL = [11, 25, 41, 56, 70, 84, 100]
frenchABSL = [15, 33, 48, 61, 71, 83, 100]
math_aaHL = [3, 11, 23, 37, 52, 68, 100]
math_aiHL = [3, 9, 18, 32, 46, 61, 100]
math_aaSL = [3, 11, 22, 39, 57, 71, 100]
math_aiSL = [3, 12, 24, 38, 54, 69, 100]
physicsHL = [14, 25, 38, 48, 58, 68, 100]
physicsSL = [13, 24, 35, 45, 56, 66, 100]
chemistryHL = [15, 30, 42, 53, 65, 76, 100]
chemistrySL = [14, 28, 43, 54, 64, 75, 100]
biologyHL = [15, 27, 41, 54, 67, 80, 100]
biologySL = [14, 26, 41, 54, 65, 78, 100]
psychologyHL = [9, 19, 36, 49, 60, 74, 100]
psychologySL = [10, 22, 37, 49, 59, 71, 100]
digital_societiesHL = [12, 25, 40, 51, 60, 71, 100]
digital_societiesSL = [10, 22, 34, 46, 57, 69, 100]
global_politicsHL = [10, 21, 35, 47, 59, 72, 100]
global_politicsSL = [10, 22, 36, 45, 59, 68, 100]
visual_artsHL = [12, 25, 40, 54, 70, 84, 100]
visual_artsSL = [12, 25, 40, 53, 70, 84, 100]
economicsHL = [13, 26, 37, 49, 62, 74, 100]
economicsSL = [11, 25, 38, 50, 63, 75, 100]
business_managementHL = [13, 27, 37, 48, 57, 68, 100]
business_managementSL = [15, 32, 44, 53, 66, 76, 100]
computer_scienceHL = [15, 32, 44, 52, 60, 69, 100]
computer_scienceSL = [14, 20, 43, 51, 60, 68, 100]
essHL = [29, 39, 49, 59, 71, 84, 100]
essSL = [29, 39, 49, 59, 71, 84, 100]

subName = {
    'english' : 'English',
    'spanishB' : 'Spanish B',
    'frenchB' : 'French B',
    'hindiB' : 'Hindi B',
    'spanishAB' : 'Spanish AB',
    'frenchAB' : 'French AB',
    'math_aa' : 'Mathematics AA',
    'math_ai' : 'Mathematics AI',
    'physics' : 'Physics',
    'chemistry' : 'Chemistry',
    'biology' : 'Biology',
    'psychology' : 'Psychology',
    'digital_societies' : 'Digital Societies',
    'global_politics' : 'Global Politics',
    'visual_arts' : 'Visual Arts',
    'economics' : 'Economics',
    'business_management' : 'Business Management',
    'computer_science' : 'Computer Science',
    'ess' : 'ESS'
}

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

def is_admin(email, password):
    cursor.execute(f'select password from admin where uid=\'{(str(email))}\'')
    table_password = cursor.fetchall()
    if len(table_password) == 0:
        return 2
    table_password = table_password[0][0]
    if password == table_password:
        return 1
    else:
        return 0

def is_student(email, password):
    cursor.execute(f'select password from student where uid=\'{(str(email))}\'')
    table_password = cursor.fetchall()
    if len(table_password) == 0:
        return False
    table_password = table_password[0][0]
    if password == table_password:
        return True
    else:
        return False

def list_to_str(array):
    string = str(array[0])
    for i in range(1, len(array)):
        string += f' {array[i]}'
    return string

def str_to_list(string):
    Array = string.split(' ')
    for i in range(len(Array)): Array[i] = int(Array[i]) 
    return Array

def set_boundary(subName, boundary_list):
    boundary_string = list_to_str(boundary_list)
    subName = f'\'{subName}\''
    boundary_string = f'\'{boundary_string}\''
    cursor.execute(f'delete from boundaries where subName={subName}')
    cursor.execute(f'insert into boundaries (subName, boundary) values ({subName}, {boundary_string})')
    db.commit()
def get_boundary(subName):
    subName = f'\'{subName}\''
    cursor.execute(f'select boundary from boundaries where subName={subName}')
    boundary_string = cursor.fetchall()[0][0]
    boundary = str_to_list(boundary_string)
    return boundary
