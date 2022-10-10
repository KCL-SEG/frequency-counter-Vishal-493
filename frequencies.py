"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for (i=0; i < len(items); i++):
        if str(items[i]) not in newList:
            newList.append(str(items[i]))
            frequencyCounter = (str(items[i]).count())
            frequencies[str(items[i])] = frequencyCounter
        else:
            continue
