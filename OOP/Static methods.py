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

#Regular methods (preiau self(instanta) ca prim argument)
    def full_Name(self):
        return "{} {}".format(self.firstName, self.lastName)
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)#poate fi modificata pentru fiecare instanta

#Class methods (preiau cls(clasa) ca prim argument, pot fi folosite ca constructori)
    @classmethod
    def set_Raise_Amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):#Contructor
        firstName, lastName, salary = employee_string.split('-')
        return cls(firstName, lastName, salary)#creeaza un nou employee object

#Static methods (nu preaiu argumente ca instanta sau clasa)
    @staticmethod
    def is_workday( day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False

        return True


#Instante
emp_1 = Employee('Alexandru', 'Pislariu', 5000)
emp_2 = Employee('Test', 'User', 2000)

emp_str_1 = "John-Doe-7000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

import datetime

my_date = datetime.date(2019, 9, 12)

print(Employee.is_workday(my_date))
