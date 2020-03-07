# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter
from tkinter import filedialog, simpledialog


import cv2

def survey():
	root = tkinter.Tk()
	center(root)
	root.withdraw()
	name =  simpledialog.askstring("Welcome to DnD Me:", "Please enter your name:")
	return name

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def select_front_image():
	return filedialog.askopenfilename(initialdir = "../raw_reference_images", title = "Select front view:")

def select_side_image():
	return filedialog.askopenfilename(initialdir = "../raw_reference_images", title = "Select side view:")