import requests

myData = {"name": "Caleb", "Email": "caleb@email.com"}

r = requests.post("http://www.w3schools.com/php/welcome.php", data = myData)

f = open("myFile.html", "w+")
f.write(r.text)

# note, this code executes perfectly, but the URL DNE
