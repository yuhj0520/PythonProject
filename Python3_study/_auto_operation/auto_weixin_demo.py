# coding:utf-8
'''
模拟操作微信定时发送信息，提前获取当前操作光标所在位置，进行鼠标和键盘的组合操作，添加定时任务来执行
pyautogui.PAUSE = 1 # 设置每一步操作的间隔（秒），可防止操作太快
print(pyautogui.position()) # 打印坐标，Point(x=148, y=879)
'''

import pyautogui
import pyperclip
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    pyautogui.PAUSE = 0

    icon_position = pyautogui.Point(x=2258, y=1417) # 任务栏图标位置
    entry_position = pyautogui.Point(x=1281, y=1256) # 输入框位置

    pyautogui.moveTo(icon_position, duration=1) # duration为执行时长，可选
    pyautogui.click(icon_position)
    pyautogui.moveTo(entry_position, duration=1)
    pyautogui.click(entry_position)
    pyperclip.copy('测试')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    for i in range(5):
        pyperclip.copy('fr')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    
scheduler = BlockingScheduler() # 实例化
scheduler.add_job(main, 'date', run_date=datetime(2021, 9, 2, 17, 1, 33)) # 添加任务
scheduler.start()
