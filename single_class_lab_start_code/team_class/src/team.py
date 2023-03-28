# Create a class called Team that has the properties properties name (str), players (list of strs) and a coach (str).
# Create an __init__ method that takes in a name (str), a list of player names (as strs) and a coach(str) to initialise the properties when a new team is created.
# Create a method add_player that takes in a string of a new players's name and adds that new player to the players list.
# Add a method has_player that takes in a string of a player's name and checks to see if they are in the players list. It should return True if the player's name is in the list and False otherwise.

class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0
        

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_to_find):
        for player in self.players:
            if player == player_to_find:
                return True
        return False

#   Alt method:
#     player_exists = False
#     for player in self.players:
#       if player == player_to_find:
#         player_exists = True
#     return player_exists

    def play_game(self, outcome):
        if outcome == True:
            self.points += 3
        else:
            self.points += 0
    
    