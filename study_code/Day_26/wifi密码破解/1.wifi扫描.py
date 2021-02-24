
import pytest
import sys
import time
import platform
import logging

import pywifi
from pywifi import const

pywifi.set_loglevel(logging.INFO)

def go_scan():

    wifi = pywifi.PyWiFi() #初始化wifi

    iface = wifi.interfaces()[0] #第一个无线网卡，
    iface.scan() #扫描
    time.sleep(5)
    bsses = iface.scan_results() #扫描结果
    for  data  in bsses: #wifi创建一个对象
        print(data.ssid)


go_scan()