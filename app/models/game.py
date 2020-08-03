from app.models.player import Player
import random

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def determine_winner(self):
        if self.player_1.choice == self.player_2.choice:
            return None
        elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1
        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1
        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1        
        else:
            return self.player_2
        
def generate_ai():
    choices = ["rock", "paper", "scissors"]
    ai_choice = choices[random.randint(0, 2)]
    ai = Player("Computer", ai_choice)
    return ai

    # logic needed which accesses player choice and determines winner, can I write game logic elsewhere???
