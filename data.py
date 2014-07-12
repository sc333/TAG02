#!/usr/bin/python

import random
import time

CLRSCR = "\n"*50

def delay(seconds):
    time.sleep(seconds)

def instructions():
    print CLRSCR
    print " HELLO EXPLORER!"
    print \
    """
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ENTER ONE OF THE FOLLOWING KEYS TO PLAY THE GAME:
   
 [N] = NORTH    [E] = EAST    [U] = UP      [P] = PICK-UP
 [S] = SOUTH    [W] = WEST    [D] = DOWN    [I] = INVENTORY
 [F] = FIGHT    [R] = RUN     [M] = MAGIC   [C] = CONSUME
 [Q] = QUIT     [H] = HELP    [?] = HELP 
     
 GOOD LUCK!
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n
     """
     
numD = 6
directionTable=[["N","\n NO EXIT THAT WAY"],
                ["S","\n THERE IS NO EXIT SOUTH"],
                ["E","\n YOU CANNOT GO IN THAT DIRECTION"],
                ["W","\n YOU CANNOT MOVE THROUGH SOLID STONE"],
                ["U","\n THERE IS NO WAY UP FROM HERE"],
                ["D","\n YOU CANNOT DESCEND FROM HERE"]]

# Set up the Travel Table
#          rm#  N S E W U D T
travelTable=[[0,2,0,0,0,0,0],    # ROOM 1   Hallway
             [1,3,3,0,0,0,0],    # ROOM 2   Audience Chamber
             [2,0,5,2,0,0,0],    # ROOM 3   Great Hall L-shape
             [0,5,0,0,0,0,0],    # ROOM 4   Private Meeting Room
             [4,0,0,3,15,13,0],  # ROOM 5   Inner Hallway
             [0,0,1,0,0,0,0],    # ROOM 6   Entrance
             [0,8,0,0,0,0,0],    # ROOM 7   Kitchen
             [7,10,0,0,0,0,0],   # ROOM 8   Store Room
             [8,8,8,8,8,8,0],    # ROOM 9   Lift
             [8,0,11,0,0,0,0],   # ROOM 10  Rear Vestibule
             [0,0,10,0,0,0,0],   # ROOM 11  Exit
             [0,0,0,13,0,0,0],   # ROOM 12  Dungeon
             [0,0,12,0,5,0,0],   # ROOM 13  Guardroom
             [0,15,17,0,0,0,0],  # ROOM 14  Master Bedroom
             [14,0,0,0,0,5,0],   # ROOM 15  Upper Hall L-shaped
             [17,0,19,0,0,0,0],  # ROOM 16  Treasury
             [18,16,0,14,0,0,0], # ROOM 17  Chambermaid's Bedroom
             [0,17,0,0,0,0,0],   # ROOM 18  Dressing Chamber
             [9,0,0,16,0,0,0]]   # ROOM 19  Small Room Outside of Castle 

# Distribute the treasure 
cnt = 0
while cnt <= 3:
        room = int(random.random()*19)+1
        if room == 6: 
            continue
        if room == 11: 
            continue
        if travelTable[room-1][6] != 0:
            continue
        b = range(10,110)
        treasure = random.choice(b)
        travelTable[room-1][6] = treasure
        cnt += 1
        
# Place androids/aliens in rooms
cnt = 4
while cnt > 0:
        room = int(random.random()*19)+1
        if room == 6: 
            continue
        if room == 11: 
            continue
        if travelTable[room-1][6] != 0:
            continue
        travelTable[room-1][6] = -cnt
        cnt -= 1
        
# Put treasure in the Private Meeting Room and the Treasury. 
# These lines overwrite anything else which has been placed there:
a = range(1,99)
travelTable[3][6]= 100 + random.choice(a)
travelTable[15][6]= 100 + random.choice(a)

