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

<h2>Kmom07-10</h2>
<h3>Inledning</h3>
<p>Då var förhoppningsvis pythonprojektet klart och jag måste säga att det här var den roligaste biten på hela kursen.  När jag började med spelet hade jag ingen röd tråd eller tanke om vad det skulle handla om. Jag provade mest ideér och det var inte förrän jag hade skapat 3 stycken ”enklare rum” som jag kom på idén om att jag skulle göra ett film quiz spel.
Jag höll mig till 7-rums exemplet och spelet går ut på att man ska läsa filmrelaterade frågor som står på lappar i de olika rummen. För att ta sig vidare ska man skrika ut det korrekta svaret och dörren till nästa rum öppnas. Det är inte alltid uppenbart vart lapparna finns och ibland måste man öppna, flytta och sparka på andra objekt för att komma åt lappen med rummets filmrelaterade fråga.
Som vägledning har man utöver ledtrådskommandot roboten Robo som finns vid ens sida genom hela spelet. Tyckte att kommandot för ledtrådar funkade bra och således använde jag mig inte av guiden Robo speciellt mycket utan lite sporadiskt.</p>
<h3>Krav 1, 2 och 3</h3>
<p>När jag gjorde mina parametrar använde jag mig inte av getopt utan jag använde mig istället av argparse då det efter en del googlade verkar vara en bättre lösning och nu när jag använt mig lite av båda måste jag hålla med. Det gick mycket smidigare att implementera en lösning med argpase tycker jag. Skriver man exempelvis python3 adventure.py -c får man se tillgängliga fuskkoder och korrekta svar. De parametrar som adventure.py accepterar är:</p>
<ul>
<li>-h —help som visar vilka parametrar som finns.</li>
<li>-v —version som visar spelets version.</li>
<li>-i —info som visar spelets handling (visar texten från   startskärmen av spelet)</li>
<li>-a —about som visar info om utvecklaren.</li>
<li>-c —cheat som visar alla korrekta svaren på frågorna samt en del fuskkoder man kan använda sig av.</li>
</ul>
<p>Spelet börjar med en startskärm med en lite tjusig ascii-art title samt lite förklarade text vad spelet går ut på samt lite tips. Bland annat står det på startskärmen att det två första rummen är designade lite som en tutorial där spelaren blir lite mer guidad genom rummen så att spelaren förstår hur spelet spelas. Det står även på startskärmen att spelaren har en anteckningsbok till sitt förfogande och att det är rekommenderat att man skriver ner de korrekta svaren i den för att alla svaren kan komma att behövas under spelets gång. Spelaren kan antingen skriva ’start’ för att starta spelet eller ’q’ / ’quit’ för att avsluta.</p>
<p>Jag valde att skriva all kod och alla kommandon på engelska då det kändes mer naturligt och de kommandon som accepteras är:</p>
<ul>
<li>info - visa information om rummet.</li>
<li>help - lista alla tillgängliga kommandon, även kommandona för objekten i rummen.</li>
<li>forward - gå framåt till nästa rum, om det är upplåst.</li>
<li>back - gå tillbaka till föregående rummet.</li>
<li>look - spelaren ser sig omkring efter vad som finns i rummet.</li>
<li>clue - Få ledtrådar om hur rummet klaras av.</li>
<li>notebook - Ta fram anteckningsboken.</li>
</ul>
<p>Objekt interagerar man med genom dessa kommandon:</p>
<ul>
<li>object - se alla objekt i rummet.</li>
<li>look &lt;object-name> - visa lite mer info om ett specifikt objekt.</li>
<li>open &lt;object-name> - öppna objektet, om möjligt.</li>
<li>kick &lt;object-name> - sparka på objektet, om det är meningsfullt.</li>
<li>move &lt;object-name> - Försök flytta objektet, om möjligt eller meningsfullt.</li>
<li>read note - Läs rummets lapp, om möjligt.</li>
</ul>
<p>Väljer man att ta fram anteckningsboken har men dessa kommandon till sitt förfogande:</p>
<ul>
<li>read - läs innehållet i anteckningsboken.</li>
<li>write - anteckna något.</li>
<li>help - få lite mer hjälp om hur anteckningsboken fungerar. Man får även lite tips om hur man kan skriva i anteckningsboken för att det ska bli bättre organiserat och överskådligt.</li>
<li>done - stoppa undan anteckningsboken och fortsätta med det nuvarande rummet.</li>
</ul>
<p>Vissa rum är svårare än andra medan det i något rum bara krävs att spelaren interagerar med lappen i rummet för att läsa den filmrelaterade frågan. Ibland måste man öppna, flytta eller sparka på objekt för att kunna läsa lappen med rummets fråga.
Alla 7 rummen är uppdelade i varsina funktioner i adventure.py och det finns även en mainfunktion som fungerar som startskärm.</p>
<p>All text som anropas när man skriver ’help’ finns i en separat fil, helper.py som anropas från adventure.py. Texterna om möjliga kommandon ligger i separata funktioner, detta för att första rummet inte innehåller interaktion med ett objekt och således behöver man inte i det första rummet veta hur man interagerar med objekt eller hur man läser en lapp. I helper.py återfinns även anteckningsboken som en separat funktion som anropas från adventure.py när man anger kommandot för anteckningsboken.
Helper.py innehåller även 2 funktioner med  Ascii-art som laddas på startskärmen och när spelet är avklarat.</p>
<p>För att hålla koll på om ett rum är avklarat, om skåp är öppnade, om lådor är flyttade eller om lappen är tillgänglig använde jag mig först av globala variabler som initierades i min main-funktion där spelet börjar. Variablerna var integers och ändrades beroende på exempelvis om rummets lapp var läst eller ej. Ledtrådarna kan ju självklart inte ge det korrekta svaret så fort man frågar efter en ledtråd utan först får man ledtrådar om vart lappen kan tänkas vara och dylikt. När man väl har läst lappen ändrades en global variabel och ledtråden ändrades till att ge det korrekta svaret. Detta fungerade bra tills jag började validera mitt projekt och då klagade pylint på mitt sätt att använda dessa globala variabler. Jag fick således skrota den idén och efter en stunds googlande fick jag ett tips. Jag flyttade över alla tidigare globala variabler till en separat fil, config.py och importerade dessa istället till adventure.py. Resultatet blev precis som jag hade tänkt mig och pylint klagade inte längre.</p>
<h3>Krav 4</h3>
<p>Svårt att avgöra om detta krav är uppfyllt men det var i alla fall den tanken jag hade med spelets anteckningsbok. Innehållet i anteckningsboken sparas i en textfil, notebook.txt. Exempelsekvensen som man kan läsa när man läser om krav fyra ser såklart lite annorlunda ut jämfört med hur jag valt att genomföra kravet. Exempelsekvensen menar att man plockar upp ett objekt från ett rum och kan använda det i det nästa rummet, till exempel en nyckel. Så ser inte flödet ut i mitt spel då det inte är någon ryggsäck man lägger saker i, utan spelaren skriver (förhoppningsvis) bara ner de korrekta svaren för varje rum då startskärmen menar att de korrekta svaren kan behövas i ett av rummen och precis så ligger det till. För att ens kunna klara spelet måste man komma ihåg alla svaren och kombinera dessa på ett visst sätt för att ta sig förbi det sista rummet. Har spelaren bra minne kanske det inte blir speciellt svårt men det är här som anteckningsboken är tänkt att verkligen komma till nytta. Har spelaren då skrivit ner alla det korrekta svaren där är det bara läsa anteckningsboken och väldigt enkelt klara av sista rummet. Lider spelaren av dåligt minne måste man således gå tillbaka till rummen och antingen läsa lapparna igen eller ledtrådarna för att kunna skriva ner de korrekta svaren i anteckningsboken.</p>
<h3>Om projektet</h3>
<p>Projektet har på det stora hela gått väldigt bra måste jag säga. Det har väldigt roligt och kändes som ett bra avslut på kursen. Det var mycket roligare att koda adventure.py än att hålla på med labbarna då labbarna gärna kändes väldigt stela och tråkiga.
Jag var först lite inne på hur man skulle kunna lösa projektet med hjälp av klasser men då kursen inte gått igenom detta såg jag ingen direkt anledning att nyttja python-klasser för att genomföra projektet. Så här i efterhand kan jag tänka att klasser säkert hade underlättat på en rad olika sätt genom arv och dylikt då min kod gärna är lite upprepande.  Men då vi som sagt inte gått igenom klasser och med  KISS-principen (keep it simple, stupid) som motivering valde jag att genomföra projektet på det sätt jag gjort.
Från början hade jag tänkt att anteckningsboken skulle representeras av en json-dictionary på fil men jag insåg att för anteckningsbokens ändamål räckte det med en vanlig textfil och hederliga, vanliga textrader.</p>
<p>Jag tycker projektet ligger inom en ett rimligt spann för vad kursen har tagit upp. Då projektet är någorlunda fritt inom vissa ramar kan man anpassa svårighetsgraden på ett bra sätt. Det finns inte endast ett korrekt sätt för att genomföra projektet på utan man kan lösa problem på olika sätt. Förvisso är kanske vissa lösningar smartare än andra men ändå.
Det är svårt att uppskatta hur mycket tid jag lagt ned på projektet men skulle jag uppskatta så kanske 40-50 timmar. Då från idé till sista punkten på redovisningstexten.</p>
<h3>Validering</h3>
<p>Valideringen var lite krånglig då jag först hade alla mina filer utanför dbwebb-mappen och hade således inte tillgång till valideringsverktygen. När jag hade kommit en bra bit med spelet valde jag att flytta över filerna till dbwebb-mappen och såklart hade jag ett drös valideringsfel, det blir ju gärna så när man validerar nästan 1000 rader kod på en gång för första gången. Förutom de problem jag hade med globala variabler som jag skrivit om tidigare hade jag väldigt många rader som var för långa. Det handlade om rader med beskrivande texter om rum och dylikt. Mycket beskrivande text togs bort och delades upp så pylint skulle bli nöjd med sin regel om 120 tecken på en rad eller vad det nu var. När jag läste genom tidigare redovisningar såg jag att pylint inte gillade när filer var längre än 1000 rader och jag var ett tag väldigt nära på att överskrida den gränsen. Detta trots att jag redan hade två filer som avbelastade kodlängden, helper.py och config.py. När jag rensade lite beskrivande text och tog bort nästan allt överflödigt mellanrum (jag gillar när det är lite mer luftigt i koden) lyckades jag trimma ned antalet rader avsevärt.</p>
<h3>Om kursen</h3>
<p>Kursen har i det stora hela varit bra. Labbarna var väldigt smart utformade men självrättningen. Tyvärr var väl labbarna i min smak lite för tråkiga. Uppgifterna med Marvin var något bättre. Tyvärr kan jag tycka att svårighetsgraden steg lite väl när det gällde moment 5 och 6.  Framförallt moment 5 hade jag stora svårigheter med och det var de moment jag satt fast på längst. Visserligen måste ju svårighetsgraden öka och uppgifterna bli svårare man jag tyckte det ökade lite väl exponentiellt, om man säger så. I alla fall för mig.
Pylint har jag även bråkat med en del och till viss del kan jag väl förstå varför pylint används. Utöver error-handling lär den ju en att skriva på ett visst ”korrekt” sätt.
Personligen gillade jag att det fanns många tillgängliga filmklipp till varje kursmoment men det var väl framför allt ”Python for imformatics” klippen som gav mig något. Jag följde gladeligen med i klippen och skrev ned all exempelkod som jag senare kunde ha som stöd när jag började med momentens uppgifter.
Då det inte var min första kurs på dbwebb var jag sedan tidigare van att skriva redovisning på tre olika ställen men jag kan förstå att det känns väldigt krångligt när man är ovan. Tycket det är väldigt svårt att sätta betyg men jag landar nog någonstans mellan 6 och 7 i betyg.</p>

