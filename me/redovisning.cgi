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
<title>Min redovisnings-sida</title>
<div class="wrapper">
<h1>Mina redovisningar</h1>
<h2>Kmom01</h2>

<h3>Allmänt</h3>

<p>Då var det första momentet avklarat. På det stora hela har det gått bra att installera de bitar av utvecklingsmiljön som krävs. Det gick även bra att jobba igenom guiderna för att skapa en me-sida och ett första python-skript.</p>

<h3>Vilken utvecklingsmiljö använder du?</h3>

<p>Jag använder mig av en MacBook Pro med OS X Yosemite. Som text editor använder jag Sublime Text. Har tidigare använt mig av Coda men hag mer och mer fastnat för Sublime Text. Gillar möjligheten att konfigurera Sublime Text som man vill och installera paket som gör editorn ännu kraftfullare. Är det något som ska göras i terminalen (vilket det hittils har varit rätt mycket av) har jag inför detta kursmoment installerat iTerm och tänkte se vad det går för.
Har även GitHub for Mac installerad och gillar hellre att jobba med det verktyget än att använda terminalen för att sköta min repon.  <br/>
Firefox, Chrome och Safari finns installerade. Använder egetligen mest Firefox i utvecklingssyfte tack vare firebug och dylikt men annars är det mest Safari som gäller till vanlig surfning.</p>

<h3>Är du bekant med Python sedan tidigare?</h3>

<p>Jag är inte bekant med python sedan tidigare utan det är något helt nytt för mig. Googlar jag lite rekommenderas det här och där att python är ett bra nybörjarspråk med en "enkel" syntax. Så förhoppningsvis kommer kursen gå bra då jag som sagt är helt nybörjare när det gäller python.</p>

<h3>Är du bekant med programmering och problemlösning sedan tidigare?</h3>

<p>Då jag har läst de andra kurspaketet som ges här på dbwebb har jag lite html, css , php och javascript i bagaget.
Har även sedan tidigare läst en kurs i Visual Basic och en kurs i C++ på gymnasiet för ett par år sedan.</p>

<h3>Är du bekant med terminalen och Unix-kommandon sedan tidigare?</h3>

<p>Första gången jag kom i kontakt med terminalen och unix-kommandon var under en gymnasiekurs. Dock var det ingen speciel djupdykning utan mer simpla saker som att navigera i mappträd osv. Annars innehöll det en del inslag av terminalen och kommandon under det andra kurspaketet här på dbwebb. Men utöver det har jag inga mer erfarenheter av det.</p>

<h3>Gick det bra att komma i gång med kursmomentet, var det lagom, för litet, för stort?</h3>

<p>Det gick bra att komma igång med kursmomentet. Det var lite ovant, men smidigt, att lägga upp filer på studentservern direkt i terminalen. Annars har jag använt mig av antingen FileZilla eller Transmit för att göra det. Så det var ett nytt inslag.
Det kändes lagom med uppgiften då det kan vara lite knepigt att få till utvecklingsmiljön och lite sådant som tar tid.
Då jag sedan tidigare använt mig av Git och GitHub var det inga svårigheter att klona python-repot</p>

<h3>Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du mest?</h3>

<p>Jag tror nog att jag gillade alla videoklipp mest.  Gillar nog att höra samt att se kodexemplen istället för att bara läsa i en bok. Böckerna var ändå bra, gillade framförallt python for informatics då det var relativt lättläst och på så vis blev det roligt att läsa igenom kapitlerna för momentet.  Med allt kursmaterial ihop blev man väl förberedd för guiderna och uppgifterna.</p>

</div>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
