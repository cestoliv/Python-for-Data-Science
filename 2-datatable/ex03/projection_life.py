import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
income_data = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
life_expectancy_data = pd.read_csv('life_expectancy_years.csv')

# Extract the relevant columns
YEAR = '1900'
income_values = income_data[YEAR]
life_expectancy_values = life_expectancy_data[YEAR]

# Create a scatter plot
plt.scatter(income_values, life_expectancy_values)

# Set the labels and title
plt.xlabel('Gross domestic product')
plt.ylabel('Life expectancy')
plt.title(YEAR)

# 0-1000 take 1/3 of the graph, 1000-10000 take 2/3 of the graph
plt.xscale('log')
plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

# Show the plot
plt.show()
