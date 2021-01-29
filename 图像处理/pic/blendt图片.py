from PIL import Image
im1=Image.open("校园.jpg")
im2=Image.open("职业.jpg")
im3=Image.blend(im1,im2,0.92)
im3.show()