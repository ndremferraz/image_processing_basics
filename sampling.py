from PIL import Image
from scipy import signal, ndimage
import numpy as np

# function to down sample an image by factor of 4
def down_sample_by4(img):
    imgarr = np.asarray(img)
    
    row = imgarr.shape[0]
    col = imgarr.shape[1]

    imgarr_down4 = np.zeros((int(row/4), int(col/4)))

    for i in range(imgarr_down4.shape[0]):
        for j in range(imgarr_down4.shape[1]):
            
            imgarr_down4[i][j] = imgarr[i*4][j*4]
            
    img_down4 = Image.fromarray(imgarr_down4.astype(np.uint8))
    
    return img_down4

# function to use gaussian smoothing filter followed by downsampling
def down_sampled_by4_gauss(img):
    imgarr = np.asarray(img)
    
    row = imgarr.shape[0]
    col = imgarr.shape[1]

    imgarr_down4 = np.zeros((int(row/4), int(col/4)))
    
    imgarr_gauss = ndimage.gaussian_filter(imgarr, 0.5)

    for i in range(imgarr_down4.shape[0]):
        for j in range(imgarr_down4.shape[1]):
            
            imgarr_down4[i][j] = imgarr_gauss[i*4][j*4]
            
    img_down4 = Image.fromarray(imgarr_down4.astype(np.uint8))
    
    return img_down4
    
    


img = Image.open("eggImagesGS/img.jpg")
img.save("subsampling/original.jpg")

img_down4 = down_sample_by4(img)
img_down4.save("subsampling/downby4.jpg")
img_dow4_gauss = down_sampled_by4_gauss(img)
img_dow4_gauss.save("subsampling/downby4_gauss.jpg")

img_down16 = down_sample_by4(img_down4)
img_down16.save("subsampling/downby16.jpg")
img_down16_gauss = down_sampled_by4_gauss(img_dow4_gauss)
img_down16_gauss.save("subsampling/downby16_gauss.jpg")




