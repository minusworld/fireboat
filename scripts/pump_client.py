#!/usr/bin/env python

import sys
from fireboat.srv import PumpControl
import rospy

def pump_control_client(on):
    rospy.wait_for_service("pump_control")
    try:
        sp_pump_control = rospy.ServiceProxy("pump_control", PumpControl)
        success = sp_pump_control(on)
        return success
    except rospy.ServiceException, e:
        print "service call failed: {0}".format(e)

if __name__=='__main__':
    d = {
        "on":   True,
        "true": True,
        "1" :   True,
        "off":  False,
        "false":False,
        "0" :   False
    }
    if len(sys.argv) == 2:
        print pump_control_client(d[sys.argv[1].lower()])
