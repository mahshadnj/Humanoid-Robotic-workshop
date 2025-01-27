/*

Author: Mahshad Nazari
Date: 06/03/2022
Name: First C++ Subscriber

*/

#include <ros/ros.h>
#include <std_msgs/Int64.h>

int counter = 0;
ros::Publisher pub;

void callback_number(const std_msgs::Int64& msg)
{
	ROS_INFO("%d", msg.data);
}

int main (int argc, char **argv)
{
	ros::init(argc, argv, "number_counter");
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("/number", 1000, callback_number);

	ros::spin();
}
