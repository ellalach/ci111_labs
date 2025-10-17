#define functions

def draw_boards(game_pieces):
    print("Tic-Tac_Toe")
    print("~~~~~~~~~~~")
    print("||1||2||3||")
    print("~~~~~~~~~~~")
    print("||4||5||6||")
    print("~~~~~~~~~~~")
    print("||7||8||9||")
    print("~~~~~~~~~~~")

    print()
    
    print("Tic-Tac_Toe")
    print("~~~~~~~~~~~")
    print(f"||{game_pieces[0]}||{game_pieces[1]}||{game_pieces[2]}||")
    print("~~~~~~~~~~~")
    print(f"||{game_pieces[3]}||{game_pieces[4]}||{game_pieces[5]}||")
    print("~~~~~~~~~~~")
    print(f"||{game_pieces[6]}||{game_pieces[7]}||{game_pieces[8]}||")
    print("~~~~~~~~~~~")


def get_player_move(piece, game_pieces):
    
    is_choosing=True
    while is_choosing:
        players_spot=int(input("Where would you like to place your piece? "))-1
        if players_spot>=0 and players_spot<9:
            if game_pieces[players_spot]=="_":
                game_pieces[players_spot]=piece
                is_choosing=False
            else:
                print("Sorry, that spot has already been chosen. Try again.")
        else:
            print("Sorry, that isn't a spot on the board. Try again.")
            
    
def determine_winner(piece, game_pieces):
    player_won=False
    if piece==game_pieces[0] and piece==game_pieces[1] and piece==game_pieces[2]:
        player_won=True
    elif piece==game_pieces[3] and piece==game_pieces[4] and piece==game_pieces[5]:
        player_won=True
    elif piece==game_pieces[6] and piece==game_pieces[7] and piece==game_pieces[8]:
        player_won=True    
    elif piece==game_pieces[0] and piece==game_pieces[3] and piece==game_pieces[6]:
        player_won=True    
    elif piece==game_pieces[1] and piece==game_pieces[4] and piece==game_pieces[7]:
        player_won=True    
    elif piece==game_pieces[2] and piece==game_pieces[5] and piece==game_pieces[8]:
        player_won=True    
    elif piece==game_pieces[0] and piece==game_pieces[4] and piece==game_pieces[8]:
        player_won=True    
    elif piece==game_pieces[2] and piece==game_pieces[4] and piece==game_pieces[6]:
        player_won=True    
    else:
        pass
        
    return player_won
        
#main code

player_1="X"
player_2="O"

current_game_pieces=['_','_','_','_','_','_','_','_','_']

#begin playing 
is_playing=True
while is_playing:
    
    draw_boards(current_game_pieces)
    
    #player 1 move
    print("Player 1, make your move")
    get_player_move(player_1, current_game_pieces)
    draw_boards(current_game_pieces)
    
    #player 1 win
    p1_win=determine_winner(player_1, current_game_pieces)
    if p1_win==True:
        draw_boards(current_game_pieces)
        print("Player 1 wins!!")
        is_playing=False
    
    #draw
    elif "_" not in current_game_pieces:
        draw_boards(current_game_pieces)
        print("Its a tie!")
        is_playing=False
    
    #player 2 move
    else:
        print("Player 2, make your move")
        get_player_move(player_2, current_game_pieces)
        p2_win=determine_winner(player_2, current_game_pieces)
        
        #player 2 win
        if p2_win==True:
            draw_boards(current_game_pieces)
            print("Player 2 wins!!")
            is_playing=False
