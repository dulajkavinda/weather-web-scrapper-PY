import requests
from bs4 import  BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=47.86127000000005&lon=-94.96922999999998#.Xths_p4zZTY")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week)

print(week.find_all(class_='tombstone-container'))