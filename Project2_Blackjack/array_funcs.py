import random

"""Adds a new card to the hand"""
def add_to_hand(Deck, hand):
    random.shuffle(Deck)
    hand.append(Deck.pop())
    

"""Gives the sum of values of all cards inside a hand"""
def sum_of_cards(hand):
    sum = 0
    for card in hand:
        sum += card.get_value()

        if(sum<21 and card.name == "ace"): #ace default value is 1, so first adding 10 to get value 11
            sum+=10                               
        
        if(sum>21 and card.name == "ace"): #now checking if the value is not over 21 with 11 value
            sum-=10;                         #if its above 21 changing to value 1
        
    return sum


"""Prints all cards inside player hand"""
def print_player_cards(player_hand, player_sum):
    print("\n")
    i = 1
    for card in player_hand:
        print(f"Player card {i}")
        card.get_name_of_card()
        i+=1

    print(f"Player card sum = {player_sum}\n")

"""Prints all cards inside dealer hand"""
def print_dealer_cards(dealer_hand, dealer_sum):
    print("\n")
    i = 1
    for card in dealer_hand:
        print(f"Dealer card {i}")
        card.get_name_of_card()
        i+=1

    print(f"Dealer card sum = {dealer_sum}\n")