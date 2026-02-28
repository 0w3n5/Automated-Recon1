import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        subdomains = set()
        for entry in data:
            name = entry["name_value"]
            subdomains.update(name.split("\n"))
        
        return list(subdomains)

    except Exception as e:
        print(f"Error fetching subdomains: {e}")
        return []
