# Combatant class: parent class for all combatants, implements minimum requirements for each class
class Combatant:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.resource = 100
        self.attack_power = attack_power

    # Deal damage to the selected dinosaur if the robot has enough power
    def attack(self, opponent):
        if self.resource > 10:
            opponent.defend(self)
            self.resource -= 10

    def defend(self, opponent):
        self.health -= opponent.get_attack_power()