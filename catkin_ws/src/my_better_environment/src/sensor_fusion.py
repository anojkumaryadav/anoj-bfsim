#!/usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan

class SensorFusion():

    def __init__(self):

        rospy.init_node("Sensor_Fusion")
        rospy.Subscriber('/robot1/scan', LaserScan, self.lidar_1)
        rospy.Subscriber('/robot2/scan', LaserScan, self.lidar_2)
        rospy.Subscriber('/robot3/scan', LaserScan, self.lidar_3)
        rospy.sleep(1)

