#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
sum=0
for number in nums:
    sum+=number


print "1.", sum


# 2. Print every even number in nums
print "2. even numbers"

#CODE GOES HERE
total=0

for number in nums:
    b=int(number)/2
    a=b*2
    if number == a:
        print a
        total += 1

# 3. Does nums only contain even numbers? 
only_even = False

#CODE GOES HERE
print "3.",
if total==len(nums):
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()

newlist=list()

for i in range(100):
    j=int(i)/2
    if j*2==i:
        i += 1
        newlist.append(i)

print "4.", newlist





# 5. [ADVANCED]  Multiply each element in nums by its index
#print "5.", __
