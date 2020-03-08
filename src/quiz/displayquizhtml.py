import webbrowser
import os
import cgi

def showquiz():
    os.chdir("..")
    webbrowser.open(os.getcwd() + "/src/quiz/base.html")

def writeresults():
    webbrowser.open(os.getcwd() + "/src/quiz/complete.html")
    form = cgi.FieldStorage()
    print(form)

