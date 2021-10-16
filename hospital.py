# Question Two
# Hospital System 

global name
global gender
global address
global phone
global type_of_patient
global department
global employee_id
global salary

name = str(input("Enter name: "))
gender = str(input("Enter gender: "))
address = str(input("Enter address: "))
phone = str(input("Enter phone: "))
department = str(input("Enter department for employees only: "))
type_of_patient = str(input("Enter type_of_patient for patients only: "))
employee_id = str(input("Enter employee_id for the employed: "))
salary = float(input("Enter salary for employee: "))
salary = (107/100) * salary
salary = str(salary)
class hospital:
    
    def __init__(self):
        print("This is the hospital Sys")      

class employees(hospital):
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
class patients(hospital):
    def __init__(self, name, gender, address, phone, type_of_patient):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.type_of_patient = type_of_patient
    def patie(self):
        print("Patient name is " + name + " with gender " + gender + " and lives in " + address + " with phone " + phone + " and is of type " + type_of_patient)
class doctors(employees):
    def __init__(self, name, gender, address, phone, department, employee_id):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department
        self.employee_id = employee_id

    def duct(self):
        print("Doctor ID: " + employee_id + "\n Doctors name: " + name + "\n Gender: " + gender + "\n Address: " + address + "\nPhone: " + phone + "\nDepartment: " + department + "\nManager salary: " + salary)
   
class nurses(employees):
    def __init__(self, name, gender, address, phone, department, employee_id):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department
        self.employee_id = employee_id
        

    def nur(self):
               
        print("Nurse ID: " + employee_id + "\n Nurse name: " + name + "\n Gender: " + gender + "\n Address: " +
              address + "\nPhone: " + phone + "\nDepartment: " + department + "\nManager salary: " + salary)


# Menu for input
def main():
    choice = int(input("Choose menu number [1, 2, 3] to determine input category: "))
    
    if choice == 1:
        print("Enter Doctors information: ")
        # Enter object values
        
        doctor1 = doctors(name, gender, address, phone, department, employee_id)
        doctor1.duct()

    elif choice == 2:
        print("Enter patients information information: ")
        patient1 = patients(name, gender, address, phone, type_of_patient)
        patient1.patie()

    # Enter data for nurses
    elif choice == 3:
        print("Enter patients information information: ")
        # Enter object values
        nurse1 = nurses(name, gender, address, phone, department, employee_id)
        nurse1.nur()
    else:
        print("Wrong choice: ")
        return main()
    


print(main())












