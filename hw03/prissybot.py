import math

#This is the part where the player enters his/her name

name=raw_input("Enter your name: ")
p="PrissyBot"

#PrissyBot uses the player's name in a sentance

print p+": Hello there,",name

#Defines the Player's response and spits it back at him/her

response1=raw_input(name + ": ")
print "%s: You mean, \"%s, sir!\"" % (p, response1)

#Asks an impossible question. The player's answer will be wrong for different reasons. If statement leads to the specific explaination for why the player is wrong.

print "%s: What positive number can you add to 4 to get 3?" % p
response2 = raw_input(name + ": ")
entry1 = float(response2)
answer1 = 4 + entry1
print "%s: 4.0 + %f = %f" % (p, entry1, answer1)
if entry1 <= 0: 
    print "%s: %f is not a positive number. You are ignorant." % (p, entry1)
    print "%s: But how ignorant?" % p
elif entry1 > 0: 
    print "%s: %f is not 3. You suck." % (p, answer1)
    print "%s: Do you know what is also not 3?" % p

#The previous 2 PrissyBot Response possibilities both lead to this next question.

#It asks for Pi in numerical form. It calculates how far away from the true number of Pi that the player's description of Pi is.

print "%s: I am thinking of a numerical value which is the area of any circle divided by the square of its Radius..." % p
print "%s: Can you tell me what that value is?" % p

#Below is the player's imperfect Pi.

response3 = raw_input(name+": ")
entry2 = float(response3)
difference = math.fabs(float(math.pi-entry2))

#Prissybot will respond saying how much approximately the player's number of Pi is off by. If it is close so that Prissybot would respond with 0.000..., it instead explains that the player is wrong in words instead of using numbers.

if difference > 0.000001: 
    print "%s: Not true! You are off by %f... You are inferior." % (p, difference)
elif difference <= 0.000001: print "%s: Not true! You are off by a miniscule value, but still you are wrong. Thus, you are inferior." % p

#This will either divide or create a fictional error of divide by zero. It's not meant to actually break. If statement will prevent this.

print "%s: I am thinking of the number 7. What should I divide it by?" % p
response4 = raw_input(name+": ")
entry3 = float(response4)
if entry3 != 0: 
    answer2 = 7 / entry3
    print "%s: 7 / %f = %f" % (p, entry3, answer2)
    print "%s: You just missed an opportunity. Goodbye, %s." % (p, name)
elif entry3 == 0: 
    print "%s: 7 / %f = I AM ERROR" % (p, entry3)
    print "Pris$,\".-'|~ </PrissyBot> ERROR: ALL YOUR BASE ARE BELONG TO US."


