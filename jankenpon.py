import random
import sys

#initializing the scores to 0
user_score = 0
computer_score = 0

janken = ['Rock', 'Paper', 'Scissor']

#computer is picking a random item from the list
computer_pick = random.choice(janken)

#user enters her choice and the computer randomly makes a choice
user_input = input('Pick rock, paper, or scissor: ')
print('\nJAN... \nKEN... \nPON!\n')

print(computer_pick+'!\n')

#initializing the result based on the user's choice and the computer's
if (user_input.lower() == 'rock') and computer_pick == 'Scissor!':
    print('OH NO!')
    user_score += 1
    print('Your score is ' + str(user_score))
    user_input = input('Pick rock, paper, or scissor: ')
    #sys.exit()
elif (user_input.lower() == 'paper') and computer_pick == 'Rock!':
    print('DANG IT! You won that one')
    user_score += 1
    print('Your score is ' + str(user_score))
    user_input = input('Pick rock, paper, or scissor: ')
elif (user_input.lower() == 'scissor') and computer_pick == 'Paper!':
    print('WHAT! NO WAY!')
    user_score += 1
    print('Your score is ' + str(user_score))
    user_input = input('Pick rock, paper, or scissor: ')
elif user_input.lower() == computer_pick.lower():
    print('Woops! A draw!')
    user_input = input('Pick rock, paper, or scissor: ')
else:
    print('YOU LOSE! HAHA!\n')
    computer_score += 1
    print('Computer score is ' + str(computer_score) + '.\n')
    user_input = input('Pick rock, paper, or scissor: ')
