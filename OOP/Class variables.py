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
        self.email = firstName + '.' + lastName + "@yahoo.com"
        self.salary = salary
        Employee.num_of_emps +=1#o modifica doar clasa

#Metode ale clasei
    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)#poate fi modificata pentru fiecare instanta



#Instante
emp_1 = Employee('Alexandru', 'Pislariu', 5000)
emp_2 = Employee('Test', 'User', 2000)

emp_1.raise_amount = 1.10
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)
