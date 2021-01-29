from PIL import Image
from PIL import ImageFilter

im1=Image.open("校园.jpg")
im2=Image.open("职业.jpg")
blur=im1.filter(ImageFilter.BLUR)
CONTOUR=im1.filter(ImageFilter.EMBOSS)
# blur.show()
CONTOUR.show()