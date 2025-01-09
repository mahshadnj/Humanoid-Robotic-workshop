
''''

Author: Mahshad Nazari
Date: 06/03/2022
Topic: ROS workshop
Name: First Topic (Subscriber)

'''

import rospy
from std_msgs.msg import Int64


def callback_number(msg):
	rospy.loginfo(msg.data)


if __name__ == '__main__':
	rospy.init_node('number_subscriber')
	sub = rospy.Subscriber("/number", Int64, callback_number)
	rospy.spin()
