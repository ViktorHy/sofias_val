#!/usr/bin/python
import random
import characters
import events

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
    return success

def pick_char(char):
    if char in characters.characters:
        return 1
    else:
        print("pick a valid character!")
        return 0

## pick character prompt ##
## only exits when you have picked a valid character
char_not_picked = 0
while(char_not_picked):
    char = input ("Pick a character, Bella, Viktor or Jonas: ")
    ok = pick_char(char)
    if ok:
        char_not_picked = 0

## for each event, per chosen character
## test ##
char = 'Viktor'
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
            print(event_skill,char_skill_level)
            dice_outcome = roll(char_skill_level)
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
    
    

    ## Jossan
    jossan_appears = jossan()

    if jossan_appears == 20 and not jossan_has_already_appeared:
        print("you move three steps back")
        score = score + 3
        jossan_has_already_appeared = 1
    input("Press ENTER to continue: ")

print("You have reached your final destination, Sofias office! You look at your watch, it took",score," minues! Yeesh")