__author__ = 'rushil'
my_dict = {
    "Name": "Watsh",
    "Age": 40,
    "LastName": "Rajneesh"
}

print my_dict.keys()
print my_dict.values()

# using zip() built-in function to iterate lists of keys and values simultaneously
for key, value in zip(my_dict.keys(), my_dict.values()):
    print key, " " , value