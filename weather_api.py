import requests

API_KEY = "YOUR_API_KEY"
CITY = "Pune"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["main"]

    print("\n===== WEATHER DATA =====\n")

    print(f"City : {CITY}")
    print(f"Temperature : {temperature} °C")
    print(f"Humidity : {humidity} %")
    print(f"Condition : {weather}")

else:

    print("Failed to fetch weather data")