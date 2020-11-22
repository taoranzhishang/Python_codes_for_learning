# encoding: utf-8
from pyecharts.charts import Geo
from pyecharts import options
from pyecharts.globals import GeoType
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import random
import cmath

gap_size = 400
image_cols = 1148 + gap_size  # 横坐标
image_rows = 1501 + gap_size  # 纵坐标
image = Image.new("RGB", (image_cols, image_rows))
star_num = 100  # 星星个数

for k in range(star_num):
    star_row = random.randint(gap_size / 2, image_rows - gap_size / 2)
    star_col = random.randint(gap_size / 2, image_cols - gap_size / 2)
    impact_cols = [star_col + i - 50 for i in range(100)]
    impact_rows = [star_row + i - 50 for i in range(100)]

    # 每个star的影响范围
    for wide in impact_cols:
        for height in impact_rows:
            position_near = (wide, height)  # 取全图中的一个点
            pixBefore = image.getpixel(position_near)  # 取一下当前的像素值
            base_value = 200  # 影响基值，现在先写成200

            # 影响系数 = 一个和距离有关的值, 或者是其他的
            distance = (cmath.sqrt(pow(wide - star_col, 2) + pow(height - star_row, 2))).real
            impact_factor = 1 / (distance + 1)

            # 影响因子大于一定的值再计算
            if impact_factor > 0.02:
                # 影响的值 = 影响系数 * 影响基值
                impact_value = impact_factor * base_value
                pixAfter = (
                pixBefore[0] + int(impact_value), pixBefore[1] + int(impact_value), pixBefore[2] + int(impact_value))
                image.putpixel(position_near, pixAfter)

        image.save("star.png")