#!/usr/bin/env python
#String: quotation, indexing, slicing, concat, formatting
#dzul.aiman@gmail.com
#2023-10-09

# Single quotes and double quotes can be used for strings
single_quoted_string = 'This is a single-quoted string.'
double_quoted_string = "This is a double-quoted string."

# Triple quotes for multiline strings
multiline_string = '''This is a
multiline string
using triple quotes.'''

# Indexing and slicing in strings
sample_string = "Hello, World!"
print(sample_string[0])     # Output: H (indexing starts from 0)
print(sample_string[7])     # Output: W
print(sample_string[0:5])   # Output: Hello (slicing returns a substring from index 0 to 4)
print(sample_string[7:])    # Output: World! (slicing returns a substring from index 7 to the end)


# Concatenation of strings
string1 = "Hello"
string2 = " World"
concatenated_string = string1 + string2
print(concatenated_string)  # Output: Hello World


# String formatting using f-strings (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)    # Output: My name is Alice and I am 30 years old.


# String formatting using format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)    # Output: My name is Alice and I am 30 years old.
