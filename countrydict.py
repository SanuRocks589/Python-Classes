country_code = {'India' : '0091', 
                    'Australia': '0025', 
                    'Nepal': '00977', 
                    'Japan' : '0081', 
                    'Afghanistan' : '0093',
                    'Maldives' : '00960', 
                    'Mauritius' : '00230', 
                    }

print("The country code of Maldives -")
print(country_code.get('Maldives', 'Not Found'))

print("The country code of the Philippines -")
print(country_code.get('Phillipines', 'Not Found'))