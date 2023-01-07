from data import *
import random

def Party(sqaud_member):
    party = dict()
    if type(sqaud_member) == int:
        if sqaud_member >= 0 and sqaud_member <= 3:
            for i in range(sqaud_member):
                party[f'member{i+1}'] = random.choice(characters)
    return party

print(Party(0))
print(Party(1))
print(Party(2))
print(Party(3))