"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    newListOne = []
    for item in items:
        newItem = (str(item))
        newListOne.append(newItem)
    frequencies = {}
    newListTwo = []
        
    for i in newListOne:
     #   if i not in newListTwo:
    #            newListTwo.append(i)
      #  else:
      #          continue
        frequencyCounter = (newListOne.count(i))
        frequencies[i] = frequencyCounter
        #frequencies{i:newListOne.count(i)}
    #except TypeError:
      #  print("Incorrect input")
