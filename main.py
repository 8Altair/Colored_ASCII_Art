from colorama import init
from termcolor import colored
from pyfiglet import figlet_format


# Function to validate the user input
def validate_input(prompt, options):
    while True:
        value = input(prompt).lower()
        if value in options:
            return value
        print(f"Invalid input. Please choose one of the following options: {', '.join(options)}\n")


# Function to print the ASCII art
def print_art(message, color, attributes=None, background=None):
    if attributes is None:
        attributes = set()
    figlet = figlet_format(message)
    colored_ascii = colored(figlet, color=color, attrs=attributes, on_color=background)
    print(colored_ascii)


init()

m = input("What would you like to print? ")  # Get the message to be printed
c = validate_input("What color would you like? ", ["red", "green", "yellow", "blue", "magenta", "cyan", "white"])   # Get the color of the message

a = set()   # Get the attributes of the message
if validate_input("Would you like to include attributes? ", ["yes", "no"]) == "yes":
    while True:
        attribute = validate_input("What attribute would you like to use? ",
                                   ["bold", "dark", "underline", "blink", "reverse", "concealed"])
        a.add(attribute)
        if validate_input("Would you like to add another attribute? ", ["yes", "no"]) == "no":
            break

b = None
if validate_input("Would you like to include color background? ", ["yes", "no"]) == "yes":
    b = validate_input("What background would you like to use? ",
                       ["on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white"])

print_art(m, c, a, b)   # Print the ASCII art with the given inputs
