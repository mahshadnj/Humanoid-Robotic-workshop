
''''

Author: Mahshad Nazari
Date: 06/03/2022
Topic: ROS workshop
Name: First Python Node

'''

import rospy

if __name__ == '__main__':
	rospy.init_node('my_first_python_node')
	rospy.loginfo("This node has been started")

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo("Hello")
		rate.sleep()
