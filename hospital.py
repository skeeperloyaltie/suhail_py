# Question Two
# Hospital System 
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
        name = values.name
        gender = values.gender
        address = values.address
        phone = values.phone
        type_of_patient = values.type_of_patient
        print("Patient name is " + name + " with gender " + gender + " and lives in " + address + " with phone " + phone + " and is of type " + type_of_patient)

class doctors(employees):
    def __init__(self, name, gender, address, phone, department):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department
    def duct(self):
        name = values.name
        gender = values.gender
        address = values.address
        phone = values.phone
        department = values.department
        print("\n Doctors name: " + name + "\n Gender: " + gender + "\n Address: " + address + "\nPhone: " + phone + "\nDepartment: " + department)
   
class nurses(employees):
    def __init__(self, name, gender, address, phone, department):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.department = department


# Menu for input
def values(self):
    name = str(input("Enter name: "))
    gender = str(input("Enter gender: "))
    address = str(input("Enter address: "))
    phone = str(input("Enter phone: "))
    department = str(input("Enter department: "))
    type_of_patient = str(input("Enter type_of_patient: "))

def menu():
    x = print(int(input("Choose menu number to determine input category: Ex: 1, 2, 3")))
    name = values.name 
    gender = values.gender
    address = values.address
    phone = values.phone
    type_of_patient = values.type_of_patient
    if x == 1:
        print("Enter Doctors information: ")
        
        department = str(input("Enter department: "))
        
        # Enter object values
        doctor1 = menu(doctors(name, gender, address, phone))
        doctor1.duct()
    elif x == 2:
        print("Enter patients information information: ")
        patient1 = patients(name, gender, address, phone, type_of_patient)
        patient1.patie()

    # Enter data for nurses
    elif x == 3:
        print("Enter patients information information: ")
        # Enter object values
        doctor1 = doctors(name, gender, address, phone)
        doctor1.duct()









