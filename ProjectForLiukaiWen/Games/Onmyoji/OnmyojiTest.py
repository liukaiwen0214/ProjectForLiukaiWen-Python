"""
@FileName：OnmyojiTest.py
@Description：
@Author：liukaiwenMac
@Time：2024/6/17 下午5:13
"""
import GetMousePosition

def test_beifan():
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

    # print("最小值的x是：" + str(GameScreenMinX) + ",最大值的x是：" + str(GameScreenMaxX) + "最小值的y是：" + str(
    #     GameScreenMinY) + "最大值的y是：" + str(GameScreenMaxY))
    # print("最小值的x是：" + str(GameStartMinX) + ",最大值的x是：" + str(GameStartMaxX) + "最小值的y是：" + str(
    #     GameStartMinY) + "最大值的y是：" + str(GameStartMaxY))

    # print(mouses_x,mouses_y)

