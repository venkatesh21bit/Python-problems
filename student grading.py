students=[]
def add_student():
    stu_name=input()
    grades = input().split(',')
    tuple = (stu_name,grades)
    students.append(tuple)
def avg_grade():
    No=len
    
    
add_student()
print(students)
avg_grade()
print(No)
