import random

#initialize the ints that correspond to moves
rock = 1
scissors = 2
paper = 3

print("1. Rock")
print("2. Paper")
print("3. Scissors")

#need to change to only accept one two or three
playermove = int(input())

#computer move is random between one two and three
computermove = random.choice([1,2,3])

#basically every combination need to make more concise 

if playermove==1 and computermove==2:
    print("paper beats rock:you lose")
elif playermove==1 and computermove==3:
    print("rock beats scissors:you win")
elif playermove==1 and computermove==1:
    print("rock ties rock:you tie")

elif playermove==2 and computermove==1:
    print("paper beats rock:you win")
elif playermove==2 and computermove==2:
    print("paper ties paper:you tie")
elif playermove==2 and computermove==3:
    print("Rock beats paper:you lose")

elif playermove==3 and computermove==1:
    print("rock beats scissors:you lose")
elif playermove==3 and computermove==2:
    print("scissors beat paper:you win")
elif playermove==3 and computermove==3:
    print("scissors ties scissors:tie")

