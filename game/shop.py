# game/shop.py
class Shop:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_items(self):
        print("Shop Inventory:")
        for item in self.inventory:
            print(f"- {item}")
