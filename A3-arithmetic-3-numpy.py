#!/usr/bin/env python
#python numpy
#dzul.aiman@gmail.com
#2023-10-09

# Installation (if NumPy is not already installed)
# pip install numpy

# Importing NumPy
import numpy as np

# Creating NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])  # 1-dimensional array
array2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2-dimensional array

print("1-D Array:")
print(array1)
print("2-D Array:")
print(array2)

# NumPy operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
addition = np.add(a, b)
subtraction = np.subtract(a, b)
multiplication = np.multiply(a, b)
division = np.divide(a, b)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Dot product
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)


# NumPy functions
array = np.array([1, 2, 3, 4, 5])

mean_value = np.mean(array)  # Mean of the array
median_value = np.median(array)  # Median of the array
std_deviation = np.std(array)  # Standard deviation of the array

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

# NumPy random module
random_integers = np.random.randint(1, 100, size=5)  # Generates 5 random integers between 1 and 100
random_floats = np.random.rand(5)  # Generates 5 random floats between 0 and 1

print("Random Integers:", random_integers)
print("Random Floats:", random_floats)
