events = {
    '1': {
        'prompt': "What do you encounter",
        'A': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You suffer this because of that, move X steps back"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "this happens",
            'fail_value': 1,
            'fail_text': "You suffer this because of that, move X steps back"
        }
    },
    '2': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
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
    }
}