import tkinter as tk

def on_click():
    print("你按了按鈕！")

window = tk.Tk()
window.title("番茄時鐘")
window.geometry("300x200")  # 設定視窗大小

label = tk.Label(window, text="番茄時鐘開始", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(window, text="開始工作", command=on_click)
button.pack()

window.mainloop()