<hr>
<h2>Kmom06</h2>
<h3>Allmänt</h3>
<p>Då var förhoppningsvis det sista momentet innan projektet avklarat, om jag tolkat alla deluppgifter på ett någorlunda rätt sätt.   <br/>
När jag började med själva uppgiften tänkte jag att den såg extremt omfattande och svår ut och kände att det aldrig skulle gå att genomföra uppgiften. När jag sedan sovit på saken efter att ha försökt förstå mig på mynameis.py och guiden kändes det något bättre att börja ta tag i uppgiften.</p>
<h3>Har du jobbat med liknande tekniker innan(JSON, HTTP, SQLite osv osv), eller var det nytt?</h3>
<p>Då jag läst webbutveckling innan var det inte första gången jag kom i kontakt med mycket av det denna uppgift tog upp.</p>
<h3>Känns det bra att jobba på kommandoraden, ser du ett användningsområde för den typen av Python-program?</h3>
<p>Det var väldigt ovant att jobba på det viset i början, måste jag säga. Men när jag vart lite mer van med arbetssättet insåg jag hur snabbt och smidigt man kunde använda kommandoraden för att få ett pythonprogram att utföra uppgifter. Att man på förhand vet vad man vill få ut av programmet och genom att exempelvis lägga till <code>--output</code> i kommandoraden för att säga åt programmet att göra en viss sak.   <br/>
Har egetligen lite svårt att se ett specifikt användningsområde för denna typen av Python-program mer än att det kan spara mycket tid om man på förhand vet vad man vill göra med programmet</p>
<h3>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik?</h3>
<p>När jag först läste igenom uppgiften och kollade igenom guiden förstod jag inte hur jag skulle klara av uppgiften. Det svåraste för mig var nog just att förstå hur mynameis.py var strukturerat och hur jag skulle kunna bygga vidare på det. Uppgift 9 var nog den svåraste, tyckte att den var omfattande även om det vart enklare att söka efter h2-element efter jag lyckats söka efter h1-element osv.</p>
<p>När jag började med själva uppgiften kopierade jag helt enkelt över mynameis.py från exempelmappen till marvin5 och byggde vidare på programmet med mynameis.py som filnamn. När jag sedan var klar med uppgiften försökte jag byta namn på filen till marvin-cli.py och därefter gick det inte att använda programmet. Fick error om Permission Denied och det fungerade inte heller när jag skapade en tom fil som hette marvin-cli.py och flyttade över koden från min mynameis.py som innehöll koden för uppgiften. Jag löste det genom att följa guiden där man skapar en symbolisk länk och jag döpte min länk till marvin-cli. Så för att använda mitt progam skriver man exempelvis <code>marvin-cli --help</code> och då anropar man den symboliska länken som bygger på min version av mynameis.py. Det finns alltså ingen marvin-cli.py i min mapp för kursmomentet.</p>
<p>Annars så fungerar väl kommandorna ungefär som det är tänkt, om jag tolkat uppgiften korrekt.  <br/>
<code>marvin-cli --output --get http://dbwebb.se</code> laddar exempelvis ner html-koden för dbwebb.se och sparar den i en bestämd fil.  <br/>
<code>marvin-cli --input --quote</code> laddar citat från en fil.</p>
<h3>Var uppgiften i tuffaste laget, villken del hade du valt bort om du hade haft det valet?</h3>
<p>Uppgiften var helt klar svår, något annat kan jag inte säga. Men när jag väl förstod "flödet" i programmet vart det lättare att beta av de olika deluppgifterna.   <br/>
Svårt att säga vilken jag hade velat ta bort. Kanske inte ha så många olika deluppgifter i momentet. Att SQLite har gjorts som en extrauppgift tror jag var väldigt bra då det kan vara tufft att sätta sig in i <em>ännu</em> en grej om mycket av detta kursmoment redan är nytt.</p>

