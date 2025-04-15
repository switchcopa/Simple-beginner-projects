
crafting_grid = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

def reset_crafting_grid():
    return [[None for _ in range(3)] for _ in range(3)]

def display_grid():
    print("\nCrafting Grid ")
    for row in crafting_grid:
        display_row = []
        for cell in row:
            if cell is not None:
                display_row.append(cell.center(15))
            else:
                display_row.append(" ".center(15))
        print("|" + "|".join(display_row) + "|")

class Item:
    def __init__(self, item_name : str):
        self.__item_name = item_name

ITEMS = {
    "stick": Item("Stick"),
    "wooden_plank": Item("Wooden Plank"),
    "iron_ingot": Item("Iron Ingot"),
    "diamond": Item("Diamond"),

    "wooden_pickaxe": Item("Wooden Pickaxe"),
    "wooden_sword": Item("Wooden Sword"),
    "iron_pickaxe": Item("Iron Pickaxe"),
    "diamond_sword": Item("Diamond Sword"),
    "iron_axe": Item("Iron Axe"),
    "diamond_axe": Item("Diamond Axe"),
    "iron_helmet": Item("Iron Helmet"),
    "iron_chestplate": Item("Iron Chestplate"),
    "diamond_leggings": Item("Diamond Leggings"),
    "shield": Item("Shield")
}

CRAFTING_GRID_RECIPES = [
    {
        "result": "wooden_pickaxe",
        "pattern": [
            ["wooden_plank", "wooden_plank", "wooden_plank"],
            [None,           "stick",        None],
            [None,           "stick",        None]
        ]
    },
    {
        "result": "wooden_sword",
        "pattern": [
            [None, "wooden_plank", None],
            [None, "wooden_plank", None],
            [None, "stick",        None]
        ]
    },
    {
        "result": "iron_pickaxe",
        "pattern": [
            ["iron_ingot", "iron_ingot", "iron_ingot"],
            [None,         "stick",      None],
            [None,         "stick",      None]
        ]
    },
    {
        "result": "diamond_pickaxe",
        "pattern": [
            ["diamond", "diamond", "diamond"],
            [None,      "stick",   None],
            [None,      "stick",   None]
        ]
    },
    {
        "result": "diamond_sword",
        "pattern": [
            [None,    "diamond", None],
            [None,    "diamond", None],
            [None,    "stick",   None]
        ]
    },
    {
        "result": "iron_axe",
        "pattern": [
            ["iron_ingot", "iron_ingot", None],
            ["iron_ingot", "stick",      None],
            [None,         "stick",      None]
        ]
    },
    {
        "result": "diamond_axe",
        "pattern": [
            ["diamond", "diamond", None],
            ["diamond", "stick",   None],
            [None,      "stick",   None]
        ]
    },
    {
        "result": "iron_helmet",
        "pattern": [
            ["iron_ingot", "iron_ingot", "iron_ingot"],
            ["iron_ingot", None,         "iron_ingot"],
            [None,         None,         None]
        ]
    },
    {
        "result": "iron_chestplate",
        "pattern": [
            ["iron_ingot", None,         "iron_ingot"],
            ["iron_ingot", "iron_ingot",  "iron_ingot"],
            ["iron_ingot", "iron_ingot",  "iron_ingot"]
        ]
    },
    {
        "result": "diamond_leggings",
        "pattern": [
            ["diamond", "diamond", "diamond"],
            ["diamond", None,      "diamond"],
            ["diamond", None,      "diamond"]
        ]
    },
    {
        "result": "shield",
        "pattern": [
            ["wooden_plank", "iron_ingot", "wooden_plank"],
            ["wooden_plank", "wooden_plank", "wooden_plank"],
            [None,           "wooden_plank", None]
        ]
    },
    {
        "result": "stick",
        "pattern": [
            [None, "wooden_plank", None],
            [None, "wooden_plank", None],
            [None, None,           None]
        ]
    }
]



