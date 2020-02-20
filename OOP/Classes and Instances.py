#Clasa
class Employee:
#Initierea atributelor unei clase
#firstName,lastName,salary,email => toate sunt atribute ale clasei
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + "@yahoo.com"
        self.salary = salary

#Metode ale clasei
    def fullName(self):
        return "{} {}".format(self.firstName,self.lastName)



#Instante
emp_1 = Employee('Alexandru', 'Pislariu', 5000)
emp_2 = Employee('Test', 'User', 2000)

print(emp_1.fullName())
print(Employee.fullName(emp_2))

