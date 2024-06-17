"""
@FileName：GetMousePosition.py
@Description：获取当前鼠标所在坐标位置
@Author：LiuKaiWenMac
@Time：2024/6/17 下午4:50
"""
import time

import pyautogui


def get_mouse_position(nums):
    mouses_x = []
    mouses_y = []  # 定义坐标系数组，前两个为屏幕，后两个为开始
    while nums > 0:
        # 获取当前鼠标位置
        my_mouses_position_x, my_mouses_position_y = pyautogui.position()
        mouses_x.append(my_mouses_position_x)
        mouses_y.append(my_mouses_position_y)
        nums -= 1
        time.sleep(1)  # 暂停5秒钟
    return mouses_x, mouses_y
