
marked = "-----"
bingo_counter = 0
row_bingo = 0
column_bingo = 0
vertical_bingo = 0
bingocard1 = [["one", "-----", "three"],["-----", "five", "-----"],["seven", "eight", "-----"]]
bingocard2 = [["one", "-----", "-----"],["-----", "five", "-----"],["seven", "eight", "-----"]]
bingocard3 = [["-----", "-----", "-----"],["four", "-----", "-----"],["-----", "eight", "-----"]]
bingocard = bingocard3

for i in bingocard:
    for j in i:
        if j == marked:
            bingo_counter += 1
            continue
        else:
            bingo_counter = 0
            break
    if bingo_counter >= 3:
        print("Bingo!")
        bingo_counter = 0
        row_bingo += 1
for k in range(3):
    for h in range(3):
        if bingocard[h][k] == marked:
            bingo_counter += 1
            continue
        else:
            bingo_counter = 0
            break
    if bingo_counter >= 3:
        print("Bingo!")
        bingo_counter = 0
        column_bingo += 1
for n in range(3):
    if bingocard[n][n] == marked:
        bingo_counter += 1
        continue
    else:
        bingo_counter = 0
        break
if bingo_counter >= 3:
    print("Bingo!")
    bingo_counter = 0
    vertical_bingo += 1
for m in range(3):
    if bingocard[2-m][m] == marked:
        bingo_counter += 1
        continue
    else:
        bingo_counter = 0
        break
if bingo_counter >= 3:
    print("Bingo!")
    bingo_counter = 0
    vertical_bingo += 1



print(bingo_counter)
print(row_bingo)
print(column_bingo)
print(vertical_bingo)
print("End of the game")

