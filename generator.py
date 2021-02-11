#!/usr/bin/env python3
"""This script generates daily schedule for commits as list of booleans"""

def generate(string):
    """Returns commit schedule as list of Booleans"""
    # Letters are 4x5 (this leaves 1 space above and below)
    # TODO: Add support for more letters
    alphabed = {
        "A": [" #  ", "### ", "# # ", "### ", "# # "],
        "B": ["##  ", "# # ", "##  ", "# # ", "##  "],
        "C": [" ## ", "#   ", "#   ", "#   ", " ## "],
        "D": ["##  ", "# # ", "# # ", "# # ", "##  "],
        "E": ["### ", "#   ", "### ", "#   ", "### "],
        "H": ["# # ", "# # ", "### ", "# # ", "# # "],
        "L": ["#   ", "#   ", "#   ", "#   ", "### "],
        "O": ["### ", "# # ", "# # ", "# # ", "### "],
    }

    # Add padding for the extra lines above and below
    letters = [["    "] + alphabed[x] + ["    "] for x in string]
    commit_days = []

    # Loop over letters replacing empty spaces with False and filled with True
    for letter in letters:
        for i in range(4):
            commit_days += eval(",".join([x[i] for x in letter]).replace(" ", "False").replace("#", "True"))
    return commit_days

if __name__ == "__main__":
    instructions = generate("HELLO")
    print(instructions)
