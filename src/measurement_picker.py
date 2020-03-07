# import the necessary packages
import argparse
import cv2
import json
import math


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
measuring = False
currentWindow = "Trace Waist: 'r' to reset, 'c' to continue"

def click_and_measure(event, x, y, flags, param):
    global refPt, measuring, currentWindow, image, clones

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        measuring = True

    if event == cv2.EVENT_MOUSEMOVE:
        if  measuring:
            image = clone.copy()
            cv2.line(image, refPt[0], (x,y), (0, 255, 0), 2)
            cv2.imshow(currentWindow, image)

    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        measuring = False
        # draw a line from start to end point
        cv2.line(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow(currentWindow, image)


# load the image, clone it, and setup the mouse callback function
image = cv2.imread("../raw_reference_images/ben_front1.JPG")

scale_percent = 20  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

measurements = ["full height",
                "waist",
                "shoulders",
                "upper arm",
                "neck",
                "chest",
                "calf",
                "forearm",
                "thigh"]

f = open("../JSON/ben.json", "w")
f.write("{")
for current_measure in measurements:
    currentWindow = "Trace across " + current_measure + " width: 'c' to continue"
    clone = image.copy()
    cv2.namedWindow(currentWindow)
    cv2.setMouseCallback(currentWindow, click_and_measure)
    while True:
        # display the image and wait for a keypress
        cv2.imshow(currentWindow, image)
        key = cv2.waitKey(1) & 0xFF

        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
            image = clone.copy()
            break

    # write data
    x1 = refPt[0][0]
    x2 = refPt[1][0]
    y1 = refPt[0][1]
    y2 = refPt[1][1]

    line_length =  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if current_measure != measurements[0]:
        f.write(",\n")

    f.write("\"" + current_measure + "\"" + ": " + str(line_length))

    # close all open windows
    cv2.destroyAllWindows()
f.write("}")
f.close()