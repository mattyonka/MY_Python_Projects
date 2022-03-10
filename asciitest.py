import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

"""This (relatively dumb) program takes an image and outputs a massive ASCII version of the image in a .txt file

To be more functionally useful I would need to either fix the braile characters or massively reduce the size of the 
text file output to be managable for posting elsewhere.
"""

"""The current images are silly ones I found on my hard drive"""
img = cv.imread("phototesting/lizardwizard.jpg")
test = cv.imread("phototesting/dog.jpg")
#px = img[100,]
#print(px)
#this character set is broken by the python writing function, not sure why.
#I can copy the characters directly into notepad 
#chars = [" ","⠁","⠃","⠋","⠛","⠟","⠿","⠿"]

#testing if other chars work
#chars = [".","^","a","d","&","%","@","#"]
chars = ["@@","@%","%%","&&","dd","aa","^^",".."]


"""Takes given image and outputs grayscale"""
gray_test = cv.cvtColor(test,cv.COLOR_RGB2GRAY)
cv.imshow("Display window",gray_test)


print(gray_test.shape)
dim = gray_test.shape
#print(gray_test)
#0-255 = 256
#32 step if /8
#only have 7 chars so gonna step by chars(floor.(grayscale_value/36))

#two different ways of filling arrays, np for float and manually doing it
#for char_array in the for loops
gray_array = np.zeros((dim[0],dim[1]))
char_array = []

#creates a character array based on my unicode chars
for i in range(0,dim[0]-1,1):
    new = []
    for j in range(0,dim[1]-1,1):
        gray_array[i][j] = int(gray_test[i][j]/32)
        new.append(chars[int(gray_array[i][j])])
    char_array.append(new)



#opening ascii in write mode, writing char_array to the text file
file = open("ascii.txt","w")

for i in range(0,dim[0]-1,1):
    for j in range(0,dim[1]-1,1):
        file.write(char_array[i][j])
    file.write("\n")
file.close()
        
#changes R,G,B values to 0
#test[:,:,1] = 0


##plt.subplot(1,1,1),plt.imshow(img,cmap="gray",vmin=0,vmax=255)
###plt.subplot(1,2,2),plt.imshow(test)
##
##plt.show()
