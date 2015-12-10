import os
from fire_scan import ServoControl

def pump_on():
    os.system("gpio write 7 {0}".format(1))

def pump_off():
    os.system("gpio write 7 {0}".format(0))

def go():
    servo_control = ServoControl()
    while 1:
        os.system("../bin/raspberrypi_video")
        servo_control.step()

if __name__ == "__main__":
    go()    
