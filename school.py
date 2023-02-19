class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.math = 0
        self.eng = 0
    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다. 저는 {self.grade}학년입니다. 저의 수학 능력은 {self.math}, 영어 능력은 {self.eng}입니다.")
    def studyMath(self):
        print("수학 공부했습니다. 수학 능력이 10 올랐어요.")
        self.math += 10



class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다. 제가 가르치는 과목은 {self.subject}입니다.")


class Class:
    def __init__(self, number, teacher):
        self.number = number
        self.teacher = teacher
        self.student = []
    def introducing(self):
        nameList = []
        for i in self.student:
            nameList.append(i.name)
        print(f"{self.number}반 담임 선생님은 {self.teacher.name} 선생님이시고, 학생은 {nameList}가 있습니다.")
    def addStudent(self, student):
        self.student.append(student)
    def mathavg(self):
        mathscoreList = []
        for i in self.student:
            mathscoreList.append(i.math)
        avg = sum(mathscoreList)/len(mathscoreList)
        print(f"이 반의 수학 능력 평균은 {avg}입니다.")