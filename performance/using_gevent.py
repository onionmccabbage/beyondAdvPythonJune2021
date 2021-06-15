# gevent is 'green event' - it runs threads for us

import gevent # may need to pip isntall it!
from gevent import socket

# a list of hosts
hosts = ['www.ericsson.com', 'www.neueda.com', 'www.crappytaxidermy.com']
jobs  = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)