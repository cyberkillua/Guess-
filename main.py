import random

class Game: 

  def get_choice(self):
    player_choice = input( "Enter a choice Player 1 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10: ")
    player_two_choice = input("Enter a choice Player 2 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10: ")
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice, "second_player": player_two_choice}
    return choices

  def check_win(self, player, computer, second_player):
    print(f"you chose {player} and {second_player} chose, and computer chose {computer}")
    if player == computer and second_player == computer:
      return "You both tie!"
    elif player == computer: 
      return "Player 1 win!!"
    elif second_player == computer:
      return "Player 2 wins!!"
    else:
      return "No winner try again"

  def play(self):
    games_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("Home many games do you want to play? "))
      except:
        print("You must enter a number.")

    while games_number < games_to_play:
      games_number += 1
      print()
      print("*" * 30)
      print(f"Game {games_number} of {games_to_play}")
      print("*" * 30)
      choices = self.get_choice()  
      result = self.check_win(choices["player"], choices["computer"], choices["second_player"])
      print(result)

g = Game()
g.play()