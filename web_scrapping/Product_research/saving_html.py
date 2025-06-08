import requests
import random
import time
import fake_useragent

ua = fake_useragent.UserAgent()


with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    proxies = [p.strip() for p in proxies if p.strip()]


def fetchAndSaveToFile(url, path, max_retries=10):
    for attempt in range(max_retries):
        print(f"attempt Number: {attempt + 1}")
        proxy = proxies[attempt]
        headers = {
            "User-Agent": ua.random,
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Referer": "https://www.google.com/",
            "DNT": "1",  # Do Not Track request header
        }
        try:
            r = requests.get(url, proxies={"http": proxy,
                                        "https": proxy},
                                        headers=headers,
                                        timeout=10)
            if r.status_code == 200:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(r.text)
                print(f"Success with proxy: {proxy}")
                return
            else:
                print(f"Failed with proxy: {proxy}, status code: {r.status_code}")

        except Exception as e:
            print(f"Error with proxy {proxy}: {e}")
        time.sleep(2)  # To avoid hitting the server too hard
        print("Retrying with a different proxy...")
    print(f"Failed to fetch data after {max_retries} attempts.")