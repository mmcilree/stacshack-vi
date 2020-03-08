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
        ability1Name = self.abilities[0].monsterName
        ability2Name = self.abilities[1].monsterName
        actionName = self.actions[0].monsterName

        ability1NameSplit = ability1Name.split()
        ability2NameSplit = ability2Name.split()
        actionNameSplit = actionName.split()


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




        if (len(ability1NameSplit)):
            if len(ability1NameSplit) == 2:
                for namePart in ability1NameSplit:
                    abilityRX4 = re.compile(namePart, re.IGNORECASE)
                    abilityRX3 = re.compile("the " + namePart, re.IGNORECASE)
                    abilityRX2 = re.compile(namePart + "'s", re.IGNORECASE)
                    abilityRX1 = re.compile("the " + namePart + "'s", re.IGNORECASE)

                    self.abilities[0].desc = re.sub(abilityRX1, self.name + "'s", self.abilities[0].desc)
                    self.abilities[0].desc = re.sub(abilityRX2, self.name + "'s", self.abilities[0].desc)
                    self.abilities[0].desc = re.sub(abilityRX3, self.name, self.abilities[0].desc)
                    self.abilities[0].desc = re.sub(abilityRX4, self.name, self.abilities[0].desc)

            if len(ability1NameSplit) == 3:
                abilityRX4 = re.compile(ability1NameSplit[0], re.IGNORECASE)
                abilityRX3 = re.compile("the " + ability1NameSplit[0] , re.IGNORECASE)
                abilityRX2 = re.compile(ability1NameSplit[0] + "'s", re.IGNORECASE)
                abilityRX1 = re.compile("the " + ability1NameSplit[0] + "'s", re.IGNORECASE)

                self.abilities[0].desc = re.sub(abilityRX1, self.name + "'s", self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX2, self.name + "'s", self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX3, self.name, self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX4, self.name, self.abilities[0].desc)

                abilityRX4 = re.compile(ability1NameSplit[2], re.IGNORECASE)
                abilityRX3 = re.compile("the " + ability1NameSplit[2], re.IGNORECASE)
                abilityRX2 = re.compile(ability1NameSplit[2] + "'s", re.IGNORECASE)
                abilityRX1= re.compile("the " + ability1NameSplit[2] + "'s", re.IGNORECASE)

                self.abilities[0].desc = re.sub(abilityRX1, self.name, self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX2, self.name, self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX3, self.name, self.abilities[0].desc)
                self.abilities[0].desc = re.sub(abilityRX4, self.name, self.abilities[0].desc)




        if (len(ability2NameSplit)):
            if len(ability2NameSplit) == 2:
                for namePart in ability2NameSplit:
                    abilityRX4 = re.compile(namePart, re.IGNORECASE)
                    abilityRX3 = re.compile("the " + namePart, re.IGNORECASE)
                    abilityRX2 = re.compile(namePart + "'s", re.IGNORECASE)
                    abilityRX1 = re.compile("the " + namePart + "'s", re.IGNORECASE)

                    self.abilities[1].desc = re.sub(abilityRX1, self.name + "'s", self.abilities[1].desc)
                    self.abilities[1].desc = re.sub(abilityRX2, self.name + "'s", self.abilities[1].desc)
                    self.abilities[1].desc = re.sub(abilityRX3, self.name, self.abilities[1].desc)
                    self.abilities[1].desc = re.sub(abilityRX4, self.name, self.abilities[1].desc)

            if len(ability2NameSplit) == 3:
                abilityRX4 = re.compile(ability2NameSplit[0], re.IGNORECASE)
                abilityRX3 = re.compile("the " + ability2NameSplit[0], re.IGNORECASE)
                abilityRX2 = re.compile(ability2NameSplit[0] + "'s",re.IGNORECASE)
                abilityRX1 = re.compile("the " + ability2NameSplit[0] + "'s",re.IGNORECASE)

                self.abilities[1].desc = re.sub(abilityRX1, self.name + "'s", self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX2, self.name + "'s", self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX3, self.name, self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX4, self.name, self.abilities[1].desc)

                abilityRX4 = re.compile(ability2NameSplit[2], re.IGNORECASE)
                abilityRX3 = re.compile("the " + ability2NameSplit[2], re.IGNORECASE)
                abilityRX2 = re.compile(ability2NameSplit[2] + "'s",re.IGNORECASE)
                abilityRX1 = re.compile("the " + ability2NameSplit[2] + "'s", re.IGNORECASE)

                self.abilities[1].desc = re.sub(abilityRX1, self.name + "'s", self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX2, self.name + "'s", self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX3, self.name, self.abilities[1].desc)
                self.abilities[1].desc = re.sub(abilityRX4, self.name, self.abilities[1].desc)




        if (len(actionNameSplit)):
            if len(actionNameSplit) == 2:
                for namePart in actionNameSplit:
                    abilityRX4 = re.compile(namePart, re.IGNORECASE)
                    abilityRX3 = re.compile("the " + namePart, re.IGNORECASE)
                    abilityRX2 = re.compile(namePart + "'s", re.IGNORECASE)
                    abilityRX1 = re.compile("the " + namePart + "'s", re.IGNORECASE)

                    for action in self.actions:
                        action.desc = re.sub(abilityRX1, self.name + "'s", action.desc)
                        action.desc = re.sub(abilityRX2, self.name + "'s", action.desc)
                        action.desc = re.sub(abilityRX3, self.name, action.desc)
                        action.desc = re.sub(abilityRX4, self.name, action.desc)

            if len(actionNameSplit) == 3:
                abilityRX4 = re.compile(actionNameSplit[0], re.IGNORECASE)
                abilityRX3 = re.compile("the " + actionNameSplit[0], re.IGNORECASE)
                abilityRX2 = re.compile(actionNameSplit[0] + "'s", re.IGNORECASE)
                abilityRX1 = re.compile("the " + actionNameSplit[0] + "'s", re.IGNORECASE)

                for action in self.actions:
                    action.desc = re.sub(abilityRX1, self.name + "'s", action.desc)
                    action.desc = re.sub(abilityRX2, self.name + "'s", action.desc)
                    action.desc = re.sub(abilityRX3, self.name, action.desc)
                    action.desc = re.sub(abilityRX4, self.name, action.desc)

                abilityRX4 = re.compile(actionNameSplit[2], re.IGNORECASE)
                abilityRX3 = re.compile("the " + actionNameSplit[2], re.IGNORECASE)
                abilityRX2 = re.compile(actionNameSplit[2] + "'s", re.IGNORECASE)
                abilityRX1= re.compile("the " + actionNameSplit[2] + "'s", re.IGNORECASE)

                for action in self.actions:
                    action.desc = re.sub(abilityRX1, self.name + "'s", action.desc)
                    action.desc = re.sub(abilityRX2, self.name + "'s", action.desc)
                    action.desc = re.sub(abilityRX3, self.name, action.desc)
                    action.desc = re.sub(abilityRX4, self.name, action.desc)

    def fixCr(self):
        self.cr = re.sub("0.125", "1/8", str(self.cr))
        self.cr = re.sub("0.25", "1/4", str(self.cr))
        self.cr = re.sub("0.5", "1/2", str(self.cr))