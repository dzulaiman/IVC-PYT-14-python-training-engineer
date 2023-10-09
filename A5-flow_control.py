#!/usr/bin/env python
#Flow control in python
#dzul.aiman@gmail.com
#2023-10-09

# Conditional statement
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# is and is not operators
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)    # Output: False (because a and b are different objects in memory)
print(a is not b) # Output: True (because a and b are different objects in memory)


# Ternary operator
x = 10
result = "even" if x % 2 == 0 else "odd"
print(result)


# in operator in loops
fruits = ["apple", "banana", "cherry"]

# for loop
for fruit in fruits:
    print(fruit)

# while loop
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1


# Loops in Python
# for loop
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

# while loop
count = 1
while count <= 5:
    print(count)  # Output: 1, 2, 3, 4, 5
    count += 1


# enumerate() function
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


# Generator function
def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

# Using the generator
for num in square_numbers(5):
    print(num)
