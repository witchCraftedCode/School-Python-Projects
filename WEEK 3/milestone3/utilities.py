import random

# 2 Functions must be written in here

# Function 1 (Rando-pick)
def randopick(L):
    random.shuffle(L)
    return random.choice(L)


# Function 2 (Importify)

def importify(T):
    with open(T, 'r') as f:
        return f.read().splitlines()