import numpy as np 
from PIL import Image
from scipy import signal

img = Image.open("eggImagesGS/img.jpg")
imgarr = np.asarray(img)

img.show()

highpass = np.array([[0, -1, 0],[-1,  4, -1], [0, -1, 0]])
lowpass = np.ones((9,9)) / 81

sobelx = np.array([[-1/8,0,1/8],[-1/4,0,1/4],[-1/8,0,1/8]])
sobely = np.array([[1/8,1/4,1/8], [0,0,0], [-1/8,-1/4,-1/8]])

highpass_imgarr = signal.convolve2d(imgarr,highpass)
lowpass_imgarr = signal.convolve2d(imgarr,lowpass)
edgex_imgarr =  signal.convolve2d(imgarr,sobelx)
edgey_imgarr =  signal.convolve2d(imgarr,sobely)
edge_img = np.sqrt(edgex_imgarr**2 + edgey_imgarr**2)

highpass_img = Image.fromarray(np.clip(highpass_imgarr, 0, 255).astype(np.uint8))
lowpass_img = Image.fromarray(np.clip(lowpass_imgarr, 0, 255).astype(np.uint8))
edgex_img = Image.fromarray(np.clip(edgex_imgarr, 0, 255).astype(np.uint8))
edgey_img = Image.fromarray(np.clip(edgey_imgarr, 0, 255).astype(np.uint8))
edge_img = Image.fromarray(np.clip(edge_img, 0, 255).astype(np.uint8))

highpass_img.show()
lowpass_img.show()
edgex_img.show()
edgey_img.show()
edge_img.show()



