import redis
import pickle
from datetime import timedelta

r=redis.Redis(host="127.0.0.1",port=6379)

def set_cache_data(key,time_expiry,value):
    try:
        r.setex(key,timedelta(seconds=time_expiry),value=value)
        return True
    except:
        return False

def get_cache_data(key):
    try:
        data=r.get(key)
        return data
    except:
        return False
    
def delete_cache_data(key):
    try:
        r.delete(key)
        return True
    except:
        return False
    