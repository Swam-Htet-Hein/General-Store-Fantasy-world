# for Player
def show_py_inventory(capacity, current_loot,loot):
    print(f"Loot Capacity : ({current_loot}/{capacity})items")
    index = 0
    for i in loot:
        # row 5 ခုပြည့်ရင် အောက်တစ်ကြောင်းဆင်းအောင်လုပ်ထားသည်။
        if index % 5 == 0 and index > 0:
            print()
        print(f"|{index}|:({i})", end=" ")
        index += 1
    print()

# For Store
def show_store_inventory(loot):
    index = 0
    for i in loot:
        if index % 5 == 0 and index > 0:
            print()
        print(f"|{index}|:({i} {loot[i]}$)", end=" ")
        index += 1
    print()