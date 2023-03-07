#!/bin/bash
conditional=`cat conditional`
testpy=`"~/weather_project/test.py"`

if [ $conditional == "True" ]; then
	while true; do 
		$testpy
	        sleep 3600
        done
else
	exit 1
fi
