## Import
###############################
from Fleet import Fleet
from Herd import Herd



# Battlefield is the main controller for the game
# It contains the fleet of robots and herd of dinosaurs, and handles the game loop
class Battlefield:
    # Get the fleet and herd initialized and show the welcome screen
    def __init__(self, ui, robot_names, robot_weapons, dinosaur_names):
        self.fleet = Fleet(robot_names, robot_weapons)
        self.herd = Herd(dinosaur_names)
        self.valid_robots = self.fleet.get_valid_combatants()
        self.valid_dinosaurs = self.herd.get_valid_combatants()
        self.winner = None
        self.ui = ui
        start_choice = self.ui.display_welcome(['DINOSAURS', 'VS.', 'ROBOTS'])
        if start_choice == 'y':
            self.run_game()

    # Main game loop
    def run_game(self):
        while self.winner == None:
            self.battle()

        winning_team = None
        if self.winner == "Robots":
            winning_team = self.valid_robots
        else:
            winning_team = self.valid_dinosaurs

        self.ui.display_winners(self.winner, winning_team)

    # The key part of the game loop
    # Checks after each attack that there isn't a winner
    def battle(self):
        for robot in self.valid_robots:
            self.combatant_turn(robot, self.valid_dinosaurs)
            self.valid_dinosaurs = self.herd.get_valid_combatants()
            if len(self.valid_dinosaurs) == 0:
                self.winner = "Robots"
                return

        for dino in self.valid_dinosaurs:
            self.combatant_turn(dino, self.valid_robots)
            self.valid_robots = self.fleet.get_valid_combatants()
            if len(self.valid_robots) == 0:
                self.winner = "Dinosaurs"
                return

    def combatant_turn(self, current_combatant, targets):
        # Show options
        user_opponent_selection = self.ui.display_game_screen("SELECT AN OPPONENT", targets, self.fleet.combatants, self.herd.combatants)

        # Conduct the attack, show user what happened
        attack_response = current_combatant.attack(user_opponent_selection)
        self.ui.display_attack(attack_response[1], attack_response[0], current_combatant, user_opponent_selection)

