import numpy as np
from PIL import Image

# RGB to grayscale function: Grayscale = (0.299*Red) + (0.587*Green) + (0.114* Blue) 
def RGBtoGrayScale(row, col, img):
    grayimg = np.zeros((row , col))
    
    for i in range(row):
        for j in range(col):
            
            grayimg[i][j] = int(img[i][j][0] *0.299 + img[i][j][1] * 0.587 + img[i][j][2] * 0.114) 
    
    return grayimg

img = Image.open("eggImagesRGB/img.jpg")

imgarr = np.asarray(img)

grayimgarr = RGBtoGrayScale(imgarr.shape[0] , imgarr.shape[1], imgarr)
grayimg = Image.fromarray(grayimgarr).convert("L")

grayimg.save("eggImagesGS/img.jpg")