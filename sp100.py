# sp100_analysis_numpy.py

import numpy as np
import matplotlib.pyplot as plt
import csv

# Load CSV with structured dtype (assumes no missing values)
data = np.genfromtxt('sp100.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

# 1. Print all company names and their sectors
print("1. Company Names and Sectors")
for company in data:
    print(f"{company['Name']} ({company['Sector']})")

# 2. Compute and print the average price and EPS
print("\n2. Average Price and EPS")
avg_price = np.mean(data['Price'])
avg_eps = np.mean(data['EPS'])
print(f"Average Price: {avg_price:.2f}, Average EPS: {avg_eps:.2f}")
