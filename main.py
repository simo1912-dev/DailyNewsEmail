# Brainstorming/Planning phase: this Prog has no user interface so we can skip the design part
import requests
from send_email import send_email

api_key = "f2c2ff78c7104f089d69cf44080f256b"
topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2024-01-13&sortBy=publishedAt&"
       "apiKey=f2c2ff78c7104f089d69cf44080f256b&language=en")

# Make a request
request = requests.get(url)

content = request.json()  # .json instead of .text: so to have a structued type that we can use in our loops to read the data

body = ""
for article in content["articles"][:20]:
    if article["description"] is not None and article["title"] is not None:
        body = ("Subject: Today's news"
                + "\n" + body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2 * "\n")

body = body.encode("utf-8")  # otherwise I will get a UnicodeEncode Error
send_email(message=body)
