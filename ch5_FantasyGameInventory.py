# a script that prints out a characters in a fantasy games inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k,v in inv.items():
        item_total = item_total + int(v)
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)