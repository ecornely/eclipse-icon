#!/usr/bin/python
import os, sys
#Using Pillow library https://pypi.python.org/pypi/Pillow/3.1.0
from PIL import Image, ImageFont, ImageDraw

#Dictionnary to place the letter for each size
fillColor="#fff"
proportion={
	16 : {
		"font":11,
		"x":5,
		"y":4
	},
	32 : {
		"font":21,
		"x":12,
		"y":11
	},
	48 : {
		"font":32,
		"x":18,
		"y":17
	},
	256 : {
		"font":170,
		"x":106,
		"y":90
	},
}


def add_letter(letter, size):
	"Draws a <letter> on top of eclipse_<size>.png according to the global proportion"
	im = Image.open("eclipse_"+str(size)+".png")
	font = ImageFont.truetype("arialbi.ttf", proportion[size]["font"])
	draw = ImageDraw.Draw(im)
	draw.text((proportion[size]["x"], proportion[size]["y"]), letter, font=font, fill=fillColor)
	im.save("letter/eclipse_"+str(size)+"_"+letter+".png")

if __name__=="__main__":
    # If one argument received only add that letter/argument on each size
	if len(sys.argv) == 2:
		for size in proportion.iterkeys():
			add_letter(sys.argv[1], size)
	else:
	    # Else apply each letter of the alphabet at all size
		for size in proportion.iterkeys():
			for i in range(26):
				letter=chr(ord("A")+i)
				add_letter(letter, size)

