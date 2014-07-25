__author__ = 'rushil'
"""
The PygLatin translator:
Takes a word, extracts the first character from it and puts it to the end
then suffixes the word with 'ay'

Note: The word should only have alpha chars.
"""
pyg = 'ay'
original = raw_input("Enter a word:")
if (len(original) > 0) and (original.isalpha()):
    print original
else:
    print "empty"

word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
print ("Translated word %s in PygLatin is: %s" %(original, new_word))