print("Hello, welcome!")

message = ""
while True:
    answer = int(input(message+" type '1' to continue:"))
    if answer > 1:
        message = str(answer)+" is not 1, please"
    elif answer < 1:
        message = str(answer)+" is not 1, please"
    else:
        break
print("Welcome to round 2")