#coding:utf-8
#!/usr/bin/env python
import requests
import json
from prometheus_client import Gauge
from settings import conf

runningQueries = Gauge('presto_runningQueries', 'Current Running Queries')
blockedQueries = Gauge('presto_blockedQueries', 'Current Blocked Queries')
queuedQueries = Gauge('presto_queuedQueries', 'Current Queued Queries')
activeCoordinators = Gauge('presto_activeCoordinators', 'Current Active Coordinators')
activeWorkers = Gauge('presto_activeWorkers', 'Current Active Workers')
runningDrivers = Gauge('presto_runningDrivers', 'Running Drivers')
totalAvailableProcessors = Gauge('presto_totalAvailableProcessors', 'Total Available Processors')
reservedMemory = Gauge('presto_reservedMemory', 'Reserved Memory')
totalInputRows = Gauge('totalInputRows', 'Total Input Rows')
totalInputBytes = Gauge('totalInputBytes', 'Total Input Bytes')
totalCpuTimeSecs = Gauge('totalCpuTimeSecs', 'Total Cpu Time Secs')

class PrestoEntry():
    
    def __init__(self):
        self.url = conf.PRESTO_URL
        self.login()

    def query_presto_data(self):
        url = "%s/ui/api/stats"%(self.url)
        try:
            r = self.s.get(url)
            if r.status_code == requests.codes.ok:
                return True,json.loads(r.text)
            return False,r.text
        except Exception as e:
            print(e)
            return False,e

    def login(self):
        url = "%s/ui/login"%(self.url)
        data = {
          "username": "admin"
        }
        self.s = requests.session()
        r = self.s.post(url, data=data)

    def get_metrics(self):
        (status, presto_data) = self.query_presto_data()
        if not status:
            raise Exception("exception", presto_data)
        runningQueries.set(presto_data.get("runningQueries"))
        blockedQueries.set(presto_data.get("blockedQueries"))
        queuedQueries.set(presto_data.get("queuedQueries"))
        activeCoordinators.set(presto_data.get("activeCoordinators"))
        activeWorkers.set(presto_data.get("activeWorkers"))
        runningDrivers.set(presto_data.get("runningDrivers"))
        totalAvailableProcessors.set(presto_data.get("totalAvailableProcessors"))
        reservedMemory.set(presto_data.get("reservedMemory"))
        totalInputRows.set(presto_data.get("totalInputRows"))
        totalInputBytes.set(presto_data.get("totalInputBytes"))
        totalCpuTimeSecs.set(presto_data.get("totalCpuTimeSecs"))

if __name__ == "__main__":
    instance = PrestoEntry()
    print(instance.query_presto_data())