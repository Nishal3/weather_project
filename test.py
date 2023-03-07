#!bin/python3

from bs4 import BeautifulSoup as bs
import requests as rq
import re
import warnings
from datetime import datetime

url = "https://weather.com/weather/today"
w_html = rq.get(url)
bsed_w_html = bs(w_html.text, "html.parser")
if not bsed_w_html:
    exit()

date_time_now = datetime.now()
date_time_w_slash = "%s/%s/%s" % (date_time_now.month, date_time_now.day, date_time_now.year)
temp_rn = bsed_w_html.find(class_="CurrentConditions--tempValue--MHmYY").text
temp_rn_feels_like = bsed_w_html.find(class_="TodayDetailsCard--feelsLikeTempValue--2icPt").text
wind_rn = bsed_w_html.find(class_="Wind--windWrapper--3Ly7c undefined").text[14:]
alerts_rn = bsed_w_html.find(class_="AlertHeadline--alertText--38xov").text if bsed_w_html.find(class_="AlertHeadline--alertText--38xov") else None

if "+" in str(alerts_rn):
    plus_val = alerts_rn.find("+")
    alert = alerts_rn[0:plus_val-1]

# Testing to try to put all alerts in data
#if alerts_rn:
#    print("condition worked")
#    alert_link = bsed_w_html.find(class_="AlertHeadline--AlertHeadline--2-IsO CurrentConditions--AlertHeadline--1C_ew AlertHeadline--overlay--1lD96 Button--default--2gfm1")

with open("weather_data.csv", mode="a") as weather_file:
    weather_file.write(f"{date_time_w_slash},{temp_rn},{temp_rn_feels_like},{wind_rn},{alerts_rn}")
