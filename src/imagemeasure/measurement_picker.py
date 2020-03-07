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


def make_measurements(frontpath, sidepath, name):
    global image, currentWindow, clone
    # load the image, clone it, and setup the mouse callback function

    front_measurements = {"height" : "Trace across full height",
                    "waist": "Trace across waist width",
                    "shoulders": "Trace across shoulder with",
                    "neck": "Trace across neck width",
                    "chest": "Trace across chest width",
                    "thigh": "Trace across thigh width",
                    "torso":"Trace across torso width"}

    side_measurements = { "coreDepth": "Trace across core width",
                          "bicep": "Trace across bicep width",
                          "forearm": "Trace across forearm width",
                          "calf": "Trace across calf width",
                          "thighDepth": "Trace across thigh width",
                          "gluteDepth": "Trace across glute width",
                          "chest": "Trace across chest width",
                          "neckNape": "",
                           }

    posture_measurements = {
        "shoulderBlades": "Select shoulder blade point",
        "backSmall": "Select inward curve of back point",
        "tailbone": "Select base of back point"
    }

    f = open("../JSON/" + name + ".json", "w")
    f.write("{")

    f.write("  \"name\": " + "\"" + name + "\",\n")

    image = cv2.imread(frontpath)
    scale_percent = 20  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    measure_image(f, front_measurements)

    image = cv2.imread(sidepath)
    scale_percent = 20  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    f.write(",\n")

    measure_image(f, side_measurements)

    select_points(f, posture_measurements)
    f.write("}")
    f.close()


def measure_image(f, front_measurements):
    global currentWindow, clone, image
    for current_measure in front_measurements.keys():
        currentWindow = front_measurements.get(current_measure) + ": 'c' to continue"
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

        line_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if (current_measure != "height" and current_measure != "shoulderDepth"):
            f.write(",\n")

        f.write("  \"" + current_measure + "\"" + ": " + str(line_length))

        # close all open windows
        cv2.destroyAllWindows()

def select_points(f, posture_measurements):
    global currentWindow, clone, image
    for current_measure in front_measurements.keys():
        currentWindow = front_measurements.get(current_measure) + ": 'c' to continue"
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

        line_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if (current_measure != "height" and current_measure != "shoulderDepth"):
            f.write(",\n")

        f.write("  \"" + current_measure + "\"" + ": " + str(line_length))

        # close all open windows
        cv2.destroyAllWindows()