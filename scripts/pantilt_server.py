#!/usr/bin/env python

import os
from fireboat.srv import *
import rospy

servoblaster = "/dev/servoblaster"

def pan_tilt_control_callback(degree, direction):
    if(direction == 0){
        rospy.set_param("pan_tilt_Y_direction", direction)

    }
    elif(direction == 1){
        rospy.set_param("pan_tilt_X_direction", direction)
    }
    os.system("echo %d=%d > %s" % (direction, degree, servoblaster))
    return True

def init_tilt_control():
    #os.system("gpio mode 7 out")
    rospy.set_param("pan_tilt_X_direction", 0)
    rospy.set_param("pan_tilt_Y_direction", 0)
    rospy.init_node("pan_tilt_control")
    s = rospy.Service("pan_tilt_control", PumpControl, pan_tilt_control_callback)
    rospy.spin()

if __name__=='__main__':
    init_tilt_control()
