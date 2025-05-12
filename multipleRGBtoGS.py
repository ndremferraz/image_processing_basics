from PIL import Image, ImageOps


for i in range(37):
    idx = i + 1
    img = Image.open(f"eggImagesRGB/img ({idx}).jpg")
    newimg = ImageOps.grayscale(img).convert("L")
    newimg.save(f"eggImagesGS/img ({idx}).jpg")
