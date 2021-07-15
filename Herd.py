###        IMPORTS
### ================================
from Combatant_Group import Combatant_Group
from Dinosaur import Dinosaur
from random import randint



# Dinosaur Combatant Group
class Herd(Combatant_Group):
    def __init__(self, names, dinosaur_count=3):
        # Make sure there are enough names to go around
        current_dinosaur_count = dinosaur_count
        if len(names) < current_dinosaur_count:
            current_dinosaur_count = len(names)

        # Get a list of dino combatants to pass to the Combatant Group constructor
        dinosaurs = self.create_herd(names, current_dinosaur_count)
        super(Combatant_Group, self).__init__(dinosaurs)

    ###        METHODS
    ### =========================================================
    def create_herd(self, names, dinosaur_count):
        dinosaurs = []
        for i in range(dinosaur_count):
            name = names.pop(randint(0, len(names) - 1))
            current_attack_power = randint(15, 30)
            current_robot = Dinosaur(name, current_attack_power)
            dinosaurs.append(current_robot)

        return dinosaurs
