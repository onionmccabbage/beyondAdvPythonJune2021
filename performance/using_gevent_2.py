import gevent
from gevent import monkey; 
monkey.patch_all()
import socket

hosts = ['www.crappytaxidermy.com', 'www.neueda.com', 'www.ericsson.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)