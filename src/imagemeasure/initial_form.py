# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter
from tkinter import filedialog, simpledialog, messagebox


import cv2

def survey():
	root = tkinter.Tk()
	center(root)
	root.withdraw()
	name = simpledialog.askstring("Welcome to DnD Me:", "Please enter your name:")
	return name

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 4) - (width // 4)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def select_front_image():
	root = tkinter.Tk()
	center(root)
	root.withdraw()
	return filedialog.askopenfilename(initialdir = "../raw_reference_images", title = "Select front view:")

def select_side_image():
	root = tkinter.Tk()
	center(root)
	root.withdraw()
	return filedialog.askopenfilename(initialdir = "../raw_reference_images", title = "Select side view:")

def complete():
	root = tkinter.Tk()
	center(root)
	root.withdraw()
	return messagebox.askyesno("Sucess:", "You have been reborn as a DnD monster. View your monster card?")