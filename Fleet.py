## Imports
##################################
from Robot import Robot


# Robot container
class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    # Initialize robots
    def create_fleet(self):
        names = ["Bleep     ", "Bloop     ", "Terminator"]
        for i in range(3):
            self.robots.append(Robot(names[i]))
