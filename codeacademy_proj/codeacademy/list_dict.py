__author__ = 'rushil'
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print inventory

prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3

stock = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

"""
Get total cost of stock items
"""

total = 0
for key in prices:
    value = prices[key]*stock[key]
    print "For %s value is %s" %(key,value)
    total += value
print total