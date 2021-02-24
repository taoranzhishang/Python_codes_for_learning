import pytest
import sys
import time
import platform
import logging
import pywifi
from pywifi import const

pywifi.set_loglevel(logging.INFO)

def go_interfaces():

    wifi = pywifi.PyWiFi() #创建wifi对象

    assert wifi.interfaces() #抓取网卡接口

    if platform.system().lower() == 'windows': #判断平台
        assert wifi.interfaces()[0].name() ==\
            '802.11n USB Wireless LAN Card'

go_interfaces()