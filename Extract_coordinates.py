'''Python 3 program to extract the latitude and longitude from the geotagged images and saving
them in an excel sheet'''
from ImageMetaData import *
import csv
from PIL import Image
import glob
import pickle
import os

coord=[]

for file in glob.glob("/home/himanshu/Documents/skylark/software_dev/images/*.JPG"):
	data = ImageMetaData(file)
	lat,long = data.get_lat_lng()
	#print(os.path.basename(file))
	coord=[os.path.basename(file),lat,long]
	with open("coordinates.csv", "a") as writeFile:
		writer = csv.writer(writeFile)
		#writer.writerow(file)
		writer.writerow(coord)
