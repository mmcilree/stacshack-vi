import numpy as np
import json

def main():
    genStats()

def genStats():
    filename = "JSON/" + input("Enter JSON file: ") + ".json"
    print("Reading from: " + filename)

    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')

    print(data)
    print("\n")

    stats = json.loads(data)

    print(stats)

if __name__== "__main__":
    main()
