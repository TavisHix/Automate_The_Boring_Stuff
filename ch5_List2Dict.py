# displaying an inventory of items while adding a list of items to the inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + int(v)
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
