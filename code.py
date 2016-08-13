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
        inputAccept.append(raw_input().split()[0])
    elif(len(inputAccept)==0):
        continue
    if not (bool(re.match(intChecker,inputAccept[0])) and bool(re.match(intChecker,inputAccept[1]))):
        print "Don't fool me!!!"
        continue
    minNumber,maxNumber = map(int,sorted(inputAccept))
    if(minNumber == maxNumber):
        print "I'm smart enough for that ;)\nStart Again!!!!"
        continue
    print "The number rolled by the die is:-",random.randint(minNumber,maxNumber)
    uWantTo = False
