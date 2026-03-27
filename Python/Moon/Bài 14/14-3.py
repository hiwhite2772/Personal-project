class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Xin chào, tôi tên là {self.name} và tôi {self.age} tuổi.")
class Student(Person):
    def __init__(self, name, age, id_student):
        super().__init__(name, age)
        self.id_student = id_student
    def study(self):
        print(f"Sinh viên {self.name} với mã số {self.id_student} đang học tập.")
student = Student("Nguyen Van A", 18, 20201923)
student.say_hello()
student.study()