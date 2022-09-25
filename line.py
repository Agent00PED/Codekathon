#เชื่อมต่อ Line nitofy เพื่อแจ้งเตือนผลจากเซนเซอร์
import requests
# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = 'ใส่รหัส Token ที่จากการลงทะเบียน'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer
'+token}
msg = 'ทดสอบการแจ้งเตือน'
r = requests.post(url, headers=headers, data = {'message':msg})
#ส่งข้อความแจ้งเตือน
print(r.text)