import time
import targeting
import os

def servo_out(servoNum, servoValue):
	with open('/dev/servoblaster', 'a') as f:
		f.write('%d=%d\n' % (servoNum, servoValue))

def main():
	import time

	# servo0 = pan
	# servo1 = tilt
	servo0_max = 150
	servo0_min = 80
	servo1_max = 150
	servo1_min = 100

	servo0_position = servo0_min
	servo1_position = servo1_min

	motion = 'pan' # values of pan or tilt

	servo0_direction = 'up' # values of up or down
	servo1_direction = 'up' # values of up or down

	fire_inView = False
	fire_targeted  = False

	servo_out(0, servo0_position)
	time.sleep(1)
	servo_out(1, servo1_position)

	while not fire_inView:
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

        score = (-1, -1)
        try:
            score = targeting.target_from_file("test0.png")
        except FileNotFoundError as e:
            continue
            
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

	#search for fire somehow
	#if (somehow see fire)
	#	fire_inView = True


#while not fire_targeted:
	#do fine tuning of pan-tilt to center fire


if __name__ == "__main__":
    main()
