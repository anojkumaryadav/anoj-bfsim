#!/usr/bin/env python

import rospy
# from goal_publisher.msg import GoalPoin
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates
from tf.transformations import euler_from_quaternion
from math import sqrt, atan2



class NavCob():
    def __init__(self):
        self.list = []
        self.x = 0
        self.y = 0
        self.theta = 0
        self.pub = rospy.Publisher("/base/twist_mux/command_teleop_keyboard", Twist, queue_size=10)
        rospy.init_node("Cob_Goal")
        rospy.Subscriber("/gazebo/model_states", ModelStates,self.position)
        rospy.sleep(1)

    def position(self, msg):
        self.x = msg.pose[3].position.x
        self.y = msg.pose[3].position.y
        rot_q = msg.pose[3].orientation

        (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])  # we find yaw angle self.theta

    def euclidean_dist(self, goal_x, goal_y):  # funct to find euclidean dist
        return sqrt(pow((goal_x - self.x), 2) + pow((goal_y - self.y), 2))

    def desired_angle_goal(self, goal_x, goal_y):
        return atan2(goal_y - self.y, goal_x - self.x)

    def move_to_goal(self):

        goal_list = [{'x': 0 , 'y': 5,},{'x': -5, 'y': 5}, {'x': 5, 'y': 5}]
        vel = Twist()
        r = rospy.Rate(2)
        for i in range(len(goal_list)):
            goal_x = goal_list[i]['x']
            goal_y = goal_list[i]['y']
            print('goal_point x', goal_x)
            print('goal_point y', goal_y)

            while self.euclidean_dist(goal_x, goal_y) > 0.1:
                # 8 conditions to perform certain task according to the laser data
                if abs(self.desired_angle_goal(goal_x, goal_y) - self.theta) > 0.5:

                        vel.linear.x = 0
                        vel.angular.z = 0.5
                else:
                        vel.linear.x = 0.5
                        vel.angular.z = 0.0
                self.pub.publish(vel)
                r.sleep()
            vel.linear.x = 0
            vel.angular.z = 0
            self.pub.publish(vel)
            r.sleep()



if __name__ == '__main__':
    obj = NavCob()
    obj.move_to_goal()
