## Imports
########################################################
import os


## Classes
########################################################

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.winner = None
        self.display_welcome()

    def run_game(self):
        while self.winner == None:
            self.battle()

    def display_welcome(self):
        os.system('cls')
        welcome_string = '''
*********************************************************************
***                                                               ***
*********************************************************************
***                                                               ***
***                                                               ***
***                           WELCOME TO                          ***
***                             ROBOTS                            ***
***                               VS.                             ***
***                            DINOSAURS                          ***
***                                                               ***
***                                                               ***
*********************************************************************
*********************************************************************'''
        print(welcome_string)

        options = '''
               ***************************************
               ***     ARE YOU READY TO BEGIN?     ***
               ***              Y/N                ***
               ***************************************
                                 '''
        user_choice = input(options)
        if (user_choice.lower() == "y"):
            self.run_game()
        else:
            exit()

    def display_game_screen(self):
        # Formats a standard menu to view the current state of the battle
        # Example Output:
        # ROBOT: NAME
        #  HEALTH: 100   POWER: 100
        game_screen = f'''
*********************************************************************
***                          BATTLEFIELD                          ***
*********************************************************************
***            ROBOTS            ||           DINOSAURS           ***
*** **************************** || ***************************** ***
***  ROBOT: {self.fleet.robots[0].name}           ||   DINOSAUR: {self.herd.dinosaurs[0].name}              ***
***   HEALTH: {self.fleet.robots[0].get_health()}   POWER: {self.fleet.robots[0].get_power()}   ||    HEALTH: {self.herd.dinosaurs[0].get_health()}   ENERGY: {self.herd.dinosaurs[0].get_energy()}  ***
***  ROBOT: {self.fleet.robots[1].name}           ||   DINOSAUR: {self.herd.dinosaurs[1].name}              ***
***   HEALTH: {self.fleet.robots[1].get_health()}   POWER: {self.fleet.robots[1].get_power()}   ||    HEALTH: {self.herd.dinosaurs[1].get_health()}   ENERGY: {self.herd.dinosaurs[1].get_energy()}  ***
***  ROBOT: {self.fleet.robots[2].name}           ||   DINOSAUR: {self.herd.dinosaurs[2].name}              ***
***   HEATLH: {self.fleet.robots[2].get_health()}   POWER: {self.fleet.robots[2].get_power()}   ||    HEALTH: {self.herd.dinosaurs[2].get_health()}   ENERGY: {self.herd.dinosaurs[2].get_energy()}  ***
***                              ||                               ***
*********************************************************************
*********************************************************************'''
        os.system('cls')
        print(game_screen)


    def battle(self):
        valid_robots = [robot for robot in self.fleet.robots if robot.health > 0]
        valid_dinosaurs = [dinosaur for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]

        for robot in valid_robots:
            self.display_game_screen()
            self.robo_turn(robot)
            valid_dinosaurs = [dinosaur for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
            if len(valid_dinosaurs) == 0:
                self.winner = "Robots"

        for dino in valid_dinosaurs:
            self.display_game_screen()
            self.dino_turn(dino)
            valid_robots = [robot for robot in self.fleet.robots if robot.health > 0]
            if len(valid_robots) == 0:
                self.winnner = "Dinosaurs"

    def dino_turn(self, dinosaur):
        valid_robots = [robot.name.rstrip() for robot in self.fleet.robots if robot.health > 0]
        self.show_dino_opponent_options()
        valid_selection = False
        while not valid_selection:
            opponent_selection = input("                              ")
            if opponent_selection in valid_robots:
                valid_selection = True
        
        robot = [robot for robot in self.fleet.robots if robot.name.rstrip() == opponent_selection]
        dinosaur.attack(robot[0])


    def robo_turn(self, robot):
        valid_dinosaurs = [dinosaur.name.rstrip() for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
        self.show_robo_opponent_options()
        valid_selection = False
        while not valid_selection:
            opponent_selection = input("                              ")
            if opponent_selection in valid_dinosaurs:
                valid_selection = True

        dinosaur = [dinosaur for dinosaur in self.herd.dinosaurs if dinosaur.name.rstrip() == opponent_selection]
        robot.attack(dinosaur[0])

    def show_dino_opponent_options(self):
        valid_targets = [robot.name for robot in self.fleet.robots if robot.health > 0]
        options = "               ***************************************\n"
        options += "               ***         SELECT OPPONENT         ***\n"
        for target in valid_targets:
            options += f"               ***            {target}           ***\n"
        options += "               ***************************************\n"
        print(options)

    def show_robo_opponent_options(self):
        valid_targets = [dinosaur.name for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
        options = "               ***************************************\n"
        options += "               ***         SELECT OPPONENT         ***\n"
        for target in valid_targets:
            options += f"               ***              {target}               ***\n"
        options += "               ***************************************\n"
        print(options)

    def display_winners(self):
        pass

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        names = ["Bleep     ", "Bloop     ", "Terminator"]
        for i in range(3):
            self.robots.append(Robot(names[i]))


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        names = ["Grr ", "Gar ", "Bill"]
        for i in range(3):
            self.dinosaurs.append(Dinosaur(names[i], 5))

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 100
        self.weapon = Weapon("weapon name", 5)

    def attack(self, dinosaur):
        if self.power >= 10:
            dinosaur.health -= self.weapon.attack_power
            self.power -= 10
        else:
            # Not enough power to attack... What to do?
            pass

    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    def get_power(self):
        if self.power > 99:
            return f'{self.power}'
        if self.power > 9:
            return f'{self.power} '
        if self.power <= 9:
            return f'{self.power}  '


class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 100

    def attack(self, robot):
        if self.energy >= 10:
            robot.health -= self.attack_power
            self.energy -= 10
        else:
            # Not enough energy to attack... What to do?
            pass

    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    def get_energy(self):
        if self.energy > 99:
            return f'{self.energy}'
        if self.energy > 9:
            return f'{self.energy} '
        if self.energy <= 9:
            return f'{self.energy}  '

battlefield = Battlefield()