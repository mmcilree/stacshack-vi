class Monster:
    def __init__(self, name, cr, type, alignment, hp, speed, str, dex, con, int, wis, cha):
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
        self.close = 100

    # Measures how "close" you are to a monster
    def closeness(self, str, dex, con, int, wis, cha):
        x = abs(str - self.str) ** 2 + abs(self.dex - dex) ** 2 + abs(self.con - con) ** 2 + abs(
            self.int - int) ** 2 + abs(self.wis - wis) ** 2 + abs(self.con - con) ** 2
        return x

    def __str__(self):
        return self.name
