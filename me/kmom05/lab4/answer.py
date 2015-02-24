#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
c2cf073c0b12a58c2dd26cb8b0dd9cf7 generated for dave14 at 2015-02-24 09:01:52 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 4 - python 
 
Dictionaries and tuples 
"""

"""
--------------------------------------------------------------------------
Section 1. Dictionaries 
 
Some basics with dictionaries. 
"""

"""
Exercise 1.1 
 
Create a small phonebook using a dictionary. Use the names as keys and
numbers as values. Use 'Chandler, Monica, Ross' and corresponding numbers:
'55523645, 55564452, 55545872'. Add the phonenumbers as integers. Answer
with the resulting dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
phonebook = {'Chandler':55523645, 'Monica':55564452, 'Ross':55545872}




ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
How many items are there in the dictionary?  

Write your code below and put the answer into the variable ANSWER.
"""
phonebook = {'Chandler':55523645, 'Monica':55564452, 'Ross':55545872}
count = 0
for value in phonebook.values():
    count += 1


ANSWER = count

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, True))

"""
Exercise 1.3 
 
Use the 'get()' method on your phonebook and answer with the phonenumber of
'Ross'.  

Write your code below and put the answer into the variable ANSWER.
"""
result = phonebook.get('Ross')




ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Get all keys from the dictionary and return them in a sorted list.  

Write your code below and put the answer into the variable ANSWER.
"""
phonebookkeylist = list(phonebook.keys())
sortedlist = sorted(phonebookkeylist)


ANSWER = sortedlist
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, True))

"""
Exercise 1.5 
 
Get all values from the dictionary and return them in a sorted list.  

Write your code below and put the answer into the variable ANSWER.
"""
phonebookvaluelist = list(phonebook.values())
sortedvalues = sorted(phonebookvaluelist)




ANSWER = sortedvalues

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the in-operator to test if the name 'Ross' exists in the dictionary.
Answer with the return boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = 'Ross' in phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Use the in-operator to test if the phone number 55545872 exists in the
dictionary. Answer with the return boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
vals = phonebook.values()


ANSWER = 55545872 in vals

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, True))

"""
Exercise 1.8 
 
Use a for-loop to walk through the dictionary and and create a string
representing it. Each name and number should be on its own row, separated
by a space. The names must come in alphabetical order. Answer with the
resulting string. 

Write your code below and put the answer into the variable ANSWER.
"""
replacement_string = ""
keys = sorted(phonebook.keys())
for key in keys:
    replacement_string += key + " " + str(phonebook[key]) + "\n"



ANSWER = replacement_string

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, True))

"""
Exercise 1.9 
 
Convert the phonenumber to a string and add the prefix '+1-', representing
the language code, to each phone-number. Answer with the resulting
dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
for key, value in phonebook.items():
    phonebook[key] = '+1-' + str(value)




ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, True))

"""
Exercise 1.10 
 
Get and remove the item 'Ross' from the phonebook (use pop()). Answer with
the resulting dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
phonebook5 = {'Chandler':55523645, 'Monica':55564452, 'Ross':55545872} # new phonebook
temporary_ross = phonebook5.pop('Ross', None)
phonebook5.pop('Ross', None)




ANSWER = phonebook5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, True))

"""
Exercise 1.11 
 
Add the item you just popped from the phonebook. Answer with the resulting
dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
phonebook5['Ross'] = temporary_ross #Add ross and its value from the pop from above assignment




ANSWER = phonebook5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Tuples 
 
Some basics with tuples 
"""

"""
Exercise 2.1 
 
Create a tuple with 'elephant, 33, 7.28, stove, 4'. Answer with the length
of the tuple as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
tupleone = ('elehant', 33, 7.28, 'stove', 4)





ANSWER = len(tupleone)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Create a tuple out of: (elephant, 33, 7.28, stove, 4). Assign each value in
the tuple to different variables: 'a','b','c','d','e'. Answer with the
variable: 'd'. Hint: a,b,c = tuple. 

Write your code below and put the answer into the variable ANSWER.
"""
a = tupleone[0]
b = tupleone[1]
c = tupleone[2]
d = tupleone[3]




ANSWER = d

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, True))

"""
Exercise 2.3 
 
Use the list [98, 5, 12, 369, 1]. Assign the first two elements to a tuple
with a slice on the list. Answer with the first element in the tuple as an
integer. 

Write your code below and put the answer into the variable ANSWER.
"""
list1 = [98, 5, 12, 369, 1]
slice1 = list1[0:2]





ANSWER = slice1[0]

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create a tuple with (moose, 12, 1.98, table, 7). Convert it to a list and
replace the second element with: 'fire'. Convert it back to a tuple and
answer with the first three elements in a comma-separated string. 

Write your code below and put the answer into the variable ANSWER.
"""
tupletwo = ('moose', '12', '1.98', 'table', '7')
listtwo = list(tupletwo)
listtwo[1] = 'fire'
slicelist = listtwo[0:3]
stringen = ', '.join(slicelist)
stringen2 = stringen.replace(' ', '')


ANSWER = stringen2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, True))


dbwebb.exitWithSummary()
