# import the necessary packages
import argparse
import cv2
import numpy as np
import signal
import json
import math

def box_area(x1, y1, x2,y2):
    return abs(y1-y2)*abs(x2-x1)

def make_measurements(frontpath, sidepath, name):
    img = cv2.imread(frontpath)

    scale_percent = 20  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    mask = make_mask(img)

    scale_percent = 20  # percent of original size
    width = int(mask.shape[1] * scale_percent / 100)
    height = int(mask.shape[0] * scale_percent / 100)
    print(str(width) + ", " + str(height))
    i = height
    while(i > 0):
        j = width
        while(mask[j, i] == 0):
            j -= 1
        cv2.circle(img, (j, i), 10, (0, 255-i, 0), 2)
        print("End: " + str(i) + ", " + str(j))

        show_progress(img)
        i-=1
    cv2.waitKey(0)

def make_mask(img):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())





    show_progress(img)
    # cv2.waitKey(0)
    # ret,img = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
    # cv2.waitKey(500)
    show_progress(img)

    boxes, weights = hog.detectMultiScale(img, winStride=(1, 1))

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    largest_area = 0
    largest_index = 0
    curr_index = 0

    for (x1, y1, x2, y2) in boxes:
        if (box_area(x1, y1, x2, y2) > largest_area):
            largest_area = box_area(x1, y1, x2, y2)
            largest_index = curr_index
        curr_index += 1

    print(boxes)

    # for (xA, yA, xB, yB) in boxes:
    # display the detected boxes in the colour picture
    #   cv2.rectangle(img, (xA, yA), (xB, yB),(0, 255, 0), 2)

    # Get largest box
    x1 = boxes[largest_index][0]
    y1 = boxes[largest_index][1]
    x2 = boxes[largest_index][2]
    y2 = boxes[largest_index][3]

    show_progress(img)

    img = img[y1:y2, x1:x2]  # Crop based on largest box

    show_progress(img)
    # img[:, :, 0] = 0
    show_progress(img)

    # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # make greyscale

    height, width, other = img.shape
    img = img[0:height, 0:int(width / 2)]
    img = np.concatenate((img, np.fliplr(img)), 1)

    lower_blue = np.array([100, 0, 0])  ##[R value, G value, B value]
    upper_blue = np.array([255, 130, 110])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    show_progress(mask)

    mask = mask[0:height, 0:int(width / 2)]
    # masked = cv2.line(masked, (int(width/2),0), (int(width/2), height), (255, 255, 255), thickness=5)
    # edges = cv2.bitwise_not(edges)
    return mask

def show_progress(img):
    cv2.imshow("Analysing...", img)

#make_measurements("../../raw_reference_images/carson_front1.JPG", "", "Carson")
make_measurements("../../raw_reference_images/ben_front6.JPG", "", "Ben")
#make_measurements("../../raw_reference_images/matthew_front1.JPG", "", "Matthew")



'''def rip():
    # img = cv2.rectangle(img, (0, height), (width, int(height / 13) * 11), (0, 0, 0), -1)

    # show_progress(img)
    # cv2.waitKey(0)

    edges = cv2.Canny(img, 100, 200)
    edges = cv2.dilate(edges, (8, 8), iterations=5)
    edges = cv2.filter2D(edges, -1, (20, 20))
    # show_progress(edges)
    # cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(edges,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    # contours.append([int(width/2),0])
    # contours.append([int(width / 2), height])
    masked = np.zeros(img.shape)

    cv2.fillPoly(masked, pts=contours, color=(255, 0, 0))'''