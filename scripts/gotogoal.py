#!/usr/bin/env python
# coding=utf-8


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
   
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
 
    goal.target_pose.pose.position.x = -7.0
    goal.target_pose.pose.position.y = 4.0

    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)

    wait = client.wait_for_result()
   
    if not wait:
        rospy.signal_shutdown("No Action Servicel!")
   
    else:
        return client.get_result()   
    
if __name__ == '__main__':
    try:
        rospy.init_node('move_base_goal')
        result = movebase_client()
        if result:
            rospy.loginfo(" Reached to Point!")
        else:
            rospy.loginfo("Go to point...")
    except rospy.ROSInterruptException:
        pass