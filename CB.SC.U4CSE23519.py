employees=[]
print('The number of employees')
no_employees=int(input())
def add_employee():
    for employee in range (no_employees):
        employee_id=input()
        employee_name=input()
        employee_position=input()
        employee_salary=int(input())
        tuple=(employee_id,employee_name,employee_position,employee_salary)
        employees.append(tuple)
    
def high_salary():
    for high_sal in employees:
        for i in range(3,no_employees,3):
            emp_salary=[]
            emp_salary.append(employees[i])
            high_salary=max(emp_salary)
            print(high_salary)
            for j in range (no_employees):
                if high_salary == employees[j]:
                    details=(employees[j-3:j-1])
                    print('The details of the employee:' , details)
                
            
            

def dis_employee():
    print(employees)
        
add_employee()
print('To know the employee with highest salary enter HIGH')
print('To display the employees details enter DISPLAY')
k=input()
h=input()
if k==HIGH:
    high_salary

if h==DISPLAY:
    dis_employee()

    
    
    
    
