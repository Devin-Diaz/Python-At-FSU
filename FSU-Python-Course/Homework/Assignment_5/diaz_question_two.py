'''
Write a class named Employee that holds the following data about an employee in attributes:
a. Name
b. ID number
c. Department
d. Job title.

    Include accessor and mutator methods for each attribute.
    Then, write a program that presents a menu to let the user perform the following actions until the
    user selects to quit the program:

    Add a new employee to the dictionary (Ask for all employee details, create an Employee
    object with those details, and store the Employee object in a dictionary using the employee
    ID number as the key; if the employee already exists, print that the ID already exists)

    Look up an employee in the dictionary (Ask for an employee ID and print all the details of
    that employee; if such an employee ID does not exist, print that the specified ID was not
    found)

    Change an existing employee's name, department, and job title in the dictionary (Ask for
    an employee ID and if such an ID exists, ask for all other details and update the dictionary
    value for that ID; if such an employee ID does not exist, print that the specified ID was not
    found)

    Delete an employee from the dictionary (Ask for an employee ID and if such an ID exists,
    delete the related employee entry from the dictionary; if such an employee ID does not
    exist, print that the specified ID was not found)

Quit the program (You may print any appropriate message (e.g. Good Bye!!))
'''

# Employee object with name, id, department, and job title fields. Getters, setters, toString provided. 
class Employee:
    def __init__(self, name: str, id: int, dep: str, job_title: str):
        self.name = name
        self.id = id
        self.dep = dep
        self.job_title = job_title

    def get_name(self): return self.name
    def get_id(self): return self.id
    def get_dep(self): return self.dep
    def get_job_title(self): return self.job_title

    def set_name(self, name): 
        if name: self.name = name

    def set_id(self, id): 
        if id: self.id = id

    def set_dep(self, dep): 
        if dep: self.dep = dep

    def set_job_title(self, job_title): 
        if job_title: self.job_title = job_title

    def to_string(self):
        return (f'Employee Data:\nName: {self.get_name()}\nId: {self.get_id()}\nDepartment: {self.get_dep()}\nTitle: {self.get_job_title()}')

# checks for employee existence via their id 
def find_employee(id: int, all_employees: dict) -> bool:
    return id in all_employees

# add's employee to our dict assuming employee with their id doesn't exist already
def add_employee(all_employees: dict) -> None:
    name = input('Enter name: ')
    id = int(input('Enter unique id: '))
    dep = input('Enter department: ')
    title = input('Enter job title: ')

    if find_employee(id, all_employees):
        print(f'*ERROR* Employee with id {id} ALREADY EXISTS.')
    else:
        employee = Employee(name, id, dep, title)
        all_employees[id] = employee
        print('Employee has been SUCCESSFULLY ADDED.')

# searches for an employee in our dict, assuming it's populated
def look_up_employee(all_employees: dict) -> None:
    if not all_employees:
        print('NO EMPLOYEE DATA AVAILABLE.')
        return
    
    id = int(input("Enter employee's id: "))
    if not find_employee(id, all_employees):
        print(f"*ERROR* Employee with Id {id} DOESN'T EXIST")
    else:
        print(all_employees[id].to_string())

# Adjusts Employee's details assuming dict is populated and the targeted employee exists. Unique id cannot be changed. 
def change_employee_details(all_employees: dict) -> None:
    if not all_employees:
        print('NO EMPLOYEE DATA AVAILABLE.')
        return

    id = int(input("Enter employee's id: "))
    if not find_employee(id, all_employees):
        print(f"*ERROR* Employee with Id {id} DOESN'T EXIST")
    else:
        name = input('Enter new name: ')
        dep = input('Enter new department: ')
        title = input('Enter new job title: ')

        employee = all_employees[id]
        employee.set_name(name)
        employee.set_dep(dep)
        employee.set_job_title(title)
        print('Employee details have been SUCCESSFULLY UPDATED.')

# deletes an employee from our dict assuming it's not empty and it exists
def delete_employee(all_employees: dict) -> None:
    if not all_employees:
        print('NO EMPLOYEE DATA AVAILABLE.')
        return

    id = int(input("Enter employee's id: "))
    if not find_employee(id, all_employees):
        print(f"*ERROR* Employee with Id {id} DOESN'T EXIST")
    else:
        del all_employees[id]
        print(f'Employee with id {id} has been SUCCESSFULLY DELETED.')

# Iterates through all saved employees in dict and displays them in a nice format
def view_all(all_employees: dict) -> None:
    if not all_employees:
        print('NO EMPLOYEE DATA AVAILABLE.')
        return
    
    print(f'{"ID":<10} {"Name":<20} {"Department":<20} {"Job Title":<20}')
    print('-' * 70)
    for id, emp in all_employees.items():
        print(f'{id:<10} {emp.get_name():<20} {emp.get_dep():<20} {emp.get_job_title():<20}')
    

# main logic that allows user to do CRUD operations on an Employee
def employee_central_database() -> None:
    all_employees = {}
    user_options = ['A', 'F', 'C', 'DEL', 'V', 'X']

    while True:
        print('---EMPLOYEE MENU---')
        user_input = input("ENTER 'A'dd Employee, 'F'ind Employee, 'C'hange Emp Details, 'DEL'ete Employee, 'V'iew all Employees or 'X' to exit: ").upper()

        if user_input not in user_options:
            print(f'*ERROR* {user_input} NOT RECOGNIZED')
            print('\n')
            continue


        if user_input == 'A':
            add_employee(all_employees)
            print('\n')

        elif user_input == 'F':
            look_up_employee(all_employees)
            print('\n')
        elif user_input == 'C':
            change_employee_details(all_employees)
            print('\n')
        elif user_input == 'DEL':
            delete_employee(all_employees)
            print('\n')
        elif user_input == 'V':
            view_all(all_employees)
            print('\n')
        elif user_input == 'X':
            print("Good Bye!!")
            break

# begins program
employee_central_database()




