from PIL import Image, ImageFilter

im = Image.open("./img/Figure_1-1.png")

print(im.format, im.size, im.mode)
print(im.getextrema())
print(im.getpixel((200,120)))

new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())
new_im.show()
new_im.save("./img/Figure_1-1_pillow.jpg",quality=95)