events = {
    '1': {
        'prompt': "What do you encounter",
        'location': "---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
    },
    '2': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '3': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "You sprint back, using extremy all your dexterity and speed. Spring back, shouting. DOKUMENTPORTALEN!",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '4': {
        'prompt': "",
        'location': "---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '5': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '6': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '7': {
        'prompt': "You pass by the last room before your final goal. At the door Andrea stands looking stern. To be able to pass by my office I need you to take a test\nWhat standard are we ackredited by\nIs it A, 15189\nor\nis it B, 15181?\n",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---",
        'A': {
            'skill_type': "question",
            'resolve': "Correct, you got lucky punk. I would have sent my cribs and blood homies at you",
            'fail_value': 1,
        },
        'B': {
            'skill_type': "question",
            'fail_value': 0,
            'fail_text': "Andrea looks dissapointed, you are incorrect. She gives you a lecture taking up the better part of a minute"
        }
    },
    '8': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '9': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
    '10': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You shout as you pass by her office, 'you can find it on dokumentsportalen!'\n",
            'fail_value': 1,
            'fail_text': "You search your mind, but you do not possess the mind capacity to solve this task, you lose 1 min of time\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You were not fast enough, this delays you another 1 min"
        }
    },
}