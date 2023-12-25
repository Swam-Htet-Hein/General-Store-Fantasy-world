from player_stats import Player_loot, loot_capacity
from Buy_and_Sell import Buying, Selling, Bag_Buying
import Show_consoles
import talking_module as talk

# Function of Check inventory
def Check_inventory():
    print("In your Inventory : ")
    print("------------------------")
    Show_consoles.show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot)
    print("------------------------")

# Function of Buying
def Buy():
    # global Player_loot
    # global loot_capacity
    print("------------------------")
    match input("Do you want to buy (bag)(items)?: "):
        # bag buying
        case 'bag':
            print("OK wait...")
            Bag_Buying()
        # items buying
        case 'items':
                if len(Player_loot) < loot_capacity[0]:
                    Buying()
                else:
                    print("Storage capacity is full")
                    pass
        case _:
            print("OK...")
    print("------------------------")

# Function of Selling
def Sell():
    print("------------------------")
    if len(Player_loot) <= 0:
        print("You have nothing to sell")
    else:
        Selling()
    print("------------------------")

# Function of Talking
def Talk():
    print("------------------------")
    talk.talk_topic()
    print("------------------------")
    pass