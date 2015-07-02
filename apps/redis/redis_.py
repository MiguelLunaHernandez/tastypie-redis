from apps.core.models import *
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)



def Get_ConnectionRedis():

    #r = redis.StrictRedis(host='localhost', port=6379, db=0)
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    return r

def ExitCache(key):

#   connection = Get_ConnectionRedis()
    
    return r.exists(key)


def SaveCache(key, value):

#   connection = Get_ConnectionRedis()
    #guarda el objeto json lo deserealiza
    r.set(key, value)

def GetCache(key):

#   connection = Get_ConnectionRedis()
    return r.get(key)

