from player_stats import *
from Storage_room import *
import Show_consoles
import random

# Shelf(dict) ကနေ Listed_shelf(list) ပြောင်းလိုက်ခြင်းသည် player က buy or sell လုပ်တဲ့အခါမှာ index number ကိုသုံးပြီး process လုပ်နိုင်အောင် ဖြစ်သည်။
Listed_shelf = list(Shelf)
# [Items, Items, ....] <-- items
# [    0,     1, ....] <-- index

Bag_shelf = [5, 10, 15, 25] # capacity values
Bag_prices = [20, 50, 80, 120] # bag prices

def Buying():
    # ###################
    # global Player_money
    # ###################

    # This is General Store
    print("We have : ")
    # Showing items in the Shelf
    Show_consoles.show_store_inventory(Shelf)

    # Player side
    while True:
        # if the inventory is full exit the loop
        if len(Player_loot) < loot_capacity[0]:
            p_input = input('Enter (check)(box)(show)(exit): ') # Making decision

            if p_input == 'exit': # Exit from the Buying Function
                break
            elif p_input == "check": # Check the money
                print(f"I have {Player_money[0]}$")
            elif p_input == "show":
                # Showing items in the Shelf
                Show_consoles.show_store_inventory(Shelf)
            elif p_input == "box": # check player inventory 
                Show_consoles.show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot)
            else: # Buying Somethings and Making Processing
                p_choice = Listed_shelf[int(p_input)] # Assign items names from index numbers
                price = Shelf[p_choice] # Assign item's values from Shelf(dict) using p_choice key
                
                print(f"{p_choice} is {price}$")
                if Player_money[0] < price: # if money doesn't enough
                    print(f"You only have {Player_money[0]}$. This is {price}$. Not Enough Money!")
                else:
                    print("Do you want to buy it?") # confirm the process
                    p_input = input("Enter (no): ")
                    if p_input == 'no':
                        print("OK!")
                        continue
                    else:
                        Player_loot.append(p_choice) # add items into your inventory
                        print(f"{p_choice} added")
                        Player_money[0] -= price # withdraw money from your pocket
        else:
            print("Storage capacity is full")
            break

def Selling():
    while True:
        # if player doesn't have anything in the inventory 
        # auto escape from the selling()
        if len(Player_loot) <= 0:
            print("You have nothing to sell")
            break
        print("Inventory: ")
        Show_consoles.show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot)

        # p_input = input('Enter (check)(box)(exit): ')
        p_input = input('Enter (check)(box)(exit): ')
        if p_input == 'check':
            print(f"I have {Player_money[0]}$") # check player money
        elif p_input == 'box':
            Show_consoles.show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot) # check player inventory
        elif p_input == 'exit':
            break
        else:
            p_index = int(p_input) # inventory index
            p_choice = Player_loot[int(p_input)] # inventory item name
            if p_choice not in Shelf:
                print(f"Sorry, we do not buy your item ({p_choice})")
            else:
                # Sell percent ပြန်ရောင်းတဲ့အခါ ဆိုင်ရှင်က စျေးနှိမ်ယူတဲ့ percent ပါ။
                # ဆိုင်ရှင်ရဲ့ sell percent က ပုံသေမဟုတ်ပါဘူး။ ကံကောင်းရင် ဝယ်စျေးအတိုင်းပြန်ရတယ်။
                sell_percent = random.choice([0, 10, 20, 30, 50])
                sell_price = Shelf[p_choice] * ((100-sell_percent)/100) # calculating sell price

                print(f"I will give you {sell_price}$ for {p_choice}") # dealing price from seller
                p_input = input('Enter (no): ') # taking comfirm
                if p_input == 'no':
                    print("Ok, next time sell percent might be changed!")
                    continue
                else:
                    Player_loot.pop(int(p_index)) # take items from inventory
                    print(f"{p_choice} taken")
                    Player_money[0] += sell_price # add money to your pocket

def Bag_Buying():
    print('We have : ')
    print('[0]:small(20$) (5)capacity')
    print('[1]:medium(50$) (10)capacity')
    print('[2]:large(80$) (15)capacity')
    print('[3]:extra-large(120$) (25)capacity')
    while True:
        match input("Enter (buyone)(check)(box)(exit): "):
            case 'check': # check player money
                print(f"I have {Player_money[0]}$")
            case 'box': # check player inventory
                Show_consoles.show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot)
            case 'buyone': # buy bag
                print("Ok, which one?: ")
                p_input = input('Enter: ')
                # if ကိုယ်ဝယ်မဲ့ အိတ်က ကိုယ့်ရှိတဲ့ အိတ်နဲ့ တူရင် ဒါ True
                if Bag_shelf[int(p_input)] == loot_capacity[0]:
                    print("You already have one!")
                    continue
                # if ကိုယ်ဝယ်မဲ့ အိတ်က ကိုယ့်ရှိတဲ့ အိတ်ထက် ပမာဏ သေးရင် ဒါ True
                elif loot_capacity[0] > Bag_shelf[int(p_input)]:
                    print("You are buying smaller one than yours!")
                    continue
                # Buying bag successful
                else:
                    if Player_money[0] < Bag_prices[int(p_input)]:
                        print("You don't have enough money to buy this bag!")
                    else:
                        match input("Do you want to buy it (no): "):
                            case 'no':
                                print("Ok!")
                                continue
                            case _:
                                loot_capacity[0] = Bag_shelf[int(p_input)]
                                print("Inventory updated")
                                Player_money[0] -= Bag_prices[int(p_input)]
                                print("Transition success!")
            case 'exit':
                break
            case _:
                print("Invalid input")