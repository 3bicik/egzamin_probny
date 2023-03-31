from random import randint

ALLOWED_DICE = [3, 4, 6, 8, 10, 12, 100]

def roll(quantity, type=6, modifier=0):
    if type not in ALLOWED_DICE:
        raise Exception("No such dice")
    else:
        result = 0
        for _ in range(quantity):
            result += randint(1, type)
    return result + modifier


print(roll(2, 6, 10))
print(roll(2, 100, 10))
print(roll(2, 7, 10))
