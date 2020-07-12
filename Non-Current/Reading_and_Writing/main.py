newFile = open("newFile.txt", "w+")  # Creating a file object in write/append mode

String = "oh, Hello there!"

newFile.write(String)  # Adding String to the file object newFile

import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0: # check if the file exists and has a size greater than 0
	oldFile = open("./ages.json", "r+") # Create a file object in read mode
	data = json.loads(oldFile.read()) # Loads it as a python usable object
	print("current age is", data["age"], "-- adding a year")
	data["age"] += 1
	print("new age is", data["age"])
else:
	oldFile = open("./ages.json", "w+")
	data = {"name": "Nick", "age": "21"}
	print("No file found, setting default age to ", data["age"])

oldFile.seek(0) # set to position 0, otherwise it would append
oldFile.write(json.dumps(data))
