class Calc:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.result = 0
    def sum(self):
        self.result = self.left + self.right
    def sub(self):
        self.result = self.left - self.right
    def multi(self):
        self.result = self.left * self.right
    def divide(self):
        self.result = self.left / self.right