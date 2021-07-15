###        IMPORTS
### ================================
from Combatant import Combatant
from random import randint


# Dinosaur. Implementation of the Combatant class
class Dinosaur(Combatant):
    def __init__(self, name, attack_power, energy=100):
        self.attack_names = ("Swipe", "Slash", "Stomp")
        super().__init__(name, attack_power, energy)

    ###        METHODS
    ### ===========================================================
    def attack(self, opponent):
        # Call the combatant attack method, then return damage and attack name for the user interface to use
        attack_name = self.attack_names[randint(0, len(self.attack_names) - 1)]
        damage_dealt = super().attack(opponent)
        return (damage_dealt, attack_name)