#!/usr/bin/python

import rospy
from gazebo_msgs.msg import ModelStates


class HumanWalk:

    def __init__(self):

        rospy.init_node('walk')
        self.human_location = None
        rospy.Subscriber('/gazebo/model_states', ModelStates, self.gazebo_pose)
        #self.pub = rospy.Publisher('/gazebo/model_states', ModelStates, queue_size=10)
        rospy.sleep(1)


    def gazebo_pose(self, gaz) :

        print(gaz)
        print(gaz.pose[1].position.x)


    def walk_human(self):
        move = ModelStates()
        print(move.pose[1].position.x)


if __name__ == '__main__':

    obj = HumanWalk()
    #obj.walk_human()