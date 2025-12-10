import requests

def get_weather(city_name):
    API_KEY = "540fa5b6f38630192266e5d365fa3468"  # 🔑 Get it from OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            print(f"\n📍 City: {city_name}")
            print(f"🌤️ Weather: {weather}")
            print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"💧 Humidity: {humidity}%")
        else:
            print(f"❌ Error: {data['message']}")
    except Exception as e:
        print("Something went wrong:", e)

# Run the app
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
