import random

def roll_dice(num_dice):
  total = 0
  for _ in range(num_dice):
    total =+ random.randint(1, 6)
  return total

def number_of_rolls(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 1,1 # rolls dice
    elif  (player1_choice == 'rock' and player2_choice == 'paper') or \
          (player1_choice == 'paper' and player2_choice == 'scissors') or \
          (player1_choice == 'scissors' and player2_choice == 'rock'):
        return 2, 1 # Player 1 rolls twice, Player 2 rolls once
    else: 
        return 1, 2 # Player 1

def get_choice(player):
    choice = ''
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input(f"{player}, pick your choice (rock, paper, or scissors): ").lower() # Each Player can select there choice of either rock, paper, or scissors
    return choice

def play_round():
    print("\nNew Round: ")
    player1_choice = get_choice('Player 1') 
    player2_choice = get_choice('Player 2')

    print(f" Player 1 chose {player1_choice}") 
    print(f" Player 2 chose {player2_choice}")

    player1_dice, player2_dice = number_of_rolls(player1_choice, player2_choice) 

    player1_roll = roll_dice(player1_dice)
    player2_roll = roll_dice(player2_dice)

    print(f" Player 1 rolls {player1_dice} dice and gets a score of {player1_roll}") 
    print(f" Player 2 rolls {player2_dice} dice and gets a score of {player2_roll}")

    if player1_roll > player2_roll:
        print("Player 1 wins this round!") # If player ones roll is higher than player two, player one wins
        return 1, 0
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!") # If player two rolls a higher number than he wins
        return 0, 1
    else:
        print("This round ended with a tie!")
        return 0, 0 

def play_game(): 
    print("Welcome to the new way to play Rock, Paper, Scissors!")
    games = int(input("Enter the number of rounds to play: "))

    player1_score = 0
    player2_score = 0

    for _ in range(games):
        player1, player2 = play_round()
        player1_score += player1
        player2_score += player2
        print (f"Scores: Player 1: {player1_score}, Player 2: {player2_score}") # This outputs but players score

    if player1_score > player2_score:
        print("Player 1 wins the game!") # If player ones score is higher than they win the game
    elif player2_score > player1_score:
        print("Player 2 wins the game!") # If player two's score is higher than they win the game
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    play_game()
    
