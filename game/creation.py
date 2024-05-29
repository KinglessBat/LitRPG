# game/creation.py

try:
    import data.characters.races
    from data.characters.races import races_data
except ImportError as e:
    print(f"Error importing race_data: {e}")
    raise

class Create:
    def __init__(self, name, gui):
        self.gui = gui
        self.gui.display_text("")
        self.gui.display_text(f"Time to pick {name}'s race")
        print("")
        print(f"Time to pick {name}'s race")
        self.name = name

    def pick_race(self):
        while True:
            self.gui.display_text("")
            self.gui.display_text("Choose a race:")
            print("")
            print("Choose a race:")
            for race in races_data:
                self.gui.display_text(f"{race}")
                print(f"{race}")

            chosen_race = input("Enter the name of the race you want to choose: ") or self.gui.get_input()

            if chosen_race in races_data:
                print("")
                print(f"You've chosen {chosen_race}. Here's the info:")
                race_info = races_data[chosen_race]
                print(f"Name: {race_info['name']}")
                print(f"Description: {race_info['description']}")
                print("Stats:")
                for stat, value in race_info['stats'].items():
                    print(f"  {stat}: {value}")
                if race_info['skills']:
                    print("Skills:")
                    for skill in race_info['skills']:
                        print(f"  {skill}")
                if 'passives' in race_info and race_info['passives']:
                    print("Passives:")
                    for passive in race_info['passives']:
                        print(f"  {passive}")
                
                print("")
                confirm = input("Confirm your choice? (yes/no): ")
                if confirm.lower() == "yes":
                    print("Race confirmed!")
                    return chosen_race, race_info
                elif confirm.lower() == "no":
                    print("Choose a different race.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("Invalid race name. Please choose from the available races.")