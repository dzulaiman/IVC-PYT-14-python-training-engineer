#!/usr/bin/env python
#Training: class
#dzul.aiman@gmail.com
#2023-10-09

# Class definition
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Creating objects (instances) of the class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing class attributes and calling class methods
car1.display_info()  # Output: Toyota Corolla
car2.display_info()  # Output: Honda Civic
