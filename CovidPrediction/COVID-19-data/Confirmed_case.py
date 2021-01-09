# Import libreries

import pandas as pd
import matplotlib.pyplot as plt

# Load the csv files

confirmed = pd.read_csv("covid19_confirmed.csv")
deaths = pd.read_csv("covid19_deaths.csv")
recovered = pd.read_csv("covid19_recovered.csv")

# Set dates as rows and countries as columns

confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis=1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)

confirmed = confirmed.groupby(confirmed["Country/Region"]).aggregate("sum")
deaths = deaths.groupby(deaths["Country/Region"]).aggregate("sum")
recovered = recovered.groupby(recovered["Country/Region"]).aggregate("sum")

confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T

# Print the numbers of infections in the last 10 days in Italy

new_cases = confirmed.copy()

for day in range(1, len(confirmed)):
    new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]

print(new_cases['Italy'].tail(10))


# Total confirmed cases visualization

ax = plt.subplot()
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('COVID-19 - Total Confirmed Cases', color='white')
ax.legend(loc="upper left")

countries = ['Austria', 'Italy', 'Spain', 'Belgium', 'Germany']

for country in countries:
    confirmed[country][0:].plot(label=country)

plt.legend(loc='upper left')
plt.show()