import requests
import tkinter as tk  #python module that helps with the GUI
from tkinter import messagebox #module that creates pop-up dialog boxes for user interaction
from datetime import datetime
from PIL import Image,ImageTk #python module that handle images

windowscreen = tk.Tk() #window for the app

#designing a welcome home page for the weather_forecasting_app
def welcome_page():
    bg_image = Image.open("D:/git and github/weather_forcast/weather.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(windowscreen, image = bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_frame = tk.Frame(windowscreen, bg = "#c9e9ff", bd=3, relief=tk.RAISED)
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(welcome_frame, text="Weather App",font=("Arial",16), bg="#87Ceeb").pack(pady=20)

    #taking the input city from the user
    global city_enter
    city_enter= tk.Entry(welcome_frame, font=("Arial",12), width=25)
    city_enter.pack(pady = 10)
    
    #show the "check weather" button
    submit_button = tk.Button(welcome_frame, text="click here to see Weather", command=show_dashboard, bg="#44af72")
    submit_button.pack(pady = 15)

#in order to switch to the next page after clicking the check weather button we need to destroy the first page 
# and build the new page, and for this we use show_dashboard to destroy and build
def show_dashboard():
    global city
    city = city_enter.get().strip()
    if not city:
        messagebox.showerror("Error", f"the city {city} does not exists")
        return
    
    for widget in windowscreen.winfo_children():
        widget.destroy()
    
    build_dashboard()

#code to build the new page
def build_dashboard():
    #left frame
    left_frame = tk.Frame(windowscreen, bg="#B5EAD7")
    left_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    #right frame
    right_frame = tk.Frame(windowscreen, bg="#B5EAD7")
    right_frame.pack(side="right", expand=True, fill="both",padx=10, pady=10)

    #background photo on the left side
    bg_image1 = Image.open("D:/git and github/weather_forcast/sun.png")
    bg_photo1 = ImageTk.PhotoImage(bg_image1)
    bg_label1 = tk.Label(left_frame, image=bg_photo1)
    bg_label1.image = bg_photo1
    bg_label1.place(x=0, y=0, relwidth=1,relheight=1)

    features = ["Temperature", "Humidity", "Pressure","Wind","Visibility","Sunrise-Sunset"]

    for feature in features:
        button = tk.Button(left_frame, text = feature,
                           command = lambda f=feature : showfeature(f,right_frame),
                           width=20)
        button.pack(pady=50, padx=10)
    
    #code to build back button on the dashboard option
    tk.Button(left_frame, text="Back", command = go_back, bg="#4caf50",fg="white", font=("Arial",12),bd=0,relief=tk.FLAT).pack(padx=20, pady=10)

#function that is responsible for displaying the feature that we have selected 
def showfeature(feature, right_frame):
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    api_key = "828e7e500e6476d88bfdbd818e9b25dc"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if(response.status_code == 200):
        # Set background image
        bg_images = {
            "Temperature": "temperature.png",
            "Humidity": "smart.png",
            "Pressure": "air.png",
            "Wind": "wind-turbine.png",
            "Visibility": "eye.png",
            "Sunrise-Sunset": "sunrise.png"
        }
        
        bg_image = Image.open(f"D:/git and github/weather_forcast/{bg_images[feature]}")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(right_frame, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Extract weather data
        Temperature = data["main"]["temp"]
        Feels_like = data["main"]["feels_like"]
        Humidity = data["main"]["humidity"]
        Pressure = data["main"]["pressure"]
        Wind_speed = data["wind"]["speed"]
        Wind_direction = data["wind"].get("deg",None)
        Visibility = data.get("visibility", "N/A")
        Sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        Sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')

        # Create consistent text display for all features
        # Enhanced text formatting for each feature
        if feature == "Temperature":
            text1 = (f"🌡️ Temperature 🌡️\n\n"
                    f"Current: {Temperature}°C\n"
                    f"Feels like: {Feels_like}°C")
            fg1 = "#d63031"  # Red for temperature

        elif feature == "Humidity":
            text1 = (f"💧 Humidity 💧\n\n"
                    f"Level: {Humidity}%\n"
                    f"{'💦 Humid' if Humidity > 70 else '🌵 Dry'}")
            fg1 = "#0984e3"  # Blue for humidity

        elif feature == "Pressure":
            pressure_status = "🔼 High" if Pressure > 1015 else "🔽 Low" if Pressure < 985 else "🟢 Normal"
            text1 = (f"🌀 Pressure 🌀\n\n"
                    f"{Pressure} hPa\n"
                    f"{pressure_status}")
            fg1 = "#8e82e7"  # Purple for pressure

        elif feature == "Wind":
            wind_dir = {
                range(0, 22): "⬆️ N", 
                range(22, 67): "↗️ NE",
                range(67, 112): "➡️ E", 
                range(112, 157): "↘️ SE",
                range(157, 202): "⬇️ S", 
                range(202, 247): "↙️ SW",
                range(247, 292): "⬅️ W", 
                range(292, 337): "↖️ NW",
                range(337, 361): "⬆️ N"
            }
            # Find the matching direction
            compass_dir = "N/A"
            if Wind_direction is not None:
                for angle_range, direction in wind_dir.items():
                    if Wind_direction in angle_range:
                        compass_dir = direction
                        break
            
            text1 = (f"🌬️ Wind 🌬️\n\n"
                    f"Speed: {Wind_speed} m/s\n"
                    f"Direction: {Wind_direction}")
            fg1 = "#00b894"  # Green for wind

        elif feature == "Visibility":
            visibility_status = "👀 Clear" if Visibility > 5000 else "🌫️ Foggy"
            text1 = (f"👁️ Visibility 👁️\n\n"
                    f"{Visibility} meters\n"
                    f"{visibility_status}")
            fg1 = "#636e72"  # Gray for visibility

        elif feature == "Sunrise-Sunset":
            text1 = (f"🌅 Sunrise & Sunset 🌇\n\n"
                    f"☀️ Rise: {Sunrise_time}\n"
                    f"🌙 Set: {Sunset_time}")
            fg1 = "#fdcb6e"  # Yellow for sunrise/sunset

        # Create the styled label
        tk.Label(right_frame,
                text=text1,
                font=("Arial", 20),
               
                fg=fg1,  # Dynamic color per feature
                padx=20,
                pady=15,
                justify="center").pack()

    
        
    else:
        messagebox.showerror("Error", "Could not fetch data")

#function that will make the user go back to the welcome page
def go_back():
    for widget in windowscreen.winfo_children():
        widget.destroy()
    welcome_page()

welcome_page()
windowscreen.mainloop()