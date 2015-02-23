#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Redovisning

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
	font-family: ‘Lucida Sans Unicode’, ‘Lucida Grande’, sans-serif;
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

<h2>Kmom04</h2>
<h3>Allmänt</h3>
<p>Då var det fjärde momentet klart. På det stora hela har det gått bra men självfallet fastnade jag lite här och där i uppgifterna.</p>
<h3>Var det svårt att bekanta sig med datastrukturen för listor eller flöt det på bra?</h3>
<p>Då syntaxen i Python är relativt lättläst var det inga svårigheter att bli bekant med listor. Listor har ju redan tagits upp litegrann så det var familjärt</p>
<h3>Hur du jobbat med listor eller arrayer, i andra programmeringsspråk - kan du isåfall jämföra Python listor mot andra programmeringsspråk?</h3>
<p>Har tidigare stött på listor både i PHP och JavaScript och Pythons "enkelhet" gör att jag tycker att pythons sätt att hantera listor är de enklare sättet. Python hanterar listor som så mycket annat på ett mer lättläst sätt vilket gör att det blir lättare att hänga med i hantering av listor, likväl som andra saker.</p>
<h3>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik när det gäller listor?</h3>
<p>Labben var väl den lättaste uppgiften av de som ingick i momentet och jag kan inte påstå att jag hade några större svårigheter att jobba igenom den. Kanske fastnade någonstans men tog mig snabbt förbi det genom att konsultera Google så att säga. Första uppgiften med Marvin var inte heller direkt svår. Att den uppgiften inte var speciellt komplex gjorde ändå att jag tycker den var väldigt lärorik.</p>
<p>Andra uppgiften med Marvin var den som tog mest tid för mig att klara av. De första kommandona, lista och visa var inte speciellt svåra att få till. Att låta Marvin plocka upp saker var snäppet svårare och när det gällde att låta Marvin slänga saker stötte jag på stora problem. Satt fast på den funktionen väldigt länge (nästan en hel dag tror jag) och vart väldigt frustrerad. Tillslut gav jag upp den typ av lösning jag ville få till och löste det på ett enklare sätt. Jag kan inte påstå att jag löste det på ett speciellt "snyggt" sätt men funktionen är i alla fall på plats.</p>
<p>När jag gjorde båda Marvin-uppgifterna så provade jag först att bryta loss det som skulle göras från själva marvinprogrammet. När jag sedan löst uppgifterna flyttade jag över koden och modifierade den för att passa "marvin-miljön".
Den mest lärorika uppgiften var nog labben då den med hjälp av många mindre uppgifter tog upp mycket om listhantering. Förvisso var Marvin uppgifterna väldigt bra och lärorika också för att de var något mer komplexa och läste från filer.</p>

<hr>

<h2>Kmom03</h3>
<h3>Allmänt</h3>
<p>Då var det tredje momentet klart och det har väl egentligen gått rätt hackigt måste jag säga. Överlag gick det väl egentligen bra men det var framförallt två deluppgifter som tog upp mest tid för mig och det var lab2 övning 2.6 och marvins tredje uppgift.</p>
<h3>Har du programmerat med filhantering tidigare, känns det lätt eller svårt?</h3>
<p>Har tidigare programmerat med databaser endast och det här sättet är för mig nytt att arbeta med filhantering.</p>
<h3>Vad tycker du om video som läromedel, tycker du att de tillför något som läromedel?</h3>
<p>Jag gillar videoklippen. Jag gillar när både öron och ögon tar in intryck och lärdom. Videoserien som bygger på en av kursböckerna gör att jag hänger med och skriver ned alla exempel som tas upp och dessa små program har jag stor nytta av när det är dags att jobba igenom uppgifterna. Fingrarna skriva lite extra kod på detta vis villket jag tycker är bra.</p>
<h3>Du har gjort din första modul i Python, känns strukturen bra?</h3>
<p>Det känns bra, jag gillar uppdelningen så slipper man plottriga program med alldeles för många kodrader.</p>
<h3>Vad tyckte du om de olika uppgifterna? Hur tänkte du när du utförde dem? Var de utmanande eller lätta?</h3>
<p>Överlag var uppgifterna relativt lätta med några tyngre delar för min del.</p>
<p>Jag satt fast väldigt länge på lab 2 övning 2.6 och tillslut lade jag den åt sidan för att jobba med marvin istället för att återgå till labben när och om jag blev klar med marvin. Uppgiften med marvin är överlag roligare då marvin har ett mindre repetativt upplägg på något vis, marvin har lite roligare dynamik också. Labben blir gärna repetativ och lite tråkig med allt (nyttigt) tragglande.</p>
<p>Fastnade redan på uppgift 1 på marvin och det tog ett tag innan jag (efter forumläsning) hittade till exemplet som man skulle bygga om marvin efter. Därefter var allting lugnt tills uppgift 3. På något sätt hade jag glömt bort att det klart och tydligt stod i uppgiftsbeskrivningen att det fanns ett väldigt bra exempel på hur uppgiften kunde lösas. Satt fast i flera timmar och det var tack vare lite grävande på forumet jag insåg att det faktiskt fanns ett exempel på hur uppgiften skulle lösas. Mycket tid hade kunant sparas om jag läst uppgiftsbeskrivningen en gång till.</p>
<p>Därefter sov jag på saken och försökter igen med lab2 övning 2.6. Det var inte förrän jag verkligen bröt ner uppgiften i molekyler och använde print som guidning på hur jag skulle gå vidare som jag löste den. Det är väl den största lärdom jag tar med mig, bryt ned i mindre bitar och använd print smart.</p>

