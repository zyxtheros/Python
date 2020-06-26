from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search_query = input("Search for:\t")

meijerParams = {"text": search_query}
request_meijer = requests.get("https://www.meijer.com/shop/en/search/", params = meijerParams)

# soup = BeautifulSoup(request_meijer.text, "html.parser")
# print(soup.prettify()) # Print out the raw HTML code, formatted for easy reading

