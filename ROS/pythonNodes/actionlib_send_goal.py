
''''
Author: Mahshad Nazari
Date: 06/13/2022
Topic: ROS workshop
Name: First Action (Client)
'''

import rospy
import actionlib

# For each action, there is a XxAction, XxGoal, XxFeedback, XxResult
# We should import them at the beginning
# Note: We have only used Action and Goal for our client

from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction, MoveBaseResult, MoveBaseFeedback



def feedback_callback(feedback):
    print(feedback)


if __name__ == "__main__":
    rospy.init_node("goal_sender")
    # we create an object named "client" or of course anything :)\
    # the type is the XxAction we imported above
    client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
    # like client in Service, we should check if the server is available
    client.wait_for_server()
    # let's get our message ready
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 1.0
    goal.target_pose.pose.position.y = 3.0
    goal.target_pose.pose.orientation.w = 1

    # we send a goal and receive a feedback in the callback from second argument
    client.send_goal(goal, feedback_cb=feedback_callback)

    # to cancel the goal 3 seconds after start uncomment
    #time.sleep(3.0)
    #client.cancel_goal()  

    # wait until the result is obtained
    # you can do other stuff here instead of waiting
    # and check for status from time to time 
    #status = client.get_state()
    # check the client API link below for more info

    client.wait_for_result()
