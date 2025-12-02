import requests

API_KEY = "DEMO_KEY"
lat, lon = 20.2961, 85.8245   # Bhubaneswar Coordinates

url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date=2023-01-01&api_key={API_KEY}"

img = requests.get(url)

with open("satellite.jpg", "wb") as f:
    f.write(img.content)

print("Satellite image saved as satellite.jpg")
