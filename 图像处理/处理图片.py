# from PIL import Image
# im = Image.open("校园.jpg")
# print(im)
# im.save("校园11.png")     ## 将"E:\mywife.jpg"保存为"E:\mywife.png"
# im = Image.open("校园11.png")  ##打开新的png图片
# print(im.format, im.size, im.mode)

# from PIL import Image
# im1 = Image.open("校园.jpg")
# im2 = Image.open("职业.jpg")
# r,g,b = im1.split()             ##分离出r，g，b
# print(b.mode)
# print(im1.mode,im1.size)
# print(im2.mode,im2.size)
# im = Image.composite(im1,im2,g)
# im.show()


from PIL import Image
img1 = Image.open("校园.jpg")
img1.show()

# getbands() - 显示该图像的所有通道，返回一个tuple
bands = img1.getbands()
print(bands)

# getbbox() - 返回一个像素坐标，4个元素的tuple
bboxs = img1.getbbox()
print( bboxs)

# getcolors() - 返回像素信息，是一个含有元素的列表[(该种像素的数量，(该种像素)),(...),...]
colors = img1.getcolors()
print( colors)

# getdata() - 返回图片所有的像素值，要使用list()才能显示出具体数值
#data = list(img1.getdata())
#print data

# getextrema() - 获取图像中每个通道的像素最小和最大值,是一个tuple类型
extremas = img1.getextrema()
print(extremas )

# getpixel() - 获取该坐标
pixels = img1.getpixel((87,180))
print( pixels)

# histogram() - 返回图片的像素直方图
print(img1.histogram())