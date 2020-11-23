import art
import random


print(art.display)
chosen_number = random.randint(1,100)

difficulty = input("Enter the difficulty(E for easy and H for hard): ")

if difficulty == 'E':
    lives = 10
else:
    lives = 5

game_won = False

while lives > 0:
    n = int(input("Enter the guessed number: "))
    if n > chosen_number:
        lives -= 1
        print("My guessed number is lower than what you chose...")
        print('You have '+ str(lives) + (' life' if lives == 1 else ' lives') + ' left')
        
    elif n < chosen_number:
        print("My chosen number is higher than you chose...")
        lives -= 1
        print('You have '+ str(lives) + (' life' if lives == 1 else ' lives') + ' left')

    else:
        print("You guessed right!")
        game_won = True
        break

if not game_won:
    print("The correct number was: "+str(chosen_number))
