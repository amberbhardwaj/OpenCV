# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:41:32 2019

@author: H307839
Parse video frame and display
"""

import cv2
#DECODER

import qrtools
qr = qrtools.QR()
#data='honeywell.png'
#qr.decode(data)
#print qr.data
print(cv2.__version__)



def FrameCaptureDefault (path):
    vidObj = cv2.VideoCapture(path)
    # Check if camera opened successfully
    if (vidObj.isOpened()== False): 
        print("Error opening video stream or file")
    count = 0
    success = True
    
    
    while success:
        success, image = vidObj.read()
     #  print("Success = ", success)
     #  if success == True:
     #      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     #      cv2.imshow('image', gray)
     #      if cv2.waitKey(25) & 0xFF == ord('q'):
     #          break
        cv2.imwrite("output/frame%d.png" % count, image)
        if count == 220:
            break
        p = " "
        qr = qrtools.QR()
        data = 'frame'+ str(count) + '.png'
        qr.decode ("output//"+data)
		print qr.data
        count +=1
         
    vidObj.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    

    
def KnowFpsCaptured():
    #Start Block: 
    #Function to get the current frame/second (only for video not for cam)
    video = cv2.VideoCapture(0);
    #video.set(cv2.cv.CV_CAP_PROP_FPS , 100)
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
    video.release()
    #End Block
    

if __name__ == '__main__':
    FrameCaptureDefault("IMG_0956.MOV")
    #KnowFpsCaptured()
    #FrameCaptureDefault ("IMG_0956.MOV");