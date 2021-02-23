#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import PoseStamped


class talker:
	def __init__(self):
		rospy.init_node('publisher',anonymous=True)
		self.pub=rospy.Publisher('publish_topic',PoseStamped,queue_size=10)
		self.rate = rospy.Rate(15) 

	def run (self):
		Coordonnee = PoseStamped()
		print (Coordonnee)

		Coordonnee.pose.position.x = 0
		Coordonnee.pose.position.y = 0

		a = 0

		while not rospy.is_shutdown():
			if (Coordonnee.pose.position.x == 0 & Coordonnee.pose.position.y == 0):
				while (Coordonne.pose.position.y != 6 ):
					Coordonnee.pose.position.y = a
					a = a + 1
					pub.publish(Coordonnee)
					rate.Sleep()

				while (Coordonne.pose.position.y != 0):
					Coordonnee.pose.position.y = a
					b = b + 1
					pub.publish(Coordonnee)
					rate.Sleep()

			elif (Coordonnee.pose.position.x == 6 & Coordonne.pose.position.y == 6 ):
				while (Coordonnee.pose.position.y !=6 ):
					Coordonnee.pose.position.x = b 
					b = b + 1
					pub.publish(Coordonnee)
					rate.sleep

	pub.publish(Coordonnee)
	rate.sleep()

if (__name__ == '__main__'):
	try:
		node=talker()
		node.run()
	except rospy.ROSInterruptException:
		pass