def roomDescriptions(roomNum):
    print
    print
    print " **************************"
    print
    print
    if roomNum == 6: room6()
    if roomNum == 1: room1()
    if roomNum == 2: room2() 
    if roomNum == 3: room3()
    if roomNum == 5: room5() 
    if roomNum == 4: room4() 
    if roomNum == 13: room13() 
    if roomNum == 12: room12()
    if roomNum == 15: room15()
    if roomNum == 14: room14() 
    if roomNum == 17: room17() 
    if roomNum == 18: room18()
    if roomNum == 16: room16() 
    if roomNum == 19: room19()
    if roomNum == 9: 
        room9()
        roomNum=8
    if roomNum == 8: room8() 
    if roomNum == 7: room7() 
    if roomNum == 10: room10() 
    if roomNum == 11: room11() 
    return roomNum

def room1():
    print " YOU ARE IN THE HALLWAY"
    if random.random() > 0.4:
        print " FROM THE DUST ON THE GROUND YOU CAN TELL"
        print " NO-ONE HAS WALKED HERE FOR A LONG, LONG TIME"
    print " THERE IS A DOOR TO THE SOUTH"
    print " THROUGH WINDOWS TO THE NORTH YOU CAN SEE A SECRET HERB GARDEN"
    print

def room2():
    print " THIS IS THE AUDIENCE CHAMBER"
    if random.random() > 0.4:
        print " THE FADED TAPE STRIES ON THE WALL ONLY"
        print " HINT AT THE SPLENDOR WHICH THIS ROOM ONCE HAD"
    print " THERE IS A WINDOW TO THE WEST. BY LOOKING TO THE RIGHT"
    print " THROUGH IT YOU CAN SEE THE ENTRANCE TO THE CASTLE."
    print


def room3():
    print " YOU ARE IN THE GREAT HALL, AN L-SHAPED ROOM"
    print " THERE ARE TWO DOORS IN THIS ROOM"
    print " THE WOOD PANELS ARE WARPED AND FADED..."
    if random.random() > 0.4:
        print " AS YOU STAND THERE, YOU HEAR A MOUSE SCAMPER ALONG"
        print " THE FLOOR BEHIND YOU..."
        print " YOU WHIRL AROUND...BUT SEE NOTHING!"
    print


def room4():
    print " THIS IS THE MONARCH'S PRIVATE MEETING ROOM."
    if random.random() < 0.4:
        print " THE ECHO OF ANCIENT PLOTTING AND WRANGLING HANGS"
        print " HEAVY IN THE MUSTY AIR..."
    print " THERE IS A SINGLE EXIT TO THE SOUTH."
    print

def room5():
    print " THIS INNER HALLWAY CONTAINS A DOOR TO THE NORTH,"
    print " AND ONE TO THE WEST, AND A CIRCULAR STAIRWELL"
    print " PASSES THROUGH THE ROOM."
    if random.random() > 0.6:
        print " THE ROOM IS SMALL, AND UNFRIENDLY"
    print " YOU CAN SEE AN ORNAMENTAL LAKE THROUGH THE"
    print " WINDOWS TO THE SOUTH"
    print

def room6():
    print " YOU ARE AT THE ENTRANCE TO A FORBIDDING-LOOKING"
    print " STONE CASTLE. YOU ARE FACING EAST"
    print

def room7():
    print " THIS IS THE CASTLE'S KITCHEN. THROUGH WINDOWS IN"
    print " THE NORTH WALL YOU CAN SEE A SECRET HERB GARDEN."
    print " IT HAS BEEN MANY YEARS SINCE MEALS WERE"
    print " PREPARED FOR THE MONARCH AND THE COURT"
    print " IN THIS KITCHEN......."
    if random.random() > 0.4:
            print " ...A RAT SCURRIES ACROSS THE FLOOR..."

def room8():
    print " YOU ARE IN THE STORE ROOM, AMIDST SPICES,"
    print " VEGETABLES, AND VAST SACKS OF FLOUR AND"
    print " OTHER PROVISIONS."
    print " THE AIR IS THICK WITH SPICE AND CURRY FUMES..."
    print

