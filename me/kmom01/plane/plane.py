#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
Some various ways of saying Hello World in Python
"""
 
#Ask user for hight over sea
meter = int(input("Höjd över havet? "))

#Ask user for speed
speed = int(input("hastighet? (km/h) "))

#Ask about temperature
Celsius = int(input("Temperatur utanför flygplanet: "))

#Convert values from user input
feet = 3.28084 * meter
miles = 0.62137 * speed
Fahrenheit = 9.0/5.0 * Celsius + 32

#Print it out
print("Höjden är:", feet, "feet \n", "Hastigheten är:", miles, "mph \n", "Temperaturen är:", Fahrenheit, "F\n")
		
#print("Hastigheten är:", miles, "mph")
#print("Temperaturen är:", Fahrenheit, "F")



