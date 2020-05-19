# rock paper scissors
from random import randint

print('...rock...\n...paper...\n...scissors...\n')

print('1 player or 2 player?')
players = input()

print('Enter Player 1 Choice:')
player1 = input().lower()

# variables declared inside conditionals still available outside the conditional
player2 = None
player2_name='Player 2'
if players == '2':
  print('Enter Player 2 Choice:')
  player2 = input().lower()
else:
  num = randint(1,3)
  if num == 1:
    player2 = 'rock'
  elif num == 2:
    player2 = "paper"
  else:
    player2 = "scissors"
  print(f'\nComputer Chooses {player2}\n')
  player2_name = 'Computer'

if player1==player2:
  print("It's a tie!!")

elif (player1 == 'rock'):
  if (player2 == 'scissors'):
    print('Player 1 Win!')
  elif (player2 == 'paper'):
    print(f'{player2_name} Win!')

elif (player1 == 'scissors'):
  if (player2 == 'paper'):
    print('Player 1 Win!')
  elif (player2 == 'rock'):
    print(f'{player2_name} Win!')

elif (player1 == 'paper'):
  if (player2 == 'rock'):
    print('Player 1 Win!')
  elif (player2 == 'scissors'):
    print(f'{player2_name} Win!')

else:
  print('input error, sorry!')

print('\n*** Thank you for playing! ***\n')

