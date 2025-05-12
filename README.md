# Image Processing Basics
For another isolated project I was prompted with writing code to detect objects on an image, but I also understood that I needed to understand some basics of image processing before anything. Hence why this repository exists


# RGB to grayscale function: Grayscale = (0.299*Red) + (0.587*Green) + (0.114* Blue) 
def RGBtoGrayScale(row, col, img):
    grayimg = np.zeros((row , col))
    
    for i in img:
        for j in img[i]:
            
            grayimg[i][j] = int(img[i][j][0] *0.299 + img[i][j][1] * 0.587 + img[i][j][2] * 0.114) 
    
    return grayimg

RGBtoGrayScale(row, col, imgarr)