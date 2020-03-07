import webbrowser
import os

def showstatblock(name):
    os.chdir("..")
    webbrowser.open(os.getcwd() + "/statblocks/" + name + ".html")