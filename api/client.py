import requests
from utils.config import BASE_URL

def get_token():
    url = f"{BASE_URL}/auth"

    data = {
        "email": "tn3115@srmist.edu.in",
        "name": "Tameka Nawal S",
        "rollNo": "RA2311028020012",
        "accessCode": "QkbpxH",
        "clientID": "Tameka-S",
        "clientSecret": "RA2311028020012"
    }

    try:

        res = requests.post(url, json=data, timeout=5, verify=False)

        if res.status_code == 200:

            return res.json().get("access_token")

    except:

        pass

    return "mock_token"  # fallback

def get_depots():

    return [

        {"id": 1, "mechanicHours": 60},

        {"id": 2, "mechanicHours": 135},

        {"id": 3, "mechanicHours": 180},

    ]

def get_vehicles():

    return [

        {"id": "1", "duration": 3, "priority": 5},

        {"id": "2", "duration": 2, "priority": 2},

        {"id": "3", "duration": 5, "priority": 8},

        {"id": "4", "duration": 1, "priority": 1},

        {"id": "5", "duration": 4, "priority": 6},

    ]