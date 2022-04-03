#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage

def callback(img):
    print(img)
    
def listener():
    rospy.init_node('camera_subscriber')
    rospy.Subscriber("camera/color/image_raw/compressed", CompressedImage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()