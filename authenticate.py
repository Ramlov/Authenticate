import requests

def auth(provided_string):
    url = "https://ramlov.org/authenticate/"

    params = {'string': provided_string}

    response = requests.get(url, params=params)
    result = response.text

    if result.startswith('Ok - Normal authenticate'):
        return 'Validation successful: ' + result
    elif result.startswith('Reset'):
        #... code to remove script
        pass
    else:
        return 'Validation failed: ' + result
