#!/usr/bin/python
import sys
import re
import random
import time

uWantTo = True              # Game control variable

print "Welcome to my first open source Project :)"
print "This is a game which will give you your lucky number after rolling a die with faces of numbers of your choice!!!"
intChecker = re.compile("^[\-]?[0-9]*$")
while uWantTo:
    inputAccept = raw_input("Enter the range of numbers you want to choose:-").split()
    if(len(inputAccept)==1):
        s=''
        while(s==''):    s=raw_input()
        inputAccept.append(s)
    elif(len(inputAccept)==0):
        continue
    if not (bool(re.match(intChecker,inputAccept[0])) and bool(re.match(intChecker,inputAccept[1]))):
        print "Don't fool me!!!"
        continue
    minNumber,maxNumber = sorted(map(int,inputAccept)[:2])
    if(minNumber == maxNumber):
        print "I'm smart enough for that ;)\nStart Again!!!!"
        continue
    sys.stdout.write("Rolling your die ")
    sys.stdout.flush()
    for _ in xrange(5):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.75)
    print "\nThe number rolled by the die is:-",random.randint(minNumber,maxNumber)
    if raw_input("\nDo You wish to play again(y/n):")=='n':
        uWantTo = False
