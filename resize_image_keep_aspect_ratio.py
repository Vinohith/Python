from PIL import Image
import sys

img = Image.open('IMG-20170808-WA0000.jpg')

img.show()

width = img.size[0]
height = img.size[1]

print('Width = {0}, Height = {1}'.format(width, height))

#mywidth = 300
script = sys.argv.pop(0)
mywidth = int(sys.argv.pop(0))
widthpercent = (mywidth/float(img.size[0]))
myheight = int(widthpercent*img.size[1])

img = img.resize((mywidth, myheight))
img.show()

print('Width = {0}, Height = {1}'.format(mywidth, myheight))