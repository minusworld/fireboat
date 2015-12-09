import time
import targeting
import os


class ServoControl:

    def __init__(self):
        self.servo0_max = 150
        self.servo0_min = 80
        self.servo1_max = 150
        self.servo1_min = 100

        self.servo0_position = servo0_min
        self.servo1_position = servo1_min

        self.motion = 'pan' # values of pan or tilt

        self.servo0_direction = 'up' # values of up or down
        self.servo1_direction = 'up' # values of up or down

	    self.fire_inView = False
	    self.fire_targeted  = False

        self.servo_out(0, self.servo0_position)
        time.sleep(1)
        self.servo_out(1, self.servo1_position)

    def servo_out(self, servoNum, servoValue):
        with open('/dev/servoblaster', 'a') as f:
            f.write('%d=%d\n' % (servoNum, servoValue))

    def step(self):
        if not fire_inView:
            if motion == 'pan' and servo0_direction == 'up':
                servo0_position += 10
                servo_out(0, servo0_position)
            elif motion == 'pan' and servo0_direction == 'down':
                servo0_position -= 10
                servo_out(0, servo0_position)
            elif motion == 'tilt' and servo1_direction == 'up':
                servo1_position += 10
                motion = 'pan'
                servo_out(1, servo1_position)
            elif motion == 'tilt' and servo1_direction == 'down':
                servo1_position -= 10
                motion = 'pan'
                servo_out(1, servo1_position)

            time.sleep(1)

            score = (-1, -1)    # needed for scoping. score format: (grid_index, grid_score)
            try:
                score = targeting.target_from_file("test0.png")
            except FileNotFoundError as e:
                return  
                
            if servo0_position > servo0_max:
                servo0_direction = 'down'
                servo0_position -= 10
                servo_out(0, servo0_position)
                motion = 'tilt'
            elif servo0_position < servo0_min:
                servo0_direction = 'up'
                servo0_position += 10
                servo_out(0, servo0_position)
                motion = 'tilt'
            elif servo1_position > servo1_max:
                servo1_direction = 'down'
                servo1_position -= 10
                servo_out(1, servo1_position)
                motion = 'pan'
            elif servo1_position < servo1_min:
                servo1_direction = 'up'
                servo1_position += 10
                servo_out(1, servo1_position)
                motion = 'pan'

            time.sleep(1)
