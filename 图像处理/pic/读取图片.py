from PIL import Image

# print(im.format,im.size,im.mode,im.palette)

# im.save("校园2.jpg","JPEG")
# im.save("校园3.png","PNG")
# im.show()
# lImage=im.convert("L")
# lImage.show()
# lImage.save("lImage校园.jpg")
#newImage=Image.new("RGB",(300,500))
#newImage=Image.new("RGB",(300,500),"red")
# newImage=Image.new("RGB",(300,500),(20,254,120))
# newImage.show()

im=Image.open("校园.jpg")
print(im.size)
# x,y=im.size
# im.thumbnail((x/8,y/8))
# im.save("缩小的校园.jpg")
# resizeimge=im.resize((750,500))
# resizeimge.show()
# rotateimage=im.rotate(30)
# rotateimage.show()
# print(im.split())
x,y,z=im.split()
# print(x)
z.show()