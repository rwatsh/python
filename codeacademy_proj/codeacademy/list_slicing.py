__author__ = 'rushil'

"""
List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

[start:end:stride]

"""
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# print all odds from start to finish so no need to specify the start and end only need stride.
print my_list[::2]
# reverse a list
backwards = my_list[::-1]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# decrypt - read message backwards every other letter from garbled.
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message