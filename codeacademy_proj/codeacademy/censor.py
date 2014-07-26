__author__ = 'rushil'
def censor(text, word):
    lst = text.split()
    for index, w in enumerate(lst):
        if w == word:
            lst[index] = "*" * len(word)
    return " ".join(lst)

censor("this hack is wack hack", "hack")