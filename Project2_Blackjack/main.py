from array_funcs import *
from card import *

Suits = ["Club", "Diamond", "Heart", "Spades"] 
Ranks = ["ace", "two", "three", "four", "five", "six", "seven",
                            "eight", "nine", "ten", "King", "Jack", "Queen"]

player_hand = [] 
dealer_hand = [] 
dealer_win_flag = False  #true for win, helps to exit main while loop while dealer wins on a hit
player_sum = 0 #stores the current sum of player hand
dealer_sum = 0 #stores the current sum of dealer hand

bet_amount = 0           #stores the bet amount of chips
winner_flag = False     #if player wins false else true

player_chip = chips(1000)  #class which holds chips for player
dealer_chip = chips(1000)  #class which holds chips for dealer

Deck = []

#Below code is deck creation
for suit in Suits:
    j = 0
    for rank in Ranks:
        Deck.append(Cards())
        Deck[-1].set_name(rank)
        Deck[-1].set_suit(suit)
        Deck[-1].set_rank(j+1)
        j+=1

#initialising player hand with 2 cards

add_to_hand(Deck, player_hand)
#player_hand[0].get_name_of_card()
add_to_hand(Deck, player_hand)


#initialising dealer hand with 2 cards
add_to_hand(Deck, dealer_hand)
add_to_hand(Deck, dealer_hand)


player_sum = sum_of_cards(player_hand) #gives the sum of cards inside a hand
dealer_sum = sum_of_cards(dealer_hand)


print("Welcome to Blackjack\n")       
bet_amount = int(input("Enter number of chips to bet\n"))  #inputing the bet amount

#printing card values
print_player_cards(player_hand, player_sum)  #printing player hand

#dealer hand with hidden card
print("Dealer card 1")
dealer_hand[0].get_name_of_card()   #dealer hand        
print("Dealer card 2")                        
print("Hidden card\n")


while(not dealer_win_flag):
    if(player_sum<21): 
        choice = input("Would you like to hit or stay, h for hit and s for stay\n")              
        if(choice == 'h'):
            add_to_hand(Deck, player_hand)   #hitting player
            player_sum = sum_of_cards(player_hand)
            print_player_cards(player_hand, player_sum)  #printing player hand                    
            print("Dealer card 1")
            dealer_hand[0].get_name_of_card()   #dealer hand                    
            print("Dealer card 2")                   
            print("Hidden card")
            continue
        
        else:                    
            print("Now dealer hits")
            if(dealer_sum>player_sum):  #this code works when player directly stay wit 0 hits
                print_player_cards(player_hand, player_sum)
                print_dealer_cards(dealer_hand, dealer_sum)                      
                print("Dealer wins")
                winner_flag = True  #to give chips to dealer
                break
            
            while(True):
                add_to_hand(Deck, dealer_hand)
                dealer_sum = sum_of_cards(dealer_hand)
                
                if(dealer_sum>21):                            
                    print_player_cards(player_hand, player_sum)
                    print_dealer_cards(dealer_hand, dealer_sum)                            
                    print("Dealer bust Player wins\n")
                    dealer_win_flag = True #to exit main while loop
                    break
                
                elif(dealer_sum>player_sum):                            
                    print_player_cards(player_hand, player_sum)
                    print_dealer_cards(dealer_hand, dealer_sum)                            
                    print("Dealer wins\n")
                    dealer_win_flag = True #to exit main while loop
                    winner_flag = True  #to give chips to dealer
                    break
                
    
    else:
        print_player_cards(player_hand, player_sum)
        print_dealer_cards(dealer_hand, dealer_sum)                           
        print("Player bust Dealer wins\n")
        winner_flag = True  #to give chips to dealer
        break
    
    

if(not winner_flag):
    player_chip.set_change_chip_value(bet_amount)
    print(f"Player chips = {player_chip.get_chip_value()}")            
    dealer_chip.set_change_chip_value(-bet_amount)
    print(f"Dealer chips = {dealer_chip.get_chip_value()}")            

else:
    player_chip.set_change_chip_value(-bet_amount)
    print(f"Player chips = {player_chip.get_chip_value()}")
    dealer_chip.set_change_chip_value(bet_amount)
    print(f"Dealer chips = {dealer_chip.get_chip_value()}")   
    
print("end")
