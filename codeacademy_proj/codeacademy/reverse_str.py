__author__ = 'rushil'

def reverse(text):
    rev_str = ""
    for i in range(len(text) - 1,-1,-1):
        print(text[i]),
        rev_str += text[i]
    return rev_str

reverse("Python!")