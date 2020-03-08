from tkinter import *
from src import dndmepostquiz
c
root = Tk()
#note this form is adapted from: https://www.geeksforgeeks.org/python-simple-registration-form-using-tkinter/

def process():
    # where the info gets processed
    # can do q1_ans.get() etc.
    print(q1_ans.get())

    # write all json
    root.destroy()
    dndmepostquiz.postQuiz()


def focus1(event):
    # set focus on the course_field box
    q1_ans.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    q2_ans.focus_set()


# Function to set focus
def focus3(event):
    # set focus on the form_no_field box
    q3_ans.focus_set()


# Function to set focus
def focus4(event):
    # set focus on the contact_no_field box
    q4_ans.focus_set()


# Function to set focus
def focus5(event):
    # set focus on the email_id_field box
    q5_ans.focus_set()


# Function to set focus
def focus6(event):
    # set focus on the address_field box
    q6_ans.focus_set()


def display():
    global q1_ans, q2_ans, q3_ans, q4_ans, q5_ans, q6_ans
    #root.withdraw()
    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("Quick Quiz")
    # set the configuration of GUI window
    root.geometry("500x300")
    heading = Label(root, text="Form", bg="light green")
    q1 = Label(root, text="Insert q1 here", bg="light green")
    q2 = Label(root, text="Insert q2 here", bg="light green")
    q3 = Label(root, text="Insert q3 here", bg="light green")
    q4 = Label(root, text="Insert q4 here", bg="light green")
    q5 = Label(root, text="Insert q5 here", bg="light green")
    q6 = Label(root, text="Insert q6 here", bg="light green")
    q7 = Label(root, text="Insert q7 here", bg="light green")
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
    # create a text entry box
    # for typing the information
    q1_ans = Entry(root)
    q2_ans = Entry(root)
    q3_ans = Entry(root)
    q4_ans = Entry(root)
    q5_ans = Entry(root)
    q6_ans = Entry(root)
    q7_ans = Entry(root)
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
    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=process)
    submit.grid(row=8, column=1)

    root.mainloop()




