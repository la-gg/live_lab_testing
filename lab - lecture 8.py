# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

def random_choices(p1, p2, choices = ['rock', 'paper', 'scissors']):
    p1 = random.choice(choices)
    p2 = random.choice(choices)

# First things first, how does someone win the game (paper beats rock, rock 
# beats scissors, scissors beats paper)
# ok lets start with who wins
def wins(p1, p2, rock, paper, scissors): # this is just the determination
    random_choices(p1, p2)
    # so I want both p1 and p2 to state their choices
    print(f'player 1 is {p1}')
    print(f'player 2 is {p2}')
    # begin by saying which wins in the three straightforward scenarios
    while p1 != p2:
        if rock and paper:
            paper > rock
            return ('Paper beats rock')
        elif paper and scissors:
            scissors > paper
            return ('Scissors beats paper')
        elif scissors and rock:
            rock > scissors
            return ('Rock beats scissors')
    # what happens if it is a draw
    while p1 == p2:
        return('Go again') # restart the loop
        continue
    
def the_game(p1, p2): # so this should just be the game
    print('Rock, paper, scissors, go!')
   # then I want to call wins
    wins(p1, p2, rock, paper, scissors)
    
    
    # then I want it to repeat if 'Go again'
    # then I want it to state who won of p1 or p2
    
    
    
        
    

