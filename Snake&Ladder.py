import random
players = [0]
Starting = 0

win = False

while not win:
    print("Hit Enter to role the dice:")
    input("")
    dice_val = random.randint(1,6)
    print(dice_val)


