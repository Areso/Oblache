# from datetime import datetime
#
# time = str(datetime.now().strftime("%d-%m-%Y_%H_%M_%S"))
# print(time)

import requests

from conftest_api import TestData

sid = TestData.sid
print(sid)

result = requests.post('https://dbend.areso.pro/is_logged')
print(result.text)
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

assert True is not None
print('True')
assert False is not None
print('False')
assert None is not None
print('None')