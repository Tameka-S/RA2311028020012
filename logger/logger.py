import requests
from utils.config import BASE_URL

def log(stack, level, package, message, token):
    url = f"{BASE_URL}/logs"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    try:
        requests.post(url, json=data, headers=headers, timeout=3, verify=False)
    except:
        # fallback 
        print(f"[{level.upper()}] {package}: {message}")