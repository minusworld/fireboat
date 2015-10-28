#!/usr/bin/env python

import os
from fireboat.srv import *
import rospy
import wiringpi2 as wpi

_OUTPUT=1
_PIN=7

def pump_control_callback(req):
    d = {
        True: 1,
        False: 0
    }
    rospy.set_param("pump_state", req.on)
    #os.system("gpio write 7 {0}".format(d[req.on]))
    val = wpi.digitalWrite(_PIN, d[req.on])
    return True

def init_pump_control():
    #os.system("gpio mode 7 out")
    wpi.wiringPiSetup()
    wpi.pinMode(_PIN, _OUTPUT)
    rospy.set_param("pump_state", False)
    rospy.init_node("pump_control")
    s = rospy.Service("pump_control", PumpControl, pump_control_callback)
    rospy.spin()

if __name__=='__main__':
    init_pump_control()
