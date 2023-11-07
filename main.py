import requests
import urllib.parse
import re

token = "95834b64978546429116076e72b179174796bd22aad"
targetUrls = ["https://jugaad.az", "https://westtown.az", "https://kbt.az"]

with open("email_results.txt", "w") as file:
    for i, targetUrl in enumerate(targetUrls, start=1):
        encoded_url = urllib.parse.quote(targetUrl)
        url = "http://api.scrape.do?token={}&url={}".format(token, encoded_url)
        response = requests.request("GET", url)

        print("URL {}: {}".format(i, targetUrl))
        html_content = response.text


        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, html_content)

        if emails:
            print("Email Addresses:")
            for email in emails:
                print(email)
        else:
            print("Email address not found.")


        file.write("URL {}: {}\n".format(i, targetUrl))
        if emails:
            file.write("Email Addresses:\n")
            for email in emails:
                file.write(email + "\n")
        else:
            file.write("Email address not found.\n")
