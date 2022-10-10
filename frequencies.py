"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    newListOne = []
    for item in items:
        newItem = (str(item))
        newListOne.append(newItem)
    frequencies = {}
    newListTwo = []
    try:
        for i in newListOne:
            if i not in newListTwo:
                newListTwo.append(i)
                frequencyCounter = (newListOne.count(i))
                frequencies[i] = frequencyCounter
            else:
                continue
    except TypeError:
        print("Incorrect input")
