## Imports
######################################
from Dinosaur import Dinosaur
from random import randint



# Dinosaur container
class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    # Initialize dinosaurs
    def create_herd(self):
        names = ["Grr ", "Gar ", "Bill"]
        for i in range(3):
            self.dinosaurs.append(Dinosaur(names[i], randint(20, 35)))
