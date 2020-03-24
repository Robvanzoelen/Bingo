# Part 3 of assignment LCP: create a bingo card and mark the terms
# Team: Evert Schonewille & Rob van Zoelen

with open("bingo_terms.txt", "r") as input_file:                    # Use the file 'bingo_terms' as input
    inp = str(input_file.readlines())                               # Make string of the input from file

terms = []                                                          # Create an empty list and append the input
input_split = inp.split()
for i in input_split:
    terms.append(i)
del terms[0]
del terms[len(terms) - 1]

def new_card(list_with_terms):                                      # Shuffle the list and make it a bingo card
    import random
    random.shuffle(terms)
    bingocard = []
    row1 = terms[0:5]
    row2 = terms[5:10]
    row3 = terms[10:15]
    row4 = terms[15:20]
    row5 = terms[20:25]
    bingocard.append(row1)
    bingocard.append(row2)
    bingocard.append(row3)
    bingocard.append(row4)
    bingocard.append(row5)
    print("---------------------------------------------------")
    for i in bingocard:
        print(i)
    return bingocard

def mark_term(row,column,bingocard):                                # Function to mark the terms that are drawn by draw terms by entering the coordinates
    bingocard[row-1][column-1] = "-----"
    print("---------------------------------------------------")
    for i in bingocard:
        print(i)
    return bingocard

bingocard = new_card(terms)                                         # Create a new card and set variables to start values

marked = "-----"
bingo_counter = 0
row_bingo = 0
column_bingo = 0
diagonal_bingo = 0
total_bingo = 0

while True:                                                         # Continue playing bingo until deciding to quit
    print("---------------------------------------------------")
    next_round = input("Press any button to continue, press '1' to quit")               # Every round there is the possibility to quit, otherwise: play new round
    if next_round != "1":
        row = int(input("Tell us the row of the term you want to mark (1-5)"))          # Possibility to enter coordinates of the given term
        column = int(input("Tell us the column of the term you want to mark (1-5)"))
        bingocard = mark_term(row, column, bingocard)
        total_bingo_start = total_bingo                                                 # Every round, amount of bingo's is counted, if this amount is increased compared to previous round, a sign is given that there is a new bingo
        row_bingo = 0                                                                   # Different types of bingo's are just counted for fun to give statistics at the end of the game
        column_bingo = 0
        diagonal_bingo = 0
        total_bingo = 0
        for i in bingocard:                                                             # Check horizontal bingo's
            for j in i:
                if j == marked:
                    bingo_counter += 1
                    continue
                else:
                    bingo_counter = 0
                    break
            if bingo_counter >= 5:
                bingo_counter = 0
                row_bingo += 1
        for k in range(5):                                                              # Check vertical bingo's
            for h in range(5):
                if bingocard[h][k] == marked:
                    bingo_counter += 1
                    continue
                else:
                    bingo_counter = 0
                    break
            if bingo_counter >= 5:
                bingo_counter = 0
                column_bingo += 1
        for n in range(5):                                                              # Check diagonal bingo (left top to right bottom)
            if bingocard[n][n] == marked:
                bingo_counter += 1
                continue
            else:
                bingo_counter = 0
                break
        if bingo_counter >= 5:
            bingo_counter = 0
            diagonal_bingo += 1
        for m in range(5):                                                              # Check diagonal bingo (left bottom to right top)
            if bingocard[4 - m][m] == marked:
                bingo_counter += 1
                continue
            else:
                bingo_counter = 0
                break
        if bingo_counter >= 5:
            bingo_counter = 0
            diagonal_bingo += 1
        total_bingo = row_bingo+column_bingo+diagonal_bingo
        if total_bingo > total_bingo_start:                                             # If amount of bingo's is bigger than previous round, show bingo sign that many times as new bingo's
            new_bingos = total_bingo-total_bingo_start
            print("---------------------------------------------------")
            for _ in range(new_bingos):
                print("!!!!!!!!!!BINGO!!!!!!!!!!")
    else:
        break

print("------------------End of the game---------------------")                         # When decided to end the game, show end sign with the results
print("Your score was: ")
print(row_bingo, " horizontal bingo('s)")
print(column_bingo, " vertical bingo('s)")
print(diagonal_bingo, " diagonal bingo('s)")
print("Which is a total of ", row_bingo + column_bingo + diagonal_bingo, " bingo's")











