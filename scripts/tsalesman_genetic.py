#!/usr/bin/env python
# coding=utf-8


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import numpy
import matplotlib.pyplot as plt
import ctypes

class Cordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @staticmethod
    def get_distance(a,b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    @staticmethod

    def get_total_dist(cords):
        dist=0
        for first, second in zip(cords[:-1],cords[1:]):
            dist += Cordinate.get_distance(first,second)
        dist+=Cordinate.get_distance(cords[0],cords[-1])
        return dist


robot_cordinates = [[ -7, 1, -2, -3, -9], [ 4, 3, -0.5, 1, -1]]
cords = []

initial_pose=(-4,5)
for i in range(1):
    for j in range(5):
        cords.append(Cordinate(robot_cordinates[i][j], robot_cordinates[i + 1][j]))

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
for first, second in zip(cords[:-1],cords[1:]):
    ax1.plot([first.x, second.x],[first.y, second.y],'b')
ax1.plot([cords[0].x,cords[-1].x],[cords[0].y, cords[-1].y],'b')

for c in cords:
    ax1.plot(c.x,c.y,'ro')

cost0=Cordinate.get_total_dist(cords)
T=30
factor=0.99
T_init=T
final_route=[]
final_route.append(initial_pose)
for i in range(500):
    print(i,"cost =", cost0)

    T=T*factor
    for j in range(500):

        r1,r2=numpy.random.randint(0,len(cords),2)
        temp=cords[r1]
        cords[r1]=cords[r2]
        cords[r2]=temp

        cost1=Cordinate.get_total_dist(cords)
        #swapping
        if cost1<cost0:
            cost0=cost1
        else:
            x=numpy.random.uniform()
            if x< numpy.exp((cost0-cost1)/T):
                cost0=cost1
            else:
                temp=cords[r1]
                cords[r1]=cords[r2]
                cords[r2]=temp


    #plot the result

for first, second in zip(cords[:-1],cords[1:]):
    ax2.plot([first.x, second.x],[first.y, second.y],'b')
ax2.plot([cords[0].x,cords[-1].x],[cords[0].y, cords[-1].y],'b')
for c in cords:
    point=(c.x,c.y)
    final_route.append(point)
    ax2.plot(c.x,c.y,'ro')

print("Final Route from initial position: " + str(final_route))
#plt.show()



def movebase_client(inp):
   
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
 
    if inp == 0:
        print("Point 1: " +str(final_route[1]))
        goal.target_pose.pose.position.x = final_route[1][0]
        goal.target_pose.pose.position.y = final_route[1][1]
        goal.target_pose.pose.position.z = 0.0  
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0
    elif inp == 1:
        print("Point 2: " +str(final_route[2]))
        goal.target_pose.pose.position.x = final_route[2][0]
        goal.target_pose.pose.position.y = final_route[2][1]
        goal.target_pose.pose.position.z = 0.0  
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0    
    elif inp == 2:
        print("Point 3: " +str(final_route[3]))
        goal.target_pose.pose.position.x = final_route[3][0]
        goal.target_pose.pose.position.y = final_route[3][1]
        goal.target_pose.pose.position.z = 0.0  
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0 
    elif inp == 3:
        print("Point 4: " +str(final_route[4]))
        goal.target_pose.pose.position.x = final_route[4][0]
        goal.target_pose.pose.position.y = final_route[4][1]
        goal.target_pose.pose.position.z = 0.0  
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0 
    else:
        print("Point 5: " +str(final_route[5]))
        goal.target_pose.pose.position.x = final_route[5][0]
        goal.target_pose.pose.position.y = final_route[5][1]
        goal.target_pose.pose.position.z = 0.0  
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

    

    client.send_goal(goal)

    bekle = client.wait_for_result()
   
    if not bekle:
        rospy.signal_shutdown("No Action Servicel!")
   
    else:
        return client.get_result()   
    
if __name__ == '__main__':
    try:
        for i in range(0,5):
            rospy.init_node('movebase_client_py')
            result = movebase_client(i)

        else:
            rospy.loginfo("Go to point...")
    except rospy.ROSInterruptException:
        pass