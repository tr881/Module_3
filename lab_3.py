"""
Program name: automobile_info.py
Author: Tarik Beyenal
Date last updated: 2/3/2025
Purpose: To simulate user input of automobile details and display vehicle information
"""

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle Information:")
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Doors:", self.doors)
        print("Roof:", self.roof)

year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Doors (2 or 4): ")
roof = input("Roof (solid or sun roof): ")

car = Automobile(year, make, model, doors, roof)
car.display_info()
