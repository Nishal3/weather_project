#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

weather_df = pd.read_csv("weather_data.csv")

# Time and date separated

weather_df["date"] = pd.to_datetime(weather_df["date"], format="%m/%d/%Y_%H:%M:%S")
weather_df["time"] = weather_df["date"].dt.time
weather_df["date"] = weather_df["date"].dt.date

# Graphing change in humidity throughout the week

# Changing the percentage humidity to a int
humidity_axis = pd.to_numeric(weather_df["humidity"].str.rstrip("%"))
time_axis = np.arange(0, 10050, step=30)  # Time increments in 30 min

plt.title("Humidty/Time in one week")
plt.xlabel("Time in minutes")
plt.ylabel("Humidity in %")
plt.scatter(time_axis, humidity_axis)

plt.show(block=True)

# GraphING both actual temp and feels like to see differences

# Giving the same treatment as I did for the humidity axis
temp = pd.to_numeric(weather_df["temp"].str.rstrip("°"))
feels_like = pd.to_numeric(weather_df["feels_like"].str.rstrip("°").astype(int))

# Same time axis

# Figure set up
temp_fig, temp_ax = plt.subplots(1, figsize=(7.5, 5))
temp_fig.suptitle("Perceived Temp. v. Actual Temp.")
plt.xlabel("time")

sns.scatterplot(ax=temp_ax, y=temp, x=time_axis, label="TEMP.")
sns.scatterplot(ax=temp_ax, y=feels_like, x=time_axis, label="FEELS LIKE")

plt.show(block=True)

# Plotting to see how the sunrise and sunset times changed throughout the week

# Convert time in sunrise and sunset to pandas datetime objects
weather_df["sunrise"] = pd.to_datetime(weather_df["sunrise"].str.split(" ").str.get(0), format="%H:%M")
weather_df["sunset"] = pd.to_datetime(weather_df["sunset"].str.split(" ").str.get(0), format="%H:%M")

# Minutes for formatting and intervalling
minutes = mdates.MinuteLocator(interval=2)
min_format = mdates.DateFormatter("%H:%M:%S")
# Same for days with the date
dates = mdates.DayLocator(interval=2)
date_format = mdates.DateFormatter("%m/%d/%Y")

# Figure to plot the graphs
rise_fig, rise_ax = plt.subplots(1, figsize=(7.5, 5))

# First graph V Plot
rise_ax.plot(weather_df["date"], weather_df["sunrise"], color="pink")
# V Locators
rise_ax.yaxis.set_major_locator(minutes)
rise_ax.xaxis.set_major_locator(dates)
# V Formatters
rise_ax.yaxis.set_major_formatter(min_format)
rise_ax.xaxis.set_major_formatter(date_format)
# Title
rise_ax.set_title("Sunrise")
# Y-axis
rise_ax.set_ylabel("Time A.M.")
# X-axis
rise_ax.set_xlabel("Date")

plt.show(block=True)

# Padding to see the left graph's ticks

set_fig, set_ax = plt.subplots(1, figsize=(7.5, 5))

# Second graph V Plot
set_ax.plot(weather_df["date"], weather_df["sunset"], color="red")
# V Locators
set_ax.yaxis.set_major_locator(minutes)
set_ax.xaxis.set_major_locator(dates)
# V Formatters
set_ax.yaxis.set_major_formatter(min_format)
set_ax.xaxis.set_major_formatter(date_format)
# Title
set_ax.set_title("Sunset")
# Y-axis
set_ax.set_ylabel("Time P.M.")
# X-axis
set_ax.set_xlabel("Date")

plt.show(block=True)

# Correlation between temperature and humidity
humidity_temp_df = weather_df.loc[:, ["humidity", "temp", "feels_like"]]

# Clean up the data
humidity_temp_df["humidity"] = pd.to_numeric(humidity_temp_df["humidity"].str.rstrip("%"))
for i in ["temp", "feels_like"]:
    humidity_temp_df[i] = pd.to_numeric(humidity_temp_df[i].str.rstrip("°"))

# Correlation matrix calculation
humidity_temp_corr_matrix = humidity_temp_df.corr()

sns.heatmap(humidity_temp_corr_matrix, annot=True, cmap="coolwarm")
plt.show(block=True)

# Graph to see correlation graphically
ht_fig, ht_ax = plt.subplots(1, 2, figsize=(15,5), sharey=False, sharex=True)
ht_fig.suptitle("Temp and Feels Like Temp in Relation to Humidity")
for j in range(0,2):
    ht_ax[j].set_xlabel("Humidity")
    ht_ax[j].set_ylabel("Temperature")

# First graph
sns.scatterplot(data=humidity_temp_df, ax=ht_ax[0], x="humidity", y="temp",
        color="red", label="Temp")
sns.scatterplot(data=humidity_temp_df, ax=ht_ax[0], x="humidity", y="feels_like",
        color="blue", label="Feels Like")

# Second graph
sns.scatterplot(data=humidity_temp_df, ax=ht_ax[1], x="humidity", y="temp",
        hue="feels_like")

plt.show(block=True)


