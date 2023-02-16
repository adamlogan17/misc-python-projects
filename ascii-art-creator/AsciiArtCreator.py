import sys, random, argparse
import numpy as np
import math
from PIL import Image
import os


# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

# the fontAspRatio is the aspect ratio of the chosen font (the default value is set to font 'courier') and the cols is the number of columns of the final ascii image
def convertImgToASCII(fileNameOfImg, fontAspRatio=0.43, cols=80, gscale = "@%#*+=-:. ", outName="out11"):
    # opens the image and converts it to grayscale
    # note: the "L" stands for luminance and iis the 'brightness' of the image
    image = Image.open(fileNameOfImg).convert("L")

    width, height = image.size[0], image.size[1]

    # below calculates the how many pixels represent a character
    tileW = width / cols
    tileH = tileW / fontAspRatio

    # calculate number of rows needed
    rows = int(height / tileH)

    # this is the ASCII image as a 1D array
    asciiImg = []

    for j in range(rows):
        yTop = int(j * tileH)
        yBottom = ((j + 1) * tileH)

        if j == rows - 1:
            yEnd = height

        asciiImg.append("")

        for i in range(cols-1):
            xRight = int(i * tileW)
            xLeft = ((i + 1) * tileW)

            if i == cols - 1:
                xLeft = tileW

            croppedImg = image.crop((xRight, yTop, xLeft, yBottom))

            avg = (int(averageBrightness(croppedImg)))

            gsval = gscale[int((avg * (len(gscale)-1)) / 255)]

            asciiImg[j] += gsval

    s = ""
    if os.path.exists(outName + ".txt"):
        newName = outName [::-1]
        version = ""
        for i in range(len(newName)):
            if newName[i].isdigit():
                version = newName[i] + version
            else:
                outName = outName[:-i] + str(int(version)+1)
                break
        print(outName)

    f = open(outName + ".txt", 'w')
    for row in asciiImg:
        s = s + row + "\n"
        f.write(row + '\n')
    print(s)
    f.close()
    return s


"""
Generates a unique file name based on the one provided

Args:
    fileName (string): the file name (without extension)

Returns:
    _type_: _description_
"""
def createFileName(fileName, ext=".txt"):
    if os.path.exists(fileName + ext):
        newName = fileName [::-1]
        version = ""
        lenOfName = len(fileName)
        for i in range(lenOfName):
            if newName[i].isdigit():
                version = newName[i] + version
            else:
                version = "0" if version == "" else version
                print("file = " + fileName)
                fileName = fileName[:lenOfName-i] + str(int(version)+1)
                return createFileName(fileName)
    else :
        return fileName

def averageBrightness(image):
    # stores the image as a numpy array
    # the numpy array is a 2D array with each element of the inner
    # array being the value of brightness of each pixel
    im = np.array(image)

    width, height = im.shape

    # im.reshape() changes the numpy array 'im' into a 1D
    return np.average(im.reshape(width * height))


if __name__ == '__main__':
    # this has 70 different characters for 70 different gray values
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^`. "

    # this has 10 different values for 10 different gray values
    gscale2 = "@%#*+=-:. "

    # img = convertImgToASCII(r"./sample1.jpg",gscale=gscale1, cols=80)
    print("name = " + createFileName("out"))


