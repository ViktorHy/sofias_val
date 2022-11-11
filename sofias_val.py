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
char_events = characters.characters[char]['events']
for event in char_events:
    ## only for the first action, Ryan might knock you out with the toilet door
    if event == '1':
        if random.randint(1,20) > 5:
            ## increase results by 1
            print("As you exit the office, Ryan comes slamming through the toilet door knocking you out. Suffer 1 minute delay\n")
        continue

    print()
    print("--[]--[X]--[]--[]--[]--[]--[]")
    print()
    print(events.events[event]['prompt'])
    chosen = input("A or B?: ")
    ## skill needed for the chosen A or B
    event_skill = events.events[event][chosen]['skill_type']
    char_skill_level = characters.characters[char][event_skill]
    print(event_skill,char_skill_level)
    dice_outcome = roll(char_skill_level)
    if dice_outcome:
        print(events.events[event][chosen]['resolve'])
    else:
        ## also add points to results
        print(events.events[event][chosen]['fail_text'])
    ## Jossan
    jossan_appears = jossan()

    if jossan_appears == 20:
        print("you move three steps back")
    