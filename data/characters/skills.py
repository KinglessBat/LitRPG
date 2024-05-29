#data/characters/skills.py

Actives_data: {
    "Template": {
        "name":"Template",
        "description":"Description",
        "classification": "Melee/Ranged/Magic",
        "typee": "Status/Attack/Defense/Healing/Other",
        "target": "self/enemy/all/field",
        "CostType1":"Sta/MP/HP",
        "Cost1":0,
        "CostType2": "Sta/MP/HP", #optional
        "Cost2":0,
        "effects": {
            "Damage":{
                "D1":{
                    "DType1":"Physical/Fire/Ice/Earth/Water/Air/Space/Time/ETC",
                    "DTotal1":1, #can be flat number
                },
                "D2":{#not required
                    "Dtype2":"Physical/Fire/Ice/Earth/Water/Air/Space/Time/ETC",
                    "DTotal2": {1,2}, #or randomized number
                }
            
            },
            "Status":{
                "S1":{
                    "name":"Burning/Poison/Paralized/ETC",
                    "target": "self/enemy/all",
                    "stacks": 0 #number of turns,
                },
                "S2":{#Not required
                    "name":"Burning/Poison/Paralized/ETC",
                    "target": "self/enemy/all",
                    "stacks": 0 #number of turns,    
                },
            },
        },
     },
}

Passives_data: {
    "Template": {
        "name":"template",
        "description":"Template Passive",
        "trigger":"TakeDamage/TakeHealing/TaleStatus/DealDamage/DealHealing/ApplyStatus/StatusCycle/StartBattle/EndBattle/Death/Kill"
    },    
}