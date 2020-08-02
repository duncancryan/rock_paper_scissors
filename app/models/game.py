from app.models.player import Player

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def determine_winner(self):
        if self.player_1.choice == self.player_2.choice:
            return None
        
    # logic needed which accesses player choice and determines winner, can I write game logic elsewhere???
