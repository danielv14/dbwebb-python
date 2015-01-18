#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update this.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")

# Here comes the content of the webpage 
content = """<!doctype html>
<meta charset="utf-8">
<style>
div.wrapper {
	width:960px;
	margin-top: 20px;
	margin-left: auto;
	margin-right: auto;
	line-height: 1.2;
	-moz-box-shadow: 1px 1px 3px #000000;
	-webkit-box-shadow: 1px 1px 3px #000000;
	box-shadow: 1px 1px 3px #000000;
	padding-left:10px;
	padding-right:10px;
	padding-top: 20px;
	padding-bottom: 20px;
}

</style>
<title>Min Me-sida</title>
<div class="wrapper">
<h1>Om mig</h1>
<p>Jag heter Daniel och bor uppe i Umeå men är ursprungligen uppväxt i Dalarna. 
Ser fram emot vad den här kursen har att erbjuda och är helt grön när det gäller python.
Har under hösten 2014 läst de andra kurspaketet som erbjuds här på BTH och tänkte fortsätta med denna.
På fritiden blir det lite av varje. Filmkvällar med vänner och flickvän, promenader i naturen eller sittande framför datorn. 
Är lite av en tv-serie nörd och följer nog på tok för många serier.. 
</p>
<a href="http://www.student.bth.se/~dave14/dbwebb-kurser/python/me/redovisning.cgi">Redovisningar</a>
</div>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
