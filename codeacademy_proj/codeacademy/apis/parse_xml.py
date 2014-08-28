__author__ = 'rushil'
from xml.dom import minidom

f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
    print(name.firstChild.nodeValue)