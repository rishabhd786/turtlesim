#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
from catkin_ws2.srv import turtle,turtle_req
PI = 3.141592653589

def line(direc,distance):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
  

    vel_msg.linear.x = 1*direc
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    speed=1
    

        
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
      
    while(current_distance < distance):
           
        velocity_publisher.publish(vel_msg)
           
        t1=rospy.Time.now().to_sec()
            
        current_distance= speed*(t1-t0)
    vel_msg.linear.x=0
    velocity_publisher.publish(vel_msg)
def angle(sense,angle):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
  

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 1*sense
    angular_speed=1
    

    t0 = rospy.Time.now().to_sec()
    current_angle = 0
        
    while(current_angle< angle):
           
        velocity_publisher.publish(vel_msg)
            
        t1=rospy.Time.now().to_sec()
           
        current_angle= angular_speed*(t1-t0)
    vel_msg.angular.z=0
    velocity_publisher.publish(vel_msg)

def handle_string_usr(request):
    response=turtle_req()
    response.b=request.a
    num=response.b
    if num==1:
     angle(1,PI/2)
     line(1,4)
     angle(1,3*PI/4)
     line(1,1)
    if num==2:
     line(1,2)
     angle(-1,PI/2)
     line(1,2)
     angle(-1,PI/2)
     line(1,2)
     angle(1,PI/2)
     line(1,2)
     angle(1,PI/2)
     line(1,PI/2)
    if num==3:
     line(1,2)
     angle(-1,PI/2)
     line(1,2)
     angle(-1,PI/2)
     line(1,2)
     angle(1,PI)
     line(1,2)
     angle(-1,PI/2)
     line(1,2)
     angle(-1,PI/2)
     line(1,2)


def main():
    rospy.init_node('server')
    num = rospy.Service('number', turtle, inpfunc)
    rospy.spin()

if __name__ == "__main__":
    main() 
