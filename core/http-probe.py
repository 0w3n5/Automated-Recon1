import requests

def check_http(domain):
    urls = [f"http://{domain}", f"https://{domain}"]

    results = {}

    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            results[url] = r.status_code
        except:
            results[url] = None

    return results
