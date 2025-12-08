import random

player_positions = [0, 0]  
current_player = 0  

winning_position = 100
dice_roll_count = 0

get_pos = {
    0: "No Play",
    1: "Ladder", 
    2: "Snake"
}

def roll_die():
    return random.randint(1, 6)

def check_option():
    return random.randint(0, 2)

def get_option_name(option):
    return get_pos.get(option, "Not valid")

def move_player(die_value, option, player_index):
    global player_positions
    
    if option == 0:  # No Play
        pass  
    elif option == 1:  # Ladder
        new_position = player_positions[player_index] + die_value
        if new_position <= winning_position:
            player_positions[player_index] = new_position
    else:  # Snake (option == 2)
        new_position = player_positions[player_index] - die_value
        if new_position < 0:
            player_positions[player_index] = 0
        else:
            player_positions[player_index] = new_position

def play_turn():
    global dice_roll_count, current_player

    die_value = roll_die()
    dice_roll_count += 1
    
    option = check_option()
    option_name = get_option_name(option)

    old_position = player_positions[current_player]

    move_player(die_value, option, current_player)
    
    player_name = f"Player {current_player + 1}"
    print(f"Turn {dice_roll_count} - {player_name}: Die = {die_value}, Option = {option_name}")
    print(f"Position: {old_position} → {player_positions[current_player]}")
    
    if option == 0:
        print("   No movement")
    elif option == 1:
        if player_positions[current_player] > old_position:
            print(f"   Ladder! Moved up by {die_value}")
        else:
            print("   Ladder blocked (would exceed 100)")
    else:
        if player_positions[current_player] == 0 and old_position > 0:
            print("   Snake! Fell below 0, back to start")
        else:
            print(f"   Snake! Moved down by {die_value}")
    
    print(f"Current positions - Player 1: {player_positions[0]}, Player 2: {player_positions[1]}")
    print()
    
    # Check if current player won
    if player_positions[current_player] == winning_position:
        return True  # Game won
    
    # Switch to next player
    current_player = 1 - current_player
    return False  # Game continues




def play_game():
    global player_positions, dice_roll_count, current_player
    
    # Reset game state
    player_positions = [0, 0]  
    current_player = 0
    dice_roll_count = 0
    
    print(" SNAKE AND LADDER GAME - 2 PLAYERS ")
    print(f"Goal: First player to reach position {winning_position} wins!")
    print(f"Starting positions - Player 1: {player_positions[0]}, Player 2: {player_positions[1]}")
    print("-" * 50)
    
    game_won = False
    while not game_won:
        game_won = play_turn()
        
        # input("Press Enter for next turn...")
    
    winner = current_player + 1
   
    print(f" PLAYER {winner} WINS! ")
  
    print(f"Final positions - Player 1: {player_positions[0]}, Player 2: {player_positions[1]}")
    print(f"Total dice rolls: {dice_roll_count}")

if __name__ == "__main__":
    play_game()