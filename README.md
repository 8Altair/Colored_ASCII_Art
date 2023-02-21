# ASCII Art Printer

This project is an ASCII art printer that allows users to print their message in various colors and attributes, 
including background color. The user inputs a message and color, and the program generates ASCII art with the 
specified color and attributes. The color and attributes can be chosen from a list of predefined options, and 
the program will validate the user's input to ensure that it is valid. The program uses the colorama and 
termcolor packages to generate colored ASCII art, and the pyfiglet package to generate the ASCII art.

## Getting Started

To use this program, you will need to have Python 3 installed on your computer. You will also need to install 
the colorama, termcolor, and pyfiglet packages by running the following command in your terminal or command prompt:
pip install colorama termcolor pyfiglet

Once you have installed the necessary packages, you can run the program by executing the following command in your 
terminal or command prompt: python ascii_art_printer.py

## Usage

When you run the program, it will prompt you to enter the message you would like to print, and the color you would 
like the message to be. You will then be asked if you would like to include any attributes (bold, dark, underline, 
blink, reverse, or concealed), and if you would like to include a background color. The program will validate your 
input to ensure that it is one of the predefined options, and if it is not, it will prompt you to enter a valid option.

After you have entered all of your choices, the program will generate the ASCII art with the specified color and 
attributes, and display it in the terminal or command prompt.

## Example

Here is an example of how the program might be used:
What would you like to print? Hello
What color would you like? red
Would you like to include attributes? yes
What attribute would you like to use? underline
Would you like to add another attribute? no
Would you like to include color background? yes
What background would you like to use? on_yellow


The program would then display the following ASCII art:
![image](https://user-images.githubusercontent.com/109831705/220365346-74e42b3b-a397-465c-8631-91a350038b42.png)

 _   _      _ _
| | | | ___| | | ___
| |_| |/ _ \ | |/ _ \
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/
