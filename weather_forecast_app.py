import tkinter as tk
from tkinter import messagebox
import requests_cache
import pandas as pd
from retry_requests import retry
import openmeteo_requests

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Function to fetch weather data from Open-Meteo API
def get_weather_data(city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,  # Replace with dynamic latitude based on city
        "longitude": 13.41,  # Replace with dynamic longitude based on city
        "current": "temperature_2m",
        "hourly": "temperature_2m",
        "timezone": "America/Chicago"
    }
    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()

        return f"Current temperature: {current_temperature_2m}°C"
    except Exception as e:
        return f"Error fetching data: {e}"

# Function to handle the button click and update the weather display
def show_weather():
    city = city_entry.get()
    weather_info = get_weather_data(city)
    weather_label.config(text=weather_info)

# Create the GUI window
window = tk.Tk()
window.title("Weather Forecast Application")

# Create input field and button
city_entry = tk.Entry(window, width=30)
city_entry.pack(pady=10)
get_weather_button = tk.Button(window, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=5)

# Create label to display weather information
weather_label = tk.Label(window, text="Enter a city and click 'Get Weather'")
weather_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
