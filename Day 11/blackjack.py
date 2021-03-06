import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def distributeCards():
    player = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]

    return (player,computer)

def printer(player, computer):
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer[0]}")

def determineWinner(player,computer):
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's cards: {computer}, current score: {sum(computer)}")

    if sum(player) > sum(computer):
        print("You won...")
    elif sum(player) == sum(computer):
        print("Draw")
    else:
        print("Computer won")

def isBust(x):
    if sum(x) > 21:
        return True
    else:
        return False
        
player, computer = distributeCards()
printer(player, computer)
game = True
playerPlays = True
computerPlays = True

while game and (playerPlays or computerPlays):
    
    choice = input("Do you want to pick one more card? y/n ")

    if choice == 'y':
        card = random.choice(cards)
        print("You picked "+str(card))
        player.append(card)
        if isBust(player):
            game = False
            print("Bust... Computer won.")
            break
        else:
            printer(player,computer)
    else:
        playerPlays = False
        print("You chose not to pick any cards: ")
    
    if(sum(computer) < 15):
            computer.append(random.choice(cards))
            if isBust(computer):
                print("Computer bust... You won")
                print(f"Computers cards were: {computer}")
                game = False
                break
    else:
        print("Computer didnt pick up any card...")
        computerPlays = False

if not playerPlays and not computerPlays:
    determineWinner(player, computer)