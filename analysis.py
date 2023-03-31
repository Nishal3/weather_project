#!/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weather_df = pd.read_csv("weather_data.csv")
weather_df.head()

# Separating time to another column

#time = weather_df.date.str.find('_'), Since all vals are 9, I will just use it as a constant
weather_df["time"] = weather_df["date"].str[10:]
weather_df.date = weather_df.date.str[:9]

# Making a graph of change in humidity throughout the week data was collected

# Lets first change the percentage humidity to just a number
weather_df["humidity"] = weather_df["humidity"].str[:2]   # Leveraging the fact that percentage never falls below double digits

humidity_axis = weather_df.humidity
# I am doing this because the graph looks better this way, the script I used collected
# data every 30 min, so if you know start time, you will be able to calculate what
# time the data was collected
time_axis = [i*30 for i in range(1, 336)]


# The humidity axis' ticks look really cluttered, so I will make my own ticks
humidity_ticks = [i*10 for i in range(11)]

plt.plot(time_axis, humidity_axis)
plt.title("Humidty/Time in one week")
plt.xlabel("Time in minutes")
plt.yticks(humidity_ticks)  # changing ticks to make it look more visually appealing
plt.ylabel("Humidity in %")

plt.show(block=True)
# As we can see, the humidity has gone up drastically and the graph resembles a
# logarithmic function


