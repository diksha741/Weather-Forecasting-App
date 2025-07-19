import requests
import tkinter as tk  #python module that helps with the GUI
from tkinter import messagebox #module that creates pop-up dialog boxes for user interaction
from datetime import datetime

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a valid city name.")
        return 
    api_key = "828e7e500e6476d88bfdbd818e9b25dc"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout = 5) #add timeout
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            wind_direction = data["wind"].get("deg", "N/A")  # Optional: Wind direction in degrees
            visibility = data.get("visibility", "N/A")  # Optional: Visibility in meters
            weather_description = data["weather"][0]["description"]
            sunrise = data["sys"]["sunrise"]  # Unix timestamp (optional)
            sunset = data["sys"]["sunset"]    # Unix timestamp (optional)
            sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
            sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')
            result_label.config(
                text=f"🌡️Temperature:{temp}°C (Feels like: {feels_like}°C)\n"f"💧Humidity:{humidity}%\n"f"🌀Pressure:{pressure} hPa \n" f"🌬️Wind:{wind_speed} m/s (Direction:{wind_direction}°) \n" f"👀Visibility:{visibility} meters \n" f"☁️Weather:{weather_description.capitalize()} \n" f"🌅Sunrise:{sunrise} (UTC)\n" f"🌇Sunset:{sunset} (UTC) \n",font=("Arial", 10)
            )
            
        else:
            messagebox.showerror(f"ERROR" , f"CITY {city} NOT FOUND")
    
    except Exception as e:
        messagebox.showerror(f"ERROR", f"SOMETHING WENT WRONG \n {e}")



# **********GUI setup****************
windowscreen = tk.Tk()
windowscreen.title("🌦 Weather Forecast App")
windowscreen.geometry("800x600")
windowscreen.configure(bg="#e6f9ff")


#***********Input Frame**************
input_frame = tk.Frame(windowscreen,bg = "#e6f9ff")
input_frame.pack(pady = 20)


#***********City Input***************
city_label = tk.Label(windowscreen,text = "enter the name of city",bg = "#e6f7ff")
city_label.pack(side = tk.LEFT)
city_entry = tk.Entry(windowscreen, width = 40,font=("Arial",12))
city_entry.pack(side = tk.LEFT , padx  = 10)


#***********Get Weather Button*******
get_weather_botton = tk.Button(windowscreen,text = "click here to check the weather conditions" , command = get_weather , bg = "#3399ff" , fg = "Black")
get_weather_botton.pack(pady = 15)


#***********Result Display***********
result_label = tk.Label(windowscreen , text = "" , bg = "#e6f7ff" ,  font=("Arial", 12))
result_label.pack(pady = 10)


#***********Run the app*************
windowscreen.resizable(False,False)
windowscreen.mainloop()
