import re

print("welcome to the calculator program")
print("type \"quit\" to exit\n")
previous = 0
run = True


def perform_math():
    global run       # import run global variable into the program for use
    global previous  # import run global variable into the program for use
    equation = ""    # initialize equation with empty string
    if previous == 0:   # first equation statement
        equation = input("Enter equation: ")    # get user input
    else:
        equation = input(str(previous))     # get previous result

    if equation == "quit":  # Exit Condition
        print("process terminated by user. Goodbye")
        run = False
    else:   # Non-exit condition
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)  # Remove letters and special characters

        if previous == 0:
            previous = eval(equation)   # evaluate the text in the string
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
