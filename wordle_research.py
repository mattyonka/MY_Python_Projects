import random
import keyboard
import pygame
import string


class word:


    #Guessed letter (and wordState) will have 4 states, 0 = not guessed, 1 = guessed and incorrect, 2 = correct letter and incorrect spot
    #3 = correct letter, correct spot
    randWord = ""
    readFile = open("wordsmod5_noupper.txt", "r")
    wordList = readFile.readlines()
    wordListMod = wordList.copy()

    def __init__(self):

        self.tries = 6
        self.wordState = [0]*5
        self.guessedLetters = [0]*26
        self.guessedPos = [0]*26
        self.cleanList()

        #these values based on letterFreq output, hard-coded them in because it would be inefficient to recalculate this a bunch.
        #You could modify these to be of the remaining set in order to optimize word.smartRec()
        self.LF = [12262, 2932, 3605, 3878, 10839, 1611, 2580, 3169, 7183, 630, 2450, 6074, 3431, 5948, 7105, 2880, 162, 7075,
          8239, 5366, 4362, 1247, 1479, 458, 3436, 604]
        self.weights = [1.0, 0.239, 0.293, 0.316, 0.883, 0.131, 0.210, 0.258, 0.585, 0.0513, 0.199, 0.495, 0.279, 0.485, 0.579, 0.234, 0.0132, 0.576, 0.671, 0.437, 0.355, 0.101, 0.120, 0.0373, 0.280, 0.049]

    def reset_params(self):
        self.wordListMod = self.wordList.copy()
        self.tries = 6
        self.wordState = [0] * 5
        self.guessedLetters = [0] * 26
        self.guessedPos = [0] * 26
        self.cleanList()

    def wrong(self):
        self.tries -= 1
        if self.tries == 0:
            print("You are out of guesses.")

    #removes \n parameters in
    def cleanList(self):
        for i in range(0,len(self.wordListMod),1):
            self.wordListMod[i] = self.wordListMod[i][:5]


    # gets random word from database
    def getWord(self):
        num = len(self.wordListMod)
        self.randWord = self.wordListMod[random.randrange(0, num)]
        #for i in range(0, len(self.randWord) - 1, 1):
            #self.guessedLetters.append("_")

    def printWord(self):
        print(self.randWord)

    # takes a guessed letter and evaluates if it exists in the random string
    # returns a correct boolean
    # also shows the player a string of the word with the correct guesses so far

    def playWordle(self,start):
        """
        It plays wordle based on a pre-generated word and data set. You could modify this code
        to input values in yourself based on wordle gameplay. If this was a smarter algorithm it wouldn't pick on random
        but rather based on how common letters are based on letter frequency data developed in another part of this module.

        Run time is a little slow, it could be sped up most likely.
        """
        tempWord = ""

        guess = start

        print(guess)
        print(self.randWord)
        #print(self.wordState)

        if self.wordState == [3,3,3,3,3]:
            return None
        #elif self.tries == 0:
        #    return None
        elif len(self.wordListMod) == 1:
            return None



        for i in range(0,len(guess),1):
            char = int(ord(guess[i])-97)
            #print(type(self.guessedLetters))

            #Correct letter, correct place
            if guess[i] == self.randWord[i]:
                self.wordState[i] = 3
                self.guessedLetters[char] = 3
                self.guessedPos = i

            #Correct letter, incorrect place
            elif (guess[i] != self.randWord[i]) and (guess[i] in self.randWord):
                self.wordState[i] = 2

                if self.guessedLetters[char] != 3:
                    self.guessedLetters[char] = 2
                    self.guessedPos = i

            #incorrect letter
            else:
                self.wordState[i] = 1
                if self.guessedLetters[char] != 3:
                    self.guessedLetters[char] = 1
                    self.guessedPos = i

        self.tries -= 1

        print(self.wordState)

        self.cutWordList(guess)
        new_guess = random.choice(self.wordListMod)
        self.playWordle(new_guess)

    def playWordleUser(self):
        """
        This version of PlayWordle is a little more developed and includes references to a "smart" decision maker based
        off of weighted value of letters in possible left-over words.

        Changes from Playwordle at the moment = numeric exemption handler input, smartRec
        """
        tempWord = ""




        #print(guess)
        #print(self.randWord)
        #print(self.wordState)

        """Termination conditions, could re-enable number of tries if wanted"""
        if self.wordState == [3,3,3,3,3]:
            retry = input("Please input Y or y to play again\n")
            if retry == "y" or retry == "Y":
                self.reset_params()
            else:
                return None
        #elif self.tries == 0:
        #    return None
        elif len(self.wordListMod) == 1:
            retry = input("Please input Y or y to play again\n")
            if retry == "y" or retry == "Y":
                self.reset_params()
            else:
                return None


        """Takes input and handles non-alphabetic exemptions"""
        g = True
        while g == True:
            guess = input("What word was input? All lowercase please. If you're stuck, type 'another'\n ")
            if not guess.isalpha():
                print("please re-input the guess\n")
            elif guess == "another":
                print(random.choice(self.wordListMod))
            else:
                g = False

        """Establishing values to put into smartRec and playWordleUser"""
        #string of word state = string state = ss
        s = True
        while s == True:
            ss= input("What was your score? The format requires 5 numbers. Ex. 31232\n")
            if ss.isalpha() or len(ss) != 5:
                print("please re-input the value\n")
            else:
                s = False
                
        self.wordState = [int(ss[0]),int(ss[1]),int(ss[2]),int(ss[3]),int(ss[4])]

        #Filling out self.GuessedLetters for double-letter handling
        for i in range(0,5,1):
            if self.guessedLetters[ord(guess[i])-97] < self.wordState[i]:
                self.guessedLetters[ord(guess[i])-97] = self.wordState[i]

        print(self.wordState)
        self.tries -= 1

        #print(self.wordState)

        self.cutWordList(guess)
        print(len(self.wordListMod))
        if len(self.wordListMod) < 25:
            print(self.wordListMod)

        self.smartRec()
        self.playWordleUser()

    def cutWordList(self,guess):
        """Marks values that don't meet parameters listed above"""

        popVals = []

        for i in range(0,len(self.wordState),1):
            for j in range(0,len(self.wordListMod),1):


                if self.wordState[i] == 1:
                    #2nd half of this if conditional handles repeated letters in guess that don't end up being true
                    if guess[i] in self.wordListMod[j] and self.guessedLetters[ord(guess[i])-97] < 2 :
                        popVals.append(j)

                if self.wordState[i] == 3:
                    if guess[i] != self.wordListMod[j][i]:
                        popVals.append(j)


                if self.wordState[i] ==2:
                    if guess[i] not in self.wordListMod[j] or guess[i] == self.wordListMod[j][i]:
                    #if guess[i] not in self.wordListMod[j]:
                        popVals.append(j)

        #print(popVals)
        for k in range(len(self.wordListMod),-1,-1):
            if k in popVals:
                self.wordListMod.pop(k)

    def smartRec(self):
        """Uses weighted values of each word to determine which one should be used next.
        Current implementation sorts by weights of ALL words and not of the remaining set.

        Ideally this information would be used by the weight of what's in the set to possibly eliminate the most options
        but I've moved onto other projects for the time being."""
        max = 0

        tempChar = 0
        tempVal = 0
        index = 0
        some_choices = []
        some_choices_vals =[]
        repeat = 0

        #print("Word List Mod Len", len(self.wordListMod))
        #print("Index val", index)

        for i in range(0,len(self.wordListMod),1):

            #creates a temporary weighting based to modify
            tempWeight = self.weights.copy()
            for j in range(0,len(self.wordListMod[i]),1):

                #assings the weighting based on the letter and temporarily reduces that rating to 0, to emphasize
                #using differnet letters instead of repeated high-value letters
                tempChar = ord(self.wordListMod[i][j])-97
                tempVal += tempWeight[tempChar]
                tempWeight[tempChar] =0

            if tempVal >= max:
                max = tempVal
                index = i
                some_choices.append(self.wordListMod[i])
                some_choices_vals.append(max)
            tempVal = 0


        #print("Word List Mod Len",len(self.wordListMod))
        #print("Index val",index)
        print("reccomended choice is:", self.wordListMod[index])


    def resetWord(self):
        self.guessedLetters = [0]*26
        self.tries = 6
        self.wordState = [0]*5
        self.getWord()

    #letters range from ascii values of (A-Z) 65-90 for uppercase, (a-z) 97-122 for lowercase
    #so uppercase -> lowercase means add 32
    def letterFreq(self):
        letterList = [0]*26
        letter = 0
        for i in range(0,len(self.wordList),1):
            for j in range(0,len(self.wordList[i])-1,1):

                letter = ord(self.wordList[i][j])

                #lowercase add value
                if letter > 91:
                    letterList[letter-97] += 1

                #uppercase add value
                if letter < 91:
                    letterList[letter - 65] += 1

        return letterList

