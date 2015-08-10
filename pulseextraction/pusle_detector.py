import cv2
from PIL import Image
import sys
from graph import PlotGraph
from config import assets_path

__author__ = "Akas Antony"
__version__ = "1.0.0"
__maintainer__ = "Akas Antony"
__email__ = "antony.akas@gmail.com"

def makeFrame():
	video_path = raw_input("Enter video path:\n")
	vidcap = cv2.VideoCapture(video_path)
	success,image = vidcap.read()
	global countImgs
	countImgs = 0
	print "Extracting frames from video %s..."%video_path
	while success:
	    success,image = vidcap.read()
	    cv2.imwrite(assets_path+"frames/frame%d.jpg"%countImgs,image)
	    print "Finished extracting frame %d...\r"%countImgs,
	    countImgs += 1
	print "Done extracting frames."
	calcIntensity()

def calcIntensity():
	data_file = open(assets_path+'out/data.dat','w')
	print "Finding intensity of image..."
	for i in range(0,countImgs-1):
		pic = Image.open(assets_path+"frames/frame%d.jpg"%i)
		imgData = pic.load()
		print "Getting data of image frame%d.jpg \r"%i,
		r,count  = 0,0
		for x in xrange(pic.size[0]):
		    for y in xrange(pic.size[1]):
		        tempr,tempg,tempb = imgData[x,y]
		        r += tempr
		        count += 1
		data_file.write(str(r/count)+'\n')
	data_file.close()
makeFrame()
plotGraph = PlotGraph();
plotGraph.plot(assets_path+'out/data.dat')
