from secret import db_details
import mysql.connector
import pandas, openpyxl

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
    
    if PE1 is None:
        return ('Incomplete information', 'Incomplete information', 'Incomplete information')
    
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
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    cursor.execute(f'select password from admin where uid=\'{(str(email))}\'')
    table_password = cursor.fetchall()
    cursor.close()
    db.close()
    if len(table_password) == 0:
        return 2
    table_password = table_password[0][0]
    if password == table_password:
        return 1
    else:
        return 0

def is_student(email, password):
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    cursor.execute(f'select password from student where uid=\'{(str(email))}\'')
    table_password = cursor.fetchall()
    cursor.close()
    db.close()
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
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    boundary_string = list_to_str(boundary_list)
    subName = f'\'{subName}\''
    boundary_string = f'\'{boundary_string}\''
    cursor.execute(f'delete from boundaries where subName={subName}')
    cursor.execute(f'insert into boundaries (subName, boundary) values ({subName}, {boundary_string})')
    db.commit()
    cursor.close()
    db.close()
def get_boundary(subName):
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    subName = f'\'{subName}\''
    cursor.execute(f'select boundary from boundaries where subName={subName}')
    boundary_string = cursor.fetchall()[0][0]
    cursor.close()
    db.close()
    boundary = str_to_list(boundary_string)
    return boundary

def parse_db(uid):
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    uid = f'\'{uid}\''
    cursor.execute(f'select * from marks where uid = {uid}')
    db_data = cursor.fetchall()[0][1:]
    cursor.close()
    db.close()
    
    temp_1 = Predictor(db_data[1], db_data[2], db_data[3], db_data[4], get_boundary(db_data[0]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
    temp_2 = Predictor(db_data[6], db_data[7], db_data[8], db_data[9], get_boundary(db_data[5]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
    temp_3 = Predictor(db_data[11], db_data[12], db_data[13], db_data[14], get_boundary(db_data[10]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
    temp_4 = Predictor(db_data[16], db_data[17], db_data[18], db_data[19], get_boundary(db_data[15]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
    temp_5 = Predictor(db_data[21], db_data[22], db_data[23], db_data[24], get_boundary(db_data[20]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)
    temp_6 = Predictor(db_data[26], db_data[27], db_data[28], db_data[29], get_boundary(db_data[25]), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)

    form_values = {     'subject_1': f'{subName[db_data[0][:-2]]} {db_data[0][-2:]}',
                        'sub1_PE1': db_data[1],
                        'sub1_PE2': db_data[2],
                        'sub1_PE3': db_data[3],
                        'sub1_PEY2': db_data[4],
                        'sub1_grade': temp_1[0],
                        'sub1_nextGrade': temp_1[1],
                        'sub1_nextMarks': temp_1[2],
                        'subject_2': f'{subName[db_data[5][:-2]]} {db_data[5][-2:]}',
                        'sub2_PE1': db_data[6],
                        'sub2_PE2': db_data[7],
                        'sub2_PE3': db_data[8],
                        'sub2_PEY2': db_data[9],
                        'sub2_grade': temp_2[0],
                        'sub2_nextGrade': temp_2[1],
                        'sub2_nextMarks': temp_2[2],
                        'subject_3': f'{subName[db_data[10][:-2]]} {db_data[10][-2:]}',
                        'sub3_PE1': db_data[11],
                        'sub3_PE2': db_data[12],
                        'sub3_PE3': db_data[13],
                        'sub3_PEY2': db_data[14],
                        'sub3_grade': temp_3[0],
                        'sub3_nextGrade': temp_3[1],
                        'sub3_nextMarks': temp_3[2],
                        'subject_4': f'{subName[db_data[15][:-2]]} {db_data[15][-2:]}',
                        'sub4_PE1': db_data[16],
                        'sub4_PE2': db_data[17],
                        'sub4_PE3': db_data[18],
                        'sub4_PEY2': db_data[19],
                        'sub4_grade': temp_4[0],
                        'sub4_nextGrade': temp_4[1],
                        'sub4_nextMarks': temp_4[2],
                        'subject_5': f'{subName[db_data[20][:-2]]} {db_data[20][-2:]}',
                        'sub5_PE1': db_data[21],
                        'sub5_PE2': db_data[22],
                        'sub5_PE3': db_data[23],
                        'sub5_PEY2': db_data[24],
                        'sub5_grade': temp_5[0],
                        'sub5_nextGrade': temp_5[1],
                        'sub5_nextMarks': temp_5[2],
                        'subject_6': f'{subName[db_data[25][:-2]]} {db_data[25][-2:]}',
                        'sub6_PE1': db_data[26],
                        'sub6_PE2': db_data[27],
                        'sub6_PE3': db_data[28],
                        'sub6_PEY2': db_data[29],
                        'sub6_grade': temp_6[0],
                        'sub6_nextGrade': temp_6[1],
                        'sub6_nextMarks': temp_6[2],
                        }
    return form_values

def get_grades(subject):
    db = mysql.connector.connect(**db_details)
    cursor = db.cursor()
    sqlsubject = f'\'{subject}\''
    grades = []
    cursor.execute(f'select uid, sub1_pe1, sub1_pe2, sub1_pe3, sub1_pey2 from marks where sub1 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.execute(f'select uid, sub2_pe1, sub2_pe2, sub2_pe3, sub2_pey2 from marks where sub2 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.execute(f'select uid, sub3_pe1, sub3_pe2, sub3_pe3, sub3_pey2 from marks where sub3 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.execute(f'select uid, sub4_pe1, sub4_pe2, sub4_pe3, sub4_pey2 from marks where sub4 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.execute(f'select uid, sub5_pe1, sub5_pe2, sub5_pe3, sub5_pey2 from marks where sub5 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.execute(f'select uid, sub6_pe1, sub6_pe2, sub6_pe3, sub6_pey2 from marks where sub6 = {sqlsubject}')
    for i in cursor.fetchall(): grades.append(i)
    cursor.close()
    db.close()
    for i in range(len(grades)):
        grades[i] = list(grades[i])
        grades[i].append(Predictor(grades[i][1], grades[i][2], grades[i][3], grades[i][4], get_boundary(subject), PE1_WEIGHTAGE, PE2_WEIGHTAGE, PE3_WEIGHTAGE, PEY_WEIGHTAGE)[0])
    return grades

