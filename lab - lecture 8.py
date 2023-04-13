# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

choices = ['rock', 'paper', 'scissors']
p1 = random.choice(choices)
p2 = random.choice(choices)

# First things first, how does someone win the game (paper beats rock, rock 
# beats scissors, scissors beats paper)
# ok lets start with who wins
def wins(rock, paper, scissors):
    # begin by saying which wins in the three straightforward scenarios
    if rock and paper:
        return('paper wins')
        pass
    elif paper and scissors:
        return('scissors wins')
        pass
    elif scissors and rock:
        return('rock wins')
        pass
    # what happens if it is a draw
    else:
        return('Go again')
        pass
def rps (p1, p2):
    print('Rock, paper, scissors, go!')
    # so I want both p1 and p2 to state their choices
    
    # then I want to call wins
    # then I want it to repeat if 'Go again'
    # then I want it to state who won of p1 or p2
    
    
    
        
    

