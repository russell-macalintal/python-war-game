import player
import deck

player_one = player.Player("One")
player_two = player.Player("Two")

new_deck = deck.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1:
    print(f'Round: {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player One Wins!')
        game_on = False
        break

    # Play the round
    # Initiate each player's pile on the table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


# Test game logic
if __name__ == '__main__':
    print(player_one)
    print(player_two)
    print(player_one.remove_one())
    print(player_two.remove_one())