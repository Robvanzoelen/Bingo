terms = []
for _ in range(5):
    terms.append(input("Which word do you want to include in your Buzzword Bingo?"))

with open("bingo_terms.txt", "w") as myfile:
    for term in terms:
        myfile.write(" ")
        myfile.write(term)
    myfile.write(" ")
