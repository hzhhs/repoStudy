from PIL import Image
im1=Image.open("校园.jpg")
im2=Image.open("职业.jpg")
x1,y1,z1=im1.split()
x2,y2,z2=im2.split()
# z2.show()
# new_image=[z1,x1,y1]
newg = x1.point(lambda i: i * 0.8)
newG = y1.point(lambda i: i * 1.2)
new_image=[newg,newG,z1]
new_mege=Image.merge("RGB",new_image)
new_mege.show()