#main.py




import sys
import random
from game.character import Character  # Ensure Character is imported
from game.save_load import SaveLoad
from data.maps.MasterMap import map_data
from data.npcs.NPCdiolouge import npc_data
from game.gui import create_gui

def create_new_character(gui):
    gui.display_text("Enter your character's name:")
    name = gui.get_input()
    player = Character(name, 1, gui)
    gui.display_text(f"New character {name} created.")
    return player

def display_location(gui, location):
    location_data = map_data.get(location, {})
    description = location_data.get("description", "You see nothing special.")
    gui.display_text(description)

def interact_with_npc(gui, npc_name, player):
    npc = npc_data.get(npc_name, {})
    dialogue_state = "start"

    while dialogue_state != "end":
        dialogue = npc["dialogue"].get(dialogue_state, {})
        gui.display_text(dialogue["text"])
        options = dialogue["options"]
        if options:
            valid_options = []
            for i, (option_text, next_state) in enumerate(options.items()):
                if isinstance(next_state, dict):
                    condition_stat = list(next_state.keys())[0]
                    required_value = next_state[condition_stat]
                    if player.stats.get(condition_stat, 0) >= required_value:
                        gui.display_text(f"{len(valid_options) + 1}. {option_text}")
                        valid_options.append(next_state["goto"])
                else:
                    gui.display_text(f"{len(valid_options) + 1}. {option_text}")
                    valid_options.append(next_state)
            
            choice = int(gui.get_input()) - 1
            selected_option = valid_options[choice]
            dialogue_state = selected_option

            if "give_quest" in dialogue:
                quest_id = dialogue["give_quest"]
                if quest_id in player.quests and not player.quests[quest_id].completed:
                    gui.display_text(f"You have received a new quest: {player.quests[quest_id].description}")
        else:
            dialogue_state = "end"

def adventure(gui, player):
    location_data = map_data.get(player.location, {})
    items = location_data.get("items", {})
    monsters = location_data.get("monsters", {})

    encounter_chance = random.random()

    if items:
        gui.display_text(f"... Not Done Yet")
        return

    if monsters:
        for monster_name, monster_info in monsters.items():
            if encounter_chance < monster_info["chance"]:
                gui.display_text(f"You encountered a {monster_name}!")
                # Placeholder for combat system
                return

    gui.display_text("You found nothing of interest.")

def move_player(gui, player, direction):
    current_location = map_data[player.location]
    if direction in current_location["directions"]:
        new_location = current_location["directions"][direction]
        player.location = new_location
        gui.display_text(f"You moved {direction} to {new_location}.")
        display_location(gui, new_location)
    else:
        gui.display_text("You can't go that way.")

def main():
    gui = create_gui()
    gui.display_text("Welcome to the LitRPG Game!")
    
    player = None

    while True:
        gui.display_text("Main Menu")
        gui.display_text("1. New Game")
        gui.display_text("2. Load Game")
        gui.display_text("3. Exit")

        choice = gui.get_input()

        if choice == '1':
            player = create_new_character(gui)
            gui.display_text(f"New game started with character {player.name}.")
        elif choice == '2':
            saves = SaveLoad.list_saves()
            if not saves:
                gui.display_text("No saved games found.")
            else:
                gui.display_text("Saved Games:")
                for character_name in saves.values():
                    gui.display_text(character_name)
                gui.display_text("Enter the character name to load:")
                character_name = gui.get_input()
                player = SaveLoad.load_game(character_name)
                if player:
                    gui.display_text(f"Loaded game with character {player.name}.")
                else:
                    gui.display_text("Failed to load game.")
        elif choice == '3':
            gui.display_text("Thanks for playing!")
            sys.exit()
        else:
            gui.display_text("Invalid choice. Please try again.")

        if player:
            while True:
                display_location(gui, player.location)
                gui.display_text("\n1. Adventure")
                gui.display_text("2. Interact with NPC")
                gui.display_text("3. Journal")
                gui.display_text("4. Inventory")
                gui.display_text("5. Move")

                choice = gui.get_input()

                if choice == '1':
                    adventure(gui, player)
                elif choice == '2':
                    location_data = map_data[player.location]
                    if "npcs" in location_data and location_data["npcs"]:
                        for i, npc in enumerate(location_data["npcs"]):
                            gui.display_text(f"{i + 1}. {npc}")
                        gui.display_text("Choose an NPC to interact with:")
                        npc_choice = int(gui.get_input()) - 1
                        interact_with_npc(gui, location_data["npcs"][npc_choice], player)
                    else:
                        gui.display_text("No NPCs to interact with here.")
                elif choice == '3':
                    while True:
                        gui.display_text("\n1. Stats")
                        gui.display_text("2. Save Game")
                        gui.display_text("3. Exit Game to Menu")
                        
                        choice = gui.get_input()
                        
                        if choice == '1': 
                            player.display_stats()
                            break
                        elif choice == '2':
                            SaveLoad.save_game(player)
                            break
                        elif choice == '3':
                            SaveLoad.save_game(player)
                            player = None
                            break
                elif choice == '4':
                    gui.display_text("Not Added yet")
                elif choice == '5':
                    gui.display_text("Available directions:")
                    current_location = map_data[player.location]
                    for direction in current_location["directions"]:
                        gui.display_text(direction)
                    gui.display_text("Enter the direction you want to move:")
                    direction = gui.get_input()
                    move_player(gui, player, direction)

                else:
                    gui.display_text("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
