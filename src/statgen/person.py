class Person:
    def __init__(self, obj):
        self.name = obj["name"]
        self.measure = []
        self.measure.append(obj["height"]) # 0
        self.measure.append(obj["waist"]) # 1
        self.measure.append(obj["shoulders"]) # 2
        self.measure.append(obj["bicep"] * 3.14) # 3
        self.measure.append(obj["neck"] * 3.14) # 4
        self.measure.append(obj["calf"] * 3.14) # 5
        self.measure.append(obj["forearm"] * 3.14) # 6
        self.measure.append(obj["thigh"]) # 7

        self.measure.append(obj["ShoulderDepth"]) # 8
        self.measure.append(obj["CoreDepth"]) # 9
        self.measure.append(obj["HipDepth"]) # 10
        self.measure.append(obj["GluteDepth"]) # 11
        self.measure.append(obj["ThighDepth"]) # 12

        self.measure.append(obj["abdomen"]) # 13

        # self.measure.append(obj["HeadOffset"]) # 13
        # self.measure.append(obj["ShoulderOffset"]) # 13
        # self.measure.append(obj["BackOffset"]) # 13
        # self.measure.append(obj["HipOffset"]) # 13
        # self.measure.append(obj["GluteOffset"]) # 13

        self.generateRatios()
        self.generateRelativeMuscleArea()
        self.generateFastTwitchMuscle()
        self.generateGreekGodRatios()
        self.generateCylinderDelta()

    def generateRatios(self):
        self.ratios = []
        # Greek God Ratios
        # W to H
        self.ratios.append(self.measure[1] * 3.14 / 2 / self.measure[0]) # 0
        # S to W
        self.ratios.append(self.measure[2] / self.measure[1]) # 1
        # A to W
        self.ratios.append(self.measure[3] / self.measure[1]) # 2
        # N to W
        self.ratios.append(self.measure[4] / self.measure[1] / 3.14) # 3
        # C to A
        self.ratios.append(self.measure[5] / self.measure[3]) # 4
        # F to A
        self.ratios.append(self.measure[6] / self.measure[3]) # 5
        # T to W
        self.ratios.append(self.measure[7] / self.measure[1]) # 6

        # Constitution Ratios
        # Shoulders
        self.ratios.append(self.measure[2] / (self.measure[8] * 2)) # 7
        # Core
        self.ratios.append(self.measure[4] / (self.measure[9] / 2)) # 8
        # Waist
        self.ratios.append(self.measure[1] / (self.measure[10])) # 9
        # Glutes
        self.ratios.append(self.measure[7] / (self.measure[11])) # 10
        # Thighs
        self.ratios.append(self.measure[7] / (self.measure[12])) # 11

        # Strength Ratios
        # S to H
        self.ratios.append(self.measure[2] / self.measure[0]) # 12
        # A to H
        self.ratios.append(self.measure[3] / self.measure[0]) # 13
        # N to H
        self.ratios.append(self.measure[4] / self.measure[0]) # 14
        # C to H
        self.ratios.append(self.measure[5] / self.measure[0]) # 15
        # F to H
        self.ratios.append(self.measure[6] / self.measure[0]) # 16
        # T to H
        self.ratios.append(self.measure[7] / self.measure[0]) # 17
        # A to H
        self.ratios.append(self.measure[13] / self.measure[0]) # 18

    def generateRelativeMuscleArea(self):
        self.strDelta = 0
        for i in range(12, 18):
            self.strDelta += self.ratios[i]


    def generateFastTwitchMuscle(self):
        self.dexDelta = 0
        self.dexDelta += self.ratios[12] * 1
        self.dexDelta += self.ratios[13] * 3
        self.dexDelta += self.ratios[15] * 5
        self.dexDelta += self.ratios[16] * 3
        self.dexDelta += self.ratios[18] * 2
        self.dexDelta += self.ratios[0]  * 2
        self.dexDelta -= self.ratios[17] * 3

    def generateGreekGodRatios(self):
        self.ggDelta = []
        self.ggDelta.append(abs(.445 - self.ratios[0]))
        self.ggDelta.append(abs(1.618 - self.ratios[1]))
        self.ggDelta.append(abs(.5 - self.ratios[2]))
        self.ggDelta.append(abs(.5 - self.ratios[3]))
        self.ggDelta.append(abs(.85 - self.ratios[4]))
        self.ggDelta.append(abs(.85 - self.ratios[5]))
        self.ggDelta.append(abs(.75 - self.ratios[6]))

        self.chrDelta = 0
        for i in range(0, len(self.ggDelta)):
            if i < 4 :
                self.chrDelta += self.ggDelta[i]
            else :
                self.chrDelta += self.ggDelta[i] * .5

    def generateCylinderDelta(self):
        self.conDelta = 0
        for i in range(7, 12):
            self.conDelta += abs(1 - self.ratios[i])

    def __str__(self):
        toReturn = ""
        toReturn = self.name + "\n"
        toReturn += "\t" + "Height:    " + str(self.measure[0]) + "\n"
        toReturn += "\t" + "Waist:     " + str(self.measure[1]) + "\n"
        toReturn += "\t" + "Shoulders:  " + str(self.measure[2]) + "\n"
        toReturn += "\t" + "Arms:      " + str(self.measure[3]) + "\n"
        toReturn += "\t" + "Neck:      " + str(self.measure[4]) + "\n"
        toReturn += "\t" + "Calves:    " + str(self.measure[5]) + "\n"
        toReturn += "\t" + "Forearms   " + str(self.measure[6]) + "\n"
        toReturn += "\t" + "Thighs:    " + str(self.measure[7]) + "\n\n"
        toReturn += "\t" + "W / H:     " + str(self.ratios[0]) + "\n"
        toReturn += "\t" + "S / W:     " + str(self.ratios[1]) + "\n"
        toReturn += "\t" + "A / W:     " + str(self.ratios[2]) + "\n"
        toReturn += "\t" + "N / W:     " + str(self.ratios[3]) + "\n"
        toReturn += "\t" + "C / A:     " + str(self.ratios[4]) + "\n"
        toReturn += "\t" + "F / A:     " + str(self.ratios[5]) + "\n"
        toReturn += "\t" + "T / W:     " + str(self.ratios[6]) + "\n\n"
        toReturn += "\t" + "W / H -GG: " + str(self.ggDelta[0]) + "\n"
        toReturn += "\t" + "S / W -GG: " + str(self.ggDelta[1]) + "\n"
        toReturn += "\t" + "A / W -GG: " + str(self.ggDelta[2]) + "\n"
        toReturn += "\t" + "N / W -GG: " + str(self.ggDelta[3]) + "\n"
        toReturn += "\t" + "C / A -GG: " + str(self.ggDelta[4]) + "\n"
        toReturn += "\t" + "F / A -GG: " + str(self.ggDelta[5]) + "\n"
        toReturn += "\t" + "T / W -GG: " + str(self.ggDelta[6]) + "\n\n"
        toReturn += "\t" + "Shoulder Depth: " + str(self.ratios[7]) + "\n"
        toReturn += "\t" + "Core Depth:     " + str(self.ratios[8]) + "\n"
        toReturn += "\t" + "Waist Depth:    " + str(self.ratios[9]) + "\n"
        toReturn += "\t" + "Glute Depth:    " + str(self.ratios[10]) + "\n"
        toReturn += "\t" + "Thigh Depth:    " + str(self.ratios[11]) + "\n\n"
        toReturn += "\tStrength Delta:  " + str(self.strDelta) + "\n"
        toReturn += "\tDexterity Delta: " + str(self.dexDelta) + "\n"
        toReturn += "\tHench Delta:     " + str(self.conDelta) + "\n"
        toReturn += "\tGreek God Delta: " + str(self.chrDelta) + "\n"
        return toReturn
