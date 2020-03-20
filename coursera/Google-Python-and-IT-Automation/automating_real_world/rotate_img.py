from PIL import Image
import sys


def rotate():
	img = str(sys.argv[1])
	if img == "":
		print("Please try again.")
		return 0

	image = Image.open(img)
	image.rotate(45).show()

if __name__ == "__main__":
	rotate()