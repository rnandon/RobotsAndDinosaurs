## Imports
########################################################
import os
import time
from random import randint



## Classes
########################################################

# Battlefield is the main controller for the game
# It contains the fleet of robots and herd of dinosaurs, and handles the game loop
class Battlefield:
    # Get the fleet and herd initialized and show the welcome screen
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.winner = None
        self.display_welcome()

    # Main game loop
    def run_game(self):
        while self.winner == None:
            self.battle()

        self.display_winners()

    # Main splash screen, allows the user to exit the game without starting it
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

    # Formats and prints the main game screen
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

    # The key part of the game loop
    # Checks after each attack that there isn't a winner
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
                self.winner = "Dinosaurs"

    # Allows the user to select a robot to attack, then conducts the attack
    def dino_turn(self, dinosaur):
        # Build out the options
        valid_robots = [robot.name.rstrip().lower() for robot in self.fleet.robots if robot.health > 0]
        self.show_dino_opponent_options()

        valid_selection = False
        while not valid_selection:
            opponent_selection = input("                              ").lower()
            if opponent_selection in valid_robots:
                valid_selection = True
        
        robot = [robot for robot in self.fleet.robots if robot.name.lower().rstrip() == opponent_selection]
        dinosaur.attack(robot[0])

    # Allows the user to select a dinosaur to attack, then conducts the attack
    def robo_turn(self, robot):
        # Build out options
        valid_dinosaurs = [dinosaur.name.rstrip().lower() for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
        self.show_robo_opponent_options()

        valid_selection = False
        while not valid_selection:
            opponent_selection = input("                              ").lower()
            if opponent_selection in valid_dinosaurs:
                valid_selection = True

        dinosaur = [dinosaur for dinosaur in self.herd.dinosaurs if dinosaur.name.rstrip().lower() == opponent_selection]
        robot.attack(dinosaur[0])

    # Get and display only the valid opponents for dinosaurs (robots)
    def show_dino_opponent_options(self):
        valid_targets = [robot.name for robot in self.fleet.robots if robot.health > 0]
        options = "               ***************************************\n"
        options += "               ***         SELECT OPPONENT         ***\n"
        for target in valid_targets:
            options += f"               ***            {target}           ***\n"
        options += "               ***************************************\n"
        print(options)

    # Get and display only the valid opponents for robots (dinosaurs)
    def show_robo_opponent_options(self):
        valid_targets = [dinosaur.name for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
        options = "               ***************************************\n"
        options += "               ***         SELECT OPPONENT         ***\n"
        for target in valid_targets:
            options += f"               ***              {target}               ***\n"
        options += "               ***************************************\n"
        print(options)

    # Format and display the winner page
    def display_winners(self):
        winner_string =  "*********************************************************************\n"
        winner_string += "***                            WINNERS                            ***\n"
        winner_string += "*********************************************************************\n"
        winner_string += "***                                                               ***\n"

        valid_winners = []

        if self.winner == "Dinosaurs":
            valid_winners = [dinosaur.name for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
            for winner in valid_winners:
                winner_string += f'***                             {winner}                              ***\n'
        else:
            valid_winners = [robot.name for robot in self.fleet.robots if robot.health > 0]
            for winner in valid_winners:
                winner_string += f'***                             {winner}                        ***\n'
        
        winner_string += "***                                                               ***\n"
        winner_string += "*********************************************************************\n"

        os.system('cls')
        print(winner_string)



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



# Robot. Basics are the same as the dinosaur, but has a weapon, power instead of energy, and only one kind of attack
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 100
        weapons = [Weapon("Sword", randint(15, 25)), Weapon("Axe", randint(10, 30)), Weapon("Stuffed Rabbit", randint(1, 50))]
        self.weapon = weapons[randint(0, len(weapons)-1)]

    # Deal damage to the selected dinosaur if the robot has enough power
    def attack(self, dinosaur):
        if self.power >= 10:
            dinosaur.health -= self.weapon.attack_power
            self.power -= 10
            print(f"     {self.name.rstrip()} attacks {dinosaur.name} for {self.weapon.attack_power} damage!")
            time.sleep(1)
        else:
            print(f"     {self.name.rstrip()} doesn't have the power to attack!")
            time.sleep(1)

    # Special formatting for health value
    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    # Special formatting for power value
    def get_power(self):
        if self.power > 99:
            return f'{self.power}'
        if self.power > 9:
            return f'{self.power} '
        if self.power <= 9:
            return f'{self.power}  '



# Controls the attack power of the robot
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power



# Dinosaur. Basics are the same as the robot, but it has its own attack power, energy instead of power, and has multiple attacks to choose from 
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 100
        self.attack_names = ("Swipe", "Slash", "Stomp")

    # Deal damage to selected robot if dinosaur has enough energy 
    def attack(self, robot):
        if self.energy >= 10:
            attack = self.attack_names[randint(0, len(self.attack_names) - 1)]
            robot.health -= self.attack_power
            self.energy -= 10
            print(f"     {self.name.rstrip()} attacks {robot.name} with {attack} for {self.attack_power} damage!")
            time.sleep(1)
        else:
            print(f"     {self.name.rstrip()} doesn't have the energy to attack!")
            time.sleep(1)

    # Special formatting for health value
    def get_health(self):
        if self.health > 99:
            return f'{self.health}'
        if self.health > 9:
            return f'{self.health} '
        if self.health <= 9:
            return f'{self.health}  '

    # Special formatting for energy value
    def get_energy(self):
        if self.energy > 99:
            return f'{self.energy}'
        if self.energy > 9:
            return f'{self.energy} '
        if self.energy <= 9:
            return f'{self.energy}  '





## Run the program
###############################################################
battlefield = Battlefield()