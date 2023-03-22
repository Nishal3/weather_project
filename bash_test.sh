#!/bin/bash
conditional=`cat /home/ubuntu/weather_project/conditional`
testpy="test.py"

while [ $conditional == "True" ]; do
	$(eval "$testpy")
	sleep 1800
done
