#!/usr/bin/env python

import sys
from fireboat.srv import PumpControl
import rospy
MIN = 60
MAX = 220
HORZ_PIN=0
VIRT_PIN=1
def pan_tilt_control_client(degree, direct):
    rospy.wait_for_service("pan_tilt_control")
    try:
        sp_pan_tilt_control = rospy.ServiceProxy("pan_tilt_control", PumpControl)
        success = sp_pan_tilt_control(degree, direct)
        return success
    except rospy.ServiceException, e:
        print "service call failed: {0}".format(e)

if __name__=='__main__':
    
    if len(sys.argv) == 3:
        degree = int(sys.argv[2])
        direct = sys.argv[1].lower()
        if(MIN <= degree <= MAX){
            if(direct = "up"){
                direct = VIRT_PIN
            }
            elif(direct == "down"){
                direct = VIRT_PIN
                degree = -degree
            }
            elif(direct == "left"){
                direct = HORZ_PIN
            }
            elif(direct == "right"){
                direct = HORZ_PIN
                degree = -degree
            }
            if((direct == VIRT_PIN or direct ==HORZ_PIN) and typeof(degree) == int){
                print pan_tilt_control_client(degree, direct)
            }
        }
        else{
            print ("The servos have a range of %d and %d." % (MIN, MAX))
        }
    else{
        print ("Syntax: pantilt_client.py {up|down|left|right} {degree of rotataion}")
    }