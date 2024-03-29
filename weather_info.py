import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.com/en-IN/weather/tenday/l/8ecdb120c02061d6fe17ec5fd60155f9da5bb988e79dd6d6e3db71248dac9b61')

soup = BeautifulSoup(page.content, 'html.parser')

main =  soup.find(id='main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806')

day_main = main.find_all(class_='date-time')

date_main = main.find_all(class_='day-detail clearfix')

temp_main = main.find_all('td',class_='temp')

desc_main = main.find_all('td',class_='description')

rain_main = main.find_all('td',class_='precip')

wind_main = main.find_all('td',class_='wind')

humi_main = main.find_all('td',class_='humidity')

days = [item.get_text() for item in day_main]
dates = [item.get_text() for item in date_main]
temp = [item.get_text() for item in temp_main]
desc = [item.get_text() for item in desc_main]
rain = [item.get_text() for item in rain_main]
wind = [item.get_text() for item in wind_main]
humi = [item.get_text() for item in humi_main]

weather_info = pd.DataFrame({
	'Day':days,
	'Date': dates,
	'Description': desc,
	'Temperature': temp,
	'Rain Percip': rain,
	'Wind': wind,
	'Humidity': humi
	})

print(weather_info)
