# Combatant class: parent class for all combatants, implements minimum requirements for each class
class Combatant:
    def __init__(self, name, attack_power=0):
        self.name = name
        self.health = 100
        self.resource = 100
        self.attack_power = attack_power

    ###        METHODS
    ### =========================================
    def attack(self, opponent):
        if self.resource > 10:
            damage_dealt = opponent.defend(self)
            self.resource -= 10
            return damage_dealt
        else:
            return None

    def defend(self, opponent):
        damage = opponent.get_attack_power()
        self.health -= damage
        return damage

    ###        GETTERS/SETTERS
    ### =========================================
    def get_attack_power(self):
        return self.attack_power

    def set_attack_power(self, attack_power):
        self.attack_power = attack_power