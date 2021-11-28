from PIL import Image
#im = Image.open("jujuEeu.jpg")
im = Image.new(mode="RGB", size=(100,100), color=(0,0,255) )

print(im.format, im.size, im.mode,)
im.save("azul.jpg")
#print(dir(im))