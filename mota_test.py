import RPi.GPIO as GPIO
import time
import serial
ser = serial.Serial("/dev/ttyACM0",9600)
ser.close()
ser.open()
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
if ser==1:
	while(True):
		GPIO.output(19, True)
		time.sleep(1)
		GPIO.output(19, False)
		time.sleep(1)
	else:
		while(True):
			GPIO.output(19, True)
			time.sleep(2)
			GPIO.output(19, False)
			time.sleep(2)
