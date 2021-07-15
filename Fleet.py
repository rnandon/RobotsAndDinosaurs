###        IMPORTS
### ================================
from Combatant_Group import Combatant_Group
from random import randint
from Robot import Robot


# Robot Combatant Group
class Fleet(Combatant_Group):
    def __init__(self, names, weapons, robot_count=3):
        # Make sure there are enough names and weapons to go around
        current_robot_count = robot_count
        if min(len(weapons), len(names)) < robot_count:
            current_robot_count = min(len(weapons), len(names))

        # Get a list of robot combatants to pass to the Combatant Group constructor
        robots = self.create_fleet(names, weapons, current_robot_count)
        super(Combatant_Group, self).__init__(robots)

    ###        METHODS
    ### =========================================================
    def create_fleet(self, names, weapons, robot_count):
        robots = []
        for i in range(robot_count):
            weapon = weapons.pop(randint(0, len(weapons) - 1))
            name = names.pop(randint(0, len(names) - 1))
            current_robot = Robot(name, weapon)
            robots.append(current_robot)

        return robots
