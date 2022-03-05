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

# Gameplay - continues while game_on == True
while game_on:
    round_num += 1
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


    at_war = True
    # Assume at_war condition (player_one_card == player_two_card) unless checked otherwise
    while at_war:
        # Check if Player One has higher card
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            break
        # Check if Player Two has higher card
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            break
        # Or else the players are at_war
        else:
            print('WAR! Each player adds 5 cards')

            # Checks whether or not each player has enough cards to proceed
            if len(player_one.all_cards) < 5:
                print('Player One does not have enough cards for war. Player Two Wins!!')
                game_on = False
                at_war = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two does not have enough cards for war. Player One Wins!!')
                game_on = False
                at_war = False
                break
            # If both players have enough cards, add them to their table piles
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

