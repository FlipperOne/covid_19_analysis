import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv("covid19_confirmed.csv")
deaths = pd.read_csv("covid19_deaths.csv")
recovered = pd.read_csv("covid19_recovered.csv")

confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis=1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis=1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis=1)

confirmed = confirmed.groupby(confirmed["Country/Region"]).aggregate("sum")
deaths = deaths.groupby(deaths["Country/Region"]).aggregate("sum")
recovered = recovered.groupby(recovered["Country/Region"]).aggregate("sum")

confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T

active_cases = confirmed.copy()

for day in range(1, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - deaths.iloc[day] - recovered.iloc[day]

# 5% of confirmed cases need hospitalization
hospitalization_rate_estimate = 0.05

hospitalization_needed = confirmed.copy()

for day in range(0, len(confirmed)):
    hospitalization_needed.iloc[day] = active_cases.iloc[day] * hospitalization_rate_estimate

print(hospitalization_needed['Italy'].tail(10))
