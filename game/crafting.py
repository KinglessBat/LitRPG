# game/crafting.py
class Crafting:
    def __init__(self, recipes):
        self.recipes = recipes

    def craft(self, recipe_name, inventory):
        recipe = self.recipes.get(recipe_name)
        if recipe and all(item in inventory.items for item in recipe['ingredients']):
            for item in recipe['ingredients']:
                inventory.remove_item(item)
            inventory.add_item(recipe['result'])
            print(f"Crafted {recipe['result']}")
        else:
            print("Missing ingredients")
