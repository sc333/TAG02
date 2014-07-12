#!/usr/bin/python

import random
import time
from data import *

def inventory(light,axe,sword,food,amulet,suit,wealth):
    """Quartermaster's Store Menu"""
    if wealth == 0:
        print " YOU HAVE NO MONEY"
        delay(2)
        print CLRSCR
        return light,axe,sword,food,amulet,suit,wealth
    print " PROVISIONS & INVENTORY" 
    choice=["0","1","2","3","4","5","6"]
    while choice != "0":
        if wealth == 0:
            print " YOU HAVE NO MONEY"
            delay(2)
            print CLRSCR
            break 
        else:
            print "\n YOU HAVE $%d" % wealth
            print "\n\n"
        print \
        """
 YOU CAN BUY  1 - FLAMING TORCH ($15)
              2 - BATTLE AXE ($10)
              3 - SWORD ($20)
              4 - FOOD ($2 PER UNIT)
              5 - MAGIC AMULET ($30)
              6 - BODY ARMOR ($50)
              0 - CONTINUE ADVENTURE """
        if light == 1:
            print " YOU HAVE A TORCH"
        if axe == 1:
            print " YOUR SUPPLIES NOW INCLUDE ONE AXE"
        if sword == 1:
            print " YOU SHOULD GUARD YOUR SWORD WELL"
        if amulet == 1:
            print " YOUR AMULET WILL AID YOU IN TIMES OF STRESS"
        if suit == 1:
            print " YOU LOOK GOOD IN ARMOR"
        buy = raw_input(" ENTER NO. OF ITEM REQUIRED? ")
        if buy not in choice:
            continue
        if buy == "0":
            print CLRSCR
            break
        if buy == "1":
            light = 1
            wealth -= 15
        if buy == "2":
            axe = 1
            wealth -= 10
        if buy == "3":
            sword = 1
            wealth -= 20
        if buy == "5":
            amulet = 1
            wealth -= 30
        if buy == "6":
            suit = 1
            wealth -= 50
        if wealth < 0:
            print " YOU HAVE TRIED TO CHEAT ME!"
            print " YOU HAVE NO MONEY"
            delay(2)
            wealth=0;suit=0;light=0;axe=0;sword=0;amulet=0;food=int(food/4)
            print CLRSCR
            return light,axe,sword,food,amulet,suit,wealth
        if buy == "4":
            if food > 0:
                print " YOU HAVE %d UNITS OF FOOD" % food
            units = raw_input(" HOW MANY UNITS OF FOOD? ")
            units = int(units)
            if 2 * units > wealth:
                print " YOU HAVEN'T GOT ENOUGH MONEY."
            food += units
            wealth -= 2 * units
        print
    return light,axe,sword,food,amulet,suit,wealth

def eatFood(food,strength):
    """[C]onsume"""
    print CLRSCR
    print " YOU HAVE",food,"UNITS OF FOOD"
    units = raw_input(" HOW MANY UNITS OF FOOD DO YOU WANT TO EAT? ")
    units = int(units)
    if units > food:
        print
        print " YOU DON'T HAVE THAT MUCH FOOD."
        delay(1)
    else:
        strength = strength + (5 * units)
        food = food - units
    print CLRSCR
    return food,strength

def fight(mK,fF,monster,strength,axe,sword,suit):
    """
    part 1 - fight preparation
    """
    if fF == 5: 
        monster = "FEROCIOUS WEREWOLF"
    if fF == 10: 
        monster = "FANATICAL FLESHGORGER"
    if fF == 15: 
        monster = "MALOVENTY MALDEMER"
    if fF == 20: 
        monster = "DEVASTATING ICE-DRAGON"
    if fF == 25: 
        monster = "HORRENDOUS HODGEPODGER"
    if fF == 30: 
        monster = "GHASTLY GRUESOMENESS"
    print
    print " IT IS A %s" % monster
    print
    print " THE DANGER LEVEL IS %d!!" % fF
    print
    delay(1)
    return mK,fF,monster,strength,axe,sword,suit

