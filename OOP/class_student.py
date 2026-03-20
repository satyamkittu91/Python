class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}."
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"
    

student1 = Student("SpongeBob", 3.5)
student2 = Student("Patrick", 2.8)
student3 = Student("Squidward", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())