'''Python 3 program to find all the images in the given range of all the
instances given in the srt file of the video'''
from distance import *
import csv

fp = open("/home/himanshu/Documents/skylark/software_dev/videos/DJI_0301.SRT").read().split("\n")

#print(fp[5])

i = 1;
for i in range(1,len(fp),4):
    time = fp[i]
    pos = fp[i+1]
    lat_long = pos.split(",")
    #print(time)
    long = lat_long[0]
    lat = lat_long[1]
    li = [time]
    #print(lat+"\n")
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
            if(dist<=35):
                li.append(img_name)
        with open("result.csv", 'a') as res:
            writer = csv.writer(res)
            writer.writerow(li)
