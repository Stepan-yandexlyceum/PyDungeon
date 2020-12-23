class Armor:
    def __init__(self, name, health_bonus, protection):
        self.health_bonus = health_bonus
        self.protection = protection
        self.name = name

    def get_health_bonus(self):
        return self.health_bonus

    def get_protection(self):
        return self.protection

    def get_name(self):
        return self.name