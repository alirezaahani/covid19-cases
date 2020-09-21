import matplotlib.pyplot as plt
import requests

user_country = input('Please write your country\'s name:')

countries_slug = []
countries = requests.get('https://api.covid19api.com/countries').json()

counter = 0
for country in countries:
    if user_country.lower() in country['Slug'].lower():
        countries_slug.append(country['Slug'])
        print('[{}] = {}'.format(counter,country['Slug']))
        counter += 1

if countries_slug:
    try:
        user_country = int(input('Please select your country:'))
        if ( user_country <= len(countries_slug) ) and (user_country >= 0):
            country_slug = countries_slug[user_country]
            print('Countery selected => ' + country_slug)
            data = []
            all_status = requests.get('https://api.covid19api.com/country/' + country_slug).json()
            for status in all_status:
                data.append(status['Deaths'])    
            update_date = status['Date']
            plt.plot(data)
            plt.title('Updated at :'+ update_date)
            plt.show()
        
        else:
            print('Please enter a vaild intager')
            exit()
    
    except ValueError:
        print('Please enter a vaild intager')
        exit()
    
else:
    print('Country not found.')
