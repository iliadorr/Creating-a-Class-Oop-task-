# Crating class Car
class Car:
    def __init__(self, make=None, model=None, year=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Make of car: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price} $")

    def give_discount(self, discount):
        if self.price:
            self.price -= self.price * (discount / 100)
        else:
            print("Sorry, can't give you discount")
        