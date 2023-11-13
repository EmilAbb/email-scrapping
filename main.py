import requests
import urllib.parse
import re

token = "901f258707514402968d954be89ce390a01ac0275c4"
base_url = "https://yellowpages.az/Az/results/page/{}/?search-title=Cihaz&sort-by=asc"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

with open("email_results.txt", "a") as file:  # Open the file in "append" mode ("a")
    page = 1
    while True:
        targetUrl = base_url.format(page)
        encoded_url = urllib.parse.quote(targetUrl)
        url = "http://api.scrape.do?token={}&url={}".format(token, encoded_url)
        response = requests.get(url)

        print("Page {}: {}".format(page, targetUrl))
        html_content = response.text

        emails = re.findall(email_pattern, html_content)

        if emails:
            print("Email Addresses:")
            for email in emails:
                print(email)
                file.write(email + "\n")

        # Manually increment the page number or change the URL structure if necessary
        page += 1

        if page > 10:  # Change this number to control how many pages you want to scrape
            break
