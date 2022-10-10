"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for (i=0; i < len(items); i++):
        if str(items[i]) not in newList:
            newList.append(items[i])
            frequencyCounter = (items[i].count())
            frequencies[items[i]] = frequencyCounter
        else:
            continue
