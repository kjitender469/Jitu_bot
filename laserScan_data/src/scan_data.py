#!/usr/bin/env python
import rospy, math, random
import numpy as np
from sensor_msgs.msg import LaserScan
from laser_geometry import LaserProjection
import sensor_msgs.point_cloud2 as pc2

class Lidar():
	def __init__(self, scan_topic="/jitu_bot/base_laser_link/scan"):
		self.scan_sub = rospy.Subscriber(scan_topic, LaserScan, self.on_scan)
		print(self.scan_sub)
		self.laser_projector = LaserProjection()

	def on_scan(self, scan):
		rospy.loginfo("Got scan, projecting")
		cloud = self.laser_projector.projectLaser(scan)
		gen = pc2.read_points(cloud, skip_nans=True, field_names=("x", "y", "z"))
		self.xyz_generator = gen
#if __name__ == '__main__':
	
