class Student:
    class_year = 2026
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"
    
student1 = Student("Spongebob", 20)
student2 = Student("Patrick", 21)
student3 = Student("Squidward", 22)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")