#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""
import string

def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
                 _______
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \ 
    """


def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage()) 
    print("Hi, I'm Robo. I am very smart. What can I do you for?") 
    print("1) Present yourself to Robo.")
    print("q) Quit.")
    print("age) Calculate your age in seconds.")
    print("moon) Calculte what you would weight on the moon.")
    print("minute) Enter minutes and see how many hours and minutes that is")
    print("celcius) Calculate Farenheit from celcius")
    print("word) Ask for a word and then a number. Repeat the word by the number")
    print("minmax) You decide min and max. Robo randomize 10 numbers inside that range")
    print("sum) Enter numbers until you're done. Robo calculates stuff.")
    print("grade) Robo will calculate your grade based on max points")
    print("guess) Game of guessing number")
    print("strings) Randomized string")
    print("throw) Throw around letters")
    print("kmom05) Init kmom05")



#klar
def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name? ")
    print("Robo says:\n")
    print("Hello there %s !" % name)
    print("Need my help?")

#Klar
def calculateAge():
    """
    Get users age and calculate seconds
    """
    age = int(input('How old are you? '))
    calc = age * 365 * 24 * 60 * 60
    print('You have lived: %s' % calc, 'seconds')

#klar
def calculateMoon():
    """
    calculate kg on moon
    """
    weight = int(input("What to you weight (kg)? I won't tell anyone...promise "))
    weightonmoon = (weight / 6)
    print('You would weight ', weightonmoon, 'kg on the moon')

#Klar
def calculateHours():
    """
    calculte hours
    """
    import math
    minutes = int(input("How many minutes? "))
    calculateminute = minutes % 60
    calculatehour = minutes / 60
    print(minutes, 'minutes is ', math.floor(calculatehour), 'hour and', calculateminute, 'minutes')

#Klar
def calculateCelcius():
    """
    calculte farenheit
    """
    celcius = int(input("How many degrees celcius? "))
    farenheit = 9.0/5.0 * celcius + 32
    print(celcius, 'degrees celcius is', farenheit, 'degrees farenheit')

#klar
def word():
    """
    loop words
    """
    word2 = input('Give me a word ')
    number = int(input('Give me a number '))
    i = 1
    while i <= number:
        print(word2)
        i = i + 1

#Klar
def minmax():
    """
    Doing stuff
    """
    import random
    number1 = int(input('Enter low number: '))
    number2 = int(input('Enter high number: '))
    i = 1
    while i <= 10:
        print(random.randint(number1, number2))
        i = i + 1

#Klar
def sum_and_average():
    """
    sum and average
    """
    inp = "Enter a number or 'done' when you're finished "
    total = 0
    count = 0
    average = 0

    while True:
        s = input(inp)
        if s == 'done':
            break
        try:
            total += float(s)
            count += 1
            average = total / count
        except ValueError:
            print("Invalid Input. Try again: ")
        continue
    print('You entered %s numbers whose total is %s and average is %s.' % (str(count), str(total), str(average)))

#Klar
def grade():
    """
    Grades
    """
    print('Lets calculate your grade!')
    yourscore = float((input('What is your score? (between 0.0 and 1.0) ')))
    if yourscore >= 0.9:
        print('Your grade is a A')

    elif yourscore >= 0.8:
        print('Your grade is a B')

    elif yourscore >= 0.7:
        print('Your grade is a C')

    elif yourscore >= 0.6:
        print('Your grade is a D')

    elif yourscore < 0.6:
        print('Your score is a F, sorry man')

    else:
        print('Thats not a score')

#Klar
def guess():
    """
    guessing Game
    """
    import random
    guesstaken = 0
    number = random.randint(1, 100)
    print('I am thinking of a number between 1 and 100.')
    while guesstaken < 6:
        print('Guess the number')
        gissning = input()
        gissning = int(gissning)

        guesstaken = guesstaken + 1

        if gissning < number:
            print('Guess is to low')

        if gissning > number:
            print('Guess is to high')

        if gissning == number:
            break

    if gissning == number:
        guesstaken = str(guesstaken)
        print('You guessed the right number in ' + guesstaken + ' guesses')
    if gissning != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)

def strings():
    """
    randomizing strings from text.txt
    """
    import random
    import time
    fhand = open('text.txt')
    line = fhand.readline()
    moods = ["happy", "sad", "furious", "enraged"]
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    floaters = [10.200, 20.345, 30.343, 67.435]
    date = time.strftime("%c") 
    mood = random.choice(moods)
    nummer1 = random.choice(integers)
    nummer2 = random.choice(floaters)
    print(line.format(mood=mood, nummer1=nummer1, nummer2=nummer2, date=date))
    #import linecache
    #randomnumber = random.randint(1, 4)
    #retriveline = linecache.getline('text.txt', randomnumber)
    #print(retriveline)

#Klar
def throwword():
    """
    Throwing around a word
    """
    import random
    string = input("Enter a word for randomizing magic: ")
    #randomizeword = random.sample(string, len(string))
    #print (randomizeword)
    shuffled = list(string)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print('Working my magic and returning: ' + shuffled)

def randomquote():
    """
    Give a random quote from quotes.txt
    """
    from random import randint
    choosequote = randint(1, 10)
    fhand = open('quotes.txt')
    lines = fhand.readlines()
    print(lines[choosequote])


def visaallt():
    """
    List everything in inventory
    """
    fhand = open('inventory.txt')
    alltihopa = fhand.readlines()
    listallt = list(alltihopa)
    print('Marvin has in his inventory: ', listallt)

def listallnumber():
    """
    how many things does Robo has? returns integer
    """
    fhand = open('inventory.txt')
    alltihopa = fhand.readlines()
    items = alltihopa
    new_items = []
    for item in items:
        new_items.extend(item.split(','))
        print('Robo has', len(new_items), 'things in his inventory')
        fhand.close()

def plockaupp():
    """
    add stuff to robos inventory
    """
    fhand = open('inventory.txt', 'a')
    fhand2 = open('inventory.txt')
    alltihopa = fhand2.readlines()
    items = alltihopa
    new_items = []
    for item in items:
        new_items.extend(item.split(','))
    if len(new_items) <= 6:   
        addthing = input('What to add to the inventory? ')
        fhand.write(',' + addthing)
        print(addthing, ' added!')

    else:
        print('Cannot add anymore stuff. Please drop something')

def removeitem():
    """
    remove stuff
    """
    fhand = open('inventory.txt', 'r')
    alltihopa = fhand.readlines()
    fhand.close()
    fhand = open('inventory.txt', 'w')
    items = alltihopa
    new_items = []
    for item in items:
        new_items.extend(item.split(','))
        print(len(new_items), 'things in bag')
        print(new_items)
        maxnumber = len(new_items) - 1
        print('Remove something with index 0 through', maxnumber)
        chooseremove = int(input('What to remove? '))
        del new_items[chooseremove]
        fhand3 = open('inventory.txt', 'w')
        s1 = ','.join(new_items)
        fhand3.write(s1)
        print('Item removed')

def kmom05():
    """
    Kmom05
    """
    # File handeling
    fname = input("Enter the name of the text-file you wish to open: ")
    try:
        fhand = open(fname)
    except:
        print(fname, ", not valid file name. Default file opens.")
        fhand = open("alice-ch1.txt")
    try:
        fhand_cw = open("common-words.txt")
    except:
        print("common-words.txt not found.")


    # Count total words    
    counts = dict()
    count_total_words = 0
    for line in fhand:
        line = line.lower()
        exclude = set(string.punctuation)
        line2 = ''.join(ch for ch in line if ch not in exclude)
        words = line2.split()
        for word in words:
            count_total_words += 1
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    
    # Most common word (unsorted)
    lst = list()
    most_common_unchecked = list()
    for key, val in counts.items():
        lst.append((val, key))
    lst.sort(reverse=True)
    for key, val in lst[:7]:
        most_common_unchecked.append((key, val))

    
    lst2 = list()
    woMostCommon = list()

    # Här sätter du varje rad(ord) i common_words.txt (antar jag?) till 'line'
    for line in fhand_cw:

        # Här använder du inte 'line', utan 'word' som jag inte vet vad är,
        # den är inte definierad i den här kodbiten, jag misstänker att det
        # är 'line' du vill använda här egentligen
        if line.strip('\n') in counts.keys():
           
            # Får du inte det resultatet du letar efter, testa att använda print()
            # för att skriva ut värdet på variablerna i fråga
            del counts[line.strip('\n' + string.punctuation + string.whitespace)]
    for key, val in counts.items():
        lst2.append((val, key))
    lst2.sort(reverse=True)
    for key, val in lst2[:7]:
        woMostCommon.append((key, val))


    


    #Count letter frequency
    #print(type(counts))


    #print total wordcount
    print("\nTotal number of words are: " + str(count_total_words) + '\n')
    #print most common words not checked with common-word
    print("The 7 most common (not checked with common words) words are: " + str(most_common_unchecked) + '\n')
    #Print the most common words (checked with common-word)
    print("The 7 most common words, regular words excepted, are: " + str(woMostCommon))    



































