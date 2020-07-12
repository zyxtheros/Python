"""ab xyz""" # an alternate way of writing comments

#User Input
selection = input("Please enter number:")
print("You entered:", selection)

#String Operations
greeting = "Hello World"
print("Greeting is: "+ greeting)
print("Greeting is: "+ str(len(greeting)) +" characters long")
print("Greeting is:", len(greeting), "characters long") #A better way to print mixed data

#Array Operations
hobbies = ["movies", "games", "python"]
print("A hobby I have is: " + hobbies[1]) #printing a vlaue from an array

#Dictionary Operations
myDict = {'name': 'Nick', 'age': 27, 'hobby': 'Coding'}
print(myDict.get("speed", "none"))  #print the value corresponding to a key.
									#"none" is printed when the key DNE (doesn't exist)
myArray = [2, 4, 6, 23, 7, 109, 81, 45]
print(myArray)          #printing an array
print(sorted(myArray))  #printing the sorted version of the array

#Function Operations
	#seperating words of a user-defined function with '_' is the standard, referred to as snake-case
def my_function(str1, str2):      #define a new function
	print("this is a function")
	print("a second thing we can do")
	print("str1 is: "+ str1 +"\nstr2 is: "+ str2) #print the input parameters on seperate lines

my_function("bubbles", "Hawaii")       #call a function
									   #my_function() would cause a run-time error
def my_function_2(name = "Unspecified", age = "Unknown"):   #creating a function with default parameter values
	print("My name is", name, "I am", age, "years old")

my_function_2("Caleb", 20)
my_function_2("Caleb")
my_function_2(age = 20) #using keywords to specify which parameter us being assigned
my_function_2(age = 20, name = "Caleb") #keywords can also be used to pass parameters out of order

	  # *sum signifies an array is being passed
def print_people(*people):  #define a function with an infinite number of parameters
	for person in people:
		print("one person is:\t", person)

print_people("Caleb", "Aaron", "Michael", "Phillip")

def add(num1, num2):    #returns the sum of num1 and num2
	return num1 + num2

print("Result is:\t", add(3, 7))

#if/else if/else operations
check = "Caleb"
if check == False:
	print("check is False")
elif check == "Caleb":
	print("Hi Caleb")
else:
	print("check is actually not False")

#For and While Operations
numbers = [1, 2, 3, 4, 5, 7, 6]
for item in numbers:
	print("my number is ", item)

run = True
current = 1
while run:
	if current == 10:
		run = False
	else:
		print(current)
		current+=1

#Importing Modules
import re
#using the regedit (re) module
string = '"I\'M NOT YELLING." she said. though we knew it to not be true'
print(string)
new1 = re.sub('[A-Z]','',string) #assign new1 as string, but remove any capital letters
print("new1:", new1)
new2 = re.sub('[a-z]','',string) #assign new2 as string, but remove any non-capital
print("new2:", new2)
new3 = re.sub('[.,\'\"]','',string) #assign new3 as string, but remove . , " and ' characters
print("new3:", new3)
new4 = re.sub('[.,\'\"A-Z]','',string) #assign new4 as string, but remove . , " and ' characters
									   # as well as capitals
print("new4:", new4)
new5 = re.sub('[.,\'\"A-Z+" "]','',string) #assign new4 as string, but remove . , " and ' characters
										   #as well as capitals and spaces
print("new5:", new5)
newString = '"I\'M NOT YELLING." she said. though we knew it to not be true. 1, 2, 3, 5, 78.9, 5, 32'
new6 = re.sub('[^0-9]','',newString) #assign new6 as string, but remove all non-numbers
print("new6:", new6)