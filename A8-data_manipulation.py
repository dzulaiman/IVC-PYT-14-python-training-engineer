#!/usr/bin/env python
#Data manipulation using panda, numpy and matplotlib
#dzul.aiman@gmail.com
#2023-10-09

#pip install pandas numpy matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a DataFrame using pandas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 22],
    'Salary': [50000, 60000, 75000, 48000, 55000]
}

df = pd.DataFrame(data)

# Performing numerical operations using numpy
ages = df['Age'].values
salaries = df['Salary'].values

average_age = np.mean(ages)
total_salary = np.sum(salaries)

# Plotting the data using matplotlib
plt.figure(figsize=(8, 6))
plt.bar(df['Name'], df['Salary'], color='skyblue', label='Salary')
plt.plot(df['Name'], df['Age'], marker='o', color='orange', label='Age')
plt.axhline(y=average_age, color='red', linestyle='--', label='Average Age')

plt.xlabel('Name')
plt.ylabel('Value')
plt.title('Salary and Age Comparison')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Outputting calculated values
print(f'Average Age: {average_age:.2f} years')
print(f'Total Salary: ${total_salary:.2f}')
