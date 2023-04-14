#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

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

# Now lets plot to see how the sunrise and sunset times changed throughout the week

# Converting the time in sunrise and sunset to pandas datetime objects
weather_df["sunrise"] = pd.to_datetime(weather_df["sunrise"].str.split(" ").str.get(0), format="%H:%M")
weather_df["sunset"] = pd.to_datetime(weather_df["sunset"].str.split(" ").str.get(0), format="%H:%M")

# Got it working somehow, with some tape and some glue lol, nvm can't do two in same gives random ass errors

# Setting up minutes for formatting and intervalling
minutes = mdates.MinuteLocator(interval=2)
min_format = mdates.DateFormatter("%H:%M:%S")
# Same for days with the date
dates = mdates.DayLocator(interval=2)
date_format = mdates.DateFormatter("%m/%d/%Y")

# Making a figure to plot the graphs
rise_fig, rise_ax = plt.subplots(1, figsize=(7.5, 5))

# First graph V Plotting
rise_ax.plot(weather_df["date"], weather_df["sunrise"], color="pink")
# V Setting locators
rise_ax.yaxis.set_major_locator(minutes)
rise_ax.xaxis.set_major_locator(dates)
# V Setting formatters
rise_ax.yaxis.set_major_formatter(min_format)
rise_ax.xaxis.set_major_formatter(date_format)
# Title
rise_ax.set_title("Sunrise")
# Y-axis
rise_ax.set_ylabel("Time A.M.")
# X-axis
rise_ax.set_xlabel("Date")

plt.show(block=True)

# Setting up padding to see the left graph's ticks

set_fig, set_ax = plt.subplots(1, figsize=(7.5, 5))

# Second graph V Plotting
set_ax.plot(weather_df["date"], weather_df["sunset"], color="red")
# V Setting locators
set_ax.yaxis.set_major_locator(minutes)
set_ax.xaxis.set_major_locator(dates)
# V Setting formatters
set_ax.yaxis.set_major_formatter(min_format)
set_ax.xaxis.set_major_formatter(date_format)
# Title
set_ax.set_title("Sunset")
# Y-axis
set_ax.set_ylabel("Time P.M.")
# X-axis
set_ax.set_xlabel("Date")

plt.show(block=True)










