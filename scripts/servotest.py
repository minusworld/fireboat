import time

# servo0 = pan
# servo1 = tilt
servo0_max = 160
servo0_min = 80
servo1_max = 160
servo1_min = 100

servo0_position = servo0_min
servo1_position = servo1_min

motion = 'pan' # values of pan or tilt

servo0_direction = 'up' # values of up or down
servo1_direction = 'up' # values of up or down

servo0_flag = False
servo1_flag = False

fire_inView = False
fire_targeted  = False


while not fire_inView:
	if motion == 'pan' and servo0_direction == 'up':
		servo0_position += 10
		servo0_flag = True
	elif motion == 'pan' and servo0_direction == 'down':
		servo0_position -= 10
		servo0_flag = True
	elif motion == 'tilt' and servo1_direction == 'up':
		servo1_position += 10
		motion = 'pan'
		servo1_flag = True
	elif motion == 'tilt' and servo1_direction == 'down':
		servo1_position -= 10
		motion = 'pan'
		servo1_flag = True

	

	#send position to servo server
	with open('/dev/servoblaster', 'a') as f:
		if servo0_flag:
			f.write('0=%d\n' % servo0_position)
			servo0_flag = False
		elif servo1_flag:
			f.write('1=%d\n' % servo1_position)
			servo0_flag = False
	
	time.sleep(1)

	if servo0_position > servo0_max:
		servo0_direction = 'down'
		servo0_position -= 10
		motion = 'tilt'
	elif servo0_position < servo0_min:
		servo0_direction = 'up'
		servo0_position += 10
		motion = 'tilt'
	elif servo1_position > servo1_max:
		servo1_direction = 'down'
		servo1_position -= 10
		motion = 'pan'
	elif servo1_position < servo1_min:
		servo1_direction = 'up'
		servo1_position += 10
		motion = 'pan'

	#search for fire somehow
	#if (somehow see fire)
	#	fire_inView = True


#while not fire_targeted:
	#do fine tuning of pan-tilt to center fire
