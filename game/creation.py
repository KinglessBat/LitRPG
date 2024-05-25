# game/creation.py
class Create:
    def __init__(self, name):
        print(f"Time to pick {name}'s race")
        self.name = name

    def pick_race(self):
        races = {
            "Human": {
                "HP": 100,
                "MP": 50,
                "Stamina": 50,
                "Strength": 10,
                "Agility": 10,
                "Intelligence": 10
            },
            "Elf": {
                "HP": 70,
                "MP": 80,
                "Stamina": 40,
                "Strength": 5,
                "Agility": 20,
                "Intelligence": 15
            },
            "Dwarf": {
                "HP": 130,
                "MP": 0,
                "Stamina": 70,
                "Strength": 16,
                "Agility": 5,
                "Intelligence": 9
            }
        }

        while True:
            print("Choose a race:")
            for race in races:
                print(f"{race}")

            chosen_race = input("Enter the name of the race you want to choose: ")

            if chosen_race in races:
                print(f"You've chosen {chosen_race}. Here's the info:")
                race_info = races[chosen_race]
                for stat, value in race_info.items():
                    print(f"{stat}: {value}")

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