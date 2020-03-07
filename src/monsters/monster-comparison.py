import json
from monsters.monster import *

JSON_FILE = "../monster_resources/5e-SRD-Monsters.json"


def loadFile():
    f = open(JSON_FILE, "r")
    contents = f.read()
    jsonContents = json.loads(contents)

    monsters = []
    closest = []  # R
    for x in jsonContents:

        # print(x)
        if not "name" in x:
            continue

        temp = Monster(x["name"], x["challenge_rating"], x["type"], x["alignment"], x["hit_points"], x["speed"],
                       x["strength"], x["dexterity"], x["constitution"], x["intelligence"], x["wisdom"], x["charisma"])

        monsters.append(temp)

    f.close()
    return monsters


def getMonsters(str, dex, con, int, wis, cha):
    monsters = loadFile()

    fiveClosest = []

    for x in monsters:
        if len(fiveClosest) < 5:
            fiveClosest.append(x)

        fiveClosest = sorted(fiveClosest, key=lambda x : x.close)
        x.close = x.closeness(str, dex, con, int, wis, cha)
        print(x.close)
        for i in fiveClosest:
            if x.closeness(str, dex, con, int, wis, cha) < i.close:
                fiveClosest[fiveClosest.index(i)] = x
                break

    return fiveClosest


def main():
    x = getMonsters(20, 8, 14, 8, 16, 10)
    for i in x:
        print(i)


if __name__ == "__main__":
    main()
