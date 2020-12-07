# debugtalk.py
import hashlib
def getsign(user,passwd):
    str=user+passwd
    md5=hashlib.md5()
    md5.update(str.encode(encoding='utf-8'))
    sign=md5.hexdigest()
    return sign


import time 
def sleep(response,t):
    if response.status_code==200:
        time.sleep(10)
    else:
        time.sleep(t)
