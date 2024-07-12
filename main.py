import requests
from rich import print
from datetime import datetime

def welcome():
  """Displays welcome message"""
  print("[underline purple bold ]Welcome to my weather app[/underline purple bold]😄🤩🤗\n")

def display_current_weather(city):
  """Displays current weather"""
  api_key = "3734of2cfc5035aca32f96t5a9b478fb"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
  
  response = requests.get(api_url)
  weather = response.json()
  country = weather['country']
  temperature = weather['temperature']['current']
  humidity = weather['temperature']['humidity']
  wind_speed = weather['wind']['speed']
  
  print(f"\n[blue bold underline]Today:[/blue bold underline] \nThe temperature of [bold purple]{city}[/bold purple] in [purple]{country}[/purple] is currently [bold blue]{round(temperature)}ºC[/bold blue] and the humidity is [bold blue]{humidity}%[/bold blue] and the windspeed is [bold blue]{round(wind_speed)} km/h[/bold blue].")

def display_forecast_weather(city):
  """Displays forecast weather"""
  api_key = "3734of2cfc5035aca32f96t5a9b478fb"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}"
  response = requests.get(api_url)
  forecast_weather_data = response.json()
  print("\n[blue bold underline]Forecast:[/blue bold underline]")
  for day in forecast_weather_data['daily']:
    timestamp = day['time']
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime('%A')
    temperature = day['temperature']['day']

    if date.date() != datetime.today().date(): 
      print(f"[green]{formatted_day}:[/green] {round(temperature)}ºC")

def credits():
  """Displays credits"""
  print("\n[yellow bold]Thank you for using my weather app![/yellow bold]\n \nThis app was made by: \n[red bold underline]Susanne van Oosterom[/red bold underline] 🥰")

welcome()
city = input("Enter a city:")
city = city.strip()

if city:
  display_current_weather(city)
  display_forecast_weather(city)
  credits()
else: 
  print("[red bold]Please try again and make sure you enter a city.[/red bold]")