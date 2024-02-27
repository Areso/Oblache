# from datetime import datetime
#
# time = str(datetime.now().strftime("%d-%m-%Y_%H_%M_%S"))
# print(time)
import json

import requests

#
# sid = TestData.sid
# print(sid)

result = requests.post('https://dbend.areso.pro/is_logged')
authorization_url = ('https://www.googleapis.com/identitytoolkit/v3/'
                     'relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY')
data_specialist_user = {"email": "autoTestSpecialist@brainup.spb.ru", "password": "password",
                        "returnSecureToken": "true"}
result_post_specialist = requests.post(authorization_url, data_specialist_user)
id_token = json.loads(result_post_specialist.text)['idToken']
print(result_post_specialist.text)
response = requests.get('https://brainup.site/api/tasks/2603',
                        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {id_token}'})
print(response.text)
print(result.status_code)
result1 = requests.post('https://dbend.areso.pro/is_logged', json={"web": 1})
print(result1.text)
print(result1.status_code)
result2 = requests.post('https://dbend.areso.pro/is_logged', sid)
print(result2.text)
print(result2.status_code)
result3 = requests.post('https://dbend.areso.pro/is_logged', sid, json={"web": 1})
print(result3.text)
print(result3.status_code)

