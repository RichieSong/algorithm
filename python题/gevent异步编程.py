#coding:utf-8
import gevent
from gevent import socket
urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
print(jobs)
gevent.joinall(jobs, timeout=2)
print(jobs)
print [job.value for job in jobs]