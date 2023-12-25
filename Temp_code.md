add = 'apple'

for i in range(7):
    if len(Player_loot) < loot_capacity:
        Player_loot.append(add)
        print(f"{add} added")
    else:
        print("Storage capacity is full")

dct = {
    'apple' : 100,
    'orange' : 300,
    'banana' : 350
}
converted = list(dct)
# print(converted.index('banana'))

# dct_to_index = {i : converted[i] for i in range(len(dct))}

print(f"{converted[0]}")

money = 100
def test():
    global money
    money -= 10

test()
print(money)

import Show_consoles

shelf = ['carrot', 'apple', 'banana', 'orange', 'grapes', 'shoes', 'clothes', 'sword', 'musket', 'bow', 'arrow', 'armor']

Show_consoles.show_py_inventory(shelf)

# def test_1():
#     print("Hello 1")
# def test_2():
#     print("Hello 2")

# match input('Enter 1 or 2 : '):
#     case '1':
#         test_1()
#     case '2':
#         test_2()
#     case _:
#         print("Invalid input")

p_input = input('Enter: ')
p_choice = Listed_shelf[int(p_input)]
sell_percent = random.choice([0, 10, 20, 30, 50, 70, 80])
print(sell_percent)
sell_price = Shelf[p_choice] * ((100-sell_percent)/100)

print(f"I will give you {sell_price}$ for {p_choice}")

Player_loot.pop(int(p_input))
print(f"{p_choice} taken")