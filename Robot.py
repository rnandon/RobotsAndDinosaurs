###        IMPORTS
### ================================
from Combatant import Combatant


# Robot. Implementation of the Combatant class
class Robot(Combatant):
    def __init__(self, name, weapon):
        self.equipped_weapon = weapon
        super(Robot, self).__init__(name)

    ###        METHODS
    ### =================================================================
    def attack(self, opponent):
        # Call the combatant attack method, then return damage and attack name for the user interface to use
        attack_name = self.equipped_weapon.name
        damage_dealt = super(Robot, self).attack(self, opponent)
        return (damage_dealt, attack_name)
