# game/save_load.py
import json
import os
import random
import string
from game.character import Character

class SaveLoad:
    @staticmethod
    def generate_unique_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    @staticmethod
    def get_save_filename(character_name):
        return f"text_rpg/data/saves/savegame_{character_name}.json"  # Adjusted file path

    @staticmethod
    def save_game(player):
        filename = SaveLoad.get_save_filename(player.name)
        data = {
            "id": player.id,
            "name": player.name,
            "level": player.level,
            "stats": player.stats,
            "skills": [skill.name for skill in player.skills],
            "status_effects": player.status_effects
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"Game saved")

    @staticmethod
    def load_game(character_name):
        filename = SaveLoad.get_save_filename(character_name)
        if not os.path.exists(filename):
            print(f"No save file found for character: {character_name}")
            return None
        
        with open(filename, 'r') as f:
            data = json.load(f)
        player = Character(data['name'], data['level'])
        player.id = data['id']
        player.stats = data['stats']
        # Assume we have a global skills dictionary
        
        player.skills = [skills[skill_name]]
        player.status_effects = data['status_effects']
        print(f"Game loaded from {filename}")
        return player

    @staticmethod
    def list_saves():
        base_directory = os.path.dirname(os.path.abspath(__file__))
        saves_directory = os.path.join(base_directory, '..', 'data', 'saves')  # Adjusted relative path
        files = [f for f in os.listdir(saves_directory) if f.startswith("savegame_") and f.endswith(".json")]
    
        saves = {}
        for file in files:
            with open(os.path.join(saves_directory, file), 'r') as f:
                data = json.load(f)
                saves[data['id']] = data['name']
        return saves
