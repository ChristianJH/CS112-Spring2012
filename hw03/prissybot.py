import math

name=raw_input("Enter your name: ")
p="PrissyBot"
print p+": Hello there,",name
response1=raw_input(name+": ")
print "%s: You mean, \"%s, sir!\"" % (p, response1)

print "%s: What positive number can you add to 4 to get 3?" % p
response2=raw_input(name+": ")
entry1=float(response2)
answer1=4+entry1
print "%s: 4.0 + %f = %f" % (p, entry1, answer1)
if entry1<=0: print "%s: %f is not a positive number. You are ignorant." % (p, entry1)
if entry1>0: print "%s: %f is not 3. You suck." % (p, answer1)

if entry1<=0: print "%s: But how ignorant?" % p
if entry1>0: print "%s: Do you know what is also not 3?" % p
print "%s: The area of any circle divided by the square of its Radius..." % p
print "%s: Can you tell me what that is?" % p
response3=raw_input(name+": ")
entry2=float(response3)
difference=float(math.pi-entry2)
if difference>0.000001: print "%s: Not true! You are off by %f... You are inferior." % (p, difference)
if difference<-0.000001: print "%s: Not true! You are off by %f... You are inferior." % (p, difference)
if -0.000001<=difference<=0.000001: print "%s: Not true! You are off by a miniscule value, but still you are wrong. Thus, you are inferior." % p

print "%s: I am thinking of the number 7. What should I divide it by?" % p
response4=raw_input(name+": ")
entry3=float(response4)
if entry3!=0: answer2=7/entry3
if entry3!=0: print "%s: 7 / %f = %f" % (p, entry3, answer2)
if entry3!=0: print "%s: You just missed an opportunity. Goodbye, %s." % (p, name)
if entry3==0: print "%s: 7 / %f = I AM ERROR" % (p, entry3)
if entry3==0: print "Pris$,\".-'|~ </PrissyBot> ERROR: ALL YOUR BASE ARE BELONG TO US."


