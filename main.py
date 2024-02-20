# class Person:
#     def init(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def get_info(self):
#         return f"Name: {self.first_name} {self.last_name}, Age: {self.age}"
#
#
# class Teacher(Person):
#     def init(self, first_name, last_name, age, subjects):
#         super().init(first_name, last_name, age)
#         self.subjects = subjects
#
#     def teach(self):
#         return "Giving lectures and conducting classes"
#
#     def evaluate_students(self):
#         return "Evaluating students' performances"
#
#
# class Student(Person):
#     def init(self, first_name, last_name, age, course):
#         super().init(first_name, last_name, age)
#         self.course = course
#
#     def study(self):
#         return "Attending classes and studying"
#
#     def get_performance(self):
#         return "Checking own academic performance"
#
#
# class Subject:
#     def init(self, name, description):
#         self.name = name
#         self.description = description
#
#     def get_info(self):
#         return f"Subject: {self.name}, Description: {self.description}"
#
#
# class Academy:
#     def init(self, name, address):
#         self.name = name
#         self.address = address
#         self.teachers = []
#         self.students = []
#         self.subjects = []
#
#     def add_teacher(self, teacher):
#         self.teachers.append(teacher)
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def add_subject(self, subject):
#         self.subjects.append(subject)
#
#     def get_overview(self):
#         teacher_info = "\n".join([teacher.get_info() for teacher in self.teachers])
#         student_info = "\n".join([student.get_info() for student in self.students])
#         subject_info = "\n".join([subject.get_info() for subject in self.subjects])
#         return f"Academy: {self.name}, Address: {self.address}\n\nTeachers:\n{teacher_info}\n\nStudents:\n{student_info}\n\nSubjects:\n{subject_info}"
#
#
#
# # Приклад використання:
# math_teacher = Teacher(first_name: "John", last_name: "Doe", age: 35, ["Mathematics", "Physics"])
# english_teacher = Teacher(first_name: "Alice", laste_name: "Smith", age: 40, ["English", "Literature"])
#
# physics_student = Student("Tom", "Jones", 20, "Physics")
# chemistry_student = Student("Emily", "Brown", 22, "Chemistry")
#
# math_subject = Subject("Mathematics", "Basic math principles")
# physics_subject = Subject("Physics", "Study of motion and energy")
#
# my_academy = Academy("ABC Academy", "123 Main Street")
# my_academy.add_teacher(math_teacher)
# my_academy.add_teacher(english_teacher)
# my_academy.add_student(physics_student)
# my_academy.add_student(chemistry_student)
# my_academy.add_subject(math_subject)
# my_academy.add_subject(physics_subject)
#
# print(my_academy.get_overview())

