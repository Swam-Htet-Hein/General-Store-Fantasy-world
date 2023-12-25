# from player_stats import *
# from Show_consoles import show_py_inventory

# # p_input = input('Enter (check)(box)(exit): ')

# match input('Enter (check)(box)(exit)'):
#     case 'check':
#         print(f"You have {Player_money[0]}$")
#     case 'box':
#         show_py_inventory(loot_capacity[0], len(Player_loot), Player_loot)
#     case 'exit':
#         pass
#     case _:
#         print('Invalid input')

match input("Do you want to buy (bag)(items)?: "):
    case 'bag':
        pass
    case 'items':
        pass
    case _:
        print("OK...")