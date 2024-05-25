#data/npcs/NPC

npc_data = {
    "Areon": {
        "name": "Areon",
        "dialogue": {
            "start": {
                "text": "Welcome to the tutorial! What do you want to know?",
                "options": {
                    "Tell me about this game": "info",
                    "I need some help": "help",
                    "Who are you?": "self",
                    "Goodbye": "end"
                }
            },
            "info": {
                "text": "This is a LitRPG game where you can explore, fight, and level up.",
                "options": {
                    "Back": "start",
                    "Gimme a quest": "quest",
                    "Goodbye": "end"
                }
            },
            "help": {
                "text": "Sure, what do you need help with?",
                "options": {
                    "How to play": "how_to_play",
                    "About skills": "about_skills",
                    "Back": "start"
                }
            },
            "how_to_play": {
                "text": "Use the menu to navigate and interact with the game world.",
                "options": {
                    "Back": "help",
                    "Goodbye": "end"
                }
            },
            "about_skills": {
                "text": "Skills can be learned and improved as you level up.",
                "options": {
                    "Back": "help",
                    "Goodbye": "end"
                }
            },
            "self": {
                "text": "I am the watcher of this area",
                "options": {
                    "Back": "start",
                    "Why are you covered in oil?": {
                        "Intelligence": 10,
                        "goto": "oil",
                    },
                }
            },
            "end": {
                "text": "Good luck on your adventure!",
                "options": {}
            },
            "quest": {
                "text": "Fine. Go to the end of the area and come back",
                "give_quest": "CompleteTutorial",
                "options": {
                    "okie": "start"    
                }
            },
            "oil": {
                "text": "I work with many things. Now begone",
                "options": {}
            }
        },
    },
    # Add more NPCs as needed
}
