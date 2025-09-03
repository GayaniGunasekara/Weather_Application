from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("Weather App")
root.geometry("00x600+250+100")
root.resizable(False, False)

root.mainloop()
