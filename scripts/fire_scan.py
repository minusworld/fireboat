import time
import targeting
import os


class ServoControl:

    def __init__(self):
        self.servo0_max = 150
        self.servo0_min = 80
        self.servo1_max = 150
        self.servo1_min = 100

        self.servo0_position = self.servo0_min
        self.servo1_position = self.servo1_min

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
        if not self.fire_inView:
            if self.motion == 'pan' and self.servo0_direction == 'up':
                self.servo0_position += 10
                self.servo_out(0, self.servo0_position)
            elif self.motion == 'pan' and self.servo0_direction == 'down':
                self.servo0_position -= 10
                self.servo_out(0, self.servo0_position)
            elif self.motion == 'tilt' and self.servo1_direction == 'up':
                self.servo1_position += 10
                motion = 'pan'
                self.servo_out(1, self.servo1_position)
            elif self.motion == 'tilt' and self.servo1_direction == 'down':
                self.servo1_position -= 10
                self.motion = 'pan'
                self.servo_out(1, self.servo1_position)

            time.sleep(1)

            score = (-1, -1)    # needed for scoping. score format: (grid_index, grid_score)
            try:
                score = targeting.target_from_file("test0.png")
		        print(score)
            except FileNotFoundError as e:
                return  
                
            if self.servo0_position > self.servo0_max:
                self.servo0_direction = 'down'
                self.servo0_position -= 10
                self.servo_out(0, self.servo0_position)
                self.motion = 'tilt'
            elif self.servo0_position < self.servo0_min:
                self.servo0_direction = 'up'
                self.servo0_position += 10
                self.servo_out(0, self.servo0_position)
                self.motion = 'tilt'
            elif self.servo1_position > self.servo1_max:
                self.servo1_direction = 'down'
                self.servo1_position -= 10
                self.servo_out(1, self.servo1_position)
                self.motion = 'pan'
            elif self.servo1_position < self.servo1_min:
                self.servo1_direction = 'up'
                self.servo1_position += 10
                self.servo_out(1, self.servo1_position)
                self.motion = 'pan'

            time.sleep(1)
