 '''Python 3 program to find the images in the given range of given points of interests'''
from distance import *
import csv


file1 = open("assets.csv", 'r')
reader = csv.reader(file1)

i = 0
'''lili: list of list of coordinates with the image name'''
lili = []

for data in reader:
    #print(data)
    i = i+1
    if i==1:
        z = data[0]
        x = data[1]
        c = data[2]
        v = data[3]
        li = [z,x,c,v]
        lili.append(li)
        #writer.writerow(li)
        continue
    name = data[0]
    long = data[1]
    lat = data[2]
    li = [name,long,lat]
    with open("coordinates.csv", 'r') as images:
        csv_reader = csv.reader(images)

        for image in csv_reader:
            #print(image)
            #image = image.read().split(",")
            img_name = image[0]
            if image[1]:
                img_lat = image[1]
            if image[2]:
                img_long = image[2]

            #print(img_lat)
            dist = distance(float(lat),float(img_lat),float(long),float(img_long))
            #print(img_name)
            if(dist<=50):
                li.append(img_name)
        lili.append(li)

file2 = open("assets.csv", 'w')
writer = csv.writer(file2)
for i in range(len(lili)):
    writer.writerow(lili[i])
