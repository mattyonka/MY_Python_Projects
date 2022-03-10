import random

limit = 10
guess = 0
count = 0
answer = random.randrange(1,limit)


print("Let's play  a guessing game from 1 to ",limit)


while guess != answer:
    guess = int(input("\nWhat's your guess?:"))
    
    if guess > limit or guess < 1:
        guess = int(input("Out of bounds, Please restate your guess:"))
        
    count = count + 1

    if guess > answer:
        print("Too high!\n")
    if guess < answer:
        print("Too low!\n")
    

print("You are correct! It took you ",count, " guesses to get it right!")
