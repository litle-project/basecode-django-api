# helpers/requests.py

from django_redis import get_redis_connection
from decouple import config
import redis

def store_redis(key, value, db = 0, expired=None):
    BASE_REDIS_URL = f"redis://{config('REDIS_URL', '127.0.0.1')}:{config('REDIS_PORT', 6379)}"
    redis_url = f"{BASE_REDIS_URL}/{db}"
    redis_helper = redis.StrictRedis.from_url(redis_url)

    if expired is None:
        redis_helper.set(key, f"{value}")
    else: 
        redis_helper.set(key, f"{value}", ex=expired)

def get_redis(key, db = 0):
    BASE_REDIS_URL = f"redis://{config('REDIS_URL', '127.0.0.1')}:{config('REDIS_PORT', 6379)}"
    redis_url = f"{BASE_REDIS_URL}/{db}"
    redis_helper = redis.StrictRedis.from_url(redis_url)

    value = redis_helper.get(key)

    if value is not None:
        return value.decode('utf-8')
    return None

def delete_redis(key, db = 0):
    BASE_REDIS_URL = f"redis://{config('REDIS_URL', '127.0.0.1')}:{config('REDIS_PORT', 6379)}"
    redis_url = f"{BASE_REDIS_URL}/{db}"
    redis_helper = redis.StrictRedis.from_url(redis_url)
    
    return redis_helper.delete(key)