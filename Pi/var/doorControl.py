import RPi.GPIO as GPIO
import time
from subprocess import call
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Waiting for button press...")

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print('Button Pressed')
		#Magic Happens
		call(["./takePic.sh"])
		call(["./converter.sh"])
		print("Uploading Picture to the world")
		call(["./imgurbash.sh", "currentPicture.png"])
		print("Success!");
		requests.get('http://############.us-west-2.compute.amazonaws.com/state.php?state=1')
		print("Waiting for button press...");
		while input_state == False:
			input_state = GPIO.input(18)
		time.sleep(0.5);
