
class Facultate:
#Clasa retine studentii unei facultati

    def __init__(self, nume_facultate, lista_studenti = None):
        self.nume = nume_facultate#numeele facultatii
    #lista de studenti
        if(lista_studenti == None):
            self.lista_studenti = []
        else:
            self.lista_studenti = lista_studenti

    def adauga_student(self, student):
        if(student not in self.lista_studenti):
            self.lista_studenti.append(student)

    def sterge_student(self, student):
        if(student in self.lista_studenti):
            self.lista_studenti.remove(student)

    def afisare_studenti(self):
        for student in self.lista_studenti:
           print(student.id, student.nume, student.prenume)

    def cautare_student(self, id_student):
    #cauta studentul dupa id
        for stud in self.lista_studenti:
            if(id_student == stud.id):
                print(stud.nume, stud.prenume)#afiseaza numele si prenumele

class Student:

    def __init__(self, id, nume, prenume):
        self.id = id
        self.nume = nume
        self.prenume = prenume

    erori = ""#afisam motivele pentru care stundentul nu este validat

    def validare_student( self):
        if(self.id == None):
            self.erori += "Trebuie introdus id"
        if(self.nume == None):
            self.erori += "Trebuie introdus nume"

        return self.erori



stud_1 = Student(1, 'Pislariu', 'Alexandru-Ilie')
stud_2 = Student(2, 'Mitrofan', 'Catalin')
stud_3 = Student(None , None, 'Gabriel')

UBB = Facultate("Universitatea Babes-Boyliai", [stud_1, stud_2, stud_3])

UBB.cautare_student(31)

help(dict)

