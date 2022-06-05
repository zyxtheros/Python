from bs4 import BeautifulSoup
import requests

search = input("Enter search term:\t") # Cue for the search query
myParam = {"q": search} # create a search variable
r = requests.get("https://www.bing.com/search", params = myParam) # Create the request

soup = BeautifulSoup(r.text, "html.parser") # tell the soup variable to look at the text from the request, parsed as HTML
# print(soup.prettify()) # Print out the raw HTML code, formatted for easy reading

results = soup.find("ol", {"id": "b_results"}) # search through the soup for an ordered list (ol), with id b_results
links = results.findAll("li", {"class": "b_algo"}) # find all list items with a class b_algo

for item in links:
	item_text = item.find("a").text # target the a element
	item_href = item.find("a").attrs["href"]

	if item_text and item_href:
		print(item_text)
		print(item_href)
		print("Summary:", item.find("a").parent.parent.find("p").text)

		# children = item.children
		# for child in children:
			# print("child:", child)

