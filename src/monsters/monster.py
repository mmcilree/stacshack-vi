CLOSENESS_MODIFIER = 8
import re
allMonsters = ["Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental", "Fey", "Fiend", "Giant", "Monstrosity", "Ooze", "Plant", "Undead"]


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

    def fixActions(self):
        actionSingular = re.compile("(The)? "+self.actions[0].monsterName, re.IGNORECASE)
        ability1Singular = re.compile("(The)? "+self.abilities[0].monsterName, re.IGNORECASE)
        ability2Singular = re.compile("(The)? "+self.abilities[1].monsterName, re.IGNORECASE)


        action = re.compile("(The)? "+self.actions[0].monsterName+"(s|'s)", re.IGNORECASE)
        ability1 = re.compile("(The)? "+self.abilities[0].monsterName + "(s|'s)", re.IGNORECASE)
        ability2 = re.compile("(The)? "+self.abilities[1].monsterName + "(s|'s)", re.IGNORECASE)

        typeCheckers = []
        for type in allMonsters:
            typeCheckers.append(re.compile("(The)? "+ type + "(s|'s)?", re.IGNORECASE))


        self.actions[0].desc = re.sub(actionSingular, self.name, self.actions[0].desc)
        self.abilities[0].desc = re.sub(ability1Singular, self.name, self.abilities[0].desc)
        self.abilities[1].desc = re.sub(ability2Singular, self.name, self.abilities[1].desc)


        self.actions[0].desc = re.sub(action, self.name+"'s", self.actions[0].desc)
        self.abilities[0].desc = re.sub(ability1, self.name+"'s", self.abilities[0].desc)
        self.abilities[1].desc = re.sub(ability2, self.name+"'s", self.abilities[1].desc)

        for checker in typeCheckers:
            self.actions[0].desc = re.sub(checker, self.name, self.actions[0].desc)
            self.abilities[0].desc = re.sub(checker, self.name, self.abilities[0].desc)
            self.abilities[1].desc = re.sub(checker, self.name, self.abilities[1].desc)