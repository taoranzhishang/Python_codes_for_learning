

import pytest
import sys
import time
import platform
import logging

import pywifi
from pywifi import const

pywifi.set_loglevel(logging.INFO)

def test_connect():

    wifi = pywifi.PyWiFi()  #wifi对象

    iface = wifi.interfaces()[0] #第一个网卡

    iface.disconnect() #断开所有的无线链接
    time.sleep(1)

    profile = pywifi.Profile() #链接wifi需要构造profile
    profile.ssid = 'hellopython'  #wifi名称
    profile.auth = const.AUTH_ALG_OPEN  #开放的
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  #默认的加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  #wifi的数据类型
    profile.key = '12345678' #wifi密码

    iface.remove_all_network_profiles() #卸载当前所有网络的wifi
    tmp_profile = iface.add_network_profile(profile) #增加一个profile用于登陆wifi

    iface.connect(tmp_profile) #根据profile链接wifi
    time.sleep(10) #休眠10秒，
    isOK=False   #假定链接不上
    if iface.status() == const.IFACE_CONNECTED:#链接上的状态
        isOK=True
        print("链接成功")

    iface.disconnect()  #断开网络
    if  isOK:
        return  isOK  #如果成功，返回

    time.sleep(1)
    if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        print("链接失败")
    return isOK


def test_disconnect():#断开网络连接，

    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0] #第一个无限网卡
    iface.disconnect()

    assert iface.status() in\
        [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]



print(test_connect())

