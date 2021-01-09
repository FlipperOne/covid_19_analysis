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
# Note: Edit line 28 for add new data about other countries. ['Italy', 'Spain']. Edit .tail(10)) for add more or less days to print.

death_cases = deaths.copy()

for day in range(1, len(deaths)):
    death_cases.iloc[day] = deaths.iloc[day] - deaths.iloc[day - 1]

print(death_cases['Italy'].tail(10))

