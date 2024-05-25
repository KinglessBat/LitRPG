# main.py
import sys
import random
from game.character import Character
from game.save_load import SaveLoad
from data.maps.MasterMap import map_data
from data.npcs.NPCdiolouge import npc_data


def create_new_character():
    name = input("Enter your character's name: ")
    player = Character(name, 1)
    print(f"New character {name} created.")
    return player

def display_location(location):
    location_data = map_data.get(location, {})
    print(location_data.get("description", "You see nothing special."))

def interact_with_npc(npc_name, player):
    npc = npc_data.get(npc_name, {})
    dialogue_state = "start"

    while dialogue_state != "end":
        dialogue = npc["dialogue"].get(dialogue_state, {})
        print(dialogue["text"])
        options = dialogue["options"]
        if options:
            valid_options = []
            for i, (option_text, next_state) in enumerate(options.items()):
                if isinstance(next_state, dict):
                    condition_stat = list(next_state.keys())[0]
                    required_value = next_state[condition_stat]
                    if player.stats.get(condition_stat, 0) >= required_value:
                        print(f"{len(valid_options) + 1}. {option_text}")
                        valid_options.append(next_state["goto"])
                else:
                    print(f"{len(valid_options) + 1}. {option_text}")
                    valid_options.append(next_state)
            
            choice = int(input("Choose an option: ")) - 1
            selected_option = valid_options[choice]
            dialogue_state = selected_option

            if "give_quest" in dialogue:
                quest_id = dialogue["give_quest"]
                if quest_id in player.quests and not player.quests[quest_id].completed:
                    print(f"You have received a new quest: {player.quests[quest_id].description}")
        else:
            dialogue_state = "end"



def adventure(player):
    location_data = map_data.get(player.location, {})
    items = location_data.get("items", {})
    monsters = location_data.get("monsters", {})

    encounter_chance = random.random()

    if items:
        print(f"... Not Done Yet")
        return

    if monsters:
        for monster_name, monster_info in monsters.items():
            if encounter_chance < monster_info["chance"]:
                print(f"You encountered a {monster_name}!")
                # Placeholder for combat system
                return

    print("You found nothing of interest.")
   
def move_player(player, direction):
    current_location = map_data[player.location]
    if direction in current_location["directions"]:
        new_location = current_location["directions"][direction]
        player.location = new_location
        print(f"You moved {direction} to {new_location}.")
        display_location(new_location)
    else:
        print("You can't go that way.")

def main():
    print("Welcome to the LitRPG Game!")
    
    player = None

    while True:
        
        print("\nMain Menu")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            player = create_new_character()
            print(f"New game started with character {player.name}.")
        elif choice == '2':
            saves = SaveLoad.list_saves()
            if not saves:
                print("No saved games found.")
            else:
                print("Saved Games:")
                for character_name in saves:
                    print(character_name)
                character_name = input("Enter the character name to load: ")
                player = SaveLoad.load_game(character_name)
                if player:
                    print(f"Loaded game with character {player.name}.")
                else:
                    print("Failed to load game.")
        elif choice == '3':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

        if player:
            while True:
                display_location(player.location)
                print("\n1. Adventure")
                print("2. Interact with NPC")
                print("3. Journal")
                print("4. Inventory")
                print("5. Move")
                

                choice = input("Enter your choice: ")

                if choice == '1':
                    adventure(player)
                elif choice == '2':
                    location_data = map_data[player.location]
                    if "npcs" in location_data and location_data["npcs"]:
                        for i, npc in enumerate(location_data["npcs"]):
                            print(f"{i + 1}. {npc}")
                        npc_choice = int(input("Choose an NPC to interact with: ")) - 1
                        interact_with_npc(location_data["npcs"][npc_choice], player)
                    else:
                        print("No NPCs to interact with here.")
                elif choice == '3':
                    while True:
                        print("\n1. Stats")
                        print("2. Save Game")
                        print("3. Exit Game to Menu")
                        
                        choice = input("Enter your choice: ")
                        
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
                    print("Not Added yet")
                elif choice == '5':
                    print("Available directions:")
                    current_location = map_data[player.location]
                    for direction in current_location["directions"]:
                        print(direction)
                    direction = input("Enter the direction you want to move: ")
                    move_player(player, direction)

                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()