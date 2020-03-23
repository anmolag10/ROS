#!/usr/bin/env python
from gpspac.srv import *
import rospy
import serial
ser=serial.Serial('/dev/ttyUSB0',4800)
ser.flushInput()
def lat(req):
  while True:
   data= ser.readline()
   data= data.decode()
   if data[0:6]=='$GPGGA':
     lat=data[14:23]
     lat = float(lat)
     print('packagestored')
     return gpslatResponse(lat)
def latserver():
    rospy.init_node('latserver')
    s=rospy.Service('lat',gpslat,lat)
    rospy.spin()
if __name__=='__main__':
    latserver()
