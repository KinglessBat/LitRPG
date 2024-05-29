#data/items/item_storage.py

item_data:{
    "weapons":{
        "melee":{
            "template melee":{
                "name":"template melee",
                "description":"Template Description here",
                "rarity": "nil",
                "type": "Sword/Scythe/Spear/ETC",
                "hand": 1, #can also be 2
                "damage":{
                    "D1Type":"Slashing/Percing/Bashing",
                    "D1": 10 #number or can do {1,10} for random
                    "D2Type":"Fire/Ice/Earth/Air/ETC", #optional
                    "D2": 0,
                },
                "bonuses":{
                    "skills":{
                        "example3", #no skills required   
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    }
                }
            },
        },
        "ranged":{
            "template ranged":{
                "name":"template ranged",
                "description":"Template Description here"
                "rarity": "nil",
                "type": "Bow/Gun/BlowGun/ETC",
                "hand": 2, #norm is 2 but not always, like pistols or hand crossbows
                "damage":{
                    "D1Type":"Percing",
                    "D1": 10 #number or can do {1,10} for random
                    "D2Type":"Fire/Ice/Earth/Air/ETC", #optional
                    "D2": 0,
                },
                "bonuses":{
                    "skills":{
                        "example3", #no skills required   
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    }
                }
        },
        "magic":{
            "template magic":{
                "name":"template magic",
                "description":"Template Description here"
                "rarity": "nil",
                "type": "Staff/Orb/ETC",
                "hand": 1, #can also be 2
                "damage":{
                    "D1Type":"Slashing/Percing/Bashing",
                    "D1": 10 #number or can do {1,10} for random
                    "D2Type":"Fire/Ice/Earth/Air/ETC", #optional
                    "D2": 0,
                },
                "bonuses":{
                    "skills":{
                        "example3", #no skills required (magic weapons typically have them though) 
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    }
                }
        },
    },
    "armor":{
        "helmet":{
            "helmet template": {
                "name":"helmet template",
                "description":"Description here",
                "rarity":"nil",
                "bonuses":{
                    "skills":{
                        "example3", #no skills required (magic weapons typically have them though) 
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    },
                    "armor":0 #ammount of armor this armor gives
                }
            }
        },
        "chestplate":{
            "chestplate template": {
                "name":"chestplate template",
                "description":"Description here",
                "rarity":"nil",
                "bonuses":{
                    "skills":{
                        "example3", #no skills required (magic weapons typically have them though) 
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    },
                    "armor":0 #ammount of armor this armor gives
                }
            }

        },
        "leg":{
            "leg template": {
                "name":"leg template",
                "description":"Description here",
                "rarity":"nil",
                "bonuses":{
                    "skills":{
                        "example3", #no skills required (magic weapons typically have them though) 
                    },
                    "passives":{
                        "example4", #no passives required 
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    },
                    "armor":0 #ammount of armor this armor gives
                }
            }
        },
    },
    "accessories":{
        "ring":{
            "Ring Template":{
                "name":"Ring Template",
                "description":"Ring Description goes here",
                "rarity":"nil",
                "bonuses":{
                    "skills":{
                        "example1", #not required    
                    },
                    "passives":{
                        "example2", #not required   
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    },
                }
            }
        },
        "necklace":{
            "necklace Template":{
                "name":"necklace Template",
                "description":"necklace Description goes here",
                "rarity":"nil",
                "bonuses":{
                    "skills":{
                        "example1", #not required    
                    },
                    "passives":{
                        "example2", #not required   
                    },
                    "stats":{
                        "Strength":0,
                        "Dexterity":0,
                        "Intelligence":0,
                        "Luck":0,
                        "Endurance":0,
                    },
                    "resources":{
                        "HP":0,
                        "MP":0,
                        "Stamina":0,
                    },
                }
            }
        },
        "consumeables":{
            "consumeable template":{
                   "name":"template",
                   "description":"Description here",
                   "rarity":"nil",
                   "effects":{
                       "stats":{
                           "Strength":{ #repeat this for each stat 
                               "Bonus":0, #flat bonus
                               "BonusDura":0, #number of turns
                               "Multi":0, #multiplyer bonus
                               "NultiDura":0, #number of turns for multibonus
                           },
                       },
                       "adds":{
                           "HP": 0, #gives hp (up to the max HP)
                           "MP": 0, #same as HP
                           "Stamina": 0, #same as HP
                           "MaxHP": 0, #gives max HP
                           "MaxMP": 0, #gives max MP
                           "MaxStamina": 0, #Gives max Stamina
                           "Skills":{
                               "Example" #would give the player a skill permently
                           },
                           "Passives":{
                               "Example2" #same as skills but passive
                           },
                           "Class":{
                               "Class" #gives the player a class
                           },
                           "Race":{
                               "Gives the player a new race"
                           },
                           
                       },

                   }
             }
            
            
        },
    },
    
}