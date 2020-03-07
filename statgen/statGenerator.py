import numpy as np
import json
import math
from person import Person

def main():
    genStats()

def genStats():
    filename = "JSON/" + input("Enter JSON file: ") + ".json"

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
    strength = 20 - (math.log(person.strDelta + 1) * 3) ** 4
    return round(strength)

def genConstitution(person):
    strength = 20 - (math.log(person.strDelta + 1) * 3) ** 4
    return round(strength)

if __name__== "__main__":
    main()
