# Question Two
# Hospital System 

global name
global gender
global address
global phone
global type_of_patient
global department

name = str(input("Enter name: "))
gender = str(input("Enter gender: "))
address = str(input("Enter address: "))
phone = str(input("Enter phone: "))
department = str(input("Enter department: "))
type_of_patient = str(input("Enter type_of_patient: "))

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
    def __init__(self, name, gender, address, phone, department):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department
    def duct(self):
        
        print("\n Doctors name: " + name + "\n Gender: " + gender + "\n Address: " + address + "\nPhone: " + phone + "\nDepartment: " + department)
   
class nurses(employees):
    def __init__(self, name, gender, address, phone, department):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department

# Menu for input
def main():
    choice = int(input("Choose menu number [1, 2, 3] to determine input category: "))
    
    if choice == 1:
        print("Enter Doctors information: ")
        # Enter object values
        doctor1 = doctors(name, gender, address, phone, department)
        doctor1.duct()
    elif choice == 2:
        print("Enter patients information information: ")
        patient1 = patients(name, gender, address, phone, type_of_patient)
        patient1.patie()

    # Enter data for nurses
    elif choice == 3:
        print("Enter patients information information: ")
        # Enter object values
        doctor1 = doctors(name, gender, address, phone)
        doctor1.duct()
    else:
        print("Wrong choice: ")
        return main()
    



   


print(main())












