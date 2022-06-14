import csv
import random
from functools import reduce
from datetime import datetime, date, timedelta


class Item():
    def __init__(self, brand, problem):
        self.brand = brand
        self.problem = problem

    def setInfo(self, brand, problem):
        self.brand = brand
        self.problem = problem


class Phone(Item):
    def __init__(self, brand, problem, os):
        self.os = os
        super().__init__(brand, problem)

    def setInfo(self, brand, problem, os):
        super().setInfo(brand, problem)
        self.os = os

    def get_data(self):
        return {"item": "Phone", "brand": self.brand, "problem": self.problem, "os": self.os}

    def getInfo(self):
        return f"Phone. Brand {self.brand}. Problem {self.problem}. OS {self.os}"


class Laptop(Item):
    def __init__(self, brand, problem, os, year):
        self.os = os
        self.year = year
        super().__init__(brand, problem)

    def setInfo(self, brand, problem, os, year):
        super().setInfo(brand, problem)
        self.os = os
        self.year = year

    def get_data(self):
        return {"item": "Laptop", "brand": self.brand, "problem": self.problem, "os": self.os, "year": self.year}

    def getInfo(self):
        return f"Phone. Brand {self.brand}. Problem {self.problem}. OS {self.os}. Year {self.year}"


class TV(Item):
    def __init__(self, brand, problem, diagonal):
        self.diagonal = diagonal
        super().__init__(brand, problem)

    def setInfo(self, brand, problem, diagonal):
        super().setInfo(brand, problem)
        self.diagonal = diagonal

    def getInfo(self):
        return f"Phone. Brand {self.brand}. Problem {self.problem}. Diagonal {self.diagonal}."

    def get_data(self):
        return {"item": "Tv", "brand": self.brand, "problem": self.problem, "diagonal": self.diagonal}


class Receipt:

    def __init__(self, id, type, name, fixed_data, repair_data, status):
        self.id = id
        self.type = type
        self.name = name
        self.fixed_data = fixed_data
        self.repair_data = repair_data
        self.status = status

    def getInfo(self):
        return f"Id {self.id}. Client name: {self.name}. Type {self.type}. In {self.fixed_data}. Out {self.repair_data}. Status {self.status}."

    def addOrder(self, dataBase, type_info):
        data = {
            'id': self.id,
            'type': type_info,
            'name': self.name,
            'fixed_data': self.fixed_data,
            "repair_data": self.repair_data,
            "status": self.status}
        dataBase.append(data)


is_open = input('Is the shop open?')

order = "order"
info = "info"
phone = "phone"
tv = "tv"
laptop = "laptop"
set_of_types = {phone, tv, laptop}
id = 0

dataBase = []
testDataBase = [{"id": 4, "type": {"item": "tv", 'brand': 'LJ', 'problem': 'not work', 'diagonal': 45}, 'name': 'Kim',
                 'fixed_data': date(2022, 6, 13), 'repair_data': date(2022, 6, 16), 'status': 'accepted'},
                {"id": 9, "type": {"item": "tv", 'brand': 'LJ', 'problem': 'not work', 'diagonal': 45}, 'name': 'Karry',
                 'fixed_data': date(2022, 6, 13), 'repair_data': date(2022, 6, 16), 'status': 'accepted'},
                {"id": 6, "type": {"item": "tv", 'brand': 'LJ', 'problem': 'not work', 'diagonal': 45}, 'name': 'Maddy',
                 'fixed_data': date(2022, 6, 13), 'repair_data': date(2022, 6, 16), 'status': 'accepted'},
                {"id": 1, "type": {"item": "tv", 'brand': 'LJ', 'problem': 'not work', 'diagonal': 45}, 'name': 'Nate',
                 'fixed_data': date(2022, 6, 13), 'repair_data': date(2022, 6, 16), 'status': 'accepted'}
                ]


def find_order_by_id_or_name(marker, type, list_of_orders):
    for item in list_of_orders:
        if(type == "id"):
            if(str(item["id"]) == marker):
                return item
        elif(type == "name"):
            if(item["name"] == marker):
                return item
        else:
            return "Order not found"


def add_to_file(data):
    for item in data:
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(item)


with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("id", "type", "name", "fixed_data", "repair_data", "status"))


while is_open == 'yes':
    type_of_service = input("Would you like to make an order or see the info?")
    if(type_of_service == order):
        delta_day = timedelta(days=random.randint(1, 5))
        id = id + 1
        name = input('name: ')
        type = input('type: ')
        status = "accepted"
        fixed_data = datetime.now()
        repair_data = fixed_data.date() + delta_day
        if(type == phone):
            brand = input('What is your brand: ')
            problem = input('What is your problem: ')
            os = input('What is your os: ')
            phone = Phone(brand, problem, os)
            res = Receipt(id, type, name, fixed_data.date(),
                          repair_data, status)
            res.addOrder(dataBase, phone.get_data())
        elif(type == tv):
            brand = input('What is your brand: ')
            problem = input('What is your problem: ')
            diagonal = input('What is your diagonal: ')
            res = Receipt(id, type, name, fixed_data.date(),
                          repair_data, status)
            tv = TV(brand, problem, diagonal)
            res.addOrder(dataBase, tv.get_data())
        elif(type == laptop):
            brand = input('What is your brand: ')
            problem = input('What is your problem: ')
            os = input('What is your os: ')
            year = input('What is your year: ')
            laptop = Laptop(brand, problem, os, year)
            res = Receipt(id, type, name, fixed_data.date(),
                          repair_data, status)
            res.addOrder(dataBase, laptop.get_data())
        else:
            print("We are not working with this type")
            add_to_file(dataBase)
        print(dataBase)
    elif(type_of_service == info):
        print("infoooo")
        id_or_name = input("Would you like to find by id or by name?")
        marker = input("Enter?")
        print(find_order_by_id_or_name(marker, id_or_name, dataBase))
        print(find_order_by_id_or_name(marker, id_or_name, testDataBase))
    else:
        print("mistake")
    is_open = input('Is the shop open?')
