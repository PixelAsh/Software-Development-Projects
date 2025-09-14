'''
Name: Ashton Sizemore
Program: Module 3 Case Study
Description: Ask the user to input different information about their vehicle and relay the information back to them using classes.
Date: 9/14/2025
'''

class Vehicle:
    def __init__(self,type):
        self.type = type

    def display_info(self):
        print(f"Vehicle Type: {self.type}")

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_auto_info(self):
        print(f"Year = {self.year}") 
        print(f"Make = {self.make}") 
        print(f"Model = {self.model}") 
        print(f"Doors = {self.doors}")
        print(f"Roof = {self.roof}")

type = "Car"
year = input("What year is the car? ")
make = input("What is the make? ")
model = input("What is the model? ")
doors = input("How many doors?(2 or 4?) ")
roof = input("What is the roof?(Solid or Sunroof?) ")

car = Automobile(type, year, make, model, doors, roof)

car.display_info()
car.display_auto_info()
