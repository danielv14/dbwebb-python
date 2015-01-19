#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
Send result as plain text.
"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


#hight over sea
meter = 1100

#speed
speed = 1000

#temperature
Celsius = -50

#Convert values
feet = 3.28084 * meter
miles = 0.62137 * speed
Fahrenheit = 9.0/5.0 * Celsius + 32


# Here comes the content of the webpage 
content = """
Planfakta
--------------
Höjden är: {convertfeet}
Hastigheten är: {convertmiles}
Temperaturen är: {converttemp}

"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(convertfeet=feet, convertmiles=miles, converttemp=Fahrenheit))



