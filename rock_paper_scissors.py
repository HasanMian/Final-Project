import random

def roll_dice(num_dice):
  total = 0
  for in range(num_dice):
    total =+ random.randint(1, 6)
  return total

def number_of_rolls(player1_choice, player2_choice):
    if player1_choice == player2_choice
        return 1,1 # rolls dice
elif (player 1_choice == 'rock' and player2_choice == 'paper') or \
    (player1_choice == 'paper' and player2_choice == 'scissors') or \
    (player1_choice == 'scissors' and player2_choice == 'rock'):
    return 2, 1 # Player 1 rolls twice, Player 2 rolls once
else: 
    return 1, 2 # Player 1

