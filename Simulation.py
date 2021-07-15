###        IMPORTS
### ================================
from Battlefield import Battlefield
from User_Interface import User_Interface
from Weapon import Weapon
from random import randint

class Simulation:
    def __init__(self):
        self.setup()
        self.new_game()

    def setup(self):
        self.ui = User_Interface()
        robot_names = ['Bleep', 'Bloop', 'Terminator', 'Clank', 'Dalek', 'Hal', 'T-1000', 'Bender', 'Ultron', 'K-2SO', 'Cyberman']
        dinosaur_names = ['Barney', 'Rex', 'Yoshi', 'Blue', 'Charlie', 'Delta', 'Echo', 'Gojira', 'Tiny', 'Tina']
        weapons = self.get_weapons()

        self.battlefield = Battlefield(self.ui, robot_names, weapons, dinosaur_names)

    def new_game(self):
        start_over = self.ui.display_restart()
        if start_over == 'y':
            self.setup()
        else:
            self.ui.display_exit()

    def get_weapons(self):
        weapons = []

        weapons.append(Weapon('Sword', randint(20, 40)))
        weapons.append(Weapon('Axe', randint(15, 45)))
        weapons.append(Weapon('Hammer', randint(22, 43)))
        weapons.append(Weapon('Stuffed Rabbit', randint(10, 50)))
        weapons.append(Weapon('Holy Hand Grenade', randint(50, 75)))
        weapons.append(Weapon('Bow', randint(20, 40)))
        weapons.append(Weapon('Sonic Screwdriver', randint(35, 40)))
        weapons.append(Weapon('Death Ray', randint(60, 90)))
        weapons.append(Weapon('Kids Music', randint(75, 90)))
        weapons.append(Weapon('Hugs', randint(25, 65)))

        return weapons