# -------------------- Import Required Libraries -------------------- #

from datetime import datetime, timedelta
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

# Set the background color of the app
root.configure(bg="white")

# ..................function


def getWeather():
    city = textfield.get().strip()  # Get city from input

    api_key = "d669a7a9aebf192cebc3a8efdd70385a"  # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,        # City name
        "appid": api_key,  # Your API key
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        json_data = response.json()

        if response.status_code == 200:
            # --- Weather Info ---
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'])
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            # --- Time Info ---
            timezone_offset = json_data["timezone"]  # seconds offset from UTC
            utc_time = datetime.utcnow()
            local_time = utc_time + timedelta(seconds=timezone_offset)
            current_time = local_time.strftime("%I:%M %p")

            # --- Update UI ---
            clock.config(text=current_time)          # Show local time
            name.config(text="CURRENT WEATHER")      # Show label

            t.config(text=f"{temp}°")                 # Big temperature
            # Condition text
            c.config(text=f"{condition} | FEELS LIKE {temp}°")
            w.config(text=f"{wind}")                  # Wind
            h.config(text=f"{humidity}")              # Humidity
            d.config(text=f"{description}")           # Description
            p.config(text=f"{pressure}")              # Pressure

        else:
            messagebox.showerror("Error", f"City not found: {city}")

    except Exception as e:
        messagebox.showerror("Error", f"Could not get weather: {e}")


# -------------------- Search Bar-------------------- #
# -------------------- Search Bar Background -------------------- #
# Open the background image for the search bar
img = Image.open("search.png")

# Resize the image (width=300, height=50)
img = img.resize((300, 50))

# Convert resized image into a format Tkinter can use
Search_image = ImageTk.PhotoImage(img)

# Place the search bar image inside the window
myimage = Label(image=Search_image, bg="white")
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
    bg="#404040",
    command=getWeather
    # Match search bar background color
)

# Place the button inside the search bar (right corner)
myimage_icon.place(x=275, y=32)


# -------------------- Weather Image -------------------- #

# Open the weather image
img_weather = Image.open("weatherImage.jpg")

# Resize the weather image (adjust width=150, height=150 as you like)
img_weather = img_weather.resize((150, 150))

# Convert to Tkinter-compatible image
Weather_image = ImageTk.PhotoImage(img_weather)

# Display the image in a label
# you can set bg to match window
weather_label = Label(root, image=Weather_image, bg="white", border=0)
weather_label.place(x=680, y=20)


# -------------------- Bottom box for displaying weather info -------------------- #

# Open the bottom box image
img_frame = Image.open("box.png")

# Resize the image (adjust width=800, height=100 as needed)
img_frame = img_frame.resize((850, 200))

# Convert resized image into Tkinter-compatible format
Frame_image = ImageTk.PhotoImage(img_frame)

# Create a label to hold the image
Frame_myimage = Label(root, image=Frame_image, bg="white")

# Place it at the bottom with padding
Frame_myimage.pack(padx=5, pady=50, side=BOTTOM)


# time
name = Label(root, font=("arial", 15, 'bold'), bg="white", fg="#4ea0be")
name.place(x=40, y=100)
clock = Label(root, font=("Helvetica", 20), bg="white", fg="#14576f")
clock.place(x=40, y=130)

# labels for displaying the weather info
Label1 = Label(root, text="WIND", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=300)

Label1 = Label(root, text="HUMIDITY", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=250, y=300)

Label1 = Label(root, text="DESCRIPTION", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=430, y=300)

Label1 = Label(root, text="PRESSURE", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=650, y=300)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)


w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=130, y=330)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=330)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=330)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=330)
# -------------------- Run the Application -------------------- #

root.mainloop()   # Keeps the window running until closed
