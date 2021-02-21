# -*- coding: UTF-8 -*-#
import win32api, win32con, win32gui


# 设置路径为背景图片
def set_wallpaper(path):
    # 打开注册表，修改这个值
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop",
                                    0,
                                    win32con.KEY_SET_VALUE)
    # 2拉伸，0居中，6适应，10填充，
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 设定一下开头
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 设定背景并实时切换
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                                  path,
                                  win32con.SPIF_SENDWININICHANGE)


set_wallpaper("C:\\Users\\Tsinghua-yincheng\\Desktop\\day26\\res\\1.jpg")
