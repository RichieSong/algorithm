# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/8/15 by Richie.Song.

"""
import threading
import redis
import time
import socket
import os
import json
from config import get_product_redis_configs

redis_configs = get_product_redis_configs()
conn = redis.StrictRedis(*redis_configs, socket_timeout=5)


class RedisLock(object):
    def __init__(self):
        self.redis_conn = conn
        self.ip = socket.gethostbyname(socket.gethostname())
        self.pid = os.getpid()

    def get_lock_key(self, key):
        lock_key = "lock_{}".format(key)
        return lock_key

    def get_lock(self, key, timeout=1):
        lock_key = self.get_lock_key(key)
        unique_value = self.gen_unique_value()
        while True:
            value = self.redis_conn.setnx(lock_key, unique_value)  # 设置成功-设置超时,没有设置成功等待
            print(value, lock_key, unique_value)
            if value:
                self.redis_conn.expire(lock_key, timeout)  # 不能放在if外 防止死锁: 进程crash时,未释放锁,却一直在续期,
                # 其他线程一直获取不到锁
                return unique_value
            else:
                thread_name = threading.current_thread().name
                print("{} is waiting ...".format(thread_name))
            time.sleep(0.1)

    # 确保每个线程的锁的值是唯一的,防止不是本线程误解锁
    def gen_unique_value(self):
        thread_name = threading.current_thread().name
        timeNow = time.time()
        unique_value = "{0}-{1}-{2}-{3}".format(self.ip, self.pid, thread_name, timeNow)
        return unique_value

    #
    def del_lock(self, key, value):
        lock_key = self.get_lock_key(key)  # lock-test
        old_lock_value = self.redis_conn.get(lock_key)  # == 1
        if old_lock_value == value:  ## 如果成立,锁没释放,手动释放即可,如果不成立,代表已经自动释放锁
            print("unlock ....")
            return self.redis_conn.delete(lock_key)


def increase_data(redis_conn, lock, datakey):
    lock_value = lock.get_lock(datakey)  # 获取锁 value是唯一的值 == gen-unique-value
    value = redis_conn.get(datakey)  # 获取数据
    # time.sleep(2.5)
    if value:
        value = int(value) + 1
    else:
        value = 0
    redis_conn.set(datakey, value)
    thread_name = threading.current_thread().name
    print(thread_name, value)
    if thread_name == "Thread-2":  # 测试进程意外crash,也没有问题
        print("thread-2 crash ...")
        import sys
        sys.exit(1)
    lock.del_lock(datakey, lock_value)  # 释放锁


if __name__ == '__main__':
    datakey = "test"
    lock = RedisLock()

    for i in range(2):
        thread = threading.Thread(target=increase_data, args=(conn, lock, datakey))
        thread.start()
