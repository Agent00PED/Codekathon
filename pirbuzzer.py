import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #เชื่อมต่อ PIR แบบรับสัญญาณเข้า
GPIO.setup(24, GPIO.OUT) #เชื่อมต่อ Buzzer แบบส่งสัญญาณออก
try:
    # หน่วงเวลา 2 วินาทีเพื่อมรอสัญญาณจาก Sensor
    time.sleep(2)
    while True:
        #ถ้ามีสัญญาณเข้ามาที่ GPIO23 ซึ่งเชื่อมต่อกับ PIR อยู่
        if GPIO.input(23):
            #สั่งจํายไฟออกให้กับ GPIO24
            GPIO.output(24, True)
            #หน่วงเวลา 0.5 วินาทีเพื่อสั่งให้ลำโพงดัง เป็นเวลา 0.5 วินาที
            time.sleep(0.5)
            #สั่งหยุดจ่ายไฟออกให้กับ GPIO24
            GPIO.output(24, False)
            #พิมพ์ข้อความออกที่หน้าจอ
            print("พบวัตถุเคลื่อนไหว......")
            #หน่วงเวลา 5 วินําทีเพื่อหลีก เลี่ยงการตรวจจับ หลายครั้ง
            time.sleep(5)
        #หน่วงเวลาการวนลูป 0.1 วินาทีซึ่งควรตั้งค่าน้อยกว่าเวลาหน่วงของการตรวจจับการเคลือนไหว
        time.sleep(0.1)
except:
    GPIO.cleanup()