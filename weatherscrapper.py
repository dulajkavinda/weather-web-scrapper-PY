import requests
from bs4 import  BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=47.86127000000005&lon=-94.96922999999998#.Xths_p4zZTY")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        'periods': period_names,
        'short_description': short_descriptions,
        'temperature': temperatures,
    }
)

print(weather_stuff)

weather_stuff.to_csv('result.csv')