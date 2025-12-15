import random
players = {
    "player1":0,
    
}

current_player = "player1"
# Starting = 0

win = False

option_name = {
    0:"No play",
    1:"Ladder",
    2:"Snake"
}

while not win:
    print("\n")
    print("Hit Enter to role the dice:")
    input("")
    dice_val = random.randint(1,6)
    print(dice_val)

    option = random.randint(0,2)
 
   
    if option == 0:
        print(f"its {option_name[0]} ")
    elif option == 1:
        print(f"its {option_name[1]} ")
        if players[current_player] + dice_val > 100:
            pass
        else:
            players[current_player] += dice_val

            # checking the win
        if players[current_player] ==100:
            win =True
    else:
         print(f"its {option_name[2]} ")
         if players[current_player] - dice_val <= 0:
             players[current_player] = 0
         
         
     

    print(f"player posction {current_player}: {players[current_player]}")     
                     
          
        




