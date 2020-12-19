class Weapon:
    def __init__(self, name, damage, ignoring_armor):
        self.name = name
        self.damage = damage
        self.ignoring_armor = ignoring_armor

    def get_damage(self):
        return self.damage

    def get_ignoring_armor(self):
        return self.ignoring_armor
