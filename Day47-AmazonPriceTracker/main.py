import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

BUY_PRICE = 55
smtp = "smtp.gmail.com"
EMAIL = "Sidewaays666@gmail.com"
PASSWORD = "Rq5fw5kqpQmXdUm"

url = "https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Glacier-4/dp/B07VBBJ6KZ/ref=sr_1_4?crid=1NC5YXCLBBHPP&keywords=ps4+controller&qid=1645416176&sprefix=ps4+%2Caps%2C221&sr=8-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(name="span", id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(smtp, 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="impressive-tie@pm.me",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
