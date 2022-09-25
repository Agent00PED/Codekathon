#เขียนโค้ด python เพื่อรับผลจากเซนเซอร์วัดอุณหภูมิและความชื้นสัมพัทธ์
#โดยในที่นี้จะเป็นการส่งผลเข้าแอพพลิเคชั่น จาก blynk ที่ได้จัดทำไว้ก่อนหน้านี้
import time
import board
import adafruit_dht
import BlynkLib
from datetime import datetime
#Blynk cloud server
BLYNK_TEMPLATE_ID = 'TMPLJQladeJB'
BLYNK_DEVICE_NAME = 'Weather'
BLYNK_AUTH = 'LFq3C_saLRaIQRQtzdxhgIY6o28Oug8F'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4) #GPIO 4 or pin 7
while True:
    #run the Blynk
    blynk.run()
    try:
        # Get the current temperature value in Celcius
        temperature_c = dhtDevice.temperature
        # Convert the current temperature value in Celcius to Farenheit
        temperature_f = temperature_c * (9 / 5) + 32
        # Get the humidity value
        humidity = dhtDevice.humidity
        # print the values to the screen
        print(
            "Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        # send the values to Blynk cloud server using the specific virtual pin
        blynk.virtual_write(0, temperature_c) #Virtual Pin V0
        blynk.virtual_write(1, humidity) #Virtual Pin V1
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        blynk.virtual_write(2, dt_string) #Virtual Pin V2
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print("Error : {}".format(error.args[0]))
        time.sleep(2.0)
        continue
    except Exception as error:
        print("divce error")
        dhtDevice.exit()
        raise error
    time.sleep(2.0)