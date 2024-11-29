"""
CP1404/CP5632 Practical
State names in a dictionary
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]:2}")
    except KeyError:
       print("Invalid short state")
    state_code = input("Enter short state: ").upper()
