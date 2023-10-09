#!/usr/bin/env python
#Working with files
#dzul.aiman@gmail.com
#2023-10-09

# Reading from a file
file_path = r"sample.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
  
#-----
# Writing to a file
file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.")
    print(f"Data written to '{file_path}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

#-----
# Appending to a file
file_path = "output.txt"

try:
    with open(file_path, "a") as file:
        file.write("\nAppending new data to the file.")
    print(f"Data appended to '{file_path}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

#-----
# Reading lines from a file
file_path = "sample.txt"

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        print("File Lines:")
        for line in lines:
            print(line.strip())  # strip() removes leading/trailing whitespaces and newline characters
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#-----
# Using with statement for file operations (automatically closes the file)
file_path = "sample.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
