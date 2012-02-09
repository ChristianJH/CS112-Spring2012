#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

print "1.", 
x = int(n/2)
y = x*2
if n==y: print "It's even."
elif n!=y: print "It's odd."


# 2. If n is odd, double it
z = n*2
print "2.", 
if n!=y: print z
elif n==y: print n


# 3. If n is evenly divisible by 3, add four
a = int(n/3)
b = a*3
c = n+4
print "3.",
if n==b: print c
elif n!=b: print n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

print "4.",
if grade>=90: print "A"
elif grade>=80: print "B"
elif grade>=70: print "C"
elif grade>=60: print "D"
elif grade>=0: print "F"

