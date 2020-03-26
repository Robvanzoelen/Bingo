# Part 2 of assignment LCP: draw the terms of the bingo one by one in a random order
# Team: Evert Schonewille & Rob van Zoelen

import random

with open("bingo_terms.txt", "r") as input_file:                            # Collect the words from the file as string
    inp = str(input_file.readlines())

terms = []                                                                  # Create a list of our terms, in random order
input_split = inp.split()
for i in input_split:
    terms.append(i)
del terms[0]
del terms[len(terms)-1]
random.shuffle(terms)

for round in range(25):                                                     # Draw the words within the list, one by one when a sign is given
    print("---------------------------------------------------------------------")
    print("You're now in round", round+1,".")
    while True:
        answer = input(" Type any character or press 'Enter' to obtain the next word:")
        if not len(answer) >= 0:
            print(" Please try any other character.")
        else:
            break
    print(" The drawn word is:", terms[round])
