🌦 Weather Application (Python & Tkinter)

A feature-rich, interactive Weather Application built using Python and Tkinter. This app allows users to search for a city and get real-time weather updates, including temperature, humidity, wind speed, pressure, and weather description, along with the local time of the searched city. The app features a user-friendly GUI with a clean, modern design.

🔹 Demo

Watch the live demo on LinkedIn: Weather App Demo

🔹 Features

✅ Search weather by city name 🌍

✅ Displays real-time temperature, humidity, wind speed, pressure, and description 📊

✅ Shows local time of the city ⏰

✅ User-friendly Tkinter GUI with custom images and design 🎨

🔹 Technologies & Libraries Used

Python → Programming language

Tkinter → GUI development

Pillow (PIL) → Image handling and resizing

Requests → API requests to OpenWeatherMap

Geopy → Convert city names to latitude/longitude

TimezoneFinder & pytz → Timezone and local time calculations

OpenWeatherMap API → Fetch live weather data 🌐



🔹 Installation

Clone the repository

git clone <repository-url>
cd <repository-folder>


Install required packages

pip install requests geopy timezonefinder pytz pillow


Run the application

python weather_app.py


Make sure you have your OpenWeatherMap API key and images (search.png, search_icon.png, weatherImage.jpg, box.png) in the project folder.

🔹 Usage

Enter the city name in the search bar.

Click the search button (magnifying glass).

The app will display:

Current temperature

Weather condition & description

Humidity, wind speed, and pressure

Local time of the city

🔹 API

Weather data is fetched from OpenWeatherMap API

Make sure to generate your API key at OpenWeatherMap
 and replace it in the code:

api_key = "YOUR_API_KEY_HERE"

