## Import
###############################
from Fleet import Fleet
from Herd import Herd
import os



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
        options += "             Type in the name of your selected opponent:"
        print(options)

    # Get and display only the valid opponents for robots (dinosaurs)
    def show_robo_opponent_options(self):
        valid_targets = [dinosaur.name for dinosaur in self.herd.dinosaurs if dinosaur.health > 0]
        options = "               ***************************************\n"
        options += "               ***         SELECT OPPONENT         ***\n"
        for target in valid_targets:
            options += f"               ***              {target}               ***\n"
        options += "               ***************************************\n"
        options += "             Type in the name of your selected opponent:"
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

        reset_option = ""
        reset_option += "               ***************************************\n"
        reset_option += "               ***                                 ***\n"
        reset_option += "               ***            NEW GAME?            ***\n"
        reset_option += "               ***               Y/N               ***\n"
        reset_option += "               ***                                 ***\n"
        reset_option += "               ***************************************\n"
        reset_option += "                                  "

        os.system('cls')
        print(winner_string)

        start_over_selection = input(reset_option)
        if start_over_selection.lower() == 'y':
            self = Battlefield()
        else:
            os.system('cls')
            print("\n\n\nGoodbye, see you again soon!!!\n\n\n")