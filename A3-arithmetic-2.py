#!/usr/bin/env python
#Math function
#dzul.aiman@gmail.com
#2023-10-09

# Built-in math functions
import math

sqrt_result = math.sqrt(25)  # Square root function
print("Square Root Result:", sqrt_result)

log_result = math.log(100, 10)  # Logarithm with base 10
print("Logarithm Result:", log_result)


# Random module for generating random numbers
import random

random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
random_float = random.random()  # Generates a random float between 0 and 1

print("Random Integer:", random_integer)
print("Random Float:", random_float)


# Seeding for reproducibility
import random

random.seed(42)  # Seed value for reproducibility
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)

print("Random Number 1:", random_number1)
print("Random Number 2:", random_number2)
