import requests

Key = "7ff839ceacc8354881f89c58db44f61c"
option = input("Please type 'city' to enter city name or type 'zip' to enter zipcode. ")

if option == 'city':
    city_name = input("city name: ")
    base_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={Key}"
    weather_data = requests.get(base_url).json()

elif option == 'zip':
    zipcode = input("enter zipcode: ")
    new_url = f"https://api.openweathermap.org/data/2.5/forecast?q={zipcode}&appid={Key}"
    weather_data = requests.get(new_url).json()
else:
    quit()

print(weather_data)