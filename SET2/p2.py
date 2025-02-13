class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def set_teacher(self, teacher):
        self.teacher = teacher

# Example usage
student1 = Student("Alice", 20, "S123")
student2 = Student("Bob", 21, "S124")
teacher1 = Teacher("Mr. Smith", 45, "T101")

course1 = Course("Math", "M101")
course2 = Course("Science", "S101")

student1.enroll(course1)
student2.enroll(course2)
teacher1.assign_course(course1)
teacher1.assign_course(course2)

course1.add_student(student1)
course2.add_student(student2)
course1.set_teacher(teacher1)
course2.set_teacher(teacher1)

print(f"Course: {course1.name}, Code: {course1.code}, Teacher: {course1.teacher.name}")
print("Students enrolled:")
for student in course1.students:
    print(f"- {student.name}")

print(f"Course: {course2.name}, Code: {course2.code}, Teacher: {course2.teacher.name}")
print("Students enrolled:")
for student in course2.students:
    print(f"- {student.name}")
