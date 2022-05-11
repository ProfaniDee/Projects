import requests


Key = "7ff839ceacc8354881f89c58db44f61c"

def display_data(weather_data):
    try:
        print("Today's temp is: " + str(weather_data["list"][0]["main"]["temp"]))
        print("Tomorrow's temp will be: " + str(weather_data["list"][8]["main"]["temp"]))
        print("The following day the temp will be: " + str(weather_data["list"][16]["main"]["temp"]))
    except KeyError:
        print("Invalid city name or zipcode. Please try again.")
        main()

def main():
    option = input("Please type 'city' to enter city name or type 'zip' to enter zipcode. ")

    if option == 'city':
        city_name = input("city name: ")
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={Key}&units=imperial"
        try:
            weather_data = requests.get(base_url).json()
        except requests.exceptions.ConnectionError:
            print("Failed to connect to openweathermap.org")



    elif option == 'zip':
        zipcode = input("enter zipcode: ")
        new_url = f"https://api.openweathermap.org/data/2.5/forecast?q={zipcode}&appid={Key}&units=imperial"
        try:
            weather_data = requests.get(new_url).json()
        except requests.exceptions.ConnectionError:
            print("Failed to connect to openweathermap.org")

    else:
        print('Invalid entry, please type city or zip. ')
        main()


    display_data(weather_data)
    run_again = input("Do you want to try another location? y/n ")
    if run_again.lower() == 'y':
        main()
    else:
        quit()
main()
