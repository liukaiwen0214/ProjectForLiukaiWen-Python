import random

import pymouse
import pyautogui
import time

# 生成脚本日志文件
logFile = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "运行日志.txt"  # 2019-08-17 15:47:58运行日志.txt
logPath = "C:\\Users\\Administrator\\Desktop\\OnmyojiAuto\\" + logFile

# 脚本运行前开启次节点代码获取点击位置



# 获取坐标信息
GameScreenMinX = input("输入游戏屏幕最小X坐标数值（小数）：")
GameScreenMaxX = input("输入游戏屏幕最大X坐标数值（小数）：")
GameScreenMinY = input("输入挑战屏幕最小Y坐标数值（小数）：")
GameScreenMaxY = input("输入挑战屏幕最大Y坐标数值（小数）：")
GameStartMinX = input("输入游戏屏幕最小X坐标数值（小数）：")
GameStartMaxX = input("输入游戏屏幕最小X坐标数值（小数）：")
GameStartMinY = input("输入游戏屏幕最小X坐标数值（小数）：")
GameStartMaxY = input("输入游戏屏幕最小X坐标数值（小数）：")
RunNums = input("输入挑战次数：")

for i in range(int(RunNums)):

    ScreenX = random.uniform(GameScreenMinX, GameScreenMaxX)
    ScreenY = random.uniform(GameScreenMinY, GameScreenMaxY)

    # 生成挑战开始的坐标
    GameStartX = random.uniform(GameStartMinX, GameStartMaxX)
    GameStartY = random.uniform(GameStartMinY, GameStartMaxY)
# 位置记录
# 游戏屏幕位置 X = 1062-1904 Y = 40-500
# 开始挑战位置 X = 1790-1867 Y = 420-499
# 游戏屏幕坐标范围
while True:
    GameScreenMinX = 1062.0
    GameScreenMaxX = 1904.0
    GameScreenMinY = 40.0
    GameScreenMaxY = 500.0
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

    # 定义挑战开始的范围
    GameStartMinX = 1790.0
    GameStartMaxX = 1867.0
    GameStartMinY = 420.0
    GameStartMaxY = 499.0
    # 生成挑战开始的坐标
    GameStartX = random.uniform(GameStartMinX, GameStartMaxX)
    GameStartY = random.uniform(GameStartMinY, GameStartMaxY)
    print("鼠标移动到：" + str(GameStartX) + "," + str(GameStartY) + "\n")
    # 生成点击屏幕时间
    GameStartTims = 1.0
    GameEndTims = 5.0
    GameClinckTimes = random.uniform(GameStartTims, GameEndTims)
    time.sleep(GameClinckTimes)
    pyautogui.click(GameStartX, GameStartY)
