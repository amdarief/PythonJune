class Student:
    Count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Student.Count += 1

    def displayCount(self):
        print("Total Employee %d" % Student.Count)

    def displayStudent(self):
        print("Student Name : ", self.name, ", Salary: ", self.salary)



stu1 = Student("Arief", 2000)

stu2 = Student("Sandeep", 5000)
stu1.displayStudent()
stu2.displayStudent()
print("Total Students %d" % Student.Count)