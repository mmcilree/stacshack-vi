# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog


import cv2
def select_image():
	path = filedialog.askopenfilename()

select_image()