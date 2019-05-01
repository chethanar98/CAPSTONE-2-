from PIL import Image

# import matplotlib.pyplot as plt 


def filter1(image):
	dog = Image.open("dog.jpg")
	global width
	global height
	width, height = image.size
	print(width, height)
	# plt.imshow(image)
	# plt.show()
	r,g,b = image.split()
 	

	pattern1 = Image.open("pattern1.jpg")
	pattern1 = pattern1.resize((width, height), Image.ANTIALIAS)
	# plt.imshow(pattern1)
	# plt.show()
	r1,g1,b1 = pattern1.split()

	new1 = Image.merge("RGB", (r1,g,b))
	# plt.imshow(new1)
	# plt.show()
	return new1

def filter2(image):
	# dog = Image.open("dog.jpg")
	# plt.imshow(image)
	# plt.show()
	r,g,b = image.split()

	pattern2 = Image.open("pattern2.jpg")
	pattern2 = pattern2.resize((width, height), Image.ANTIALIAS)
	# plt.imshow(pattern2)
	# plt.show()
	r2,g2,b2 = pattern2.split()

	new2 = Image.merge("RGB", (g2,g,b))
	# plt.imshow(new2)
	# plt.show()
	return new2

def filter3(image):
	# dog = Image.open("dog.jpg")
	pattern3 = Image.open("pattern3.jpg")
	pattern3 = pattern3.resize((width, height), Image.ANTIALIAS)
	# plt.imshow(image)
	# plt.show()
	r,g,b = image.split()

	# plt.imshow(pattern3)
	# plt.show()
	r3,g3,b3 = pattern3.split()

	new3 = Image.merge("RGB", (b3,g,b))
	# plt.imshow(new3)
	# plt.show()
	return new3

def filter4(image):
	# dog = Image.open("dog.jpg")
	pattern4 = Image.open("pattern4.jpg")
	pattern4 = pattern4.resize((width, height), Image.ANTIALIAS)
	# plt.imshow(image)
	# plt.show()
	r,g,b = image.split()

	# plt.imshow(pattern4)
	# plt.show()
	r4,g4,b4 = pattern4.split()

	new4 = Image.merge("RGB", (r4,g,b))
	# plt.imshow(new4)
	# plt.show()
	return new4

if __name__ == '__main__':
	dog = Image.open("dog.jpg")
	filter1(dog)
	filter2(dog)
	filter3(dog)
	filter4(dog)
	