#ชุดคำสั่งเปิดหลอดไฟ
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print("ไฟ LED เปิด")
GPIO.output(17,GPIO.HIGH)