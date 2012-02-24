#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

# def greeter(name):

def greeter(name):
    name = str(name)
    print "hello,", name.lower()


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

# def box(w,h):

def box(w,h):
    if w<=0 or h<=0 or type(w)!=int or type(h)!=int:
        print "Error: Invalid Dimensions"
        return

    corner1 = "+"
    edge1 = "|"
    if w >= 2:
        corner2 = "+"
        edge2 = "|"
    else:
        corner2 = ""
        edge2 = ""
    topgate = "-" *(w-2)
    rowspace = " " *(w-2)
    top = corner1+topgate+corner2
    row = edge1+rowspace+edge2
    
    print top
    for i in range(h-2):
        print row
    if h > 1:
        print top


# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

