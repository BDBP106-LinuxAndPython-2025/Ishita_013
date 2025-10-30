#!/usr/bin/python3
# (1) Define a class called Car
class Car:
    showroom = "Default Showroom"  # Class attribute

    def __init__(self, make, model, year, color):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    # (g) Define __str__ method to print the car's info
    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    # (h) Define static method to print purpose of class
    @staticmethod
    def show_intro_message():
        print("This class represents a car with attributes like make, model, and year.")

    # (e) Define class method to change class attribute showroom
    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name


# (a) Create instance toyota_camry
toyota_camry = Car("Toyota", "Camry", 2022, "Red")
print(toyota_camry.make, toyota_camry.model, toyota_camry.year, toyota_camry.color)

# (b) Create another instance ford_mustang
ford_mustang = Car("Ford", "Mustang", 2022, "Black")
print(ford_mustang.make, ford_mustang.model, ford_mustang.year, ford_mustang.color)

# (c) Check Car.make (will give AttributeError)
# print(Car.make)  # Uncomment to see the error (make belongs to instances, not class)

# (d) Show the dictionary of instance attributes
print("Car.__dict__:", Car.__dict__)  # Shows class namespace
print("toyota_camry.__dict__:", toyota_camry.__dict__)  # Shows instance attributes

# (e) Use class method to change showroom
Car.change_showroom("NewAge Motors")
print("Car.showroom:", Car.showroom)
print("toyota_camry.showroom:", toyota_camry.showroom)

# (f) Compare __dict__ values
print("toyota_camry.__dict__:", toyota_camry.__dict__)  # Instance attributes only
print("Car.__dict__ has class attributes and methods")

# (g) Test magic methods
print(str(toyota_camry))  # Calls __str__
print(str(ford_mustang))  # Calls __str__

# (h) Static method
Car.show_intro_message()
