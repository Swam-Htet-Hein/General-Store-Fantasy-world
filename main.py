from player_stats import *
from function_module import *

print("Welcome to General Store")

while True:
    print(f"Player : {Player_money[0]}$")
    print("1. Check Inventory")
    print("2. Buy")
    print("3. Sell")
    print("4. Talk")
    print("0. Exit")
    p_input = input('Player : ')
    # Check Inventory
    if p_input == '1':
        Check_inventory() # Done

    # Buy something
    elif p_input == '2':
        Buy() # Done

    # Sell something
    elif p_input == '3':
        Sell() # Done

    # Talk about something
    elif p_input == '4':
        Talk() # Done
        
    # Quit interacting
    elif p_input == '0':
        print("Have a good day!")
        break

    # Uncertainly response
    else:
        print("Sorry!, What?")