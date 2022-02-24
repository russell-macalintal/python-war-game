import card             # Import card.py file
import deck             # Import deck.py file

class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        pass

    def add_cards(self, new_cards):
        pass

    def __str__(self):              # Default print method for Player object
        return f'Player {self.name} has {len(self.all_cards)} cards.'




# Test Player Class functionality
if __name__ == '__main__':
    new_player = Player('Quinn')
    print(new_player)