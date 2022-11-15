events = {
    '1': {
        'prompt': "What do you encounter",
        'location': "---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
    },
    '2': {
        'prompt': "You are closing in on the usually eerily empty room, but your new colleague Camilla is now inhabiting the closest chair to the door. \n She's doing quality assurance work and need your help to find a document.\n Will you A: Try to remember where this document is \n or \n will you B: run back to your computer to find where it is?",
        'location': "---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'skill_type': "diceroll",
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
        'prompt': "You pass by bioinformatikrum 2, they are having a really nerdy conversation about games. When they see you they stop their bickering, and Sailendra asks you would you rather\nA, play a game of chess against me\nor\nB, play a game of mario cart against Paul?",
        'location': "---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---[ ]---",
        'skill_type': "diceroll",
        'A': {
            'skill_type': "intelligence",
            'resolve': "You do one of you famous opening moves, check mate, took you no time at all\n",
            'fail_value': 1,
            'fail_text': "Sailendra dominates you in a long game, playing with you. This has taken a long time, lose 1 min\n"
        },
        'B': {
            'skill_type': "agility",
            'resolve': "You drop a banana peel, collect every speed-up and lap Paul easily. VICTORY",
            'fail_value': 1,
            'fail_text': "Paul totally stomps you out. After lapping you three times, he decides to keep throwing turtle shells at you for a while. Lose 1 minute of time"
        }
    },
    '4': {
        'prompt': "As you pass by hmhm room, Mina enter from the lab corridor, she has trouble running the Tecan in post-PCR. She says the plate reader wont work\nWill you A, try to convince her to restart the machine (again)?\nor\nWill you B, help her fix it yourself?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---[ ]---",
        'skill_type': "diceroll",
        'A': {
            'skill_type': "charisma",
            'resolve': "You wave your hand like Obi-Wan Kenobi and say 'You will restart it again', and Mina repeats 'I will restart it again' and walks off\n",
            'fail_value': 1,
            'fail_text': "Your try to convince her to do it herself, but Mina just smiles and says 'I have already restarted it, again'. You follow Mina into post-PCR and help her. Lose 1 minute\n"
        },
        'B': {
            'skill_type': "intelligence",
            'resolve': "You follow Mina to the machine, and with your brilliant mind you can easily see that the screen is in fact off. You turn it on without losing any time",
            'fail_value': 1,
            'fail_text': "You fail to understand the problem, and end up restarting everything everywhere all at once, lose 1 minute of time"
        }
    },
    '5': {
        'prompt': "You are closing in on genetiker/analytiker rum 2, you can hear Maria arguing with Sahn (a totally fictional character). Will you A, try to sneak past\nor\nwill you B, say hello?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---[ ]---",
        'skill_type': "diceroll",
        'A': {
            'skill_type': "stealth",
            'resolve': "You expertly sneak past, dodging, weaving, all whilst remaining hidden in the shadows. Even using the varumottagning room to evade Sahn's ever-present gaze",
            'fail_value': 1,
            'fail_text': "Blast!, you trip on an empty box left outside of varumottagningen. Sahn catches you and starts talking about genlistor...bla..genlistor...bla....Delaying you 1 minute"
        },
        'B': {
            'skill_type': "charisma",
            'resolve': "You greet Sahn with a warm, smooth, charming hello! He stumbles, 'did I have anything to say? Never mind forget it be on your way!'",
            'fail_value': 1,
            'fail_text': "You mutter hello, he's not impressed. You end up talking about genlistor for 1 minute"
        }
    },
    '6': {
        'prompt': "On your way past labb-rum 1 Maria catches you 'can you help me with Clarity?' You look around you in panic, is Bella here today? No...\nWill A, search your mind palace for answer?\nor\nWill you B, try to bribe Maria with your home-made cookies?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---[ ]---",
        'skill_type': "diceroll",
        'A': {
            'skill_type': "clarity",
            'resolve': "With your immense clarity skills you solve this, and it took no time at all. Bella would have been proud\n",
            'fail_value': 1,
            'fail_text': "All you could remember is, artefact, ice-bucket, workflow and master step...nothing helps. Lose 1 minute of time\n"
        },
        'B': {
            'skill_type': "baking",
            'resolve': "Your newly baked goods, gives off an irresistable aroma all the way from the lunch room. Maria forgets, clarity? shmarity..I want cookies!",
            'fail_value': 1,
            'fail_text': "Maria shrugs, why would I want those burnt hollow shells, a pathetic excuse for a cookie. Help me with clarity instead. Lose 1 minute of time"
        }
    },
    '7': {
        'prompt': "You pass by the last room before your final goal. At the door Andrea stands looking stern. To be able to pass by my office I need you to take a test\nWhat standard are we ackredited by\nIs it A, 15189\nor\nis it B, 15181?\n",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---[ ]---",
        'skill_type': "question",
        'A': {
            'resolve': "Correct, you got lucky punk. I would have sent my cribs and blood homies at you",
            'fail_value': 1,
        },
        'B': {
            'fail_value': 0,
            'fail_text': "Andrea looks dissapointed, you are incorrect. She gives you a lecture taking up the better part of a minute"
        }
    },
    '8': {
        'prompt': "You come up to Sofias office, the door is closed and Rendas (fictional character) is yapping on about pilot-projekt never even pausing for a breath; she cannot hear you!\nYou need to crack the code to her door\nYou know you had the code written down somewhere in your office, maybe on a whiteboard?",
        'location': "---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[ ]---[X]---",
        'skill_type': "question_freeform",
        'fail_value': 1,
        'fail_text': "You type the code...wrong..this took you 1 minute",
        '1587': {
            'char': 'Viktor',
            'resolve': "Your type the code 1  5  8  7...CORRECT! You enter the room",
        },
        '1235': {
            'char': 'Jonas',
            'resolve': "Your type the code 1  2  3  5...CORRECT! You enter the room",
        },
        '8899': {
            'char': 'Bella',
            'resolve': "Your type the code 8  8  9  9...CORRECT! You enter the room",
        },
    },
}