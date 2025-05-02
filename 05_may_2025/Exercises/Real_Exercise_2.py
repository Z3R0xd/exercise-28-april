class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.__id = emp_id
        self.__name = emp_name
        self.__salary = emp_salary
        self.__department = emp_department
        
    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50 :
            overtime = hours_worked-50
            salary =+ overtime*(salary/50)
        self.__salary = salary
    
    def assign_department(self, department):
        self.__department = department
    
    def print_employee_details(self):
        print(f"Name : {self.__name}\nID : {self.__id}\nSalary : {self.__salary}\nDepartment : {self.__department}")
        
        
Name = input("Name : ")
ID = input("ID : ")
Salary = int(input("Salary : "))
Department = input("Department : ")

employee = Employee(ID,Name,Salary,Department)

employee.print_employee_details()