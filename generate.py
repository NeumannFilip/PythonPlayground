"""from random import choice # this allows me to just use choice
#import random so random.choice, random.x

coin = choice(["heads", "tails"])
print(coin)"""

"""import random

number = random.randint(1,10)
print(number)"""

import random
cards = ["jacks", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
