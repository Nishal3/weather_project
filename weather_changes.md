#!/bin/markdown

# Analyzing data from weather data

## Humidity Changes
The humidity had fluctuations similar to a sine or cosine graph, and in the end, the humidity increased.

![Humidity Graph]

-------------------------------------------------------------------------------

## Temperature Changes
The temperature also had quite a lot of changes throughout the week. As can be seen, the temperature also somewhat resembles a sine or cosine graph. The temperature also slowly increases and reaches 70 degrees Fahrenheit at its peak.  
The temperature gets chilly at night, which is probably the cause for why the temperature is going up and down.

![Temp Graph]


-------------------------------------------------------------------------------

## Sunrise & Sunset Changes 
The days lengthened drastically during the data collection, and the graph affirms this stipulation. The sunrise and sunset times both jump up and down significantly, but the days still lengthen nonetheless.

![Sunrise Graph]
![Sunset Graph]

-------------------------------------------------------------------------------

## Humidity v. Temp. and Feels Like Temp.
## Humidity v. Temp. and Perceived Temp.
Humidity and temperature share somewhat of a positive correlation; higher humidity equals higher temperature. The perceived temperature has a higher correlation to the humidity than the temperature. So, in conclusion: the temperature can feel hotter or colder depending on changes in the moisture content in the air.

This shows the correlation coefficients between the humidity, temperature, and perceived temperature:
![Temp-FeelsLike-Humidity-Cmatrix]

This is a graph of the temperature and perceived temperature as humidity goes up or down:
![Temp-FeelsLike-Humidity-Graph]





<!--- Image References -->
[Humidity Graph]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/humidity_graph.png "Humidity Data"
[Temp Graph]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/temp_graph.png "Temp Data"
[Sunrise Graph]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/sunrise_graph.png "Sunrise Data"
[Sunset Graph]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/sunset_graph.png "Sunset Data"
[Temp-FeelsLike-Humidity-Cmatrix]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/humidity_temp_feelslike_cmatrix.png "Temp, Feels-Like, and Humidity Correlation Matrix"
[Temp-FeelsLike-Humidity-Graph]:https://d3b7zz3nij9kip.cloudfront.net/Weather_Project_Stuff/temp_feelslike_humidity_graph.png "Temp and Feels-Like Changes as Humidity Changes"
