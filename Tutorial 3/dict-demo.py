#!usr/bin/env python3

"""
Note: this program is extremely trivial and does not test any inputs.
You should clone this repo and make this program useful by adding input testing and exception handling as challenge.
"""


class Employees(object):

    employees_information = None

    def __init__(self):
        self.employees_information = list()

    def add(self, id: int, name: str, age: int) -> None:
        employee_information = {"id": id, "name": name, "age": age}
        self.employees_information.append(employee_information)

    def update_id(self, id: int) -> None:
        for employee in self.employees_information:
            if employee["id"] == id:
                employee["id"] = id
                print("Update complete!")

    def update_name(self, name: str) -> None:
        for employee in self.employees_information:
            if employee["name"] == name:
                employee["name"] = name
                print("Update complete!")

    def update_age(self, age: int) -> None:
        for employee in self.employees_information:
            if employee["age"] == age:
                employee["age"] = age
                print("Update complete!")

    def print_information(self) -> None:
        index = 1
        print("Employees:")
        for employee in self.employees_information:
            print(str(index) + ". \n" + "ID: " + str(employee["id"]))
            print("Name: " + str(employee["name"]))
            print("Age: " + str(employee["age"]))
            index += 1

    def print_names(self) -> None:
        index = 1
        print("Employees:")
        for employee in self.employees_information:
            print(str(index) + ". " + str(employee["name"]))
            index += 1
