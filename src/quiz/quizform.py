from tkinter import *
from src import dndmepostquiz

root = Tk()


# note this form is adapted from: https://www.geeksforgeeks.org/python-simple-registration-form-using-tkinter/

def process():
    # where the info gets processed
    # can do q1_ans.get() etc.
    yesOrNo = re.compile(r"(yes|no)", re.IGNORECASE)
    number = re.compile(r"\d+")
    day = re.compile(r"\w+", re.IGNORECASE)

    p1 = (yesOrNo.match(q1_ans.get()))
    p2 = (yesOrNo.match(q2_ans.get()))
    p3 = (yesOrNo.match(q3_ans.get()))
    p4 = (yesOrNo.match(q4_ans.get()))
    p5 = (number.match(q5_ans.get()))
    p6 = (day.match(q6_ans.get()))
    p7 = (yesOrNo.match(q7_ans.get()))
    p8 = (yesOrNo.match(q8_ans.get()))
    p9 = (number.match(q9_ans.get()))
    p10 = (yesOrNo.match(q10_ans.get()))

    if not (p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9 and p10):
        print("invalid answer given")
        display()

    int = 10
    wis = 10

    if (q1_ans.get().lower().strip()) == "yes":
        int += 2
        print("int added1")
    else:
        int -= 2

    if (q2_ans.get().lower().strip()) == "yes":
        int -= 2
    else:
        int += 2
        print("int added2")


    if (q3_ans.get().lower().strip()) == "yes":
        int += 2
        print("int added3")
    else:
        int -= 2

    if (q4_ans.get().lower().strip()) == "yes":
        wis += 2
        print("wis added4")

    else:
        wis -= 2

    if (q5_ans.get().lower().strip()) == "28":
        int += 2
        print("int added5")

    else:
        int -= 2

    if (q6_ans.get().lower().strip()) == "tuesday":
        int += 2
        print("int added6")

    else:
        int -= 2

    if (q7_ans.get().lower().strip()) == "yes":
        wis -= 2
    else:
        wis += 2
        print("wis added7")


    if (q8_ans.get().lower().strip()) == "yes":
        wis += 2
        print("wis added8")
    else:
        wis -= 2

    if (q9_ans.get().lower().strip()) == "5":
        wis += 2
        print("wis added9")
    else:
        wis -= 2

    if (q10_ans.get().lower().strip()) == "yes":
        wis -= 2
    else:
        wis += 2
        print("wis added10")

    print("THE VALUES ARE {0} {1}".format(int, wis))

    # write all json
    root.destroy()
    dndmepostquiz.postQuiz(int, wis)


def focus1(event):
    q1_ans.focus_set()


# Function to set focus
def focus2(event):
    q2_ans.focus_set()


# Function to set focus
def focus3(event):
    q3_ans.focus_set()


# Function to set focus
def focus4(event):
    q4_ans.focus_set()


# Function to set focus
def focus5(event):
    q5_ans.focus_set()


# Function to set focus
def focus6(event):
    q6_ans.focus_set()


# Function to set focus
def focus7(event):
    q7_ans.focus_set()


# Function to set focus
def focus8(event):
    q8_ans.focus_set()


# Function to set focus
def focus9(event):
    q9_ans.focus_set()


# Function to set focus
def focus10(event):
    q10_ans.focus_set()


def display():
    global q1_ans, q2_ans, q3_ans, q4_ans, q5_ans, q6_ans, q7_ans, q8_ans, q9_ans, q10_ans
    # root.withdraw()
    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("Quick Quiz")
    # set the configuration of GUI window
    root.geometry("900x300")
    # create the labels for the inputs
    heading = Label(root, text="Form", bg="light green")
    q1 = Label(root, text="Do you speak two or more langauges?", bg="light green")
    q2 = Label(root, text="Do you often get lost in places you have been before?", bg="light green")
    q3 = Label(root, text="Do you know the date of all saints day?", bg="light green")
    q4 = Label(root, text="is a pepper a fruit?", bg="light green")
    q5 = Label(root, text="1,5,6,11,17 - what is the missing number?", bg="light green")
    q6 = Label(root, text="if it is Monday today, what day will it be in 50 days?", bg="light green")
    q7 = Label(root, text="WITHOUT looking back, was question 1 about places you have never been before?", bg="light green")
    q8 = Label(root, text="Do you know how to treat a burn?", bg="light green")
    q9 = Label(root, text="How many swords are drawn in the Honey building?", bg="light green")
    q10 = Label(root, text="Do you often make impulsive decisions?", bg="light green")
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    q1.grid(row=1, column=0)
    q2.grid(row=2, column=0)
    q3.grid(row=3, column=0)
    q4.grid(row=4, column=0)
    q5.grid(row=5, column=0)
    q6.grid(row=6, column=0)
    q7.grid(row=7, column=0)
    q8.grid(row=8, column=0)
    q9.grid(row=9, column=0)
    q10.grid(row=10, column=0)
    # create a text entry box
    # for typing the information
    q1_ans = Entry(root)
    q2_ans = Entry(root)
    q3_ans = Entry(root)
    q4_ans = Entry(root)
    q5_ans = Entry(root)
    q6_ans = Entry(root)
    q7_ans = Entry(root)
    q8_ans = Entry(root)
    q9_ans = Entry(root)
    q10_ans = Entry(root)
    # bind method of widget is used for
    # the binding the function with the events
    # whenever the enter key is pressed
    # then call the focus1 function
    q1_ans.bind("<Return>", focus1)
    # whenever the enter key is pressed
    # then call the focus2 function
    q2_ans.bind("<Return>", focus2)
    # whenever the enter key is pressed
    # then call the focus3 function
    q3_ans.bind("<Return>", focus3)
    # whenever the enter key is pressed
    # then call the focus4 function
    q4_ans.bind("<Return>", focus4)
    # whenever the enter key is pressed
    # then call the focus5 function
    q5_ans.bind("<Return>", focus5)
    # whenever the enter key is pressed
    # then call the focus6 function
    q6_ans.bind("<Return>", focus6)
    # whenever the enter key is pressed
    # then call the focus7 function
    q7_ans.bind("<Return>", focus7)
    # whenever the enter key is pressed
    # then call the focus8 function
    q8_ans.bind("<Return>", focus8)
    # whenever the enter key is pressed
    # then call the focus9 function
    q9_ans.bind("<Return>", focus9)
    # whenever the enter key is pressed
    # then call the focus10 function
    q10_ans.bind("<Return>", focus10)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    q1_ans.grid(row=1, column=1, ipadx="100")
    q2_ans.grid(row=2, column=1, ipadx="100")
    q3_ans.grid(row=3, column=1, ipadx="100")
    q4_ans.grid(row=4, column=1, ipadx="100")
    q5_ans.grid(row=5, column=1, ipadx="100")
    q6_ans.grid(row=6, column=1, ipadx="100")
    q7_ans.grid(row=7, column=1, ipadx="100")
    q8_ans.grid(row=8, column=1, ipadx="100")
    q9_ans.grid(row=9, column=1, ipadx="100")
    q10_ans.grid(row=10, column=1, ipadx="100")
    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=process)
    submit.grid(row=11, column=1)  # if q7 uncommented should be row=8

    root.mainloop()
