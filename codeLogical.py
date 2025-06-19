# 程式邏輯
import time

def working():
    sec = 0
    rest = 1
    while True:
        time.sleep(1)
        sec += 1
        if sec == 10:
            break
    print("工作時間結束，是否進入休息時間？")   # 讓使用者選擇是否繼續執行程式
    if rest == 1:
        resting()
    else:
        print("結束程式")

def resting():
    sec = 0
    work = 1
    while True:
        time.sleep(1)
        sec += 1
        if sec == 300:
            break
    print("休息時間結束，是否進入工作時間？")   # 讓使用者選擇是否繼續執行程式
    if work == 1:
        working()
    else:
        print("結束程式")

working()