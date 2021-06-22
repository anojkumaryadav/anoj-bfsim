#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

rospy.init_node('frwd')
pub = rospy.Publisher("/robot1/cmd_vel", Twist, queue_size=10)

rate = rospy.Rate(2)
vel = Twist()
rate.sleep()
for i in range(1000):
    
    
    vel.angular.z=0.0
    t0 = rospy.get_rostime()
    while rospy.get_rostime() -t0 <= rospy.Duration(10):
        vel.linear.x = 0.5
        pub.publish(vel)
        rospy.loginfo(vel)
    t1 = rospy.get_rostime()
    while rospy.get_rostime() -t1 <= rospy.Duration(2):
        vel.linear.x = 0.0
        pub.publish(vel)
        rospy.loginfo(vel)
    rospy.sleep(1)
    t2 = rospy.get_rostime()
    while rospy.get_rostime() -t2 <= rospy.Duration(10):
        vel.linear.x = -0.5
        pub.publish(vel)
        rospy.loginfo(vel)
    t3 = rospy.get_rostime()
    while rospy.get_rostime() -t3 <= rospy.Duration(2):
        vel.linear.x = 0.0
        rospy.loginfo(vel)
        pub.publish(vel)
    rospy.sleep(1)

      
