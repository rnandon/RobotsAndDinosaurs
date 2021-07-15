###        IMPORTS
### ================================
# No imports needed at this time


class Combatant_Group:
    def __init__(self, combatants):
        self.combatants = combatants
        self.valid_combatants = self.get_valid_combatants()

    def get_valid_combatants(self):
        current_valid_combatants = []

        for combatant in self.combatants:
            if combatant.health > 0:
                current_valid_combatants.append(combatant)

        self.valid_combatants = current_valid_combatants
        return self.valid_combatants