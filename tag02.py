#!/usr/bin/python

from data import *
from actions import *

def main():
    print CLRSCR 
    #INITIALISE
    roomNum = 6
    strength = 60 + int(random.random() * 100)
    wealth = 30 + int(random.random() * 100)
    food = 0
    tally = 0
    mK = 0 # monsters killed
    sword = 0
    amulet = 0
    axe = 0
    suit = 0
    light = 0
    player = raw_input(" WHAT IS YOUR NAME, EXPLORER? ")
    print CLRSCR 
    exploring = True
    while exploring: # main game loop
        #########################################################
        strength -= 5
        if strength <= 10:
            print " WARNING, %s, YOUR STRENGTH" % player
            print " IS RUNNING LOW"
            print
        if strength <= 0:
            print " YOU HAVE DIED........."
            break
        #########################################################
        # STATUS AREA
        print " "+ player +", YOUR STRENGTH IS %d" % strength
        if wealth > 0:
            print " YOU HAVE $%d" % wealth
        if food > 0:
            print " YOUR PROVISIONS SACK HOLDS",food,"FOOD UNITS."
        if suit > 0:
            print " YOU ARE WEARING ARMOR"
        if light>0 and axe>0 or sword>0 or amulet>0:
            print " YOU ARE CARRYING",
            if axe > 0:
                print "AN AXE",
            if sword > 0:
                print "A SWORD",
            if (axe >= 1 or sword >= 1) and amulet >= 1:
                print "AND",
            if amulet > 0:
                print "AN AMULET"
        #########################################################
        if light < 1:
            print " IT IS TOO DARK TO SEE ANYTHING"
            print
        if light > 0:
            roomNum = roomDescriptions(roomNum)
        #########################################################
        # ROOM CONTENTS
        contents = travelTable[roomNum-1][6]
        #########################################################
        # IS MONSTER IN ROOM?
        monster=""
        if contents < 0:
            if contents == -1:
                fF = 5 # ferocity Factor
            elif contents == -2:
                fF = 10
            elif contents == -3:
                fF = 15
            elif contents == -4:
                fF = 20
            elif contents == -5:
                fF = 25
            elif contents == -6:
                fF = 30
            print
            print
            print " DANGER...THERE IS A MONSTER HERE...."
            time.sleep(2)
            mK,fF,monster,strength,axe,sword,suit=fight(mK,fF,monster,strength,axe,sword,suit) 
        #########################################################
        # IS TREASURE IN ROOM?
        if travelTable[roomNum-1][6] > 9 and random.random() <= 0.5:
            print " THERE ARE GEMS HERE WORTH $",travelTable[roomNum-1][6]
        elif travelTable[roomNum-1][6] > 9 and random.random() > 0.5:
            print " THERE IS TREASURE HERE WORTH $",travelTable[roomNum-1][6]
        #########################################################
        while True:
            vocabulary=["Q","N","S","E","W","U","D","R","F","I","C","P","M","T","H","?"]
            print
            move = raw_input(" WHAT DO YOU WANT TO DO? ")
            if move.upper() not in vocabulary:
                continue
            else: break
        print
        print
        print " ------------------------------------"
        print
        #########################################################
        # HELP
        if move.upper() == "H" or move.upper() == "?":
            instructions()
        #########################################################
        # QUIT
        if move.upper() == "Q":
            exploring = False
        #########################################################
        if move.upper() == "R" and travelTable[roomNum-1][6] < 0:
            if random.random() > .7:
                print " NO, YOU MUST STAND AND FIGHT"
                print
                move = "F"
                delay(1)
            else:
                move = raw_input(" WHICH WAY DO YOU WANT TO FLEE? ")
        #########################################################
        # NO MOVE THAT WAY: NSEWUD
        for inx in range(0,numD):
            if move.upper() == directionTable[inx][0] \
                    and travelTable[roomNum-1][inx] == 0:
                print
                print directionTable[inx][1]
                print
        #########################################################
        # NOTHING TO FIGHT
        if move.upper() == "F" and travelTable[roomNum-1][6] > -1:
            print " THERE IS NOTHING TO FIGHT HERE."
            print
        #########################################################
        if move.upper() == "I":
            light,axe,sword,food,amulet,suit,wealth = inventory(light,axe,sword,food,amulet,suit,wealth)
        #########################################################
        if move.upper() == "C":
            if food > 0:
                food, strength = eatFood(food, strength)
            else:
                print " YOU HAVE NO FOOD TO EAT."
                print
            tally -= 1
        #########################################################
        if move.upper() == "P":
            if travelTable[roomNum-1][6] != 0:
                if light == 0:
                    print " YOU CANNOT SEE WHERE IT IS."
                    print
                else:
                    #print "\n YOU PICK UP THE TREASURE."
                    wealth = wealth + travelTable[roomNum-1][6]
                    travelTable[roomNum-1][6] = 0
            else:
                print " THERE IS NOTHING TO PICK UP HERE."
                print
            tally -= 1
        tally += 1
        #########################################################
        # FIGHT MONSTER
        if move.upper() == "F" and travelTable[roomNum-1][6] < 0:
            mK,fF,monster,light,strength,axe,sword,suit=battle(mK,fF,monster,light,strength,axe,sword,suit) 
            travelTable[roomNum-1][6] = fF # this should be ZER0 after fight routines 
        #########################################################
        # MOVE TO ROOM
        for inx in range(0,numD):
            if move.upper() == directionTable[inx][0] \
                    and travelTable[roomNum-1][inx]!=0:
                roomNum = travelTable[roomNum-1][inx]
        #########################################################
        if move.upper() == "M":
            for j in range(1,30):
                print "\t","*"*j
                delay(.25)
            roomNum = random.randint(0,20)
            while roomNum == 6 or roomNum == 11:
                roomNum = random.randint(1,20)
        #########################################################
        # SHOW TALLY
        if move.upper() == "T":
            print " YOUR TALLY AT PRESENT IS %d" % \
                    (3 * tally + 5 * strength + 2 * wealth + food + 30*mK)
        if move.upper() == "T" and random.random() > 0.5:
            print " YOU HAVE KILLED %d MONSTERS SO FAR..." % mK
        #########################################################
        if roomNum == 11:
            print "\n YOU'VE DONE IT!!"
            delay(2)
            print " THAT WAS THE EXIT FROM THE CASTLE"
            delay(1)
            print "\n YOU HAVE SUCCEEDED, %s!" % player
            print "\n YOU MANAGED TO GET OUT OF THE CASTLE"
            delay(1)
            print "\n WELL DONE!"
            delay(2)
            exploring = False
        #########################################################
    strength = strength * 5
    wealth = wealth * 2
    tally = tally * 3
    mK = mK * 30
    score = strength+wealth+tally+food+mK
    print "\n YOUR SCORE IS:",score

if __name__ == "__main__":
    main()
