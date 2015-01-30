#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
de1c4fe0caaa46ce39fbd9561c687f12 generated for dave14 at 2015-01-30 09:11:16 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more. 
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic. 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 15. Create another
variable called 'numTwo' and give it the value 94. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 15
numTwo = 94
result = numOne + numTwo




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 10. Create
another variable called 'numFour' and give it the value 94. Subtract
'numThree' from 'numFour' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numThree = 10
numFour = 94
result = numFour - numThree




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
result = numOne * numThree




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 30 / 5




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 72.5. Create
another variable called 'floatTwo' and give it the value 73.88. Sum the two
values and answer with the result, rounded to 2 decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
floatOne = 72.5
floatTwo = 73.88
result = floatOne + floatTwo




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, True))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
result = floatOne - floatTwo




ANSWER = round(result, 2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
result = floatOne * floatTwo




ANSWER = round(result, 4)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 256, 'n2' = 228 and 'n3' = 82. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
n1 = 256
n2 = 228
n3 = 82
result = n1 + n2 - n3




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 666 modulo (%) 18. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 666%18




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'error' to the word: 'barbeque' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'barbeque'
word2 = 'error'
result = word + word2



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 
 
"""

"""
Exercise 2.1 
 
Answer with the boolean value of: 322 is less than 162. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 322 < 162




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 245 is larger than 394. 

Write your code below and put the answer into the variable ANSWER.
"""
result = 245 > 394




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 322 == 245. 

Write your code below and put the answer into the variable ANSWER.
"""
value = 322 == 245
result = value




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 5, 'd2' = 3 and
'd3' = 4. Sum them up and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
d1 = 5
d2 = 3
d3 = 4
result = d1 + d2 + d3




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.  

Write your code below and put the answer into the variable ANSWER.
"""
a = 5
b = 7
dice = a + b
result = 'change me'
if dice >= 11:
    result = 'big'
else:
    result = 'nothing'

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, True))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks. 

Write your code below and put the answer into the variable ANSWER.
"""
a = 5
b = 7
c = 3
summa = a + b + c
result = 'change me'
if a == b == c:
    result = 'triple'
elif summa >= 11:
    result = 'big'

elif summa <= 10:
    result = 'small'




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions 
"""

"""
Exercise 3.1 
 
Use max() to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
serie = [6, 7, 94, 2, 12, 152, 3, 78, 621, 45]
result = max(serie)



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use min() to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
serie = [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]
result = min(serie)




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use len() to find the number of letters in the word: input. Answer with the
result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = 'input'
result = len(word)




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 74 to a string and add it to the word 'input'. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
number = 74
result = 'input' + str(number)




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 918.81 to an integer and then to a string. Add it to the
beginning of the word: 'input'. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
number = 918.81
word = 'input'
intnumber = int(number)
strnumber = str(intnumber)
result = strnumber + word




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions 
"""

"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 31 and 90. The
function should return the product of the numbers. Answer with a call to
the function.  

Write your code below and put the answer into the variable ANSWER.
"""
def prodNr(arg1, arg2):
    """
    docstring för att göra pylint nöjd...
    """
    total = arg1 * arg2
    return total
    



ANSWER = prodNr(31, 90)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'resort' and
answer with a call to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def funnyWord(resort):
    """
    docstring för att göra pylint nöjd...
    """
    string = ' is a funny word'
    resultfunny = resort + string
    return resultfunny




ANSWER = funnyWord('resort')

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 21 and answer with a call
to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def inRange(arg):
    """
    docstring för att göra pylint nöjd...
    """
    if arg > 50 and arg < 100:
        return True
    else:
        return False




ANSWER = inRange(21)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, True))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops.  
"""

"""
Exercise 5.1 
 
Create a while-loop that adds 5 to the number 30, 49 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
number = 30
stop = 1
while stop <= 49:
    number = number + 5
    stop = stop + 1
    
print(number)




ANSWER = number

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, True))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 9 from 85, 71 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
number = 85
stop = 71
while stop >= 1:
    number = number - 9
    stop = stop - 1



ANSWER = number

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
number = 0
for count in [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]:
    number = number + 1




ANSWER = number

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:
67,2,12,28,128,15,90,4,579,450. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
summa = 0
for array in [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]:
    summa = summa + array




ANSWER = summa

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
largest_so_far = 1
for the_num in [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]:
    if the_num > largest_so_far:
        largest_so_far = the_num




ANSWER = largest_so_far

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:
67,2,12,28,128,15,90,4,579,450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.  

Write your code below and put the answer into the variable ANSWER.
"""
number = 1
result = 0
for number in [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]:
    if number % 2 == 0:
        result = result + number

    if number % 2 != 0:
        result = result - number




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
