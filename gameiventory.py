import collections

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

 
def display_inventory(inventory):
    longest_key_dictionary = 0
    for item in inventory:
        if longest_key_dictionary < len(item):
            longest_key_dictionary = len(item)

    longest_value_dictionary = max([i for i in inventory.values()]) 
    longest_value_dictionary = len(str(longest_value_dictionary))

    counter_line = 0

    if longest_key_dictionary > 13:
        for i in range(13, longest_key_dictionary):
            counter_line += 1
    

    print("Invetory:" )
    print("{:6} {:>13}".format("count", "item name"))
    print(20 * "-", counter_line * "-", sep = "")

    total = 0
    for item in inventory:
        print("{:6} {:>13}".format(inventory[item], item))
        total = total + inventory[item]
    print(20 * "-", counter_line * "-", sep = "")

    print("Total number of items: {}\n".format(total))
    
def add_to_inventory(inventory,added_items):

    for add_item in added_items:
        if add_item not in inventory:
            dic = {add_item : 0}
            inventory.update(dic)

    for item in inventory:
        for add_item in added_items:
            if item == add_item:
                inventory[item] +=1

    display_inventory(inventory)

def print_table(inventory,order):

    if order == "count,asc":
        od = collections.OrderedDict(sorted(inventory.items(), key = lambda t: t[1], reverse = False))
        display_inventory(od)

    elif order == "count,desc":
        od = collections.OrderedDict(sorted(inventory.items(), key = lambda t: t[1], reverse = True))
        display_inventory(od)

def main():
    display_inventory(inventory)
    add_to_inventory(inventory,dragon_loot)
    print_table(inventory,"count,asc")
    print_table(inventory,"count,desc")

if __name__ == '__main__':
    main()