class Weapon:
    def __init__(self, name, damage, ignoring_armor=False):
        self.name = name
        self.damage = damage
        self.ignoring_armor = ignoring_armor
        # название : урон
        self.weapon_lib = {
            "Меч": 5,
            "Булава": 4,
            "Посох": 3}

    def get_damage(self):
        return self.damage

    def get_ignoring_armor(self):
        return self.ignoring_armor
