import random
import string

symbols = ["a", "b", "c", "d", "e", "f", "g", "h"]

# creating random set of symbols for mastermind
field = ["_", "_", "_", "_"]
print("This is a mastermind game. Four symbols need to be guessed from a-h")
print("A correct guess will be set in place, if it is a correct symbol")
print("but in the wrong position it will be indicated.")
tries = 5
answer = []
for i in range(1, len(field) + 1, 1):
    answer.append(random.choice(symbols))

print(answer) #Only comment this out for testing, shows the answer
numcorret = 0  # number correct of a given symbol
while tries > 0:
    guess = input("What is your guess?(4 letters long)\n")

    while len(guess) != 4:
        guess = input("Please re-enter your guess.\n")

    for i in range(0, len(guess), 1):  # searches guess for any equal values to answer
        # also searches for misplaced values
        numcorrect = 0  # number correct of a given symbol
        for j in range(0, len(answer), 1):

            if guess[i] == answer[j] and i != j:  # correct value but wrong position, sets the field to the guess and a question mark to denote wrong tile
                field[i] = guess[i] + "?"
                numcorrect += 1

            if guess[i] == answer[i]:  # correct value but wrong position
                field[i] = answer[i]


        if numcorrect > 0:
            print(guess[i], " has ", numcorrect, " other values")

    tries -= 1
    print(field)
    print(tries, " tries left.")

    if field == answer:
        print("You win!")
        break


# null
