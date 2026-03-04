import random
import sys

#Names
player_1 = input("Enter the player-1 name: ").title()
player_2 = input("Enter the player-2 name: ").title()

player1_score,player2_score = 0,0 #Initial scores
winning_point = 100 #Total winning points

snakes = {16:8, 32:20, 43:4, 50:27, 73:32, 87:49, 98:6}
ladders = {7:24, 14:40, 25:89, 37:42, 57:76, 79:83}

def dice(): #For random number between 1-6
    return random.randint(1,6)


def player1_turn():  #Turn of player 1
    global player1_score   #To make loops compile out of the function
    player1_status = input(f"{player_1}, you want to [c]ontinue or [q]uit: ")
    if player1_status=='c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')
        player1_score += cur_dic

        if player1_score>=winning_point:  #To not repeat player 2 after winnning
            print(f'congrats {player_1}, you won the Game!!!')
            sys.exit()
            
        if player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f'Board position after snake bite: {player1_score}------')
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f'Board position after ladder: {player1_score}++++++++')
        else:
            print(f'Bord position: {player1_score}')
    else:
        print(f'congrats {player_2}, you won the Game!!!')


def player2_turn():  #Turn of player 2
    global player2_score
    player2_status = input(f"{player_2}, you want to [c]ontinue or [q]uit: ")
    if player2_status=='c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')
        player2_score += cur_dic
            
        if player2_score in snakes:
            player2_score = snakes[player2_score]
            print(f'Board position after snake bite: {player2_score}------')
        elif player2_score in ladders:
            player2_score = ladders[player2_score]
            print(f'Board position after ladder: {player2_score}++++++++')
        else:
            print(f'Bord position: {player2_score}')
    else:
        print(f'congrats {player_1}, you won the Game!!!')


while player1_score<winning_point and player2_score<winning_point:
    player1_turn()
    player2_turn()

if player1_score > player2_score:
    print(f'congrats {player_1}, you won the Game!!!')
else:
    print(f'congrats {player_2}, you won the Game!!!')
