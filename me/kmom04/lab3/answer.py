#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
9e44f39d35d3e78f6ea5b78c7e03a9dc generated for dave14 at 2015-02-19 14:44:43 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 3 - python 
 
 
"""

"""
--------------------------------------------------------------------------
Section 1. List basics 
 
 
"""

"""
Exercise 1.1 
 
Concatenate the two lists [guitar, butterfly] and [wall, flute]. Answer
with your list.  

Write your code below and put the answer into the variable ANSWER.
"""
list1 = ['guitar', 'butterfly']
list2 = ['wall', 'flute']
list3 = list1 + list2




ANSWER = list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Use the list [wasp, fly, butterfly, bumblebee, mosquito]. Add the words:
'hotdog' and 'pirate' as the second and third element. Answer with the
modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list4 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
list4.insert(1, 'hotdog')
list4.insert(2, 'pirate')




ANSWER = list4

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, True))

"""
Exercise 1.3 
 
Use the list [wasp, fly, butterfly, bumblebee, mosquito]. Replace the third
word with: 'cord'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list4 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
list4[2] = 'cord'




ANSWER = list4

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Sort the list [lion, tiger, ozelot, bobcat, cougar] in ascending
alphabetical order. Answer with the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
list5 = ['lion', 'tiger', 'ozelot', 'bobcat', 'cougar']
list5.sort()




ANSWER = list5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Use the list from the last excercise ([lion, tiger, ozelot, bobcat,
cougar]) and sort it in decending alphabetical order. Answer with the
sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
list6 = ['lion', 'tiger', 'ozelot', 'bobcat', 'cougar']
list6.sort(reverse=True)




ANSWER = list6

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use pop() to get the second and the last element in the list: [wasp, fly,
butterfly, bumblebee, mosquito]. Answer with the popped elements in a new
list. 

Write your code below and put the answer into the variable ANSWER.
"""
list7 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
list7.pop(3)
list7.pop(2)
list7.pop(0)


ANSWER = list7
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, True))

"""
Exercise 1.7 
 
Use remove() to delete the word: 'mosquito' from the list: [wasp, fly,
butterfly, bumblebee, mosquito]. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list8 = ['wasp', 'fly', 'butterfly', 'bumblebee', 'mosquito']
list8.remove('mosquito')





ANSWER = list8

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions 
 
Some basic built-in functions 
"""

"""
Exercise 2.1 
 
Use a built-in function to sum all numbers in the list: [567, 23, 12, 36,
7]. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
list9 = [567, 23, 12, 36, 7]




ANSWER = sum(list9)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Use built-in functions, such as 'sum' and 'len' to get the average value of
the list: [67, 50, 2, 39, 15]. Answer with the result as a float with at
most one decimal. 

Write your code below and put the answer into the variable ANSWER.
"""
list10 = [67, 50, 2, 39, 15]




ANSWER = sum(list10)/len(list10)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Use a built-in function to get the lowest number in the list: [567, 23, 12,
36, 7]. Answer with the result as a integer. 

Write your code below and put the answer into the variable ANSWER.
"""
listlowest = [567, 23, 12, 36, 7]
lowlow = min(listlowest)



ANSWER = lowlow

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Use the built-in functions split() and join() to fix this string:
'The?rain?is?pouring' into a real sentence, (without '?'). Answer with the
fixed string. 

Write your code below and put the answer into the variable ANSWER.
"""
string = 'The?rain?is?pouring'
thing = string.split('?')
thing2 = ' '.join(thing)



ANSWER = thing2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, True))

"""
Exercise 2.5 
 
Use the string: 'For every minute you are angry you lose sixty seconds of
happiness.' and split it with the delimiter ' ' (space). Answer with the
element at index 0. 

Write your code below and put the answer into the variable ANSWER.
"""
string2 = 'For every minute you are angry you lose sixty seconds of happiness'
convert = string2.split()





ANSWER = convert[0]

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, True))

"""
Exercise 2.6 
 
Use slice on the list [tree, stone, grass, water, sky] and replace the
second and third element with 'freezer, fridge'. Answer with the modified
list. 

Write your code below and put the answer into the variable ANSWER.
"""
list11 = ['tree', 'stone', 'grass', 'water', 'sky']
list11[1] = 'freezer'
list11[2] = 'fridge'



ANSWER = list11

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, True))

"""
Exercise 2.7 
 
Use slice on the list [tree, stone, grass, water, sky] and replace the last
two elements with 'freezer, fridge'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list12 = ['tree', 'stone', 'grass', 'water', 'sky']
list12[-1] = 'fridge'
list12[-2] = 'freezer'




ANSWER = list12

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, True))

"""
Exercise 2.8 
 
Use slice on the list [tree, stone, grass, water, sky] and insert the words
'freezer, fridge' after the third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list13 = ['tree', 'stone', 'grass', 'water', 'sky']
list13.insert(3, 'freezer')
list13.insert(4, 'fridge')




ANSWER = list13

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, True))

"""
Exercise 2.9 
 
Use 'del' on the list [pig, horse, cow, cat, dog] and delete the first
element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list14 = ['pig', 'horse', 'cow', 'cat', 'dog']
del list14[0]



ANSWER = list14

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, True))

"""
Exercise 2.10 
 
Use 'del' on the list [pig, horse, cow, cat, dog] and delete the second and
third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list15 = ['pig', 'horse', 'cow', 'cat', 'dog']
del list15[1]
del list15[1]




ANSWER = list15

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, True))

"""
Exercise 2.11 
 
Assign the list [c, b, a, e, d] to a variable called 'list1'. Assign the
list again, but to another variable called 'list2'. Answer with the result
of 'list1 is list2'.  

Write your code below and put the answer into the variable ANSWER.
"""
list1 = ['c', 'b', 'a', 'e', 'd']
list2 = ['c', 'b', 'a', 'e', 'd']
result = list1 is list2



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12 
 
Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this: list3 = list1. Answer with the result of 'list1
is list3'. 

Write your code below and put the answer into the variable ANSWER.
"""
list3 = list1
result2 = list3 is list1



ANSWER = result2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13 
 
Use your lists from the last exercise. Change the first element in 'list1'
to 'x'. Answer with 'list3'. 

Write your code below and put the answer into the variable ANSWER.
"""
list1[0] = 'x'




ANSWER = list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments 
 
Some excercises with passing lists as arguments to a function. 
"""

"""
Exercise 3.1 
 
Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10. Use the
list: [567, 23, 12, 36, 7], and the built-in method 'sort()'. Answer with
the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
def dostuff():
    """
    do stuff
    """
    list16 = [567, 23, 12, 36, 7]
    result23 = [x * 10 for x in list16]
    print(result23.sort())
    return result23




ANSWER = dostuff()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, True))

"""
Exercise 3.2 
 
Create a function that takes the list: [67, 50, 2, 39, 15] as argument. The
function should multiply all even numbers by 1 and add 5 to all odd
numbers. Answer with the modified list sorted in numerical order,
descending. 

Write your code below and put the answer into the variable ANSWER.
"""
def odds(arg):
    """
    odds
    """
    for a in arg:
        if a % 2 != 0:
            yield a + 5


def even(arg):
    """
    even
    """
    for b in arg:
        if b % 2 == 0:
            yield b * 1


items = [67, 50, 2, 39, 15]

copy = list(odds(items))
copy2 = list(even(items))

copy3 = copy + copy2



ANSWER = sorted(copy3, reverse=True)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, True))


dbwebb.exitWithSummary()
