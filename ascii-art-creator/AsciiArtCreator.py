import argparse
import numpy as np
from PIL import Image
import os

# the fontAspRatio is  and the cols is the 
def convertImgToASCII(fileNameOfImg, fontAspRatio=0.43, cols=80, gscale = "@%#*+=-:. ", outName="out"):
    """

    grayscale level values from http://paulbourke.net/dataformats/asciiart/

    Args:
        fileNameOfImg (str): the directory of the image to be changed
        fontAspRatio (float, optional): the aspect ratio of the chosen font. Defaults to 0.43 (font 'courier').
        cols (int, optional): number of columns of the final ascii image. Defaults to 80.
        gscale (str, optional): the ASCII characters that are included in the image. Defaults to "@%#*+=-:. ".
        outName (str, optional): the name of the file which contains the output, do not include an extension. Defaults to "out".

    Returns:
        str: The original image in ASCII format 
    """
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
    outName = createFileName(outName)

    f = open(outName + ".txt", 'w')
    for row in asciiImg:
        s = s + row + "\n"
        f.write(row + '\n')
    f.close()
    return s


def createFileName(fileName, ext=".txt"):
    """
    Generates a unique file name based on the one provided

    Args:
        fileName (str): the file name (without extension)
        ext (str, optional): the extension of the file. Defaults to ".txt".

    Returns:
        _type_: _description_
    """
    if os.path.exists(fileName + ext):
        newName = fileName [::-1]
        version = ""
        lenOfName = len(fileName)
        for i in range(lenOfName):
            if newName[i].isdigit():
                version = newName[i] + version
            else:
                version = "0" if version == "" else version
                fileName = fileName[:lenOfName-i] + str(int(version)+1)
                return createFileName(fileName)
    else :
        return fileName


def averageBrightness(image):
    """
    Calculates the average brightness of an image

    Args:
        image (PIL Image): the image to get the average brightness of

    Returns:
        float: the average brightness of the image
    """

    im = np.array(image) # stores the image as a numpy array the numpy array is a 2D array with each element of the inner array being the value of brightness of each pixel

    width, height = im.shape

    # im.reshape() changes the numpy array 'im' into a 1D
    return np.average(im.reshape(width * height))


if __name__ == '__main__':
    # this has 10 different values for 10 different gray values
    gscale1 = "@%#*+=-:. "

    # this has 70 different characters for 70 different gray values
    gscale2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^`. "

    allScales = [gscale1, gscale2]

    descStr = "This program will take an image and convert it into ASCII art"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument("--image", dest="imgFile", required=False, default=r"./sample1.jpg", help="The directory of the image you wish to convert to ASCII art.")
    parser.add_argument("--out", dest="outFile", required=False, default="out", help="The name of the file you wish for the output to go to. If a file with this name exists a a number will be added to the end of the name to prevent it from being overwritten. Do not include a file extension.")
    parser.add_argument("--gscale", dest="scale", required=False, default="1", choices=["1","2"], help="Which scale you would like to apply.")

    args = parser.parse_args()
    print(args.scale)

    scale = allScales[int(args.scale) - 1]
    print(scale)

    img = convertImgToASCII(args.imgFile,gscale=gscale1, outName=args.outFile)
    print(img)