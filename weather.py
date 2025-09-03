# -------------------- Import Required Libraries -------------------- #

from tkinter import *                 # Import all tkinter GUI components
# Import tkinter with alias 'tk' (useful for widgets)
import tkinter as tk
# For converting city names ↔ latitude/longitude
from geopy.geocoders import Nominatim
# ttk = styled widgets, messagebox = pop-up alerts
from tkinter import ttk, messagebox
# For finding timezone from latitude/longitude
from timezonefinder import TimezoneFinder
from datetime import datetime         # For handling date and time
# For making API requests (like weather API)
import requests
import pytz                           # For timezone handling with datetime
# Pillow library (for resizing and handling images)
from PIL import Image, ImageTk


# -------------------- Main Window Setup -------------------- #

root = Tk()                                           # Create the main window
root.title("Weather App")                             # Set window title
# Set size (900x500) and position (+300+200)
root.geometry("900x500+300+200")
root.resizable(False, False)                          # Disable window resizing


# -------------------- Search Bar-------------------- #

# -------------------- Search Bar Background -------------------- #

# Open the background image for the search bar
img = Image.open("search.png")

# Resize the image (width=300, height=50)
img = img.resize((300, 50))

# Convert resized image into a format Tkinter can use
Search_image = ImageTk.PhotoImage(img)

# Place the search bar image inside the window
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)


# -------------------- Text Field (User Input) -------------------- #

# Entry widget for typing city name
textfield = tk.Entry(
    root,
    justify="center",                 # Align text to center
    width=15,                         # Width of entry box
    font=("poppins", 13, "bold"),     # Font style
    bg="#404040",                     # Background color
    border=0,                         # No border
    fg="white"                        # Text color
)
textfield.place(x=50, y=40)           # Place it on top of search image
textfield.focus()                     # Cursor auto-focuses here on start


# -------------------- Search Icon Button -------------------- #

# Open the search icon image
icon = Image.open("search_icon.png")

# Resize the search icon (make it smaller to fit inside search bar)
icon = icon.resize((25, 25))

# Convert resized icon into Tkinter-compatible format
Search_icon = ImageTk.PhotoImage(icon)

# Create a button with the search icon
myimage_icon = Button(
    root,
    image=Search_icon,
    borderwidth=0,    # Remove button border
    cursor="hand2",   # Cursor changes to hand when hovered
    bg="#404040"      # Match search bar background color
)

# Place the button inside the search bar (right corner)
myimage_icon.place(x=275, y=32)


# -------------------- Weather Image-------------------- #


# -------------------- Run the Application -------------------- #

root.mainloop()   # Keeps the window running until closed
