# import the necessary packages
import argparse
import cv2
import json
import math
import random
from .initial_form import *

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

def click_and_record(event, x, y, flags, param):
    global refPt, measuring, currentWindow, image, clones

    if event == cv2.EVENT_LBUTTONDOWN:
        image = clone.copy()
        refPt = [(x, y)]
        measuring = True

    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        measuring = False
        # draw a line from start to end point
        cv2.circle(image, refPt[0], 10, (255, 0, 0), 2)
        cv2.imshow(currentWindow, image)

def click_and_crop(event, x, y, flags, param):
    global refPt, measuring, currentWindow, image, clones

    if event == cv2.EVENT_LBUTTONDOWN:
        image = clone.copy()
        refPt = [(x, y)]
        measuring = True

    if event == cv2.EVENT_MOUSEMOVE:
        if measuring:
            image = clone.copy()
            cv2.rectangle(image, refPt[0], (x,y), (0, 0, 255), 2)
            cv2.imshow(currentWindow, image)

    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        measuring = False
        # draw a line from start to end point
        refPt.append((x, y))
        cv2.rectangle(image, refPt[0], (x,y), (0, 0, 255), 2)
        cv2.imshow(currentWindow, image)

def make_measurements(frontpath, sidepath, name):
    global image, currentWindow, clone
    # load the image, clone it, and setup the mouse callback function

    front_measurements = {"height" : "Trace across full height",
                          "neck": "Trace across neck width",
                          "shoulders": "Trace across shoulder with",
                          "chest": "Trace across chest width",
                          "torso": "Trace across torso width",
                          "waist": "Trace across waist width",
                          "thigh": "Trace across thigh width"}

    side_measurements = { "chestDepth": "Trace across chest width",
                           "coreDepth": "Trace across core width",
                          "bicep": "Trace across bicep width",
                          "forearm": "Trace across forearm width",
                          "gluteDepth": "Trace across glute width",
                           "thighDepth": "Trace across thigh width",
                          "calf": "Trace across calf width",
                           }

    posture_measurements = {
        "neckNape": "Select neck nape point",
        "shoulderBlades": "Select shoulder blade point",
        "backSmall": "Select inward curve of back point",
        "tailbone": "Select base of back point"
    }

    f = open("../JSON/" + name + ".json", "w")
    f.write("{")
    with open('../monster_resources/name_expand.json') as g:
        name_expand = json.load(g)
    print(name_expand["starters"][0])
    ##TODO COULD MOVE THIS to Ben's
    new_name = name_expand["starters"][random.randrange(0, len(name_expand["starters"]))] + name + name_expand["enders"][random.randrange(0, len(name_expand["enders"]))]
    print(new_name)
    f.write("  \"name\": " + "\"" + new_name + "\",\n")

    image = cv2.imread(frontpath)
    scale_percent = 20  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    currentWindow = "Drag and select face: 'c' to continue"

    clone = image.copy()
    cv2.namedWindow(currentWindow)
    cv2.setMouseCallback(currentWindow, click_and_crop)
    while True:
        # display the image and wait for a keypress
        cv2.imshow(currentWindow, image)
        key = cv2.waitKey(1) & 0xFF

        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
            image = clone.copy()
            break

    # close all open windows
    cv2.destroyAllWindows()

    print(refPt)
    cropped = image[(refPt[0][1]):(refPt[1][1]), (refPt[0][0]):(refPt[1][0])]

    edges = cv2.Canny(cropped, 100, 200)
    edges = cv2.bitwise_not(edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    combined = cv2.addWeighted(cropped, 0.4, edges, 0.1, 0)

    scale_percent = 180  # percent of original size
    width = int(combined.shape[1] * scale_percent / 100)
    height = int(combined.shape[0] * scale_percent / 100)
    dim = (width, height)
    combined = cv2.resize(combined, dim, interpolation=cv2.INTER_AREA)

    cv2.imwrite('picture.jpg', combined)



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

    return new_name


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

        if (current_measure != "height" and current_measure != "chestDepth"):
            f.write(",\n")

        f.write("  \"" + current_measure + "\"" + ": " + str(line_length))

        # close all open windows
        cv2.destroyAllWindows()

def select_points(f, posture_measurements):
    global currentWindow, clone, image
    for current_measure in posture_measurements.keys():
        print("Got here")
        currentWindow = posture_measurements.get(current_measure) + ": 'c' to continue"
        clone = image.copy()
        cv2.namedWindow(currentWindow)
        cv2.setMouseCallback(currentWindow, click_and_record)
        while True:
            # display the image and wait for a keypress
            cv2.imshow(currentWindow, image)
            key = cv2.waitKey(1) & 0xFF

            # if the 'c' key is pressed, break from the loop
            if key == ord("c"):
                image = clone.copy()
                break

        f.write(",\n")
        # write data
        x1 = refPt[0][0]

        f.write("  \"" + current_measure + "\"" + ": " + str(x1))

        # close all open windows
        cv2.destroyAllWindows()