class Player:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class Inventory(Player):
    def __init__(self, name):
        super().__init__(name)
        self.__inventory = {}

    def display_inventory(self):
        return self.__inventory

    def add_inventory(self, item_name, quantity=1):
        item_qtt = self.__inventory.get(item_name, 0)
        if not item_name in ITEMS:
            print("item not found")
        elif quantity <= 0:
            print("quantity cannot have such value")
        elif quantity > 1000000:
            print("quantity too high")
        else:
            item_qtt += quantity
            self.__inventory.update({item_name : item_qtt})
            print(f"Added {item_qtt} {item_name} to your inventory")

    def clear_inventory(self):
        self.__inventory = {}

    def remove_inventory(self, item_name, quantity=1):
        item_qtt = self.__inventory.get(item_name, 0)
        if item_qtt == 0:
            return f"{item_name} not in inventory"
        elif item_qtt < quantity:
            return "quantity too high"
        item_qtt -= quantity
        self.__inventory[item_name] = item_qtt
        if item_qtt <= 0:
            self.__inventory.pop(item_name, None)

    def craft_from_grid(self):
        global crafting_grid
        for recipe in CRAFTING_GRID_RECIPES:
            if crafting_grid == recipe["pattern"]:
                self.add_inventory(recipe["result"], quantity = 1)
                print("Crafted recipe!")
                print(f"\nAdded {recipe["result"]} to player inventory")
                crafting_grid = reset_crafting_grid()

    def add_item_to_grid(self, item_name):
        if item_name in self.__inventory:
            if item_name in ITEMS:
                try:
                    row = int(input("Enter your row (1 -> 3"))
                    column = int(input("Enter your column (1 -> 3"))
                    if 1 <= row <= 3 and 1 <= column <= 3:
                        row -= 1
                        column -= 1
                        crafting_grid[row][column] = item_name
                    else:
                        print("Please select the correct row and column")
                except ValueError:
                    print("row and column should only be integers between 1 and 3")
            else:
                print(f"{item_name} not found")
        else:
            print(f"You don't have {item_name}")

    def remove_item_from_grid(self, item_name, row, column):
        if crafting_grid[row][column] is not None:
            crafting_grid[row][column] = None
            self.__inventory[item_name] += 1

def game_loop():
    while True:
        plr_name = input("Enter your name: ")
        player = Player(plr_name)
        inventory = Inventory(plr_name)

        print("\n    Welcome to the Crafting Grid!     ")
        display_grid()
        while True:
            try:
                move = int(input("\n (1) Add an item to your inventory\n (2) Add item to your grid\n (3) Remove item from grid\n (4) Remove item from your inventory\n (5) Display inventory \n (6) Clear inventory\n (7) Reset Crafting Grid \n"))
                if move == 1:
                    item_name = input("\nEnter your item: ")
                    try:
                        quantity = int(input("Enter your quantity: "))
                        inventory.add_inventory(item_name, quantity)
                    except ValueError:
                        print("Please enter a valid quantity")
                elif move == 2:
                    item_name = input("\nEnter your item: ")
                    inventory.add_item_to_grid(item_name)
                    inventory.craft_from_grid()
                elif move == 3:
                    try:
                        item = input("Enter your item ")
                        row = int(input("Enter your row number (1 -> 3) "))
                        column = int(input("Enter your column number (1 -> 3 )"))
                        if 1 <= row <= 3 and 1 <= column <= 3:
                            row -= 1
                            column -= 1
                            inventory.remove_item_from_grid(item, row, column)
                        else:
                            print("Please enter a valid row and column number")
                    except ValueError:
                        print("row and column values should be integers between 1 and 3")
                elif move == 4:
                    item = input("Enter your item ")
                    try:
                        quantity = int(input("Enter your quantity "))
                        inventory.remove_inventory(item, quantity)
                    except ValueError:
                        print("Quantity value should be a positive integer")
                elif move == 5:
                    print(inventory.display_inventory())
                elif move == 6:
                    inventory.clear_inventory()
                elif move == 7:
                    reset_crafting_grid()
                    print("crafting grid reset")
                else:
                    print("Please enter a valid number (1 -> 7)")
                display_grid()
            except ValueError:
                print("Please enter a valid number (1 -> 7)")

game_loop()
