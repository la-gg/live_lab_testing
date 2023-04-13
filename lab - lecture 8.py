# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

choices = ['rock', 'paper', 'scissors']
#To start, need to make a function
def rock_paper_scissors(p1, p2):
    # Args
    p1 = random.choice(choices)
    p2 = random.choice(choices)
    # If you get the same thing
    if p1 == p2:
        print('Go again.')
        pass
    # Need to say what happens for someone to win
    elif 
