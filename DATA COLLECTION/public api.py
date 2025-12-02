import requests
import csv

API_KEY = "YOUR_API_KEY"
city = "Bhubaneswar"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url).json()

data = [
    ["City", "Temperature", "Humidity"],
    [city, response["main"]["temp"], response["main"]["humidity"]]
]

with open("weather.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("weather.csv created")
