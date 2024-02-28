#An application that attempts to connect to a website or server every so many minutes or
# a given time and check if it is up. If it is down,
# it will notify you by posting a notice on screen. 

import requests
import time

def website_up_checker(url, interval):
    while True:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print("Website is down!")
            else:
                print("Website is up.")
        except Exception as e:
            print("Error:", e)
        time.sleep(interval)

# Example usage
website_up_checker("https://example.com", 300)  # Check every 5 minutes