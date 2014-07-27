__author__ = 'rushil'
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11


print bin(5)
print hex(5)
print oct(15)

print int("110", 2)

print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("0b11001001", 2)

shift_right = 0b1100
shift_left = 0b1

shift_right >>= 2
shift_left <<= 2

print bin(shift_right)
print bin(shift_left)

print bin(0b1110 ^ 0b101)

print bin(12)
print bin(42)
print bin(12 ^ 42)


# check 4th bit
def check_bit4(input):
    bit = input & 0b1000
    print bit
    if bit > 0:
        return "on"
    else:
        return "off"

check_bit4(0b10000)

# turn on 3rd bit from right
a = 0b10111011
print bin(a | 0b100)

# flip all bits
a = 0b11101110
print bin(a ^ 0b11111111)

# flip the nth bit
def flip_bit(number, n):
    mask = 1 << (n-1)
    result = number ^ mask
    return bin(result)

print flip_bit(0b111, 2)