import requests
city = input("Enter the city:")
API_KEY = '***'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'q': city, 'appid': API_KEY, "units": "metric", "lang": "en"}
response = requests.get(url, params=params)
data = response.json()
print(
    f"The temperature in {data['name']}: {round(int(data['main']['temp']))}°C ({data['weather'][0]['description']})")