def room9():
    print " YOU HAVE ENTERED THE LIFT..."
    delay(1)
    print " IT SLOWLY DESCENDS..."
    print
    print " **************************"
    delay(2)
    print

def room10():
    print " YOU ARE IN THE REAR VESTIBULE"
    print " THERE ARE WINDOWS TO THE SOUTH FROM WHICH YOU"
    print " CAN SEE THE ORNAMENTAL LAKE"
    print " THERE IS AN EXIT TO THE EAST AND"
    print " ONE TO THE NORTH"
    print

def room11():
    return

def room12():
    print " YOU ARE IN THE DANK, DARK DUNGEON"
    print " THERE IS A SINGLE EXIT, A SMALL HOLE IN"
    print " THE WALL TOWARDS THE WEST"
    if random.random() > 0.4:
        print " ...A HOLLOW, DRY CHUCKLE IS HEARD"
        print " FROM THE GUARD ROOM...."
    print

def room13():
    print " YOU ARE IN THE PRISON GUARDROOM, IN THE"
    print " BASEMENT OF THE CASTLE. THE STAIRWELL"
    print " ENDS IN THIS ROOM. THERE IS ONE OTHER"
    print " EXIT, A SMALL HOLE IN THE EAST WALL"
    print " THE AIR IS DAMP AND UNPLEASANT...A CHILL WIND"
    print " RUSHES INTO THE ROOM FROM GAPS IN THE STONE"
    print " AT THE TOP OF THE WALLS"
    print

def room14():
    print " YOU ARE IN THE MASTER BEDROOM ON THE UPPER"
    print " LEVEL OF THE CASTLE...."
    print " LOOKING DOWN FROM THE WINDOWS TO THE WEST YOU"
    print " CAN SEE THE ENTRANCE TO THE CASTLE, WHILE THE"
    print " SECRET HERB GARDEN IS VISIBLE BELOW THE NORTH"
    print " WINDOW. THERE ARE DOORS TO THE EAST AND"
    print " TO THE SOUTH...."
    print

def room15():
    print " THIS IS THE L-SHAPED UPPER HALLWAY."
    if random.random() > 0.4:
        print " ...A MOTH FLITS ACROSS NEAR THE CEILING..."
    print " TO THE NORTH IS A DOOR, AND THERE IS A"
    print " STAIRWELL IN THE HALL AS WELL. YOU CAN SEE"
    print " THE LAKE THROUGH THE SOUTH WINDOWS"
    print

def room16():
    print " THIS ROOM WAS USED AS THE CASTLE TREASURY IN"
    print " BYGONE YEARS...."
    if random.random() > 0.4:
        print " ...A SPIDER SCAMPERS DOWN THE WALL........"
    print " THERE ARE NO WINDOWS, JUST EXITS"
    print


def room17():
    print " OOOOOH... YOU ARE IN THE CHAMBERMAIDS' BEDROOM."
    print " FAINT PERFUME STILL HANGS IN THE AIR..."
    print " THERE IS AN EXIT TO THE WEST AND A DOOR"
    print " TO THE SOUTH...."
    print

def room18():
    print " THIS TINY ROOM ON THE UPPER LEVEL IS THE"
    print " DRESSING CHAMBER. THERE IS A WINDOW TO THE"
    print " NORTH, WITH A VIEW OF THE HERB GARDEN DOWN"
    print " BELOW. A DOOR LEAVES TO THE SOUTH"
    print
    print " YOU CATCH A GLIMPSE OF YOURSELF IN THE MIRROR"
    print " HANGING ON THE WALL AND ARE SHOCKED AT YOUR"
    print " DISHEVELED APPEARANCE"


def room19():
    print " THIS IS THE SMALL ROOM OUTSIDE THE CASTLE. THERE IS"
    print " A LIFT WHICH CAN BE ENTERED BY A DOOR TO THE NORTH"
    print " ANOTHER DOOR LEADS TO THE WEST. YOU CAN SEE"
    print " THE ORNAMENTAL LAKE THROUGH THE SOUTHERN WINDOWS"
    print

