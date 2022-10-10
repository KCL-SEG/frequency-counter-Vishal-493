"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newList = []
    if len(items) != 0
        for i in items:
            if str(i) not in newList:
                newList.append(str(i))
                frequencyCounter = (items.count(str(i)))
                frequencies[str(i)] = frequencyCounter
            else:
                continue
    else:
        print("Incorrect input")
