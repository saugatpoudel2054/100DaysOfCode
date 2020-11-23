import data
import art
import random

#Print the art message
def printer(A,B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")



#Choose 2 random items from the data part for comparision
def chooseItems(itemA):
    itemB = random.choice(data.data)
    while random.choice(data.data) == itemA:
        itemB = random.choice(data.data)
    return itemB


#Ask for input and check if the comaprision made was correct. If yes game continues, else print final score
def higher(A,B):
    choice = input("Who has more followers, type A or B: ")
    if choice == 'A':
        if A['follower_count'] > B['follower_count']:
            return 1
        else:
            return 0
    else:
        if B['follower_count'] > A['follower_count']:
            return 1
        else:
            return 0

#Actual game run
score = 0
print(art.logo)
itemA = random.choice(data.data)

while True:
    itemB = chooseItems(itemA)
    printer(itemA, itemB)
    if higher(itemA, itemB) == 1:
        score += 1
        print("Correct choice... Your score is "+str(score))
        itemA = itemB
    else:
        print(f"Wrong choice... Your final score is {score}")
        break
    print()