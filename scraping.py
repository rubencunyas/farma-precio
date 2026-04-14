import requests

urls = [
    "https://www.inkafarma.com.pe",
    "https://inkafarma.com.pe",
    "https://www.farmacias.com.pe"
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"{url}: {r.status_code}")
    except Exception as e:
        print(f"{url}: Error - {type(e).__name__}")