import random
players = {
    "player1":0,
    
}

report={

}

current_player = "player1"

count = 0
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
    count += 1
    input("")
    dice_val = random.randint(1,6)
    print(dice_val)

    option = random.randint(0,2)
 
   
    if option == 0:
        print(f"its {option_name[0]} ")

        report[count] =f"Position:  {players[current_player]}-->{players[current_player]}"


    elif option == 1:
        print(f"its {option_name[1]} ")
        if players[current_player] + dice_val > 100:
            pass
        else:
            previous_posiction = players[current_player]
            players[current_player] += dice_val
            report[count] = f"Position:  {previous_posiction}-->{players[current_player]}"



            # checking the win
        if players[current_player] ==100:
            print("\n------Report---------\n")
            for key,value in report.items():
                print(f"{key}:   {value}")
            win =True

    else:
         print(f"its {option_name[2]} ")
         if players[current_player] - dice_val <= 0:
             previous_posiction = players[current_player]
             players[current_player] = 0
             report[count] = f"Position:{previous_posiction}-->{players[current_player]}"
         
         
     

    print(f"\n player postion {current_player}: {players[current_player]} :at {count}")     
                     
          
        




