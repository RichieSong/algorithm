# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/8/15 by Richie.Song.

"""
import getpass
user = getpass.getuser()

# redis config
def get_product_redis_configs():
    if user == 'RichieSong':

        redis_host = '172.28.34.97'
        redis_port = '6379'
        redis_db = '1'
        redis_password = 'redis123'
    else:
        redis_host = '10.19.35.30'
        redis_port = '6379'
        redis_db = '8'
        redis_password = ''
    return redis_host, redis_port, redis_db, redis_password