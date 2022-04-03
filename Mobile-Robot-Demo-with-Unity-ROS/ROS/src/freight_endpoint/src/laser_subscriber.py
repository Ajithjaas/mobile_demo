#!/usr/bin/env python
import numpy as np
import rospy
from sensor_msgs.msg import LaserScan

range = np.empty()

def callback(scan):
    print(scan)
    
def listener():
    rospy.init_node('laser_subscriber')
    rospy.Subscriber("base_scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
