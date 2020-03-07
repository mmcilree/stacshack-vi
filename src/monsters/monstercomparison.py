import json
from monsters.monster import *
from monsters.monsterability import *
from monsters.generatestatblockhtml import *

from random import seed
from random import random

import math

JSON_FILE = "../monster_resources/5e-SRD-Monsters.json"
ACTION_NUMBER = 2
SPECIAL_ABILITY_NUMBER = 1


def loadFile():
    f = open(JSON_FILE, "r")
    contents = f.read()
    jsonContents = json.loads(contents)

    monsters = []
    for x in jsonContents:

        # print(x)
        if not "name" in x:
            continue


        if "special_abilities" in x:
            abilities = x["special_abilities"]
        else:
            abilities = []

        if "actions" in x:
            actions = x["actions"]
        else:
            actions = []

        parsedAbilities = []
        parsedActions = []

        for y in abilities:
            parsedAbilities.append(Ability(x["name"], y["name"], y["desc"]))

        for y in actions:
            parsedActions.append(Ability(x["name"], y["name"], y["desc"]))

        temp = Monster(x["name"], x["challenge_rating"], x["type"], x["alignment"], x["hit_points"], x["speed"],
                       x["strength"], x["dexterity"], x["constitution"], x["intelligence"], x["wisdom"], x["charisma"],
                       x["senses"], x["armor_class"], parsedAbilities, parsedActions)

        monsters.append(temp)

    f.close()
    return monsters


def getMonsters(str, dex, con, int, wis, cha):
    monsters = loadFile()

    fiveClosest = []

    for x in monsters:
        if len(fiveClosest) < 5:
            fiveClosest.append(x)

        fiveClosest = sorted(fiveClosest, key=lambda x: x.close)
        x.close = x.closeness(str, dex, con, int, wis, cha)
        for i in fiveClosest:
            if x.closeness(str, dex, con, int, wis, cha) < i.close:
                fiveClosest[fiveClosest.index(i)] = x
                break

    return fiveClosest


def makeMonster(name, str, dex, con, intelligence, wis, cha):
    fiveClosest = getMonsters(str, dex, con, intelligence, wis, cha)

    hashed = 0
    for i in range(0, len(name)):
        hashed += ord(name[i])


    seed(hashed)

    cr = 0
    for i in fiveClosest:
        cr = cr + eval(i.cr)
    cr = math.floor(cr / 5)

    type = "Humanoid"

    #TODO change
    alignment = "Neutral"

    hp = 0
    for i in fiveClosest:
        hp = hp + int(i.hp)
    hp = math.floor(hp / 5)

    rand = math.floor(random() * 5)
    speed = fiveClosest[rand].speed

    rand = math.floor(random() * 5)

    print(fiveClosest[rand])
    senses = fiveClosest[rand].senses

    ac = 0
    for i in fiveClosest:
        ac = ac + int(i.ac)
    ac = math.floor(ac / 5)

    #TODO what if none of these? What if the same ability twice?
    rand = math.floor(random() * 5)
    abilities = fiveClosest[rand].abilities

    rand = math.floor(random() * 5)
    rand2 = math.floor(random() * float(len(abilities)))
    print(fiveClosest[rand])

    while len(fiveClosest[rand].abilities) == 0:
        rand = math.floor(random() * 5)
        rand2 = math.floor(random() * float(len(abilities)))
        abilities = fiveClosest[rand].abilities

    ability1 = abilities[rand2]

    rand = math.floor(random() * 5)
    abilities = fiveClosest[rand].abilities

    rand = math.floor(random() * 5)
    rand2 = math.floor(random() * float(len(abilities)))
    print(fiveClosest[rand])

    while len(fiveClosest[rand].abilities) == 0:
        rand = math.floor(random() * 5)
        rand2 = math.floor(random() * float(len(abilities)))
        abilities = fiveClosest[rand].abilities

    ability2 = abilities[rand2]

    rand = math.floor(random() * 5)
    actions = fiveClosest[rand].actions

    rand = math.floor(random() * 5)
    rand2 = math.floor(random() * float(len(actions)))
    print(fiveClosest[rand])

    while len(fiveClosest[rand].actions) == 0:
        rand = math.floor(random() * 5)
        rand2 = math.floor(random() * float(len(actions)))
        actions = fiveClosest[rand].actions

    action = actions[rand2]
    print(action)

    allAbilities = [ability1, ability2]
    allActions = [action]

    result = Monster(name, cr, type, alignment, hp, speed, str, dex, con, intelligence, wis, cha, senses, ac, allAbilities, allActions)
    result.fixActions()
    return result

def makeMonster(name, str, dex, con, int, wis, cha):
    me = makeMonster()
    generate_file(me)