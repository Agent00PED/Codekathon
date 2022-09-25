#เปิดปิดไฟในที่นี้จะเป็นการใช้ blynk python สั่งเข้าสู่ blynk clound ที่สร้างไว้
import BlynkLib
import socket
import RPi.GPIO as GPIO

#set GPIO pinout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO 17 or Pin 11
gpiopin = 17
#setup pins as input
GPIO.setup(gpiopin, GPIO.IN)

#cloud server
BLYNK_TEMPLATE_ID = 'TMPLJQladeJB'
BLYNK_DEVICE_NAME = 'Test01'
BLYNK_AUTH = '8kbXXufX8hc48XkF-xHtRphcZpLr70Zf'

blynk = BlynkLib.Blynk(BLYNK_AUTH)

#for data stream Virtual Pin V0
@blynk.on('V0')
def S1_write_handler(value):
print("value v0 = {}".format(value[0]))
if int(value[0]) == 1:
    print('LED on')
    GPIO.setup(gpiopin, GPIO.OUT)
    GPIO.output(gpiopin, GPIO.HIGH)
else :
    print('LED off')
    GPIO.setup(gpiopin, GPIO.OUT)
    GPIO.output(gpiopin, GPIO.LOW)
@blynk.on("connected")
def blynk_connected():
print('Updating values from the server...')
#sync virtual pin V0
blynk.sync_virtual(0)
if __name__ == "__main__":
    while True:
        try:
            blynk.run()
        except socket.error as e:
            print(e)
            blynk.connect()