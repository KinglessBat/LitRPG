# game/inventory.py

consumables = {
    "Potion": {
        "effect": "heal",
        "value": 50
    },
    "ManaPotion": {
        "effect": "restore_mana",
        "value": 30
    }
}

weapons = {
    "TutorialSword": {
        "damage": 10,
        "type": "physical",
        "hands": 1
    },
    "GreatAxe": {
        "damage": 20,
        "type": "physical",
        "hands": 2
    }
}

armor = {
    "LeatherArmor": {
        "defense": 5,
        "slot": "Armor Middle"
    },
    "IronHelmet": {
        "defense": 3,
        "slot": "Armor Head"
    }
}

ring_data = {
    "Ring of Strength": {
        "description": "A ring imbued with the power of strength.",
        "stat_buffs": {
            "Strength": 5
        }
    },
    "Ring of Agility": {
        "description": "A ring imbued with the power of agility.",
        "stat_buffs": {
            "Agility": 5
        }
    }
}

necklace_data = {
    "Necklace of Intelligence": {
        "description": "A necklace imbued with the power of intelligence.",
        "stat_buffs": {
            "Intelligence": 5
        }
    },
    "Necklace of Vitality": {
        "description": "A necklace imbued with the power of vitality.",
        "stat_buffs": {
            "HP": 20
        }
    }
}

class Inventory:
    def __init__(self):
        self.items = {
            "consumable": [],
            "weapon": [],
            "armor": [],
            "ring": [],  # New category for rings
            "necklace": []  # New category for necklaces
        }
        self.equipped = {
            "Armor Head": None,
            "Armor Middle": None,
            "Armor Bottom": None,
            "Right Hand": None,
            "Left Hand": None,
            "Necklace": None,
            "Ring": None,
            "Amulet": None
        }

    def add_item(self, item_type, item_name, description=None):
        item = {
            "name": item_name,
            "description": description  # New field for item description
        }
        self.items[item_type].append(item)

    def view_items(self, page):
        items_per_page = 10
        all_items = []
        for item_type, items in self.items.items():
            all_items.extend([(item_type, item) for item in items])

        if not all_items:
            print("Your inventory is empty.")
            return False

        start_index = (page - 1) * items_per_page
        end_index = start_index + items_per_page

        if start_index >= len(all_items):
            print("No more items to display.")
            return False

        print("\nInventory:")
        for index, (item_type, item) in enumerate(all_items[start_index:end_index], start=start_index + 1):
            print(f"{index}. {item['name']} ({item_type})")

        print("\n'n' for next page, 'p' for previous page, 'b' to go back")
        return True

    def equip_item(self, item_index):
        categories = ["weapon", "armor", "ring", "necklace"]
        equipped_slot = None

        for category in categories:
            if 0 <= item_index < len(self.items[category]):
                equipped_item = self.items[category].pop(item_index)
                equipped_slot = category.capitalize() if category != "necklace" else "Necklace"
                break

        if equipped_slot:
            if equipped_slot == "Ring" or equipped_slot == "Necklace":
                if self.equipped[equipped_slot]:
                    self.items[equipped_slot.lower()].append(self.equipped[equipped_slot])
                self.equipped[equipped_slot] = equipped_item
            else:
                current_equipped_item = self.equipped[equipped_slot]
                if current_equipped_item:
                    self.items[current_equipped_item["name"].lower()].append(current_equipped_item)
                self.equipped[equipped_slot] = equipped_item
            print(f"{equipped_item['name']} equipped in {equipped_slot}.")
        else:
            print("Invalid item index.")

    def unequip_item(self, slot_name):
        if slot_name in self.equipped:
            if self.equipped[slot_name]:
                item = self.equipped[slot_name]
                self.equipped[slot_name] = None
                self.items[item["name"].lower()].append(item)
                print(f"{item['name']} unequipped from {slot_name}.")
            else:
                print("No item equipped in this slot.")
        else:
            print("Invalid slot name.")

    def use_item(self, item_index):
        pass  # Implement use item logic

