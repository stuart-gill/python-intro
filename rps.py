# rock paper scissors

print('...rock...\n...paper...\n...scissors...\n')

print('Enter Player 1 Choice:')
player1 = input()

print('Enter Player 2 Choice:')
player2 = input()

if (player1 == 'rock'):
  if (player2 == 'scissors'):
    print('Player 1 Win!')
  elif (player2 == 'paper'):
    print('Player 2 Win!')
  else:
    print('Tie!!')

elif (player1 == 'scissors'):
  if (player2 == 'paper'):
    print('Player 1 Win!')
  elif (player2 == 'rock'):
    print('Player 2 Win!')
  else:
    print('Tie!!')

elif (player1 == 'paper'):
  if (player2 == 'rock'):
    print('Player 1 Win!')
  elif (player2 == 'scissors'):
    print('Player 2 Win!')
  else:
    print('Tie!!')

else:
  print('input error, sorry!')

