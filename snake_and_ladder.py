import random

player_position = 0
winning_position = 100
WINNING_POSITION = 100
dice_roll_count = 0

get_pos ={
    0:"No Play",
    1:"snake",
    2:"Ladder"
}

def roll_die():
   
    return random.randint(1, 20)

def check_option():
    
    return random.randint(0, 2)

def get_option_name(option):
    return get_pos.get(option,"Not valid")
 
    # if option == 0:
    #     return "No Play"
    # elif option == 1:
    #     return "Ladder"
    # else:
    #     return "Snake"

def move_player(die_value, option):
   
    global player_position
    
    if option == 0:  
        pass  
    elif option == 1:  
        new_position = player_position + die_value
        if new_position <= winning_position:
            player_position = new_position
    else:  
        new_position = player_position - die_value
        if new_position < 0:
            player_position = 0
        else:
            player_position = new_position

def play_turn():
   
    global dice_roll_count

    die_value = roll_die()
    dice_roll_count += 1
   
    option = check_option()
    option_name = get_option_name(option)

    old_position = player_position

    move_player(die_value, option)
  
    print(f"Turn {dice_roll_count}: Die = {die_value}, Option = {option_name}")
    print(f"Position: {old_position} → {player_position}")
    
    if option == 0:
        print("   No movement")
    elif option == 1:
        if player_position > old_position:
            print(f"   Ladder! Moved up by {die_value}")
        else:
            print("   Ladder blocked (would exceed 100)")
    else:
        if player_position == 0 and old_position > 0:
            print("   Snake! Fell below 0, back to start")
        else:
            print(f"   Snake! Moved down by {die_value}")
    
    print()

def play_game():
    
    global player_position, dice_roll_count
  
    print(f"Goal: Reach position {winning_position}")
    print(f"Starting at position {player_position}")
   
    
   
    while player_position != winning_position:
        play_turn()
        # input("Press Enter for next turn...")
    

    print("🎉 YOU WON! 🎉")
    print(f"Total dice rolls: {dice_roll_count}")

if __name__ == "__main__":
    play_game()