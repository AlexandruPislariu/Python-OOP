#Clasa
class Employee:
#Initierea atributelor unei clase
#firstName,lastName,salary,email => toate sunt atribute ale clasei

#Variabile de clasa
    raise_amount = 1.04#poate fi modificata pentru fiecare instanta(variabila de instanta)
    num_of_emps = 0#nu are rost sa fie modificata de fiecare instanta(variabila de clasa)

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        Employee.num_of_emps +=1#o modifica doar clasa

#Metode ale clasei
    def email(self):#Creeaza adresa de email a fiecarui obiect
        return "{}.{}@mail.com".format(self.firstName, self.lastName)

    def fullName(self):#Creeaza numele fiecarui obiect
        return "{} {}".format(self.firstName,self.lastName)

    def apply_raise(self):#Aplica marirea pentru fiecare obiect
        self.salary = int(self.salary * self.raise_amount)#poate fi modificata pentru fiecare instanta

#METODE SPECIALE(DUNDER)
    def __repr__(self):#Afiseaza fiecare instanta
        return "Employee('{}', '{}', '{}')".format(self.firstName, self.lastName, self.salary)

    def __str__(self):
        return "{} -> {}".format(self.fullName(), self.email())

    def __add__(self, other):#se foloseste pentru variabile cu acelasi tip de date
        return self.salary + other.salary

    def __len__(self):#Lungimea totala a numelui
        return len(self.fullName())



#Instante
emp_1 = Employee('Alexandru', 'Pislariu', 5000)
emp_2 = Employee('Test', 'User', 2000)

print(emp_1)

print(emp_1.__repr__())
print(emp_1.__str__())

print(len(emp_2))
