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

print(events.events['1'])

## pick character prompt

## for each event, per chosen character
jossan_appears = jossan()

if jossan_appears == 20:
    print("you move three steps back")