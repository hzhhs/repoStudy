from PIL import Image
# pic_Im=Image.open("校园.jpg")
# pic_Im.show()

# 生成新的125*125的黑色图片
# newIm=Image.new('RGB',(125,125))
# newIm.show()
# newIm2=Image.new('RGB',(125,125),"red")
# newIm2=Image.new('RGB',(125,125),(255, 255, 0))
# newIm2.show()

# from PIL import Image
# im = Image.open("校园.jpg")
# print(im.format) ## 打印出格式信息输出是JPEG
# im.show()

# from PIL import Image
# im = Image.open("校园2.jpg")
# print(im.mode) ## 打印出模式信息
# im.show()

# 另存为其它格式图片
# pic_Im.save("校园3.png")
# 转为灰度图片
# Im=pic_Im.convert('L')
# Im.save("校园2.jpg")
# print(pic_Im.getbands())

# from PIL import Image
# im = Image.open("校园.jpg")
# new_im = im.convert('p')
# print(new_im.mode)
# new_im.save("校园4.jpg")
# new_im.show()


# from PIL import Image
# im = Image.open("校园3.jpg")
# print(im.size) ## 打印出尺寸信息
# print(im.palette)
# im.show()

# 对图像进行convert操作，转换成“P”模式，返回值为ImagePalette类
# from PIL import Image
# im = Image.open("校园.jpg")
# new_im = im.convert('P')
# print(new_im.mode)
# print(new_im.palette)

# from PIL import Image
# im = Image.open('timg.gif')      # 读入一个GIF文件
# try:
#     im.save('picframe{:02d}.png'.format(im.tell()))
#     while True:
#         im.seek(im.tell()+1)
#         im.save('picframe{:02d}.png'.format(im.tell()))
# except:
#     print("处理结束")


# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('校园.jpg')
# # 获得图像尺寸:
# w, h = im.size
# # 缩放到50%:
# im.thumbnail((w/8, h/8))
# # 把缩放后的图像用jpeg格式保存:
# im.save('校园thumbnail.jpg', 'jpeg')
#
# from PIL import Image
# im = Image.open("定妆.jpg")
# region = im.resize((400, 400))     ##重新设定大小
# region.save("定妆2.jpg",'jpeg')
# region.show()

# from PIL import Image
# im = Image.open("定妆.jpg")
# im_45 = im.rotate(45)
# im_30 = im.rotate(30, Image.NEAREST,1)
# print(im_45.size,im_30.size)
# im_45.show()
# im_30.show()

#
# from PIL import Image
# im1 = Image.open("校园.jpg")
# im2 = Image.open("职业.jpg")
# r1,g1,b1 = im1.split()
# r2,g2,b2 = im2.split()
# print(r1.mode,r1.size,g1.mode,g1.size)
# print(r2.mode,r2.size,g2.mode,g2.size)
# new_im=[r1,g2,b2]
# print(len(new_im))
# im_merge = Image.merge("RGB",new_im)
# im_merge.show()
#
# from PIL import Image
# im1 = Image.open("校园.jpg")
# im2 = Image.open("职业.jpg")
# print(im1.mode,im1.size)
# print(im2.mode,im2.size)
# im = Image.blend(im1, im2, 0.2)
# im.show()

# from PIL import Image, ImageFilter
# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('校园.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('校园blur.jpg', 'jpeg')
#

from PIL import Image
from PIL import ImageFilter                         ## 调取ImageFilter
imgF = Image.open("校园.jpg")
bluF = imgF.filter(ImageFilter.BLUR)                ##均值滤波
conF = imgF.filter(ImageFilter.CONTOUR)             ##找轮廓
edgeF = imgF.filter(ImageFilter.FIND_EDGES)         ##边缘检测
imgF.show()
bluF.show()
conF.show()
edgeF.show()