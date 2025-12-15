import random
players = {
        0:0,
        1:0
    
}
count={
    0:0,
    1:0
}
report_player1={
}

report_player2={

}

players_report ={
    0:report_player1,
    1:report_player2
}





current_player = 0


# Starting = 0

win = False

option_name = {
    0:"No play",
    1:"Ladder",
    2:"Snake"
}

while not win:
    print("\n")
    print(f"Player {current_player} plz Hit Enter to role the dice:")
    count[current_player] += 1
    input("")
    dice_val = random.randint(1,6)
    print(f"dice val:{dice_val}")

    option = random.randint(0,2)
 
   
    if option == 0:
        print(f"its {option_name[0]} ")

        players_report[current_player][count[current_player]] =f"Position:  {players[current_player]}-->{players[current_player]}"
        print(f"\n player postion of palyer-{current_player}: {players[current_player]} :at count {count[current_player]}")  
        current_player = 1 - current_player


    elif option == 1:
        print(f"its {option_name[1]} ")
        if players[current_player] + dice_val <= 100:
            previous_posiction = players[current_player]
            players[current_player] += dice_val
            players_report[current_player][count[current_player]] = f"Position:  {previous_posiction}-->{players[current_player]}"
            print(f"\n player postion of palyer-{current_player}: {players[current_player]} :at count {count[current_player]}")  
           

            # checking the win
        if players[current_player] == 100:
            print(f"\n------Report---------\n for player {current_player }")
            for key,value in players_report[current_player].items():
                print(f"{key}:   {value}")
            win =True
        current_player = 1 - current_player

    else:
         print(f"its {option_name[2]} ")
         if players[current_player] - dice_val <= 0:
             previous_posiction = players[current_player]
             players[current_player] = 0
             players_report[current_player][count[current_player]] = f"Position:  {previous_posiction}-->{players[current_player]}"
             print(f"\n player postion of palyer-{current_player}: {players[current_player]} :at count {count[current_player]}")  
             current_player = 1 - current_player
         else:
             
             previous_posiction = players[current_player]
             players[current_player] -= dice_val
           
             players_report[current_player][count[current_player]] = f"Position:  {previous_posiction}-->{players[current_player]}"
             print(f"\n player postion of palyer-{current_player}: {players[current_player]} :at count {count[current_player]}")  
             current_player = 1 - current_player

         
         
     

      
                     
          
        




