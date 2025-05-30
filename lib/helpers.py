from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
     #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)
   
       
def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found')


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(int(id_))
    if employee:
       print(employee)
    else: 
       print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id_input = input("Enter the employee's department id: ")

    try:
        department_id = int(department_id_input)
        employee = Employee.create(name, job_title, department_id)
        
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee:", exc)

def update_employee():
    try:
        id_ = int(input("Enter the employees's id: "))
        if employee := Employee.find_by_id(id_):
            try:
                name = input("Enter the employee's new name: ")
                employee.name = name
                job_title = input("Enter the employee's new job title: ")
                employee.job_title = job_title

                employee.update()
                print(f'Success: {employee}')
            except Exception as exc:
                print("Error updating employee: ", exc)
        else:
            print(f'Employee {id_} not found')
    except ValueError:
        print("ID must be an integer.")


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
        department = Department.find_by_id(dept_id)

        if not department:
            print(f"Department {dept_id} not found")
            return

        employees = [e for e in Employee.get_all() if e.department_id == dept_id]
        for employee in employees:
            print(employee)

    except ValueError:
        print("Invalid input. Department ID must be an integer.")