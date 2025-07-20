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
    submit_button = tk.Button(welcome_frame, text="click here to see Weather", command=show_dashboard, bg="#2e8b57")
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
    bg_label1.pack()

    
    features = ["Temperature", "Humidity", "Pressure","Wind","Visibility","Sunrise-Sunset"]

    for feature in features:
        button = tk.Button(left_frame, text = feature,
                           command = lambda f=feature : showfeature(f,right_frame),
                           width=20)
        button.pack(pady=15)
    
    #code to build back button on the dashboard option
    tk.Button(left_frame, text="Back", command = go_back, bg="#4caf50",fg="white", font=("Arial",12),bd=0,relief=tk.FLAT).pack(padx=20, pady=10)









#function that is responsible for displaying the feature that we have selected 
def showfeature(feature , right_frame):
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    api_key = "828e7e500e6476d88bfdbd818e9b25dc"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if(response.status_code == 200):
        Temperature = data["main"]["temp"]
        Feels_like = data["main"]["feels_like"]
        Humidity = data["main"]["humidity"]
        Pressure = data["main"]["pressure"]
        Wind_speed = data["wind"]["speed"]
        Wind_direction = data["wind"].get("deg", "N/A")  # Optional: Wind direction in degrees
        Visibility = data.get("visibility", "N/A")  # Optional: Visibility in meters
        Weather_description = data["weather"][0]["description"]
        Sunrise = data["sys"]["sunrise"]  # Unix timestamp (optional)
        Sunset = data["sys"]["sunset"]    # Unix timestamp (optional)
        Sunrise_time = datetime.fromtimestamp(Sunrise).strftime('%H:%M:%S')
        Sunset_time = datetime.fromtimestamp(Sunset).strftime('%H:%M:%S')

        if(feature == "Temperature"):
            icon_image = Image.open("D:/git and github/weather_forcast/temperature.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            tk.Label(right_frame, text=f"current is {Temperature}degree celcius  and it feels like\n{Feels_like}", font=("Arial",16)).pack(pady=80, padx=10)

            
        elif(feature == "Humidity"):
            icon_image = Image.open("D:/git and github/weather_forcast/smart.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            
            tk.Label(right_frame, text=Humidity, font=("Arial",20)).pack(pady=80, padx=10)
        elif(feature == "Pressure"):
            icon_image = Image.open("D:/git and github/weather_forcast/air.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            tk.Label(right_frame, text=f"atmospheric pressure is {Pressure}hpa ", font=("Arial",10)).pack(pady=80, padx=10)
        elif(feature == "Wind"):
            icon_image = Image.open("D:/git and github/weather_forcast/wind-turbine.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            tk.Label(right_frame, text=f"wind speed is {Wind_speed}\n wind direction is {Wind_direction} ", font=("Arial",20)).pack(pady=80, padx=10)
        elif(feature == "Visibility"):
            icon_image = Image.open("D:/git and github/weather_forcast/eye.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            tk.Label(right_frame, text=Visibility, font=("Arial",20)).pack(pady=80, padx=10)
        elif(feature == "Sunrise-Sunset"):
            icon_image = Image.open("D:/git and github/weather_forcast/sunrise.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(right_frame, image=icon_photo)
            icon_label.image = icon_photo #preventing garbage collection
            icon_label.pack()
            tk.Label(right_frame, text=f"the sunrise time is{Sunrise_time} and the sunset time is {Sunset_time}", font=("Arial",20)).pack(pady=80, padx=10)
        
    else:
        messagebox.showerror("Error",f"Could not fetch data")










#function that will make the user go back to the welcome page
def go_back():
    for widget in windowscreen.winfo_children():
        widget.destroy()
    welcome_page()

welcome_page()
windowscreen.mainloop()