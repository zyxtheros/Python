# © 2020 Caleb Capps. This Project is available for educational purposes under the MIT License


import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os


def get_query():
	return input("Search for:\t")


def create_user():
	print("© 2020 Caleb Capps. This Project is available for educational purposes under the MIT License")
	retrieve.first_name = input("First Name:\t")
	retrieve.last_name = input("Last Name:\t")
	retrieve.email = input("Email:\t")
	retrieve.postal_code = input("Postal Code:\t")
	# TODO: Ensure proper call of retrieve class when instantiating a user


class retrieve:
	def __init__(self, first_name, last_name, email, postal_code):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.postal_code = postal_code

	def meijer(self, search_query):
		meijer_params = {"text": str(search_query)}
		request_meijer = requests.get("https://www.meijer.com/shop/en/search/?text=" + str(search_query))
		print(request_meijer.url)
		soup = BeautifulSoup(request_meijer.text, "html.parser")
		print(soup.prettify())  # Print out the raw HTML code, formatted for easy reading
		# TODO: pass user input to the site
		# TODO: Parse the HTML data to retrieve product info

	def aldi(self, search_query):
		aldi_url = "https://shop.aldi.us/store/aldi/search_v3/" + str(search_query)
		print("URL to request:", aldi_url)
		request_aldi = requests.get(aldi_url)
		print(request_aldi.url)
		print(request_aldi.content)
		# TODO: pass user input to the site
		# TODO: Parse the HTML data to retrieve product info

	def walmart(self, search_query):
		walmart_params = {"query": str(search_query)}
		request_walmart = requests.get("https://www.walmart.com/search/", params=walmart_params)
		print(request_walmart.content)
		# TODO: Parse the HTML data to retrieve product info