<hr>

<h2>Kmom02</h2>
<h3>Allmänt</h3>
<p>Då var det andra momentet avklarat. Överlag gick det bra och de störta problemen jag hade var att bråka med pylint. Då jag hade följt med Chucks videos som låg under läshänvisningar och skrivit ned alla exempel i en testfil hade jag en del att stödja mig på och återanvända när det var dags att göra uppgiften. Det var väldigt skönt.</p>
<p>Tycker det var bra att lab1 och marvin var uppdelade i mindre deluppgifter. Detta gjorde att det kändes lättare att ta sig an dem då man kunde beta av en deluppgift i taget.</p>
<h3>Hur känns syntaxen i Python? Är det enkelt att se programmets struktur och vad den gör?</h3>
<p>Syntaxen är väldigt lättläst egentligen och det går bra (än så länge) att enkelt se vad koden gör. Det är även väldigt bekvämt att skriva python kod och jag börjar avvänja mig något med att avsluta varje kodsnutt med ';' och dylikt.   <br/>
Däremot har min hjärna fått för sig att det ska vara ett mellanslag efter print. Detta gillar såklart inte pylint. Antingen gör jag det omedvetet eller så är det min texteditor som vill göra det lite svårare för mig. Kanske har något plugin installerat till Sumblime Text som spökar. Men förmodligen är det jag som inte riktigt vant mig vid syntaxen än.</p>
<h3>Hur går det med valideringen av uppgifterna? Är du överens med pylint om eventuella felmeddelanden vid valideringen?</h3>
<p>Valideringen är väldigt frustrerande än så länge. Visst, den hjälper till så att man lär sig "korrekt" syntax men det är svårt att frångå frustration när programmet fungerar som det ska men pylint är en surpuppa och klagar ändå. När jag trodde att jag var klar med hela uppgiften klagade pylint på marvin övning 9 och jag vart verkligen inte klok på felet. Rättade till det genom att skriva om koden totalt och använda ett annat tillvägagångssätt.  <br/>
Hade några gånger problem med 'outer scope' i lab1 uppgiften som jag fick lösa genom att ändra lite variabelnamn. Men det gick väldigt enkelt att rätta till</p>
<h3>Hur gick det att utföra uppgifterna, var de enkla eller svåra?</h3>
<p>Uppgifterna rullade på bra och det var som sagt skönt att jag redan hade en del kod att stödja mig av tack vare att jag skrev upp alla exempel från Chucks videos. Det som egentligen tog mest tid i denna uppgift var att rätta till problem som pylint klagade på.   <br/>
När jag provkörde marvin då jag kände att jag var klar med alla uppgifter upptäckte jag att marvin inte riktigt gjorde som han skulle när det gällde att omvandla minuter. Jag provade att mata in 50 minuter och marvin påstod att det hade gått en timme. Min kod fungerade som så att den rundande upp och jag skrev om koden med math.floor.</p>

<hr>

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
