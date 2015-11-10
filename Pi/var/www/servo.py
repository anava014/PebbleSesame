import serial
import requests
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

while True:
	isUnlocked = requests.get('http:#######.us-west-2.compute.amazonaws.com/doorState.txt')
	if(int(isUnlocked.text) == 1):
		port.write("1");
	else:
		port.write("0");

	#print (isUnlocked.text)
	time.sleep(1)
