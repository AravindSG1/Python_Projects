print("start\n")

"""this function prints the board"""
def board(k):
    print(k[7] + " | " + k[8] + " | " + k[9])
    print("----------")
    print(k[4] + " | " + k[5] + " | " + k[6])
    print("----------")
    print(k[1] + " | " + k[2] + " | " + k[3])

"""winner logic finds the winner"""
def winner_check(k, current_player_token, player_name):
    a = False
    if(((k[1]==k[2] and k[2]==k[3]) and (k[1]!=' ')) or ((k[4]==k[5] and k[5]==k[6]) and (k[4]!=' ')) or
       ((k[7]==k[8] and k[8]==k[9]) and (k[7]!=' ')) or ((k[1]==k[4] and k[4]==k[7]) and (k[1]!=' ')) or
       ((k[2]==k[5] and k[5]==k[8]) and (k[2]!=' ')) or ((k[3]==k[6] and k[6]==k[9]) and (k[3]!=' ')) or
       ((k[1]==k[5] and k[5]==k[9]) and (k[1]!=' ')) or ((k[3]==k[5] and k[5]==k[7]) and (k[5]!=' '))):

        #std::cout<<player_name<<" played with "<<current_player_token<<" is the winner"<<std::endl;
        
        a = True
       
    return a

"""First find out which key is pressed and then stores the token x or o of the corresponding
player to board positions matching with the key positions"""
def input_to_board(input_1, current_player_token, k):
    input_1 = int(input("\n"))  #casting to integer from string
    if input_1 == 1:
        k[1] = current_player_token
    
    elif input_1 == 2:
        k[2] = current_player_token
    
    elif input_1 == 3:
        k[3] = current_player_token

    elif input_1 == 4:
        k[4] = current_player_token

    elif input_1 == 5:
        k[5] = current_player_token

    elif input_1 == 6:
        k[6] = current_player_token

    elif input_1 == 7:
        k[7] = current_player_token

    elif input_1 == 8:
        k[8] = current_player_token

    elif input_1 == 9:
        k[9] = current_player_token


k = ['s']*10 #holds the characters for keys
#keys = [1,2,3,4,5,6,7,8,9,0]
player_side = None #to store player1 choice x or o
player_1 = None
player_2 = None
input_1 = None      #user input value given to the board throug keys 1-9
current_player_token = None #stores current player's token x or o
option = None 

"""winner_check(keys,'x',"player 1")
print(winner_check(keys,'x',"player 1"))
input_to_board(input_1, 'o', keys)
keys[5] = 'd'
print(keys)"""

"""The program starts from here"""
print("Welcome to Tic-Tac-Toe")
    
while(True):
    #this is for clearing the board also initialising with value ' '
    k = [' ']*10
   
    player_side=input("Player 1 please select your side, x or o\n") #receiving the side
    player_1 = player_side;  #assigning sides
    if(player_side == 'x' or player_side == 'o'):        #if(player_side == ('x'||'o')) not working why
        if(player_1 == 'x'):
            player_2 = 'o'
        
        else:
            player_2 = 'x'
        
        print(f"Player 1 is {player_1} and Player 2 is {player_2}")
            
    else:
        print("Choose correct character")
        continue #go back and enter correct character
    

    player_flag = False 
    """To switch between player1 and player2, value 0 for player1 and value 1 for
    player2. After each time a player is played flag value will be switched"""
    while(True):
        winner_flag = False   
        """Stores the value returned by winner_check function, value 0 for no 
        results and value 1 for win"""
        if(not player_flag):
            current_player_token = player_1
            print(f"Player 1 enter input {current_player_token}")
            input_to_board(input_1, current_player_token, k)
            board(k)
            winner_flag = winner_check(k, current_player_token, "Player1")
            
            if(winner_flag):
                """This piece of code decides to continue game or not after winning"""              
                option = input("Would you like to continue, press y to continue and n to end\n")
                if(option == 'y'):
                    break
                
                else:
                    quit() #return 0
                
            player_flag = True
        
        else:
            current_player_token = player_2
            print(f"Player 2 enter input {current_player_token}")
            input_to_board(input_1, current_player_token, k)
            board(k)
            winner_flag = winner_check(k, current_player_token, "Player2")
            if(winner_flag):
                """This piece of code decides to continue game or not"""                
                option = input("Would you like to continue, press y to continue and n to end\n")
                if(option == 'y'):
                    break
                
                else:
                    quit() #return 0
                
            
            player_flag = False


        """Below statements check if the board is full, if all the positions are not ' '
        then it will be draw condition"""
        if(k[1]!= ' ' and k[1]!= ' ' and k[2]!= ' ' and k[3]!= ' ' and k[4]!= ' ' and k[5]!= ' ' and
            k[6]!= ' ' and k[7]!= ' ' and k[8]!= ' ' and k[9]!= ' '): 
            print("Well, its a draw")

            """This piece of code decides to continue game or not"""               
            option = input("Would you like to continue, press y to continue and n to end\n")
            if(option == 'y'):
                break
            
            else:
                quit() #return 0
            
            
        
        
         

    
  

#return 0;

print("\nend")