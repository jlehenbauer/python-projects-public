from PIL import Image
import os

path = 'test_images'
new_path = 'image_project'
filenames = os.listdir(path)

for file in filenames:
	img = Image.open(path + '/' + file)
	img.rotate(-90).resize((128,128)).save(new_path + '/' + file[:-4] + ".png")
	img.close()
