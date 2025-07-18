import requests

api_key = "828e7e500e6476d88bfdbd818e9b25dc"  # Replace with your actual API key

city = input("Enter the name of the city that you want to check the weather conditions of: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # Extract basic weather info
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

    # Print all details
    print("\n🌦️ Weather Report for", city)
    print("-" * 30)
    print(f"🌡️ Temperature: {temp}°C (Feels like: {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌀 Pressure: {pressure} hPa")
    print(f"🌬️ Wind: {wind_speed} m/s (Direction: {wind_direction}°)")
    print(f"👀 Visibility: {visibility} meters")
    print(f"☁️ Weather: {weather_description.capitalize()}")
    print(f"🌅 Sunrise: {sunrise} (UTC)")
    print(f"🌇 Sunset: {sunset} (UTC)")
else:
    print("❌ Error:", data.get("message", "Failed to fetch weather data"))