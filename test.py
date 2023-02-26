#!/bin/python3

from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://weather.com/weather/today"
w_html = rq.get(url)
bsed_w_html = bs(w_html.text, "html.parser")
if bsed_w_html:
    print("Website Read")
else:
    print("Cannot Read Website")
    exit()
temp_rn = bsed_w_html.find(["span"], class_="CurrentConditions--tempValue--MHmYY")
print(temp_rn)
