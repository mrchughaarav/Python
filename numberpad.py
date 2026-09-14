# Import neccessary libraries
from tkinter import *


# Create window
root = Tk()
root.title("number pad")
root.geometry("250x300")

# Create a frame to organise elements better
frame = Frame(master=root, height = 200, width = 360, bg="#60c3f5")
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]

for i in range(4):
    #Configure rows and columns to resize windows
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=nums[i][j], bg="#60c3f5")
        label.pack(padx=3, pady=3)


root.mainloop()