# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/8/15 by Richie.Song.

"""

import os
import random
import threading
import time

from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock
from retrying import retry


class ZooKeeperLock(object):
    def __init__(self, hosts, id_str, lock_key, timeout=0.1):
        self.hosts = hosts
        self.id_str = id_str
        self.lock_key = lock_key
        self.timeout = timeout
        self.zk_clinet = None
        self.lock_handle = None
        self._init = self.create_lock()

    def create_lock(self):
        try:
            self.zk_clinet = KazooClient(hosts=self.hosts, timeout=self.timeout)
            self.zk_clinet.start(timeout=self.timeout)
        except Exception as e:
            print("Kazoo clinet create fail: %s" % str(e))
            return
        try:
            lock_path = os.path.join("/", "locks", self.lock_key)
            self.lock_handle = Lock(self.zk_clinet, lock_path)
        except Exception as e:
            print("client lock init fail: %s" % str(e))
            return

    def destory_lock(self):
        if self.zk_clinet != None:
            self.zk_clinet.stop()
            self.zk_clinet = None

    def acquire(self, blocking=True, timeout=None):
        if self.lock_handle == None:
            return None
        try:
            return self.lock_handle.acquire(blocking=blocking, timeout=timeout)
        except Exception as e:
            print("Acquire lock failed : %s" % str(e))
            return None

    def release(self):
        if self.lock_handle == None:
            return None
        return self.lock_handle.release()

    def __del__(self):
        self.destory_lock()


value = 0
count = 0


def increase_data(lock):
    try:
        # ret = lock.acquire()  # 获取锁,速度贼慢
        ret = 0
        global value, count
        value += 1

        thread_name = threading.current_thread().name
        print("\n", count)
        # if thread_name == "Thread-4":  # 测试进程意外crash,也没有问题
        #     print("thread-4 crash ...")
        #     import sys
        #     sys.exit(1)
        # lock.release()  # 释放锁
        # time.sleep(2)
        return True
    except Exception as e:
        raise Exception("test")

def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)

# @retry(stop_max_attempt_number=5, stop_max_delay=1000, wait_fixed=2000,retry_on_exception=retry_if_io_error)
@retry(stop_max_attempt_number=5,retry_on_exception=retry_if_io_error, wrap_exception=True)
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        print "just have a test"
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


if __name__ == '__main__':
    zk_hosts = "172.28.60.62:2181,172.28.60.63:2181,172.28.34.98:2181"
    lock_key = "test"
    lock = ZooKeeperLock(zk_hosts, "id is 1", lock_key)
    # lock.create_lock()
    # for i in range(1):
    #     thread = threading.Thread(target=increase_data, args=(lock,))
    #     thread.start()
    print(do_something_unreliable())
    time.sleep(2)
