class Coffeeshop:
    def __init__(self, name):
        self.name = name
        self.property = 100000
        self.coffeeList = {"아이스 아메리카노": 2000,
                           "라떼": 3000,
                           "딸기 스무디": 4000}
        self.stockList = {"아이스 아메리카노": 10,
                          "라떼": 15,
                          "딸기 스무디": 20}
    def introducing(self):
        print(f"안녕하세요. {self.name}입니다. 재산은 {self.property}원입니다.")
    def addMenu(self):
        new = input("메뉴 이름을 입력해주세요: ")
        price = input(f"{new}의 가격을 입력해주세요: ")
        self.coffeeList[new] = price
    def showMenu(self):
        for x, y in self.coffeeList.items():
            print(f"이름: {x} 가격: {y}")
    def showStock(self):
        for x, y in self.stockList.items():
            print(f"이름: {x} 재고: {y}")
    def sale(self):
        a = input("구매할 음료의 이름을 입력해주세요: ")
