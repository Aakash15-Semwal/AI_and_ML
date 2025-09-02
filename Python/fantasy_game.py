stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))

def add_to_inventory(inv, loot):
    for i in loot:
        if i in inv.keys():
            inv[i] = inv[i] + 1
        else:
            inv.setdefault(i, 1)
    return inv

print("Before defeating the Dragon : ")
display_inventory(stuff)

stuff = add_to_inventory(stuff, dragon_loot)

print("After defeating the Dragon : ")
display_inventory(stuff)
