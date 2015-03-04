#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script. 
"""
import sys
import os
from datetime import datetime
import getopt
import requests
import time
import json
from bs4 import BeautifulSoup



#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Daniel"
VERSION = "0.1 BETA"
USAGE = """{program} - Kmom06. By {author}, version {version}.

Usage:
  {program} [options] <URL-if-required-as-arg>

Options:
--help                      Display this help message.
--silent                    Do not display any details or statistics about the execution.
--verbose                   Verbose mode
--version                   Print version and exit.
--ping <site>               Ping a website.
--ping-history              See the ping history.
--get <site>                Load entire webpage.
--output                    Save to a fixed file instead.
--input                     Read from fixed file.
--quote                     Get a random quote.
--title <site>              Print a webpage <title> element
--seo <site>                Get some SEO stats from a webbpage
--json                      Use with --seo to generat JSON-Format



""".format(program=PROGRAM, author=AUTHOR, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)




#
# Global default settings affecting behaviour of script in several places
#
SILENT = False
VERBOSE = False
OUTPUT = False
INPUT = False
JSON = False

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION) 
    sys.exit(EXIT_SUCCESS)



def quotefunct():
    """
    quote function
    """
    # OM input är sant
    if INPUT:
        quotes_file = open("quotes.json", 'r')
        quotes_dict = json.load(quotes_file)
        quotes_file.close()
        print(quotes_dict)
        sys.exit(EXIT_SUCCESS)

    if VERBOSE:
        url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"
        print('url är av typ ', type(url))
        print('variabeln url ser ut såhär: ', url)
        sys.exit(EXIT_SUCCESS)

    # Vad ska hända annars
    print('Det här ska hända när input INTE är angivet')
    url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"
    try:
        req = requests.get(url)
        json_quote = req.json()
        print("\nQuote of today is:\n\"{quote}\"\n".format(quote=json_quote["quote"]))
        sys.exit(EXIT_SUCCESS)

    except requests.ConnectionError:
        print("Failed to connect.")
        sys.exit(EXIT_SUCCESS)

def pingsite(arg):
    """
    Ping a site and save result to .json
    """
    try:

        # Get current time
        rTime = time.ctime(time.time())

        req = requests.head(arg)


        if SILENT:
            print("Recieved status code: ", req.status_code)
            sys.exit(EXIT_SUCCESS)

        if VERBOSE:
            print('Verbose info: ')
            print('rTime är av typ: ', type(rTime))
            print('req är av typ: ', type(req))
            print('arg är av typ; ', type(arg))

            sys.exit(EXIT_SUCCESS)


        # Request header from url
        print("Ready to send HTTP request to ", arg, end='')


        print("Request to ", arg, " \nsent at ", rTime)
        print("Recieved status code: ", req.status_code)
        print("Page was last modified: ", req.headers["Last-Modified"])        
        # Create a dict from the url and statuscode
        ping_dict = {
            'URL' : arg,
            'Status Code' : req.status_code
        }
    
        # Save the dict to .json
        fhand = open("pinghistory.json", 'w')
        json.dump(ping_dict, fhand, indent=4)

        sys.exit(EXIT_SUCCESS)

    except requests.ConnectionError:

        print("Failed to connect")

    sys.exit(EXIT_SUCCESS)


def printsitehistory():
    """
    Print out the .json ping-history
    """
    in_file = open("pinghistory.json", 'r')
    new_dict = json.load(in_file)
    in_file.close()
    print(new_dict)


def getsite(arg):
    """
    Print out entire webpage as html code
    """
    #Vad ska hända när output är sant?
    if OUTPUT:
        try:
            req2 = requests.get(arg)
            soup = BeautifulSoup(req2.text)
            getallcontent = soup.find()
            fhand3 = open('getsite.html', 'w')
            fhand3.write(str(getallcontent))
            fhand3.close()
            print('The site has been saved to getsite.html')

            sys.exit(EXIT_SUCCESS)

        except requests.ConnectionError:
            print('Failed to connect')


    if VERBOSE:
        req3 = requests.get(arg)
        soup = BeautifulSoup(req3.text)
        getsitehtml = soup.find()
        print('req3 är av typ ', type(req3)) 
        print('soup är av typ ', type(soup))
        print('getsitehtml är av typ', type(getsitehtml))
        sys.exit(EXIT_SUCCESS)
     
    #vad händer annars?
    try:
        req3 = requests.get(arg)
        soup = BeautifulSoup(req3.text)
        getsitehtml = soup.find()
        print("\n The scraped content from site is:\n", getsitehtml)
        sys.exit(EXIT_SUCCESS)


    except requests.ConnectionError:
        print('Failed to connect')


def titlefunct(arg):
    """ funct for title
    """
    # Om input är sant
    if INPUT:
        fhand_title = open('getsite.txt', 'r')
        read_file = fhand_title.readlines()
        soup2 = BeautifulSoup(str(read_file))
        print("The <title> element from getsite.txt is: ", soup2.title)
        sys.exit(EXIT_SUCCESS)

    if VERBOSE:
        req4_verbose = requests.get(arg)
        print("The submitted URL: ", arg)
        print("The respons is: ", req4_verbose)
        sys.exit(EXIT_SUCCESS)

    # Om input INTE är sant
    try:
        req4 = requests.get(arg)
        soup1 = BeautifulSoup(req4.text)
        get_title_element = soup1.find("title")
        print("The <title> of ", arg, " is: ", get_title_element)
        sys.exit(EXIT_SUCCESS)

    except requests.ConnectionError:
        print('Failed to connect')

    
def seofunct(arg):
    """
    Seo function
    """
    try:
        req_seo = requests.get(arg)
        soup_seo = BeautifulSoup(req_seo.text)

        #Variables for seo if only seo is the option
        get_all_h1 = soup_seo.find_all("h1")
        get_all_h2 = soup_seo.find_all("h2")
        get_all_links = soup_seo.find_all("a")
        title_length = len(soup_seo.title.string)


        if VERBOSE:
            print('The title is: ', soup_seo.title.string)
            sys.exit(EXIT_SUCCESS)

        if JSON and not INPUT:
            seo_dict = {
                'Title length' : title_length,
                'Number of <h1>' :len(get_all_h1),
                'Number of <h2>' : len(get_all_h2),
                'Number of <a>' : len(get_all_links)
            }
            print(json.dumps(seo_dict, sort_keys=True, indent=4, separators=(',', ':')))

            sys.exit(EXIT_SUCCESS)

        if INPUT and not JSON:
            # Read the file and make it beautiful
            fhand_seo = open('getsite.txt', 'r')
            read_seo = fhand_seo.readlines()
            soup_seo_from_file = BeautifulSoup(str(read_seo))

            # Variables for html elements
            seo_title_length = len(soup_seo_from_file.title.string)
            h1_seo_file = soup_seo_from_file.find_all("h1")
            h2_seo_file = soup_seo_from_file.find_all("h2")
            link_seo_file = soup_seo_from_file.find_all("a")

            #Print it out
            print('Reading SEO from file...')
            print('<title> length: ', seo_title_length)
            print('Number of <h1>: ', len(h1_seo_file))
            print('Number of <h2>: ', len(h2_seo_file))
            print('Number of <a>: ', len(link_seo_file))

            sys.exit(EXIT_SUCCESS)

        if JSON and INPUT:
            #Read the file once more
            fhand_seo_input = open('getsite.txt', 'r')
            read_seo_input = fhand_seo_input.readlines()
            soup_seo_input_from_file = BeautifulSoup(str(read_seo_input))

            # Variables for html elements
            seo_input_json_title_length = len(soup_seo_input_from_file.title.string)
            h1_seo_input_file = soup_seo_input_from_file.find_all("h1")
            h2_seo_input_file = soup_seo_input_from_file.find_all("h2")
            link_seo_input_file = soup_seo_input_from_file.find_all("a")

            #Print it out
            seo_dict_json_and_input = {
                'Title length' : seo_input_json_title_length,
                'Number of <h1>' : len(h1_seo_input_file),
                'Number of <h2>' : len(h2_seo_input_file),
                'Number of <a>' : len(link_seo_input_file)
            }
            print(json.dumps(seo_dict_json_and_input, sort_keys=True, indent=4, separators=(',', ':')))

            sys.exit(EXIT_SUCCESS)

        #Print out the <title> and its length
        print('Titeln för ', arg, 'är: ', soup_seo.title.string) #Verbose kanske?
        print('<title> length: ', len(soup_seo.title.string))
        print('Number of <h1> tags: ', len(get_all_h1))
        print('Number of <h2> tags: ', len(get_all_h2))
        print('Number of <a>  tags: ', len(get_all_links))

        sys.exit(EXIT_SUCCESS)

    except requests.ConnectionError:
        print('Failed to connect')
        sys.exit(EXIT_FAILED)

def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global VERBOSE, SILENT, OUTPUT, INPUT, JSON

        opts, args = getopt.getopt(sys.argv[1:], "d:hr:sv", ["ping=", "get=", "title=", "seo=", "output",
                                                             "input", "verbose", "ping-history", "help", "version", 
                                                             "quit", "json", "silent", "quote"])

        for opt, arg in opts:
            if opt in "--ping":
                pingsite(arg)

            elif opt in "--get":
                getsite(arg)
                
            elif opt in "--quote":  
                quotefunct()

            elif opt in '--title':
                titlefunct(arg)

            elif opt in "--seo=":
                seofunct(arg)

            elif opt in "--help":
                printUsage(EXIT_SUCCESS)

            elif opt in "--silent":
                SILENT = True

            elif opt in "--version":
                printVersion()

            elif opt in "--ping-history":
                printsitehistory()
                sys.exit(EXIT_SUCCESS)

            elif opt in "--output":
                OUTPUT = True

            elif opt in "--input":
                INPUT = True

            elif opt in "--verbose":
                VERBOSE = True

            elif opt in "--json":
                JSON = True

            else:
                assert False, "Unhandled option"

    
        



    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)




def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()
    
    parseOptions()
    
    timediff = datetime.now()-startTime
    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))
    
    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