def battle(mK,fF,monster,light,strength,axe,sword,suit):
    #print "\n ------------------------------------\n"
    raw_input(" PRESS ENTER KEY TO FIGHT\n")
    #print CLRSCR
    if suit > 0:
        print " YOUR ARMOR INCREASES YOUR CHANCE OF SUCCESS"
        fF=(3*(int(fF/4)))
        delay(1.5)
        #print CLRSCR
    for i in range(0,6): 
        print" *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
    if axe == 0 and sword == 0:
        print " YOU HAVE NO WEAPONS"
        print " YOU MUST FIGHT WITH BARE HANDS!"
        print
        fF=int(fF+(fF/5))
        delay(1)
    if axe == 1 and sword == 0:
        print " YOU ONLY HAVE AN AXE TO FIGHT WITH."
        print
        fF=(4*(int(fF/5)))
    if axe == 0 and sword == 1:
        print " YOU MUST FIGHT WITH YOUR SWORD."
        print
        fF=(3*(int(fF/4)))
        delay(1)
    if axe == 1 and sword == 1:
        z=""
        while z != "1" and z != "2":
            z = raw_input(" WHICH WEAPON? 1 - AXE, 2 - SWORD ")
            print
            if z == "1": 
                fF=(4*(int(fF/5)))
                break
            if z == "2": 
                fF=(3*(int(fF/4)))
                break
    """
    part 2 - the battle: fight monster
    """
    while True:
        if random.random() > .5:
            print
            print " %s ATTACKS" % monster
        else:
            print " YOU ATTACK"
        delay(2)
    
        if random.random() > .5 and light == 1:
            print " YOUR TORCH WAS KNOCKED FROM YOUR HAND"
            light = 0
            delay(1)
            
        if random.random() > .5 and axe == 1:
            print " YOU DROP YOUR AXE IN THE HEAT OF BATTLE"
            axe = 0
            delay(1)
            
        if random.random() > .5 and sword == 1:
            print " YOUR SWORD IS KNOCKED FROM YOUR HAND"
            sword = 0
            delay(1)
            
        if random.random() > .5:
            print
            print " YOU MANAGE TO WOUND IT."
            fF=int(5*(fF/6))
        
        if random.random() > .95:
            print " AAAAARGH!!!"
            delay(1)
            print " RIP! TEAR! RIP!"
            
        if random.random() > .9:
            print " YOU WANT TO RUN BUT YOU STAND YOUR GROUND...."
        else:    
            print " &%%$#$% $%# !! @ #$$# #$@! #$ $#$" 
            
        if random.random() > .7:
            print " WILL THIS BE A BATTLE TO THE DEATH?" 
            
        elif random.random() > .7:
            print " HIS EYES FLASH FEARFULLY" 
            
        elif random.random() > .7:
            print " BLOOD DRIPS FROM HIS CLAWS"
            
        elif random.random() > .7:
            print " YOU SMELL THE SULPHUR ON HIS BREATH"
            
        elif random.random() > .7:
            print " HE STRIKES WILDLY, MADLY..........."
            
        elif random.random() > .7:
            print " YOU HAVE NEVER FOUGHT AN OPPONENT LIKE THIS!!"
        
        elif random.random() > .5:
            print
            print " THE MONSTER WOUNDS YOU."
            strength -= 5
        else:
            pass
            
        delay(1)
        
        attack = random.randint(0,100)
        
        if random.random() > .35:
            continue
        else:
            break

    """part 3 - fight aftermath"""
    if random.random()*16 > fF:
        print
        print " AND YOU MANAGED TO KILL THE %s" % monster
        print 
        print
        mK += 1
    else:
        print
        print " THE %s DEFEATED YOU" % monster 
        print 
        print
        strength = int(strength/2)
    fF = 0
    delay(2)
    return mK,fF,monster,light,strength,axe,sword,suit
