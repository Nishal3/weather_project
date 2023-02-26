#!/bin/python3

from bs4 import BeautifulSoup as bs
import requests as rq
import re
import warnings
from datetime import datetime

url = "https://weather.com/weather/today"
w_html = rq.get(url)
bsed_w_html = bs(w_html.text, "html.parser")
if bsed_w_html:
    print("Website Read")
else:
    print("Cannot Read Website")
    exit()

date_time_now = datetime.now()
date_time_w_slash = "%s/%s/%s" % (date_time_now.month, date_time_now.day, date_time_now.year)
temp_rn = bsed_w_html.find(class_="CurrentConditions--tempValue--MHmYY").text
temp_rn_feels_like = bsed_w_html.find(class_="TodayDetailsCard--feelsLikeTempValue--2icPt").text
wind_rn = bsed_w_html.find(class_="Wind--windWrapper--3Ly7c undefined").text[14:]
alerts_rn = bsed_w_html.find(class_="AlertHeadline--alertText--38xov").text if bsed_w_html.find(class_="AlertHeadline--alertText--38xov") else None
print(date_time_w_slash + "\n" + temp_rn + "\n" + temp_rn_feels_like + "\n" + wind_rn + "\n" + str(alerts_rn))



