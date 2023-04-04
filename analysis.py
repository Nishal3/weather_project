#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weather_df = pd.read_csv("weather_data.csv")

# Separating time to another column

#time = weather_df.date.str.find('_'), Since all vals are 9, I will just use it as a constant
weather_df["time"] = weather_df["date"].str[10:]
weather_df.date = weather_df.date.str[:9]

# Making a graph of change in humidity throughout the week data was collected

# Lets first change the percentage humidity to just a number
weather_df["humidity"] = weather_df["humidity"].str[:2]   # Leveraging the fact that percentage never falls below double digits
weather_df["humidity"] = weather_df["humidity"].astype(int)  # Changing the string to int; could cause problems later.

humidity_axis = weather_df.humidity

plt.title("Humidty/Time in one week")
plt.xlabel("Time in minutes")
plt.ylabel("Humidity in %")
plt.scatter(np.arange(0, 10050, step=30), humidity_axis)  # Making the time increment in 30 min so that plotting this is easier

plt.show
