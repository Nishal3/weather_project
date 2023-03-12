#!/bin/bash
conditional=`cat /home/nish/weather_project/conditional`
testpy="test.py"

while [ $conditional == "True" ]; do
	$(eval "$testpy")
	sleep 7200
done
