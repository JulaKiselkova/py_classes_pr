class Item():
    def __init__(self, brand, problem):
        self.brand = brand
        self.promlem = problem


class Phone(Item):
    def __init__(self, brand, problem, os):
        self.os = os
        super().__init__(brand, problem)


class Laptop(Item):
    def __init__(self, brand, problem, os, year):
        self.os = os
        self.year = year
        super().__init__(brand, problem)


class TV(Item):
    def __init__(self, brand, problem, diagonal):
        self.diagonal = diagonal
        super().__init__(brand, problem)


class Receipt:
    brand = 'Kia'
    isWork = True


type_of_service = input("Would you like to make an order or see the info?")
order = "order"
info = "info"
if(type_of_service == order):
    print("orderrr")
elif(type_of_service == info):
    print("infoooo")
else:
    print("mistake")
