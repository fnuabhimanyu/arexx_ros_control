#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Float64
from std_msgs.msg import String
import math 

class Arexx(object):
	def __init__(self):
		self.publishers_list=[]
		self.angle=[0,0,0,0,0,0]
		self.orientation=rospy.Publisher('/arexx/orientation_position_controller/command',Float64, queue_size=1)
		self.shoulder=rospy.Publisher('/arexx/shoulder_position_controller/command',Float64, queue_size=1)
		self.ellbow=rospy.Publisher('/arexx/ellbow_position_controller/command',Float64, queue_size=1)
		self.wrist_bend=rospy.Publisher('/arexx/wrist_bend_position_controller/command',Float64, queue_size=1)
		self.wrist_rotate=rospy.Publisher('/arexx/wrist_rotate_position_controller/command',Float64, queue_size=1)
		self.gripper=rospy.Publisher('/arexx/gripper_position_controller/command',Float64, queue_size=1)
		
		self.publishers_list.append(self.orientation)
		self.publishers_list.append(self.shoulder)
		self.publishers_list.append(self.ellbow)
		self.publishers_list.append(self.wrist_bend)
		self.publishers_list.append(self.wrist_rotate)
		self.publishers_list.append(self.gripper)

		self.j=0

	def publishAngle(self,angles):
		i=0
		for pubs in self.publishers_list:
			jointAngles=Float64()
			jointAngles.data=angles[i]
			pubs.publish(jointAngles)
			i=i+1

	
	def generateAngle(self):
		theta=(math.pi)/2
		self.angle=[0,0,0,0,0,0]
		self.angle[1]=theta                   #put no. between 0-5 to test all DOF
		self.publishAngle(self.angle)
		self.j=self.j+1
		if self.j==6:
			self.j=0


if __name__=="__main__":
	rospy.init_node('joint_publisher_node')
	rate_value = 0.2
	arexx_control=Arexx()
	rate = rospy.Rate(rate_value)
	while not rospy.is_shutdown():
		arexx_control.generateAngle()
		rate.sleep()
			
