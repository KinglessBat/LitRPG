# game/character.py
from game.creation import Create
from game.inventory import Inventory
from data.characters.class_storage import class_data

class Character:
    def __init__(self, name, level, gui):
        self.name = name
        self.Class = "None"
        self.level = level
        self.XP = 0
        self.location = "Tutorial1"
        self.gui = gui
        gui.display_text("Test Before Forward")
        chosen_race, race_info = Create(name, gui).pick_race()
        self.race = chosen_race
        self.resources = {
            "HP": race_info['stats']["HP"],
            "MP": race_info['stats']["MP"],
            "Stamina": race_info['stats']["Stamina"],
            "MaxHP": race_info['stats']["HP"],
            "MaxMP": race_info['stats']["MP"],
            "MaxStamina": race_info['stats']["Stamina"],
        }
        self.stats = {
            "Strength": race_info['stats']["Strength"],
            "Dexterity": race_info['stats']["Dexterity"],
            "Intelligence": race_info['stats']["Intelligence"],
            "Luck": race_info['stats']["Luck"],
            "Endurance": race_info['stats']["Endurance"],
        }
        self.bonus = {
            "HPBonus": 0,
            "MPBonus": 0,
            "StaminaBonus": 0,
            "StrBonus": 0,
            "DexBonus": 0,
            "IntBonus": 0,
            "LuckBonus": 0,
            "EndBonus": 0,
            "HPMulti": 0,
            "MPMulti": 0,
            "StaminaMulti": 0,
            "StrMulti": 0,
            "DexMulti": 0,
            "IntMulti": 0,
            "LuckMulti": 0,
            "EndMulti": 0,
        }
        self.skills = list(race_info.get('skills', [])) + list(race_info.get('passives', []))
        self.status_effects = {}
        self.inventory = Inventory()
        self.completed_quests = []
        self.id = None  # Unique identifier for the character

    def display_stats(self):
        self.gui.display_text(f"\nName: {self.name}")
        self.gui.display_text(f"Level: {self.level}")
        for stat, value in self.stats.items():
            self.gui.display_text(f"{stat}: {value}")
        self.gui.display_text("\nSkills:")
        for skill in self.skills:
            self.gui.display_text(f"  {skill}")

    def correct_resources(self):
        self.resources["HP"] = (10 + (self.stats["Endurance"] * 2.5)) + self.bonus["HPBonus"]
        self.resources["MP"] = (5 + (self.stats["Endurance"] * 2)) + self.bonus["MPBonus"]
        self.resources["Stamina"] = ((self.stats["Dexterity"] * 2) + self.stats["Endurance"]) + self.bonus["StaminaBonus"]

    def level_up(self):
        required_xp = (self.level + 10) * 1.5
        if self.XP >= required_xp:
            self.XP -= required_xp
            self.level += 1
            self.gui.display_text("\n\nYou have gained a level!")

            ClassData = class_data.get(self.Class, {})
            level_stats = ClassData.get('level_stats', {})

            for stat, increment in level_stats.items():
                if stat in self.stats:
                    self.stats[stat] += increment

            free_stat_points = level_stats.get("Free", 0)
            self.assign_free_stats(free_stat_points)

    def assign_free_stats(self, points):
        while points > 0:
            self.gui.display_text(f"\nYou have {points} free stat points to assign.")
            self.gui.display_text("Choose a stat to increase:")
            for stat in self.stats:
                self.gui.display_text(f"{stat}: {self.stats[stat]}")

            chosen_stat = self.gui.get_input("Enter the stat you want to increase:").capitalize()
            if chosen_stat in self.stats:
                self.stats[chosen_stat] += 1
                points -= 1
                self.gui.display_text(f"Increased {chosen_stat} by 1. Remaining points: {points}.")
            else:
                self.gui.display_text("Invalid stat choice. Please try again.")

        self.gui.display_text("All free stat points assigned.")
        self.correct_resources()

    def Manage(self, target, type, new):
        target = target.lower()

        if target in self.stats:
            if type == "Add":
                self.stats[target] += new
            elif type == "Subtract":
                self.stats[target] -= new
            elif type == "Set":
                self.stats[target] = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Use 'Add', 'Subtract', or 'Set'.")

        if target in self.bonus:
            if type == "Add":
                self.bonus[target] += new
            elif type == "Subtract":
                self.bonus[target] -= new
            elif type == "Set":
                self.bonus[target] = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Use 'Add', 'Subtract', or 'Set'.")

        if target in self.resources:
            if type == "Add":
                self.resources[target] += new
            elif type == "Subtract":
                self.resources[target] -= new
            elif type == "Set":
                self.resources[target] = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Use 'Add', 'Subtract', or 'Set'.")

        elif target == "xp":
            if type == "Add":
                self.XP += new
            elif type == "Subtract":
                self.XP -= new
            elif type == "Set":
                self.XP = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Use 'Add', 'Subtract', or 'Set'.")

        elif target == "class":
            if type == "Set":
                self.Class = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Only 'Set' is valid for Class.")

        elif target == "level":
            if type == "Add":
                self.level += new
            elif type == "Subtract":
                self.level -= new
            elif type == "Set":
                self.level = new
            else:
                self.gui.display_text(f"Invalid type: {type}. Use 'Add', 'Subtract', or 'Set'.")

        elif target in ["location", "name"]:
            if type == "Set":
                setattr(self, target, new)
            else:
                self.gui.display_text(f"Invalid type: {type}. Only 'Set' is valid for {target.capitalize()}.")

        else:
            self.gui.display_text(f"Invalid target: {target}. Cannot manage this attribute.")

        for stat in self.stats:
            if self.stats[stat] < 0:
                self.stats[stat] = 0

        self.correct_resources()
