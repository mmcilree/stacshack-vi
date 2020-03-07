CLOSENESS_MODIFIER = 8


class Monster:
    def __init__(self, name, cr, type, alignment, hp, speed, str, dex, con, int, wis, cha, senses, ac, abilities, actions):
        self.name = name
        self.type = type
        self.cr = cr
        self.alignment = alignment
        self.hp = hp
        self.speed = speed
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.senses = senses
        self.close = 100
        self.ac = ac
        self.abilities = abilities
        self.actions = actions

    # Measures how "close" you are to a monster
    def closeness(self, str, dex, con, int, wis, cha):
        x = abs(str - self.str) ** CLOSENESS_MODIFIER + abs(self.dex - dex) ** CLOSENESS_MODIFIER + abs(
            self.con - con) ** CLOSENESS_MODIFIER + abs(
            self.int - int) ** CLOSENESS_MODIFIER + abs(self.wis - wis) ** CLOSENESS_MODIFIER + abs(
            self.con - con) ** CLOSENESS_MODIFIER
        return x

    def __str__(self):
        return self.name
