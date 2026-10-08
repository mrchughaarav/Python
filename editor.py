# Import neccessary packages
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Set up root window
window = Tk()
window.title("Codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize = 800, weight = 100)
window.columnconfigure(1, minisize = 800, weight = 100)

# Function to open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes = (["Text files", "*txt"], "All files", ".")
    )
    if not filepath():
        return
    txt_edit.delete(1.0, END)
    # If a file is open display the contents of the file
    with open (filepath, "r") as input_file:
        # Read contents of the input
        text = input_file.read()
        # Insert contents of the file in the editor
        txt_edit.insert(END, text)
        input_file.close()
    window