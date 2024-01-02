# This is a color picker project 
# using tkinter's color chooser tool

#Libraries 
import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor()[1]  # Ask the user to choose a color and get the hex code
    if color:
        color_label.config(foreground=color)  # Set the foreground color of the Label

#Create the main window
root = tk.Tk()
root.title("Color Bear")

#Window dimensions
w = 400 # Width 
h = 300 # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Create a Label widget
color_label = tk.Label(root, text="ʕ•ᴥ•ʔ", font=("Helvitica", 54))
color_label.pack(pady=50)

# Create a button to open the color dialog
color_button = tk.Button(root, text="Change my color", command=pick_color)
color_button.pack()

# Start the Tkinter main loop
root.mainloop()