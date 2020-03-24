# Part 1 of assignment LCP: collecting the terms and create term file
# Team: Evert Schonewille & Rob van Zoelen

terms = []                                                                              # Create empty list to add the terms
for _ in range(25):                                                                     # We want to play bingo with 25 buzzwords
    terms.append(input("Which word do you want to include in your Buzzword Bingo?"))

with open("bingo_terms.txt", "w") as myfile:                                            # Open our file and enter all of our 25 chosen words
    for term in terms:
        myfile.write(" ")
        myfile.write(term)
    myfile.write(" ")
