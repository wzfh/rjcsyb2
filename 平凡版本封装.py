import tkinter as tk
from tkinter import messagebox


def show_custom_warning():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 创建一个新的顶级窗口
    top = tk.Toplevel(root)
    top.title("欢迎")

    # 创建一个标签显示消息
    label = tk.Label(top, text="我是僵尸宝宝一号，欢迎使用本软件程序", wraplength=200)
    label.pack(padx=20, pady=20)

    # 创建一个自定义按钮1
    def on_button1_click():
        top.destroy()  # 关闭窗口

    button1 = tk.Button(top, text="快快退下", command=on_button1_click)
    button1.pack(side=tk.LEFT, padx=10)

    # 创建一个自定义按钮2
    def on_button2_click():
        # 在这里添加你想要执行的操作，例如继续游戏等
        pass

    button2 = tk.Button(top, text="留下我再玩一会", command=on_button2_click)
    button2.pack(side=tk.RIGHT, padx=10)

    top.mainloop()


show_custom_warning()
