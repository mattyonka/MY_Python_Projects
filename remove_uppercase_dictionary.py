import random
import string

##class word:
##    randWord = ""
##
##    def getWord():
##        


readFile = open("wordsmod5.txt","r")
#creating words file without anything alphabetic characters
writeFile = open("wordsmod5_noupper.txt","r+")
wordList = readFile.readlines()


#searches readFile for alphabetic strings
for i in range(0,len(wordList),1):
    tempWord = ""
    for j in range(0,len(wordList[i])-1,1):

        #if value of word is less than lowercase a
        if ord(wordList[i][j]) < 97:

            tempWord += chr(ord(wordList[i][j])+32)
        else:
            tempWord += wordList[i][j]

    if tempWord.isalpha() == True:
        writeFile.write(tempWord)
        writeFile.write("\n")
        

""" Version of file to cut down wordsmod file into 5-letter words for worlde testing
import random
import keyboard
import pygame
import string

##class word:
##    randWord = ""
##
##    def getWord():
##


readFile = open("wordsmod.txt","r")
#creating words file without anything alphabetic characters
writeFile = open("wordsmod5.txt","r+")
wordList = readFile.readlines()


#searches readFile for alphabetic strings
for i in range(0,len(wordList),1):
    tempWord = ""
    for j in range(0,len(wordList[i])-1,1):
        tempWord += wordList[i][j]
    if len(tempWord) == 5:
        writeFile.write(tempWord)
        writeFile.write("\n")"""