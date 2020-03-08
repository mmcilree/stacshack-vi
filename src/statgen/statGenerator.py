import numpy as np
import json
import math
from .person import Person

MAX_LIMIT = 200
MIN_LIMIT = 0

def main():
    genStats(input("Filename: "))

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
    strength = min(MAX_LIMIT, max(MIN_LIMIT, 4 + (16 / (1 + math.e ** (-2.9 * (person.strDelta - .77))))))
    return round(strength)

def genDexterity(person):
    dexterity = min(MAX_LIMIT, max(MIN_LIMIT, 5 + (16 / (1 + math.e ** (-4 * (person.dexDelta - .77))))))
    return round(dexterity)

def genConstitution(person):
    constitution = min(MAX_LIMIT, max(MIN_LIMIT, 5 + (16 / (1 + math.e ** (9.5 * (person.conDelta - 2.1))))))
    return round(constitution)

def genInteligence(person):
    inteligence = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(inteligence)

def genWisdom(person):
    wisdom = 20 - (math.log(person.conDelta + 1) * 3) ** 4
    return round(wisdom)

def genCharisma(person):
    charisma = min(MAX_LIMIT, max(MIN_LIMIT, 27 - math.log(person.chaDelta * 3) * 12))
    return round(charisma)

if __name__== "__main__":
    main()