def main():
    newWord = word()
    newWord.getWord()
    #print(newWord.randWord)



    #Game Loop!
    print("Wordle Test\n")
    print("This program helps you play wordle by inputing the word you guessed and the result, and giving a possible next guess.\n")

    isPlaying = "y"

    #testWord = "crane"
    #newWord.playWordle(testWord)
    newWord.playWordleUser()


    """PYGAME LOOP - Currently only visualizes letter frequency data. You could make this visualize the potential solutions remaining 
    for wordle.

    # screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
    # screen = pygame.transform.flip(screen,True,False)
    pygame.display.flip()
    pygame.font.init()

    # init pygame
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("LetterFreq")
    screen_width = 520
    screen_height = 520
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Visualizing letter frequency data
    #This calc is unnecessary besides the first time so I stored the data in LF
    # lettersFrequency = newWord.letterFreq()
    LF = [12262, 2932, 3605, 3878, 10839, 1611, 2580, 3169, 7183, 630, 2450, 6074, 3431, 5948, 7105, 2880, 162, 7075,
          8239, 5366, 4362, 1247, 1479, 458, 3436, 604]
    largestLetter = LF[0]
    print(LF)

    # establishing Screen
    screen.fill([0, 0, 0])

    # starting pyfont to put character next to frequency rectangle
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    char_font = pygame.font.Font(default_font, 12)

    # visualizing character frequency data
    for i in range(0, len(LF), 1):
        H = 520 * LF[i] / largestLetter
        y_pos = 520 - H
        char = chr(i + 97)
        pygame.draw.rect(screen, (0, 0, 255), (i * 20, y_pos, 20, H), 0)
        screen.blit(pygame.font.Font.render(char_font, char, 1, (255, 255, 255)), (8 + (i * 20), 508))

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()



    END PYGAME LOOP"""

if __name__ == "__main__":
    main()