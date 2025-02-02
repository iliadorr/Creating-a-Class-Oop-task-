from car import Car

if __name__ == '__main__':
    n = int(input("Enter the number of cars: "))
    cars = []

    # Creating objects of a Car class
    for i in range(n):
        make = input("Enter the make of a car: ")
        model = input("Enter the model of a car: ")
        year = int(input("Enter the year of a car: "))
        price = float(input("Enter the price of a car ($): "))
        discount = int(input("Enter the discount(%) for the car, if no discount enter 0: "))

        car = Car(make, model, year, price)
        car.give_discount(discount)
        cars.append(car)

    print("\nCars info:")
    for car in cars:
        car.display_info()
