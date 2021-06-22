#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians


class move_cob():
    def __init__(self):
        # initiliaze
        rospy.init_node('frwd_1')
        cmd_vel = rospy.Publisher('/base/twist_mux/command_teleop_keyboard', Twist, queue_size=10)
        r = rospy.Rate(5) 
        move_cmd = Twist()  

        while not rospy.is_shutdown():

            rospy.loginfo("Going Straight")
            for x in range(0,225):  
                move_cmd.linear.x = 0.2
                cmd_vel.publish(move_cmd)
                r.sleep()
                
            for z in range(0,10):
            	
            	move_cmd.linear.x = 0.0
            	move_cmd.angular.z = 0.0
            	cmd_vel.publish(move_cmd)
            	r.sleep()
            
            rospy.loginfo("Turning")
            for y in range(0, 20):  
                move_cmd.angular.z= radians(45)
                cmd_vel.publish(move_cmd)
                r.sleep()
                
            for i in range(0,10):
            	
            	move_cmd.linear.x = 0.0
            	move_cmd.angular.z = 0.0
            	cmd_vel.publish(move_cmd)
            	r.sleep()



if __name__ == '__main__':
    try:
        move_cob()
    except:
        rospy.loginfo("node terminated.")
