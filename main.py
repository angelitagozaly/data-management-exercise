import random

numOfHead = 0
numOfTail = 0

userName = input('Who are you?\n')
print("Hello, ", userName, "!")

print("Tossing a coin...")
for round in range(3):
    coinToss = random.randint(1, 2)
    if coinToss == 1:
        print("Round", round, ": Heads")
        numOfHead += 1
    elif coinToss == 2:
        print("Round", round, ": Tails")
        numOfTail += 1
if numOfHead > numOfTail:
    print("You won!")
else:
    print("You lost!")
print("Heads: ", numOfHead, ", Tails: ", numOfTail)
