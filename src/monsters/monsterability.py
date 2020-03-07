class Ability:
    def __init__(self, monsterName, name, desc):
        self.monsterName = monsterName
        self.name = name
        self.desc = desc

    def __str__(self):
        return self.name
