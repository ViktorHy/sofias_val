#!/usr/bin/python
import random

## function to call upon each step you take forward
## if 20, jossan appears and calls you to fika
def jossan():
    jossan = random.randint(1,20)
    return jossan



jossan_appears = jossan()

if jossan_appears == 20:
    print("you move three steps back")