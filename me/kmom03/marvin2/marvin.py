#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""


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