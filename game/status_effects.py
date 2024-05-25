# game/status_effects.py
class StatusEffect:
    def __init__(self, name, duration, effect):
        self.name = name
        self.duration = duration
        self.effect = effect

    def apply(self, target):
        print(f"Applying {self.name} to {target.name} for {self.duration} turns.")
        # Apply effect to target (this can be expanded based on the effect)
        if self.effect == "Burning":
            target.stats["HP"] -= 5  # Example effect: reduces HP by 5 each turn
            target.status_effects[self.name] = self.duration

status_effects = {
    "Burning": StatusEffect(name="Burning", duration=3, effect="Burning"),
    "Poison": StatusEffect(name="Poison", duration=5, effect="Poison"),
    "Silenced": StatusEffect(name="Silenced", duration=2, effect="Silenced"),
    "Slowed": StatusEffect(name="Slowed", duration=4, effect="Slowed"),
    "Weakened": StatusEffect(name="Weakened", duration=3, effect="Weakened"),
    "Blinded": StatusEffect(name="Blinded", duration=1, effect="Blinded"),
    "Bound": StatusEffect(name="Bound", duration=2, effect="Bound"),
    "Asleep": StatusEffect(name="Asleep", duration=3, effect="Asleep")
    # Add more status effects here
}
