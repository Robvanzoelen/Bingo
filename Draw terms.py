import random

with open("bingo_terms.txt", "r") as input_file:
    input = str(input_file.readlines())

terms = []
input_split = input.split()
for i in input_split:
    terms.append(i)
del terms[0]
del terms[len(terms)-1]
random.shuffle(terms)

message = ""
for round in range(5):
    print("You're now in round", round+1,".")
    while True:
        answer = int(input(message + " type '1' if you are ready for the next word:"))
        if answer > 1:
            message = str(answer) + " is not 1, please"
        elif answer < 1:
            message = str(answer) + " is not 1, please"
        else:
            break
    print(terms[round])

print(terms)