<hr>

<h2>Kmom05</h2>
<h3>Allmänt</h3>
<p>Då var det femte momentet kvar och för mig var detta moment helt klart det svåraste hittils. Förvisso kanske det ska bli svårare och svårare för varje moment men jag satt i alla fall fast väldigt länge med detta momentet.</p>
<h3>Hur kändes det med datastrukturerna dictionaries och tupler? Har du sett något liknande förut?</h3>
<p>Dictionaries var lite svårt att greppa först tack vare att indexeringen är väldigt annorlunda i dictionaries samt att när man printar ut en dict kan ordningen bli lite hur som helst. Tuples var lite enklare att greppa även om labben var relativt kort med just tuples vilket gjorde att potentialen med tuples inte riktigt kom fram helt, i alla fall för mig</p>
<h3>Kändes det som du fick ordning på listor, dictionaries och tupler? När man ska använda respektive och hur de kan användas?</h3>
<p>När jag hade jobbat igenom labben kände jag mig som en mästare på dictionaries, tupler och listor men den känslan byttes snart ut mot osäkerhet när jag började arbeta med käre Marvin. Jag fick gå tillbaka till litteraturen en gång till för att verkligen försöka få in för- och nackdelarna med respektive tupler och dictionaries. Styrkorna och svagheterna sitter inte än till 100% men efter detta moment är jag i alla fall på god väg.</p>
<h3>Använde du något av listor, dictionaries eller tupler när du gjorde uppgifterna, på vilket sätt?</h3>
<p>I Marvinuppgiften var det främst dictionaries och listor som användes. En dictionary håller koll på orden samt hur många gånger det används. Dessa värden flyttas över i en lista och sorteras och förkortas med slice.</p>
<h3>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik?</h3>
<p>Labben flöt på väldigt bra och den var inte heller speciellt lång eller svår. Förvisso fastnade jag på uppgift 1.8-1.10 men med hjälp av forumet kunde jag ta mig förbi de problem jag hade stött på. Tuplesövningarna gick bra, dock fastnade jag lite på 2.4 tack vare alla konvertering hit och dit mellan listor, tupler och strängar. Vart förvånad när jag validerade labben och det på första försöket gick igenom validatorn smärtfritt.     <br/>
Marvin var en helt annan historia. Uppgift 4 och 5 hade jag enorma problem med av någon anledning. Först krånglade jag till det i onödan med onödigt mycket kod. Tillslut insåg jag att den lösningen inte skulle fungera och fick börja om på nytt. Sedan försökte jag följa övningsexemplerna i litteraturnen med en funktion för varje deluppgift men det hela vart bara väldigt rörigt och jag skrotade den koden också. Därefter kom jag äntligen på rätt väg efter att ha vänt mig till forumet och jag kom äntligen vidare i uppgiften.    <br/>
Mest lärorik måste nog ändå Marvin ha varit då den uppgiften är lite mer komplex även om labbens mindre deluppgifter är enklare att hänga med i och förstå.</p>
<h3>Gjorde du någon av extrauppgifterna?</h3>
<p>Det gjorde jag tyvärr inte, då jag satt fast så länge med Marvin kände jag att tiden inte var på min sida.</p>

<hr>

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
