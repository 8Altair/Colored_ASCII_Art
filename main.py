from colorama import init
from termcolor import colored
from pyfiglet import figlet_format

init()


def color_check(color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    while color not in valid_colors:
        print(f"\n{color} is not valid. Please choose another color.")
        print("These are the valid colors: ", sep="")
        for e in valid_colors:
            print("  ", e, sep="")
        color = input("\nWhat color would you like? ")
    return color


def attribute_check():
    answer = input("Would you like to include attributes? ")
    while answer.lower() not in ("yes", "no"):
        print('The answer must be "yes" or "no".')
        answer = input("\nWould you like to include attributes? ")

    if answer == "yes":
        attributes = []
        valid_attributes = ("bold", "dark", "underline", "blink", "reverse", "concealed")
        while 1:
            attribute = input("What attribute would you like to use? ")

            while attribute not in valid_attributes:
                print(f"\n{attribute} is not valid. Please choose another attribute.")
                print("These are the valid attribute:", sep="")
                for e in valid_attributes:
                    print("  ", e, sep="")
                attribute = input("\nWhat attribute would you like to use? ")
            attributes.append(attribute)

            answer = input("\nWould you like to add another attribute? ")
            while answer.lower() not in ("yes", "no"):
                print('The answer must be "yes" or "no".')
                answer = input("\nWould you like to include attributes? ")

            if answer == "yes":
                continue
            break

        return set(attributes)
    return None


def print_art(message, color):
    final_color = color_check(color)

    ascii_art = figlet_format(message)
    attributes = attribute_check()
    if attributes:
        colored_ascii = colored(ascii_art, color=final_color, attrs=attributes)
    else:
        colored_ascii = colored(ascii_art, color=final_color)

    print(colored_ascii)


m = input("What would you like to print? ")
c = input("What color would you like? ")
print_art(m, c)
# Dodaj on_color.
