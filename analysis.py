#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weather_df = pd.read_csv("weather_data.csv")

# Separating time to another column

weather_df["date"] = pd.to_datetime(weather_df["date"], format="%m/%d/%Y_%H:%M:%S")
weather_df["time"] = weather_df["date"].dt.time
weather_df["date"] = weather_df["date"].dt.date

# Making a graph of change in humidity throughout the week data was collected

# Lets first change the percentage humidity to just a number
humidity_axis = pd.to_numeric(weather_df["humidity"].str.rstrip("%"))
time_axis = np.arange(0, 10050, step=30)  # Making the time increment in 30 min so that plotting this is easier

plt.title("Humidty/Time in one week")
plt.xlabel("Time in minutes")
plt.ylabel("Humidity in %")
plt.scatter(time_axis, humidity_axis)

plt.show(block=True)

# Now lets make a graph with both actual temp and feels like to compare the differences between the two

# I'll give them the same treatment as I did for the humidity axis
temp = pd.to_numeric(weather_df["temp"].str.rstrip("°"))
feels_like = pd.to_numeric(weather_df["feels_like"].str.rstrip("°").astype(int))

# I'll use the same time axis
# The temp axis looks fine in the graph so I won't make a temp axis

# Setting up the figure
fig, axes = plt.subplots(1, figsize=(7.5, 5))
fig.suptitle("Perceived Temp. v. Actual Temp.")
plt.xlabel("time")

sns.scatterplot(ax=axes, y=temp, x=time_axis)
sns.scatterplot(ax=axes, y=feels_like, x=time_axis)

plt.show(block=True)












