__author__ = 'rushil'
with open("text.txt", "w") as my_file:
	my_file.write("Success!")

print my_file.closed

# redundant since with..as takes care of closing the file
if not my_file.closed:
    my_file.close()
print my_file.closed