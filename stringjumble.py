"""
stringjumble.py
Author: <your name>
Credit: <sources>

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

text = input("Please enter a string of text (the bigger the better):")
print('You entered "' + text + '". Now jumble it:')

i = len(text)
alphanums = range(1, int(i)+1)
Alphabet = list(text)

print(text[::-1])

words = text.split(" ")
print(' '.join(words[::-1]))

l = len(words)
b = 0

while int(l) > int(b):
    sw = words[int(b)]
    print(sw[::-1], end = ' ')
    b = int(b)+1