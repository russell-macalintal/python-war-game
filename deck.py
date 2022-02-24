import card                         # Import card.py file
import random                       # Import built-in Python random module

class Deck:
    
    def __init__(self):
        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                # Create the Card Object
                created_card = card.Card(suit, rank)
                # Add newly created Card Object to list
                self.all_cards.append(created_card)

    def shuffle(self):
        # random.shuffle destructively affects the passed in arg. It does not return a new "shuffled" list
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Returns the last card removed from the list
        return self.all_cards.pop()




# Test Deck Class functionality
if __name__ == '__main__':
    # Create new Deck Object
    new_deck = Deck()
    # Show the last Card Object created and included into the Deck
    top_card = new_deck.all_cards[-1]
    print(f'The top card is {top_card}')         # Ace of Clubs

    print('Shuffling...')
    new_deck.shuffle()
    top_card = new_deck.all_cards[-1]
    print(f'The top card is now {top_card}') 

    print('Dealing...')
    my_card = new_deck.deal_one()
    print(f'My card is {my_card}. The deck now has {len(new_deck.all_cards)} cards left')
