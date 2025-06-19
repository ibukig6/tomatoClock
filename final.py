# 最終版
import tkinter as tk

sec = 0
rest = 0

def end():
    window.destroy()

def working():
    global sec
    sec += 1
    label.config(text=f"工作中：{sec} 秒")      # 修改label內容
    if sec == 10:
        sec = 0
        label.config(text="工作結束！點下開始休息")
        btn.config(text="開始休息", command=resting)
        tk.Button(window, text="結束", command=end).pack(pady=20)
    else:
        window.after(1000, working)

def resting():
    global rest
    rest += 1
    label.config(text=f"休息中：{rest} 秒")
    if rest == 10:
        rest = 0
        label.config(text="休息結束！點下開始工作")
        btn.config(text="開始工作", command=working)
        tk.Button(window, text="結束", command=end).pack(pady=20)
    else:
        window.after(1000, resting)

# 初始 GUI
window = tk.Tk()
window.title("簡易版番茄時鐘")
window.geometry("300x200")

label = tk.Label(window, text="番茄時鐘開始", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(window, text="開始工作", command=working)
btn.pack()

window.mainloop()
