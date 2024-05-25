# data/maps/MasterMap.py

map_data = {
    "Tutorial1": {
        "description": "You are in a small tutorial room. There is a door to the north.",
        "directions": {"north": "Tutorial2"},
        "items": {
            "Potion": {
                "chance": 0.5,
                "multiple": True
            }
        },
        "monsters": {
            "Slime": {
                "chance": 0.5
            }
        },
        "npcs": ["Areon"]
    },
    "Tutorial2": {
        "description": "You are in the second room of the tutorial. There is a door to the south and east.",
        "directions": {"south": "Tutorial1", "east": "Tutorial3"},
        "items": {
            "TutorialSword": {
                "chance": 0.3,
                "multiple": False
            }
        },
        "monsters": {
            "Goblin": {
                "chance": 0.2
            }
        },
        "npcs": []
    },
    "Tutorial3": {
        "description": "You are in the third room of the tutorial. There is a door to the west.",
        "directions": {"west": "Tutorial2"},
        "items": {
            "Rainbow Soul": {
                "chance": 0.0001,
                "multiple": False
            }
        },
        "monsters": {
        },
        "npcs": []
        }
    # Add more locations as needed
}