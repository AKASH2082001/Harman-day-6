class Car:
    def __init__(self, model, color, year,coustomer,amount):
        self.model = model
        self.color = color
        self.year = year
        self.coustomer = coustomer
        self.amount = amount

    def printdata(self):
        print(self.model)
        print(self.color)
        print(self.year)
        print(self.coustomer)
        print(self.amount)

bmw = Car("3 series","Red","2019","akash","120000")
benz = Car("C class","Black","2020","ram","200000")


bmw.printdata()
benz.printdata()
