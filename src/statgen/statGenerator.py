import numpy as np
import json
import math
from person import Person

def main():
    genStats()

def genStats():
    filename = "../JSON/" + input("Enter JSON file: ") + ".json"

    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')

    stats = json.loads(data)

    print(stats)
    person = Person(stats)

    print(str(person))

    STR = genStrength(person)
    CON = genConstitution(person)
    print(STR, CON)

def genStrength(person):
    strength = max(4, math.log(person.strDelta ** 2 * 30 + 10) * 5 - 5)
    return round(strength)

def genDexterity(person):
    dexterity = 20 - (math.log(person.dexDelta + 1) * 3) ** 4
    return round(dexterity)

def genConstitution(person):
    constitution = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(constitution)

def genCharisma(person):
    strength = min(20, 30 - math.log(person.chrDelta * 10 - 5) * 8)
    return round(strength)

if __name__== "__main__":
    main()
