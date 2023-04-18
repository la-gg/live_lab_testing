# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

def choice(choices = ['rock', 'paper', 'scissors']):
    random.choice(choices)

##Answers [Global]: I could have created a dictionary to state what beats what, and then created an if else block
## Answers[functions]: 


# First things first, how does someone win the game (paper beats rock, rock 
# beats scissors, scissors beats paper)
# ok lets start with who wins
def wins(p1, p2, 'rock', 'paper', 'scissors'): # this is just the determination
    p1 = choice()
    p2 = choice()
    # so I want both p1 and p2 to state their choices
    print(f'player 1 is {p1}')
    print(f'player 2 is {p2}')
    # begin by saying which wins in the three straightforward scenarios
    while p1 != p2:
        if 'rock' and 'paper':
            'paper' > 'rock'
            return print('Paper beats rock')
        elif 'paper' and 'scissors':
            'scissors' > 'paper'
            return print('Scissors beats paper')
        elif 'scissors' and 'rock':
            'rock' > 'scissors'
            return print('Rock beats scissors')
    # what happens if it is a draw
    while p1 == p2:
        return print('Go again') # restart the loop
        continue

wins

def the_game(): # so this should just be the game
    __init__(self, p1, p1):
        self.p1 = p1
        self.p2 = p2
    print('Rock, paper, scissors, go!')
   # then I want to call wins
    wins(p1, p2, 'rock', 'paper', 'scissors')
    # then I want it to state who won of p1 or p2
    
    
## I'm going to look at the answers more this weekend
        
    

