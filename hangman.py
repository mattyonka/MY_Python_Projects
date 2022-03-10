import random
import string

"""This game simply plays hangman against a very-large dictionary of english words."""

#If you work on this later, functionality to add:
#1.show list of ALL guessed letters, current guessedLetters list is a bit of a misnomer
#it shows what letters were guessed of the correct string
#
#2.Order list of all guessed letters alphabetically
#
#3.Dont count a try if the letter was already guessed
#
#4.Fix word list to not include capital letters?
#
#5.? add more if you want to

class word:
    randWord = ""
    readFile = open("wordsmod.txt","r")
    wordList = readFile.readlines()
    guessedLetters = []

    
    def __init__(self):
        "null"
        
    #gets random word from database    
    def getWord(self):
        num = len(self.wordList)
        self.randWord = self.wordList[random.randrange(0,num)]
        #for whatever reason the random word get from a text file has an additional space or new line character, this slices that off
        self.randWord = self.randWord[:len(self.randWord)-1]

        for i in range(0,len(self.randWord),1):
            #print(self.randWord[i]) # For testing characters length
            self.guessedLetters.append("_")

        #for testing
        #print(len(self.randWord))
        #print(self.randWord)

    def printWord(self):
        print(self.randWord)

    #takes a guessed letter and evaluates if it exists in the random string
    #returns a correct boolean
    #also shows the player a string of the word with the correct guesses so far
    def wordGuess(self,char):
        correct = 0
        tempWord =""
        
        for i in range(0,len(self.randWord),1):
            if char == self.randWord[i]:
                correct = 1
                #print("you guessed the letter")
                self.guessedLetters[i] = char

        for j in range(0,len(self.guessedLetters),1):
            tempWord += self.guessedLetters[j]
            tempWord += ""

        if correct == 1:
            print("\nYou guessed a correct letter.\n")
            
        else:
            print("\nYou did not guess a correct letter.\n")
        

        print(self.guessedLetters)
        #print(tempWord)
        return correct,tempWord
        
    def resetWord(self):
        #print("test")
        self.guessedLetters = []
        self.getWord()
        
        
class score:
    tries = 6
    
    def __init__(self):
        "null"
        
    def scoreDown(self):
        self.tries -=1
        print(self.tries, "guesses left.\n")
        
    def resetTries(self):
         self.tries = 6
    
def main():
    print("Hangman game - Guess a letter and see if it matches the word. 6 Guesses are allowed")
    unknown = word()
    unknown.getWord()
    #unknown.printWord()
    player = score()

    isPlaying = "y"

    """Currently no excemption handling is implemented - For an example of that check out the wordle research program"""
    while isPlaying == "y" or "Y":
        print(unknown.guessedLetters)
        while player.tries > 0:

            guess = input("What is your guess?\n\n")
            isRight,tempWord = unknown.wordGuess(guess)
            
            if isRight == 0:
                player.scoreDown()
            #print(tempWord,unknown.randWord)
            if tempWord == unknown.randWord:
                print("You got it right!")
                player.tries = 0
            
        isPlaying = input("Do you want to play again? Y or N\n\n") 
        #print("test")
        unknown.resetWord()
        player.resetTries()

        
if __name__ == "__main__":
    main()
    
