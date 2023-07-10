import requests
from json import dumps

def auth(provided_string):
    url = ""
    user_agent = "Custom User Agent"
    webhookurl = ""

    headers = {
        "User-Agent": user_agent
    }

    params = {'string': provided_string}

    response = requests.get(url, headers=headers, params=params)
    result = response.text

    data = {
        "username": "Ramlov - Auth",
        "embeds": [
            {
                "title": "Authenticator",
                "color": 5763719,
                "description": f'Authenticator used! \n{result} \n Response code: {response} \n Access code: {provided_string} ',
                "footer": {
                    "text": "Author: Ramlov",
                    "icon_url": "https://avatars.githubusercontent.com/u/17428562?v=4",
                    "url": "https://github.com/Ramlov"
                }
            }
        ]
    }
    payload = dumps(data)
    response = requests.post(webhookurl, data=payload, headers={"Content-Type": "application/json"})




    if result.startswith('Ok'):
        return 'Validation successful: ' + result
    elif result.startswith('BLOCKED'):
        #... code to remove script
        pass
    else:
        return 'Validation failed: ' + result
