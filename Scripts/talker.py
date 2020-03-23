#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial

ser=serial.Serial('/dev/ttyUSB0',4800)
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
      while 1:
            data= ser.readline()
            data= data.decode()
            if data[0:6]=='$GPGGA':
    
                 Latitude=str(data[14:23])
                 Longitude=str(data[26:36])
                 
                 pub.publish(Latitude)
                
                 pub.publish(Longitude)
                 rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
