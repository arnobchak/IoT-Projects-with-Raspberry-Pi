import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED_PIN=21
BUTTON_PIN=20
GPIO.setup(LED_PIN,GPIO.IN)
GPIO.setup(BUTTON_PIN,GPIO.IN)
pull_up_down=GPIO.PUD_DOWN
while True:
    if GPIO.input(BUTTON_PIN)==GPIO.HIGH:
        GPIO.output(LED_PIN,GPIO.HIGH)
    else:
        GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)