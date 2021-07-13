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
            break
        print("closing the game now")

    def display_welcome(self):
        os.system('cls')
        welcome_string = '''
*********************************************************************
*********************************************************************
***                                                               ***
***                           WELCOME TO                          ***
***                             ROBOTS                            ***
***                               VS.                             ***
***                            DINOSAURS                          ***
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

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

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

battlefield = Battlefield()