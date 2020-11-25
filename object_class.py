class Student:
    def __init__(self,new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades)/ len(self.grades)
Student_one = Student('rolf smith', [78,87,78,90,68])
print(Student_one.average())