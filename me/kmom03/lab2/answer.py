#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
ac13f43f0c99170203027341d0a680a1 generated for dave14 at 2015-02-10 13:58:03 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 2 - python 
 
Strings and files 
"""

"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings 
"""

"""
Exercise 1.1 
 
Assign the word: 'bus' to a variable and put your variable as the answer. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'bus'




ANSWER = word

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'bus' to a variable. Create another variable where you put
the first and the last letter in the word. Answer with the second variable. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'bus'
word2 = word[0] + word[2]




ANSWER = word2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, True))

"""
Exercise 1.3 
 
Assign the word: lollipop to a variable. Answer with the length of the word
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'lollipop'
answer = len(word)




ANSWER = answer

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'train' contains the letter 'a'.
Answer with a boolean result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'train'
result = 'a' in word




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'lollipop' capitalized. Answer with the
capitalized word. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'lollipop'.upper()




ANSWER = word

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function 'startswith()' to see if the word 'lollipop'
starts with the letter 'i'. Answer with the boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'lollipop'.startswith('i')




ANSWER = word

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'soda' and 'lollipop' to two different variables. Create
a function and pass the two words as arguments to it. Your function should
return them as a single word. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word1 = 'soda'
word2 = 'lollipop'
word3 = word1 + word2




ANSWER = word3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'bus' to it. Your function should
return the sentence: 'This word was: bus'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 'This word was: %s' % ('bus')




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'lollipop' to it. Your function should
return the string 'yes' if the word is longer than 5 characters. Else
return 'no'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def ettnio():
    """
	bla bla
	"""
    lollipop = 'lollipop'
    if len(lollipop) > 5:
        svar = 'yes'
        return svar
    else:
        svar = 'no'
        return svar




ANSWER = ettnio()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, True))

"""
Exercise 1.10 
 
Create a function and pass the word: 'lollipop' to it. Your function should
return a string with the word backwards. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def etttio():
    """
	bla bla
	"""
    result3 = 'lollipop'
    reverse = result3[::-1]
    return reverse




ANSWER = etttio()
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'soda' to it. Your function should
exclude the first and the last letter of the word and return it. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def ettelva():
    """
	bla bla
	"""
    result4 = 'soda'
    cut = result4[1:3]
    return cut




ANSWER = ettelva()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use the format operator to print out: 'My 'string' has 'integer' 'string''.
Use the values: 'book', '398' and 'pages'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
result5 = 'My %s has %i %s' % ('book', 398, 'pages')




ANSWER = result5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use 'find' and 'slice' on the string: '154.84.56.0 : (wallpaper), soda' to
get the word inside the parenthesis. Answer with the word as a string. 

Write your code below and put the answer into the variable ANSWER.
"""
def etttretton():
    """
	bla bla
	"""
    string = '154.84.56.0 : (wallpaper), soda'
    firstpos = string.find('(')
    secpos = string.find(')')
    result6 = string[firstpos+1 : secpos]
    return result6




ANSWER = etttretton()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: 'httpd-access.txt' 
"""

"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def counting():
    """
	bla bla blaha
	"""
    openfile1 = open('httpd-access.txt')
    count = 0
    for line1 in openfile1:
        if line1.startswith('81'):
            count = count + 1
    return count




ANSWER = counting()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def findout():
    """
    bla bla
    """
    openfile2 = open('httpd-access.txt')
    line3 = openfile2.readlines()
    specificline = line3[820]
    result7 = specificline[168 : -1]
    return int(result7)






ANSWER = findout()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, True))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def ip():
    """
	bla bla
	"""
    openfile3 = open('httpd-access.txt')
    count = 0
    for line4 in openfile3:
        if line4.startswith('95.19.133.73'):
            count = count + 1
		#elif line.startswith('95.19.133.73'):
			#count = count + 1
    return int(count)



ANSWER = ip()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, True))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file. Use the built-in
function count() on the file after you have converted it to a string.
Answer with the result as an integer.  

Write your code below and put the answer into the variable ANSWER.
"""
openfile4 = open('httpd-access.txt')
data = openfile4.read()
period = "."
result8 = data.count(period)



ANSWER = result8

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, True))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included. Answer with the piece of
string you found. 

Write your code below and put the answer into the variable ANSWER.
"""
def specific():
    """
	bla bla
	"""
    openfile5 = open('httpd-access.txt')
    line5 = openfile5.readlines()
    specificline = line5[636]
    cut = specificline[65:76]
    return cut




ANSWER = specific()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, True))

"""
Exercise 2.6 
 
Find the last element on each line and sum all that are even numbers.
Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
file = open("httpd-access.txt", "rU")
next(file, None)
summering = 0
for line in file:
    line = line.strip()
    number = line[-1:]
    if (number.isdigit() and int(number) % 2 == 0): 
        summering = summering + int(number)






ANSWER = summering

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, True))


dbwebb.exitWithSummary()
