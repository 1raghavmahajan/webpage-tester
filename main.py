import requests
import os
from time import sleep

urls = {"forum": "https://in.bookmyshow.com/buytickets/pvr-the-forum-mall-koramangala/cinema-bang-PVBN-MT/20211227"}

payload = {}

while(True):
    print("Checking...")
    for name in urls:
        response = requests.request(
            "GET", urls[name], data=payload, allow_redirects=False)
        sleep(2)
        if response.status_code != 301:
            if "Spider-Man" in response.text:
                os.system(f'say "Ticket book karo {name}"')
                print("found")

    sleep(2*60)
