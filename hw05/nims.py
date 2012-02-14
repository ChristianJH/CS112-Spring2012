#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
x = raw_input("Number of stones in the pile: ")
pile = int(x)


turn = 0
turnLabel = 1
decrease = 0

while pile > 0:
    decrease = raw_input('%d stones left. Player %d [1-5]: ' % (pile,turnLabel))
    decrease = int(decrease)

    if decrease <= 5 and decrease > 0 and pile - decrease >= 0:
        turn = turn * -1 + 1
        turnLabel = turn + 1
        pile -= decrease
    elif pile - decrease < 0 and pile < 6:
        print "Not enough stones."
    elif decrease > 5 or decrease <= 0:
        print "Invalid number of stones."
print "Player %s Wins!" %turnLabel
