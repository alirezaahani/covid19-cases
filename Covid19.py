import matplotlib.pyplot as plt
import requests
from colorama import Fore

user_country = input(Fore.WHITE + 'Please write your country\'s name:')

print(Fore.YELLOW + 'Connecting to the api server ...')
try:
    countries_slug = []
    countries = requests.get('https://api.covid19api.com/countries').json()
    print(Fore.GREEN + 'Connected!')
except:
    print(Fore.RED + 'Failed to connect .\nPlease check your internet connection.')
    exit()

counter = 0
for country in countries:
    if user_country.lower() in country['Slug'].lower():
        countries_slug.append(country['Slug'])
        print(Fore.WHITE + '\t[{}] = {}'.format(counter,country['Slug']))
        counter += 1

if countries_slug:
    try:
        user_country = int(input(Fore.YELLOW + 'Please select your country:'))
        if ( user_country <= len(countries_slug) ) and (user_country >= 0):
            country_slug = countries_slug[user_country]
            print(Fore.GREEN + 'Countery selected => ' + country_slug)
            print(Fore.GREEN + 'Api link:','https://api.covid19api.com/country/' + country_slug)
            print(Fore.YELLOW + 'Getting data from api server ...')
            data = []
            try:
                all_status = requests.get('https://api.covid19api.com/country/' + country_slug).json()
                print(Fore.GREEN + 'Data received.')
            except:
                print(Fore.RED + 'Failed to received data .\nPlease check your internet connection.')
                exit()

            for status in all_status:
                data.append(status['Deaths'])    
            update_date = status['Date']

            print(Fore.YELLOW + 'Making the plot ...')
            plt.plot(data)
            plt.title('Updated at :'+ update_date)
            print(Fore.GREEN + 'Plot made!')
            plt.show()

        else:
            print(Fore.RED + 'Please enter a vaild intager')
            exit()
    
    except ValueError:
        print(Fore.RED + 'Please enter a vaild intager')
        exit()
    
else:
    print(Fore.RED + 'Country not found.')
