import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIGGER_PIN = 20
ECHO_PIN = 21
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
def ultra():
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.000005)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.000002)
while GPIO.input(ECHO_PIN) == GPIO.LOW:
         signaloff = time.time()
while GPIO.input(ECHO_PIN) == GPIO.HIGH:
         signalon = time.time()
         timepassed = signalon - signaloff
         distance = (timepassed * 34300) / 2
         print("The distance from object is ",distance,"cm")
while True:
   ultra()
   time.sleep(1)
    
