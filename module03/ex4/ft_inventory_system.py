import sys

DICTIONARY = ["sword", "potion", "shield", "armor", "helmet", "key", ]


def parse_args(argv):
    inventory = {}
    for arg in argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, quantity = arg.split(":", 1)

        if name not in DICTIONARY:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty_str = int(quantity)
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue

        inventory[name] = qty_str
    return inventory


def most_least_abundant(inventory):
    most_name = most_qty = None
    least_name = least_qty = None
    for name, qty in inventory.items():
        if most_qty is None or qty > most_qty:
            most_name, most_qty = name, qty
        if least_qty is None or qty < least_qty:
            least_name, least_qty = name, qty
    print(f"Item most abundant: {most_name} with quantity {most_qty}")
    print(f"Item least abundant: {least_name} with quantity {least_qty}")


def percentage_inv(inventory, total):
    for name, qty in inventory.items():
        percentage = round(qty / total * 100, 1)
        print(f"Item {name} represents {percentage}%")


def display_inv(inventory):
    inv_len = len(inventory)
    total = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {inv_len} items: {total}")
    percentage_inv(inventory, total)
    most_least_abundant(inventory)

    for item in DICTIONARY:
        if item not in inventory:
            inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = parse_args(sys.argv)
    display_inv(inventory)
