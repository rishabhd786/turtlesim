#!/usr/bin/env python
import sys
import rospy
from catkin_ws2.srv import turtle,turtle_req

def main():
    rospy.init_node('client')
    rospy.wait_for_service('number')
    num = rospy.ServiceProxy('number',turtle)
    x = int(input("Enter Number : "))  
    request=turtle_req(x)
    response=num(request)
    
    return response

if __name__ == "__main__":
	main()