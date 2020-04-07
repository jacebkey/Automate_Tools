#! python3
# bulletPointerAdder.py - Adds Wikipedia bullet points to the start
# of each line of tet on the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split("\n")
print(lines)
for i in range(len(lines)):  # loop through all idnexes in yhe "lines" list
    lines[i] = "* " + lines[i]  # add star to each string in "line" list
text = "\n".join(lines)

pyperclip.copy(text)
