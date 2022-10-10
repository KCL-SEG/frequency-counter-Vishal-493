"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newList = []
    try:
        for i in items:
            if str(i) not in newList:
                newList.append(str(i))
                frequencyCounter = (items.count(str(i)))
                frequencies[str(i)] = frequencyCounter
            else:
                continue
    except TypeError:
        print("Incorrect input")
