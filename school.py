class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다. 저는 {self.grade}학년입니다.")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다. 제가 가르치는 과목은 {self.subject}입니다.")


class Class:
    def __init__(self, number, teacher, student):
        self.number = number
        self.teacher = teacher
        self.student = student
    def introducing(self):
        print(f"{self.number}반 담임 선생님은 {self.teacher} 선생님이시고, ")