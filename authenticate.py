import requests

url = "https://ramlov.org/authenticate/"
provided_string = "String"

params = {'string': provided_string}

response = requests.get(url, params=params)
result = response.text

if result.startswith('Ok'):
    print('Validation successful:', result)
elif result.startswith('Reset'):
    #... code to remove script
    pass
else:
    print('Validation failed:', result)
