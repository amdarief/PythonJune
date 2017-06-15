class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Student(Person):

    def __init__(self, first, last, stuId):
        Person.__init__(self,first, last)
        self.stuIdnumber = stuId

    def GetStudent(self):
        return self.Name() + ", " +  self.stuIdnumber

x = Person("Arief", "Akbar")
y = Student("Sandeep", "bobba", "1021")

print(x.Name())
print(y.GetStudent())