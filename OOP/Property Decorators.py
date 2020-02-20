#Clasa
class Employee:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

#Metode ale clasei
    @property#pentru a folosi metoda sub forma de atribut
    def email(self):
        return "{}.{}@email.com".format(self.firstName, self.lastName)

    @property
    def fullName(self):#Creeaza numele fiecarui obiect
        return "{} {}".format(self.firstName,self.lastName)

    @fullName.setter#seteaza un atribut
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.firstName = None
        self.lastName = None

#Instante
emp_1 = Employee('Alexandru', 'Pislariu')
emp_2 = Employee('Test', 'User')

emp_1.fullName = 'Test user'

print(emp_1.firstName)
print(emp_1.email)
print(emp_1.fullName)

del emp_1.fullName
