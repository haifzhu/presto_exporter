#coding:utf-8
#!/usr/bin/env python
from prometheus_client import start_http_server
from prestoentry import PrestoEntry
import time
from settings import conf

if __name__ == '__main__':
    start_http_server(conf.BINDPORT)
    print("server is running on port %d"%(conf.BINDPORT))
    instance = PrestoEntry()
    while True:
        try:
            instance.get_metrics()
            time.sleep(15)
        except Exception as e:
            print(e)
            time.sleep(3)