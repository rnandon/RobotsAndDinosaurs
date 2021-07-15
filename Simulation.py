###        IMPORTS
### ================================
from Battlefield import Battlefield
from User_Interface import User_Interface

class Simulation:
    def __init__(self):
        self.ui = User_Interface()
        self.battlefield = Battlefield(self.ui)
        self.new_game()

    def new_game(self):
        start_over = self.ui.display_restart()
        if start_over == 'y':
            self.battlefield = Battlefield(self.ui)
        else:
            self.ui.display_exit()
