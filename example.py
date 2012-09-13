
"""
Better to use an object as a manager, 


>>> rds = FlaskRedis(host="localhost",port=6379)
>>> assert "redis_version" in rds.rsvr_info.keys()
>>> rds.rsvr.flushall()
True
>>> testuid = '41c8c6a0-7ce0-4257-8316-2da290ca6961'
>>> test_jsonstr = '{"test": "Hello World"}'
>>> rds.add_json(testuid, test_jsonstr)
True
>>> j = rds.retr_json(testuid)
>>> assert j == test_jsonstr


.. todo:: security
.. todo:: write to disk
.. todo:: master slave
.. todo:: better json handling

"""

import redis
import json





class RedisBackendError(Exception):
    pass


class FlaskRedis(object):

    def __init__(self, host="localhost", port=6379):
        self.rsvr = redis.Redis(host=host, port=port)
        self.rsvr_info = self.rsvr.info()

    def doesexist(self, uid):
        if self.rsvr.exists(uid):
            return True
        else:
            return False

    def add_json(self, uid, json_str):
        """Store this """

        res = self.rsvr.set(uid, json_str)
        if res != True:
            raise RedisBackendError("Failed to store %s" % uid)
        else:
            return True

    def retr_json(self, uid):
        """ """
        res = self.rsvr.get(uid)
        if not res:
            return None
        else:
            return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
