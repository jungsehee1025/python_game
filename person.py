class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
class Korean(Person):
    def hello(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")
class Japanese(Person):
    def hello(self):
        print(f"こんにちは。私は{self.name}です。")
class Englishman(Person):
    def hello(self):
        print(f"Hello, I'm {self.name}.")
class French(Person):
    def hello(self):
        print(f"Bonjour, je suis {self.name}.")