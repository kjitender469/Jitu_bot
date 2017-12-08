#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#global vel_msg 


from pynput import keyboard
print('--------------------------------')
print('Use arrow keys to move the Robot')

def on_press(key):
	#print('{0} pressed'.format(key))
	#print('starting............')
	var='{0}'.format(key)
	#print(type(var))
	#print(var)
	#print('ending.............')
	
	if var=='Key.down':
		#print('aaj mai niche')
		#rospy.init_node('control_bot', anonymous=True)
		velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
		vel_msg= Twist()
		vel_msg.linear.x = -2
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0
		#print('value is assigned')
		velocity_publisher.publish(vel_msg)
		
		"""
		while not rospy.is_shutdown():

        #Setting the current time for distance calculus
			t0 = rospy.Time.now().to_sec()
			current_distance = 0

        #Loop to move the turtle in an specified distance
		while(current_distance < distance):
            #Publish the velocity
			velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
			t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
			current_distance= speed*(t1-t0)
        #After the loop, stops the robot
			vel_msg.linear.x = 0
			rospy
        #Force the robot to stop
			velocity_publisher.publish(vel_msg)		"""
    
	elif var=='Key.up':
		velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
		vel_msg= Twist()
		vel_msg.linear.x = 2
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0
		#print('value is assigned for up key')
		velocity_publisher.publish(vel_msg)
		
	elif var=='Key.left':
		#print('aaj mai baye')
		velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
		vel_msg= Twist()
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 40
		#print('value is assigned for up key')
		velocity_publisher.publish(vel_msg)
	elif var=='Key.right':
		#print('aaj mai daye')
		velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
		vel_msg= Twist()
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = -40
		#print('value is assigned for up key')
		velocity_publisher.publish(vel_msg)	

def on_release(key):
	#print('starting...release............')
	var='{0}'.format(key)
	#print(type(var))
	#print(var)
	#print('ending...release.............')
    #print('{0} release'.format(key))
	velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
	vel_msg= Twist()
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)

def monitor():
	rospy.init_node('control_bot', anonymous=True)
	velocity_publisher = rospy.Publisher('/jitu_bot/cmd_vel', Twist, queue_size=10)
	vel_msg= Twist()
	with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:listener.join()
	rospy.spin()
	


if __name__ == '__main__':
	monitor()




    
    
  
   
 
    
  

