import random

import pymouse
import pyautogui
import time
import GetMousePosition

# 生成脚本日志文件
logFile = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "运行日志.txt"  # 2019-08-17 15:47:58运行日志.txt
logPath = "C:\\Users\\Administrator\\Desktop\\OnmyojiAuto\\" + logFile


"""
1、获取到的数据样例 [100,233,948,827] [130,43,428,87]
2、对数据进行切分合并，前两个为屏幕，后两个为开始 
    切分后的数据为 屏幕：[x,x,y,y] 开始：[x,x,y,y]
3、把切分后的数据拆分进行坐标定位 得到的效果为
    屏幕范围: minx - maxx miny - maxy; 开始范围: minx - maxx miny - maxy;
    
"""
# 获取坐标信息
mouses_x = GetMousePosition.get_mouse_position(4)[0]
mouses_y = GetMousePosition.get_mouse_position(4)[1]
if mouses_x[0] < mouses_x[1]:
    GameScreenMinX = mouses_x[0]
    GameScreenMaxX = mouses_x[1]
else:
    GameScreenMinX = mouses_x[1]
    GameScreenMaxX = mouses_x[0]

if mouses_y[0] < mouses_y[1]:
    GameScreenMinY = mouses_y[0]
    GameScreenMaxY = mouses_y[1]
else:
    GameScreenMinY = mouses_y[1]
    GameScreenMaxY = mouses_y[0]

if mouses_x[2] < mouses_x[3]:
    GameStartMinX = mouses_x[2]
    GameStartMaxX = mouses_x[3]
else:
    GameStartMinX = mouses_x[3]
    GameStartMaxX = mouses_x[2]

if mouses_y[2] < mouses_y[3]:
    GameStartMinY = mouses_x[2]
    GameStartMaxY = mouses_x[3]
else:
    GameStartMinY = mouses_y[3]
    GameStartMaxY = mouses_y[2]
# 循环开始
while True:

    # 定义挑战开始的范围

    GameStartX = random.uniform(GameStartMinX, GameStartMaxX)
    GameStartY = random.uniform(GameStartMinY, GameStartMaxY)

    # 生成点击屏幕时间
    GameStartTims = 1.0
    GameEndTims = 5.0
    GameClinckTimes = random.uniform(GameStartTims, GameEndTims)
    time.sleep(GameClinckTimes)
    pyautogui.click(GameStartX, GameStartY)

    # 生成游戏屏幕坐标
    ScreenX = random.uniform(GameScreenMinX, GameScreenMaxX)
    ScreenY = random.uniform(GameScreenMinY, GameScreenMaxY)

    print("鼠标移动到：" + str(ScreenX) + "," + str(ScreenY) + "\n")
    #生成点击屏幕时间
    StartTims = 8.0
    EndTims = 13.0
    ClinckTimes = random.uniform(StartTims, EndTims)
    time.sleep(ClinckTimes)
    #鼠标点击生成的坐标
    pyautogui.click(ScreenX, ScreenY)

