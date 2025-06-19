# 測試版
import tkinter as tk
import time

def working():    # 計時器模組
    global sec
    sec+=1
    if sec == 1500:
        sec = 0
        tk.Button(restingDesk,
                  text="開始休息",
                  command=resting
        ).pack()


    window.after(1000, working)   # 每一秒都會呼叫自己

def resting():
    global rest
    rest += 1
    if rest == 300:
        rest = 0
        tk.Button(workingDesk,
                  text="開始工作",
                  command=working
        ).pack()
        
    window.after(1000, resting)   # 每一秒都會呼叫自己

sec = 0
rest = 0


window = tk.Tk()
window.title("簡易版番茄時鐘")
window.geometry("300x200")  # 設定視窗大小

workingDesk = tk.Toplevel(window)
workingDesk.title("工作中")
workingDesk.geometry("300x200")  # 設定視窗大小

restingDesk = tk.Toplevel(window)
restingDesk.title("休息中")
restingDesk.geometry("300x200")  # 設定視窗大小

label = tk.Label(window, text="番茄時鐘開始", font=("Arial", 16))
label.pack(pady=20)     # 行距大小

button = tk.Button(window, text="開始工作", command=working)
button.pack()

window.mainloop()