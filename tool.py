import random

def Dice(maxi=6, walk_range=[]):
    ret = random.randint(1, maxi)
    if ret in walk_range:
        ret = 0
    return ret