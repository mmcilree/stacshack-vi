class Person:
    def __init__(self, obj):
        self.name = obj["Name"]
        self.measure = []
        self.measure.append(obj["Height"]) # 0
        self.measure.append(obj["Waist"]) # 1
        self.measure.append(obj["Shoulders"]) # 2
        self.measure.append(obj["Arms"] * 3.14) # 3
        self.measure.append(obj["Neck"] * 3.14) # 4
        self.measure.append(obj["Calves"] * 3.14) # 5
        self.measure.append(obj["Forearms"] * 3.14) # 6
        self.measure.append(obj["Thighs"]) # 7

        self.measure.append(obj["ShoulderDepth"]) # 8
        self.measure.append(obj["CoreDepth"]) # 9
        self.measure.append(obj["HipDepth"]) # 10
        self.measure.append(obj["GluteDepth"]) # 11
        self.measure.append(obj["ThighDepth"]) # 12


        self.generateRatios()
        self.generateGreekGodRatios()
        self.generateCylinderDelta()

    def generateRatios(self):
        self.ratios = []
        # Strength Ratios
        # W to H
        self.ratios.append(self.measure[1] / self.measure[0])
        # S to W
        self.ratios.append(self.measure[2] / self.measure[1])
        # A to W
        self.ratios.append(self.measure[3] / self.measure[1])
        # N to W
        self.ratios.append(self.measure[4] / self.measure[1])
        # C to A
        self.ratios.append(self.measure[5] / self.measure[3])
        # F to A
        self.ratios.append(self.measure[6] / self.measure[3])
        # T to W
        self.ratios.append(self.measure[7] / self.measure[1])

        # Constitution Ratios
        # Shoulders
        self.ratios.append(self.measure[2] / self.measure[8])
        # Core
        self.ratios.append(self.measure[4] / self.measure[9])
        # Waist
        self.ratios.append(self.measure[1] / self.measure[10])
        # Glutes
        self.ratios.append(self.measure[7] / self.measure[11])
        # Thighs
        self.ratios.append(self.measure[7] / self.measure[12])

    def generateGreekGodRatios(self):
        self.ggDelta = []
        self.ggDelta.append(abs(.445 - self.ratios[0]))
        self.ggDelta.append(abs(1.618 - self.ratios[1]))
        self.ggDelta.append(abs(.5 - self.ratios[2]))
        self.ggDelta.append(abs(.5 - self.ratios[3]))
        self.ggDelta.append(abs(.85 - self.ratios[4]))
        self.ggDelta.append(abs(.85 - self.ratios[5]))
        self.ggDelta.append(abs(.75 - self.ratios[6]))

        self.strDelta = 0
        for i in range(0, len(self.ggDelta)):
            if i < 4 :
                self.strDelta += self.ggDelta[i]
            else :
                self.strDelta += self.ggDelta[i] * .5

    def generateCylinderDelta(self):
        self.conDelta = 0
        for i in range(7, len(self.ratios)):
            self.conDelta += abs(1 - self.ratios[i])

    def __str__(self):
        toReturn = ""
        toReturn = self.name + "\n"
        toReturn += "\t" + "Height:    " + str(self.measure[0]) + "\n"
        toReturn += "\t" + "Waist:     " + str(self.measure[1]) + "\n"
        toReturn += "\t" + "Shoulders: " + str(self.measure[2]) + "\n"
        toReturn += "\t" + "Arms:      " + str(self.measure[3]) + "\n"
        toReturn += "\t" + "Neck:      " + str(self.measure[4]) + "\n"
        toReturn += "\t" + "Calves:    " + str(self.measure[5]) + "\n"
        toReturn += "\t" + "Forearms:  " + str(self.measure[6]) + "\n"
        toReturn += "\t" + "Thighs:    " + str(self.measure[7]) + "\n\n"
        toReturn += "\t" + "W / H:     " + str(self.ratios[0]) + "\n"
        toReturn += "\t" + "S / W:     " + str(self.ratios[1]) + "\n"
        toReturn += "\t" + "A / W:     " + str(self.ratios[2]) + "\n"
        toReturn += "\t" + "N / W:     " + str(self.ratios[3]) + "\n"
        toReturn += "\t" + "C / A:     " + str(self.ratios[4]) + "\n"
        toReturn += "\t" + "F / A:     " + str(self.ratios[5]) + "\n"
        toReturn += "\t" + "T / W:     " + str(self.ratios[6]) + "\n\n"
        toReturn += "\t Greek God Delta: " + str(self.strDelta) + "\n"
        toReturn += "\t Hench Delta: " + str(self.strDelta) + "\n"
        return toReturn
