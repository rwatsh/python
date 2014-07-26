__author__ = 'rushil'

def anti_vowel(text):
    for char in text:
        if char in "AEIOUaeiou":
            text = text.replace(char,'')
    return text

print anti_vowel("Hey You!")
