#Amy Schaeffer
#Final Project for Introduction to Programming Course
#A program that pulls and displays weather data from a website for a user specififed zip code

import urllib.request
import json

#Checks for valid 5 digit zipcode entry
def zipcode_valid(zipcode):
    if len(zipcode) != 5 or not zipcode.isdecimal():
        return False
    return True

#Defining personal API key and welcoming user
api_key = "de1f88cdddc1b682411f98e25592f569"
print("Welcome, earthling.")

#Function displaying weather
def display_weather():
    zipcode = input("Please enter a zip code: ")
    if not zipcode_valid(zipcode):
        print("Please enter a five digit zip code")
        return
    #Defining url to draw information from    
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zipcode},us&units=imperial&appid={api_key}"

    #Opening URL, reading the returned object and turns string into python object
    weather_response = urllib.request.urlopen(url)
    response_text = weather_response.read()
    response_data = json.loads(response_text)
    
    #Pulling information from the dictionary
    city = response_data['city']
    city_name = city['name']
    
    main = response_data['list'][0]['main']
    temp = main['temp']
    feels_like = main['feels_like']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    humidity = main['humidity']
    
    weather = response_data['list'][0]['weather'][0]
    description = weather['description'] 
    
    wind = response_data['list'][0]['wind']
    wind_speed = wind['speed']

    #printing data to the console
    print()
    print(f"Weather Report for {city_name}")
    print(f"Temperature: {temp} degrees fahrenheit")
    print(f"Feels like: {feels_like} degrees fahrenheit")
    print(f"Temperature Low: {temp_min} degrees fahrenheit")
    print(f"Temperature High: {temp_max} degrees fahrenheit")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {description.capitalize()}")
    print(f"Wind Speed: {wind_speed} MPH")

#Looping weather display function until user breaks it    
while True:

    #Allows errors to be caught by the exception to display error
    try:
        display_weather()
    except Exception as e:
         print(f"Error: {e}")

    stay = input("Type anything to try another zip code, type 'exit' to exit: ")
    if stay == "exit":
        break
