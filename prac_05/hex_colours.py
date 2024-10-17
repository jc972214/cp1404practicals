"""Hex to Colour Calculator"""

COLOUR_TO_HEX = {"Amethyst": "#9966cc",
                 "Aqua": "#00ffff",
                 "Aureolin": "#fdee00",
                 "Baby Blue": "#89cff0",
                 "Baby Pink": "#f4c2c2",
                 "Gray21": "#363636",
                 "LightSalmon4": "#8b5742",
                 "Shamrock Green": "#009e60",
                 "Tart Orange": "#fb4d46",
                 "Zomp": "#39a78e"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {COLOUR_TO_HEX[colour_name.title()]}")
    except KeyError:
        print("Invalid Colour")
    colour_name = input("Enter colour name: ")
