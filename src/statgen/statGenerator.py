import numpy as np
import json
import math
from .person import Person

def main():
    genStats()

def genStats(jsonName):
    filename = "../JSON/" + jsonName + ".json"

    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')

    stats = json.loads(data)

    print(stats)
    person = Person(stats)

    print(str(person))

    STR = genStrength(person)
    DEX = genDexterity(person)
    CON = genConstitution(person)
    INT = genInteligence(person)
    WIS = genWisdom(person)
    CHR = genCharisma(person)

    print(STR, DEX, CON, INT, WIS, CHR)
    return [STR, DEX, CON, INT, WIS, CHR]

def genStrength(person):
    strength = min(20, max(4, (person.strDelta - .1) ** .32 * 60 - 47))
    return round(strength)

def genDexterity(person):
    dexterity = min(20, max(4, (person.dexDelta / 3 - .1) ** .32 * 60 - 47))
    return round(dexterity)

def genConstitution(person):
    constitution = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(constitution)

def genInteligence(person):
    inteligence = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(inteligence)

def genWisdom(person):
    wisdom = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(wisdom)

def genCharisma(person):
    charisma = min(20, 30 - math.log(person.chrDelta * 10 - 5) * 8)
    return round(charisma)

if __name__== "__main__":
    main()
