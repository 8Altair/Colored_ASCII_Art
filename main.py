from colorama import init  # Imports init function from colorama library
from termcolor import colored  # Imports colored function from termcolor library
from pyfiglet import figlet_format  # Imports figlet_format function from pyfiglet library

init()  # Initializes colorama library


# Function to check if color input is valid and return the valid color
def color_check(color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")  # List of valid colors
    while color not in valid_colors:  # Loop until a valid color is inputted
        print(f"\n{color} is not valid. Please choose another color.")
        print("These are the valid colors: ", end="")
        for e in valid_colors:
            print("  ", e, end="")
        color = input("\nWhat color would you like? ")
    return color


# Function to check if the user wants to include attributes
def attribute_check():
    answer = input("Would you like to include attributes? ")  # Ask user if they want to include attributes
    while answer.lower() not in ("yes", "no"):  # Loop until user inputs either "yes" or "no"
        print('The answer must be "yes" or "no".')
        answer = input("\nWould you like to include attributes? ")

    if answer == "yes":  # If user inputs "yes", proceed to input attributes
        attributes = []  # List to store inputted attributes
        valid_attributes = ("bold", "dark", "underline", "blink", "reverse", "concealed")  # List of valid attributes
        while 1:  # Loop to input attributes
            attribute = input("What attribute would you like to use? ")

            while attribute not in valid_attributes:  # Loop until user inputs a valid attribute
                print(f"\n{attribute} is not valid. Please choose another attribute.")
                print("These are the valid attribute:", end="")
                for e in valid_attributes:
                    print("  ", e, end="")
                attribute = input("\nWhat attribute would you like to use? ")
            attributes.append(attribute)

            answer = input(
                "\nWould you like to add another attribute? ")  # Ask user if they want to add another attribute
            while answer.lower() not in ("yes", "no"):  # Loop until user inputs either "yes" or "no"
                print('The answer must be "yes" or "no".')
                answer = input("\nWould you like to include attributes? ")

            if answer == "yes":  # If user inputs "yes", loop back to input another attribute
                continue
            break  # If user inputs "no", exit loop

        return set(attributes)  # Return the list of attributes as a set to eliminate duplicates
    return None  # If user inputs "no", return None


# Function to check if the user wants to include a background color and return the valid background color
def on_color_check():
    answer = input(
        "Would you like to include color background? ")  # Ask user if they want to include a background color
    while answer.lower() not in ("yes", "no"):  # Validate the user's answer
        print('The answer must be "yes" or "no".')
        answer = input("\nWould you like to include color background? ")

    if answer == "yes":  # If the user wants to include a color background, ask for the background color
        valid_backgrounds = ("on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white")  # List of valid background colors
        background = input("What background would you like to use? ")   # Ask the user for the background color

        while background not in valid_backgrounds:  # Validate the user's answer
            print(f"\n{background} is not valid. Please choose another background.")
            print("These are the valid background:", end="")
            for e in valid_backgrounds:
                print("  ", e, end="")
            background = input("\nWhat background would you like to use? ")

        return background   # Return the background color
    return None  # If the user does not want to include a color background, return None


def print_art(message, color):
    final_color = color_check(color)

    ascii_art = figlet_format(message)
    attributes = attribute_check()
    background = on_color_check()

    if attributes:
        if background:
            colored_ascii = colored(ascii_art, color=final_color, attrs=attributes, on_color=background)
        else:
            colored_ascii = colored(ascii_art, color=final_color, attrs=attributes)
    else:
        if background:
            colored_ascii = colored(ascii_art, color=final_color, on_color=background)
        else:
            colored_ascii = colored(ascii_art, color=final_color)

    print(colored_ascii)


m = input("What would you like to print? ")
c = input("What color would you like? ")
print_art(m, c)
