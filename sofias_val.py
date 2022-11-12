#!/usr/bin/python
import random
import characters
import events
from time import sleep

## function to call upon each step you take forward
## if 20, jossan appears and calls you to fika
def jossan():
    jossan = random.randint(1,20)
    return jossan

def roll(skill):
    roll = random.randint(1,20)
    success = 0
    if (roll <= skill):
        success = 1
    return roll,success

def pick_char(char):
    if char in characters.characters:
        return 1
    else:
        print("pick a valid character!")
        return 0

def check_input(input):
    input = input.upper()
    if input == 'A' or input == 'B':
        return 1,input
    else:
        return 0,input


### welcome to game, explain the goal
print("## Welcome to the game of CMD: Sofias Val!")
print("## Your task is to leave this room, and reach Sofias office")
print("## but....")
print("## on your way there might be obstacles that will delay you")
print("## You'll either play as Bella, Jonas or Viktor")
print("## and each of the characters come with their own skillset")
print("## and perhaps different attractions?")


## pick character prompt ##
## only exits when you have picked a valid character
char_not_picked = 1
while(char_not_picked):
    char = input ("Pick a character, Bella, Viktor or Jonas: ")
    ok = pick_char(char)
    if ok:
        char_not_picked = 0

## for each event, per chosen character
## test ##
#char = 'Viktor'
print("Hi, ",char,"!",sep="")
input("press ENTER to continue:")
score = 0
jossan_has_already_appeared = 0
char_events = characters.characters[char]['events']
for event in range(1,8):
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    
    ## only for the first action, Ryan might knock you out with the toilet door
    if str(event) == '1':
        score = score +1
        if random.randint(1,20) > 10:
            ## increase results by 1
            print("          R")
            print("          /")
            print(events.events[str(event)]['location'])
            print("---MAJ---BF1---GA1---BF2---MIX---GA2---LB1---LB2--SOFIA--")
            print("As you exit the office, Ryan comes slamming through the toilet door knocking you out. Suffer 1 minute delay\n")
            score = score +1
            #input("Press ENTER to continue: ")
            
        else:
            print(events.events[str(event)]['location'])
            print("---MAJ---BF1---GA1---BF2---MIX---GA2---LB1---LB2--SOFIA--")
            print()
            print("You exit the office into the corridor, and nothing happens. Weird?")
            #input("Press ENTER to continue: ")
            

    
    ## now only trigger events that is defined per character in characters.characters['events']
    elif str(event) in characters.characters[char]['events']:
        print(events.events[str(event)]['location'])
        print("---MAJ---BF1---GA1---BF2---MIX---GA2---LB1---LB2--SOFIA--")
        print()
        print(events.events[str(event)]['prompt'])
        score = score +1
        chosen = input("A or B?: ")
        # check input, allow lower case a or b. nothing else
        ok,chosen = check_input(chosen)
        while(not ok):
            chosen = input("not a valid option. A or B?: ")
            ok,chosen = check_input(chosen)


        ## skill needed for the chosen A or B
        event_skill = events.events[str(event)][chosen]['skill_type']
        
        ## event has a question
        if event_skill == "question":
            answer = events.events[str(event)][chosen]['fail_value']
            if answer:
                ## add no score
                print(events.events[str(event)][chosen]['resolve'])
            else:
                # add score, wrong answer
                score = score +1
                print(events.events[str(event)][chosen]['fail_text'])
        
        ## event has a skill check
        else:
            char_skill_level = characters.characters[char][event_skill]
            print("You have chosen an option that requires",event_skill,"roll a D20 below your skill level:",char_skill_level)
            #print(event_skill,char_skill_level)
            input("Press ENTER to roll the die:")
            print("...",end='')
            rolltime = random.randint(1,3)
            sleep(rolltime)
            value,dice_outcome = roll(char_skill_level)
            print(value)
            sleep(2)
            if dice_outcome:
                print(events.events[str(event)][chosen]['resolve'])
            else:
                ## also add points to results
                score = score + 1
                print(events.events[str(event)][chosen]['fail_text'])
    else:
        print(events.events[str(event)]['location'])
        score = score +1
        print("---MAJ---BF1---GA1---BF2---MIX---GA2---LB1---LB2--SOFIA--")
        print("You pass by and noone wants to speak to you..rude")
    
    input("Press ENTER to continue: ")

    ## Jossan can appear only once, but anywhere on your journey that isnt room 1
    jossan_appears = jossan()

    if jossan_appears > 1 and not jossan_has_already_appeared and not event == 1:
        print("Down the corridor you see Jossan, she gesturing everyone with an imaginary cup of coffee. You cannot resist her call and join her for fika")
        print("This detour to the fika room has delayed you 3 minutes!")
        score = score + 3
        jossan_has_already_appeared = 1
        input("Press ENTER to continue: ")

print("You have reached your final destination, Sofias office! You look at your watch, it took",score," minues! Yeesh")