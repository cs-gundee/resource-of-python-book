class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def getName(self):
        return f"{self.lastname}-н {self.firstname}"

class Student(Person):
    def __init__(self, f, l, code):
        super().__init__(f, l)
        self.studentCode = code
        self.year = 2021

    def getCode(self):
        return self.studentCode
    
    def getYear(self):
        return self.year

student1 = Student("Болор", "Хишиг", "SW202101")
student2 = Student("Од", "Заяа", "SW202102")
print(f"{student1.getName()} таны оюутны код {student1.getCode()}")       
# Хишиг-н Болор таны оюутны код SW202101