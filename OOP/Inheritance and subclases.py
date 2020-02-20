#Clasa
class Employee:
#Initierea atributelor unei clase
#firstName,lastName,salary,email => toate sunt atribute ale clasei

#Variabile de clasa
    raise_amount = 1.04#poate fi modificata pentru fiecare instanta(variabila de instanta)

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + "@yahoo.com"
        self.salary = salary

#Regular methods (preiau self(instanta) ca prim argument)
    def full_Name(self):
        return "{} {}".format(self.firstName, self.lastName)
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)#poate fi modificata pentru fiecare instanta

#SUBCLASELE SE FOLOSESC PENTRU ATRIBUTE SI METODE SPECIFICE UNEI CLASE
#Ex: intr-o firma sunt mai multe tipuri de angajati, programatori, manageri, secretare, fiecare are atribute specifice care trebuie delimitate
#prin o noua subclasa
class Developer(Employee):#subclasa, are toate atributele si metodele clasei Employee
#Se pot modifica anumite atribute si metode
    raise_amount = 1.10

    def __init__(self, firstName, lastName, salary, prog_language):
        Employee.__init__(self, firstName, lastName, salary)
        self.prog_lang = prog_language

class Manager(Employee):

    def __init__(self, firstName, lastName, salary, lst_Employees = None):
        Employee.__init__(self, firstName, lastName, salary)
        if(lst_Employees is None):
            self.employees = []
        else:
            self.employees = lst_Employees

    def add_emp(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def remove_emp(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.full_Name(), end = ", ")

#Instante
dev_1 = Developer('Alexandru', 'Pislariu', 5000, "Python")
dev_2 = Developer('Test', 'User', 2000, "Java")

man_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(man_1.email)

man_1.add_emp(dev_2)

man_1.remove_emp(dev_1)

man_1.print_emp()


