# game/character.py
from game.creation import Create
from game.inventory import Inventory
from data.characters.class_storage import class_data

class Character:
    def __init__(self, name, level):
        self.name = name
        self.Class = "None"
        self.level = level
        self.XP = 0
        self.location = "Tutorial1"
        choosen_race, race_info = Create(name).pick_race()
        self.race = choosen_race
        self.stats = {
            "HP": race_info["HP"],
            "MP": race_info["MP"],
            "Stamina": race_info["Stamina"],
            "Strength": race_info["Strength"],
            "Agility": race_info["Agility"],
            "Intelligence": race_info["Intelligence"]
        }
        self.skills = []
        self.status_effects = {}
        self.inventory = Inventory()
        self.completed_quests = []
        self.id = None  # Unique identifier for the character

    def display_stats(self):
        print(f"\nName: {self.name}")
        print(f"Level: {self.level}")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")

    def level_up(self):
        required_xp = (self.level + 10) * 1.5
        if self.XP >= required_xp:
            self.XP -= required_xp
            self.level += 1
            print("\n\nYou have gained a level!")
            
            ClassData = class_data.get(self.Class, {})
            level_stats = ClassData.get('level_stats', {})
            
            for stat, increment in level_stats.items():
                if stat in self.stats:
                    self.stats[stat] += increment

            free_stat_points = level_stats.get("Free", 0)
            self.assign_free_stats(free_stat_points)
            
    def assign_free_stats(self, points):
        while points > 0:
            print(f"\nYou have {points} free stat points to assign.")
            print("Choose a stat to increase:")
            for stat in self.stats:
                print(f"{stat}: {self.stats[stat]}")
                
            chosen_stat = input("Enter the stat you want to increase: ").capitalize()
            if chosen_stat in self.stats:
                self.stats[chosen_stat] += 1
                points -= 1
                print(f"Increased {chosen_stat} by 1. Remaining points: {points}.")
            else:
                print("Invalid stat choice. Please try again.")
                
        print("All free stat points assigned.")