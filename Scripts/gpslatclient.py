#!/usr/bin/env python
import sys
import rospy
from gpspac.srv import *
print('client started')
def latval():   	
    rospy.wait_for_service('lat')
    try:
        lat=rospy.ServiceProxy('lat',gpslat)
        resp=lat()
        print('PrintGPS:',resp)
    except rospy.ServiceException, e:
        print('Service failed')
if __name__=='__main__':
	latval()
