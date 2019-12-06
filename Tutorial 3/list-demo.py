#!usr/bin/env python3

"""
Note: this program is extremely trivial and does not test any inputs.
You should clone this repo and make this program useful by adding input testing and exception handling as challenge.
"""


class ShoppingList(object):

    shopping_list = None

    def __init__(self):
        self.shopping_list = list()

    def update(self, item: str, index: int) -> None:
        self.shopping_list[index] = item
        print("Update complete!")

    def add(self, item: str) -> None:
        self.shopping_list.append(item)
        print("Added " + item + "!")

    def delete(self, index: str) -> None:
        self.shopping_list.pop(index)
        print("Deleted item!")

    def print_list(self) -> None:
        index = 1
        print("Shopping List:")
        for item in self.shopping_list:
            print(str(index) + ". " + str(item))
            index += 1

    def sort_list(self) -> None:
        self.shopping_list.sort()
        self.print_list()


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("Apples")
    shopping_list.add("12 Bananas")
    shopping_list.add("12 Eggs")
    shopping_list.add("Jaffa Cakes")
    shopping_list.add("Dorritos")
    shopping_list.print_list()
    shopping_list.delete(1)
    shopping_list.print_list()
    shopping_list.update("6 Eggs", 1)
    shopping_list.print_list()
    shopping_list.sort_list()
